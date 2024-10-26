from celery import shared_task
from django.db.models import F

from apps.discounts.models import Discount



@shared_task(bind=True, max_retries=3)
def update_discount_comment_count(discount_id, action):
    """
    Celery task to update the comment count of a specific discount.

    Args:
        discount_id (int): The ID of the discount whose comment count needs to be updated.
        action (str): The action to perform, either 'increment' to increase the count
                      or 'decrement' to decrease the count.
        self: The task instance (provided when bind=True). Allows access to task-specific
              methods like `self.retry()` for retrying the task in case of failure.

    Logic:
        - If action is 'increment', the comment count will be increased by 1.
        - If action is 'decrement', the comment count will be decreased by 1.
        - The update uses F() expressions to perform atomic increments or decrements directly in the database.
    """

    try:
        discount = Discount.objects.get(id=discount_id)

        if action == 'increment':
            discount.comment_counts = F('comment_counts') + 1
        else:  # ==== action is 'decrement' ====
            discount.comment_counts = F('comment_counts') - 1

        discount.save()

    except Discount.DoesNotExist:
        pass
