from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.likes.models.dislikes import DiscountDislike
from apps.likes.models.likes import DiscountLike
from apps.likes.tasks.update_discount_likes_count import \
    update_discount_likes_count


@receiver(post_save, sender=DiscountLike)
def post_save_discount_like(sender, instance, created, **kwargs) -> None:
    """
    Update the total number of likes for a discount when a like is created.
    Delegates the actual count update to a Celery task.
    """
    if not instance.discount:
        return

    if created:
        update_discount_likes_count.delay(
            discount_id=instance.discount.id,
            action='increment_like'
        )


@receiver(post_delete, sender=DiscountLike)
def post_delete_discount_like(sender, instance, **kwargs) -> None:
    """
    Update the total number of likes when a like is deleted.
    Delegates the actual count update to a Celery task.
    """
    if not instance.discount:
        return

    update_discount_likes_count.delay(
        discount_id=instance.discount.id,
        action='decrement_like'
    )


@receiver(post_save, sender=DiscountDislike)
def post_save_discount_dislike(sender, instance, created, **kwargs) -> None:
    """
    Update the total number of dislikes when a dislike is created.
    Delegates the actual count update to a Celery task.
    """
    if not instance.discount:
        return

    if created:
        update_discount_likes_count.delay(
            discount_id=instance.discount.id,
            action='increment_dislike'
        )


@receiver(post_delete, sender=DiscountDislike)
def post_delete_discount_dislike(sender, instance, **kwargs) -> None:
    """
    Update the total number of dislikes when a dislike is deleted.
    Delegates the actual count update to a Celery task.
    """
    if not instance.discount:
        return

    update_discount_likes_count.delay(
        discount_id=instance.discount.id,
        action='decrement_dislike'
    )