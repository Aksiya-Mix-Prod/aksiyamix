from celery import shared_task
from django.db.models import F

from apps.discounts.models import Discount


@shared_task(bind=True, max_retries=3)
def update_discount_likes_count(discount_id: int, action: str) -> None:
    """
    Celery task to update the number of likes or dislikes for a particular discount.

    Args:
        discount_id (int): The id of the discount to update.
        action (str): The action to perform, one of:
            - 'increment_like': Increase likes count by 1
            - 'decrement_like': Decrease likes count by 1
            - 'increment_dislike': Increase dislikes count by 1
            - 'decrement_dislike': Decrease dislikes count by 1
    Logic:
        Uses F() expressions to perform atomic increments/decrements directly in the DB.
        Retries up to 3 times if the discount is not found.
    """
    try:
        updates = {
            'increment_like':{'likes_count':F('likes_count') + 1},
            'decrement_like':{'likes_count':F('likes_count') - 1},
            'increment_dislike':{'dislikes_count':F('dislikes_count') + 1},
            'decrement_dislike':{'dislikes_count':F('dislikes_count') - 1}
        }

        if action not in updates:
            raise ValueError(f"Invalid action: {action}")

        # ========= Check if the discount exists and update in one query ========
        updated = Discount.objects.filter(id=discount_id).update(**updates[action])

        # ========= If no rows were updated, the discount doesn't exist ========
        if not updated:
            raise Discount.DoesNotExist(f"Discount with id {discount_id} does not exist")

    except Discount.DoesNotExist:
        pass