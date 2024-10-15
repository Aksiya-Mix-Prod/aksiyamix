from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Rating(models.Model):
    """
    Model to rate company. Company is rated by user only one time.
    """

    # which company to rate
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)

    # which user is rating
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL)

    # rating of user
    rating_value = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "rating"
        unique_together = (('company', 'user'),)

