from celery import shared_task
from django.db import DatabaseError
from django.db.models import F

from apps.discounts.models import Discount



@shared_task(bind=True, max_retries=3)
def update_discount_comment_count(self, discount_id, action):
    """
    Celery task to update discount comment count.

    Args:
        discount_id: ID of the discount to update
        action: Either 'increment' or 'decrement'
    """
    try:
        discount = Discount.objects.get(id=discount_id)

        if action == 'increment':
            discount.comment_count = F('comment_count')+1
        else:  # ==== # action is 'decrement' ====
            discount.comment_count = F('comment_count')-1

        discount.save()

    except Discount.DoesNotExist:
        self.retry(countdown=60)  # Retry after 1 minute
    except DatabaseError as e:
        self.retry(countdown=180)  # Retry after 3 minutes
