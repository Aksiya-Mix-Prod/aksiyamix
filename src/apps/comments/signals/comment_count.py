from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from apps.comments.models import Comment
from apps.comments.tasks.celery_count_comments import update_discount_comment_count



@receiver(post_save, sender=Comment)
def update_discount_comment_count_on_delete(sender, instance, created, **kwargs):
    """
    Signal to handle comment count updates when a comment is created or updated.
        Delegates the actual count update to a Celery task.

        Why F() expressions?
        We use F('comment_count') instead of direct number manipulation
        This prevents race conditions when multiple users are creating/deleting comments simultaneously
    """

    if not instance.discount:
        return

    if created and not instance.is_deleted:
        # =========  Only increment if it's a new non-deleted comment =========
        update_discount_comment_count.delay(
            discount_id=instance.discount.id,
            action='increment'
        )
    elif not created:
        # ======== Handle case where comment is being updated (e.g., marked as deleted) ========
        old_instance = Comment.objects.get(pk=instance.pk)
        if old_instance.is_deleted != instance.is_deleted:
            # ======== If deletion status changed, update the count accordingly ========
            action = 'decrement'if instance.is_deleted else 'increment'
            update_discount_comment_count.delay(
                discount_id=instance.discount.id,
                action=action
            )


@receiver(post_delete, sender=Comment)
def update_discount_comment_count_on_delete(sender, instance, **kwargs):
    """
    Signal to handle comment count updates when a comment is permanently deleted.
    Delegates the actual count update to a Celery task.
    """
    if not instance.discount or instance.is_deleted:
        return

    # ========= Only decrement if it wasn't already marked as deleted ========
    update_discount_comment_count.delay(
        dicount_id=instance.discount.id,
        action='decrement'
    )






