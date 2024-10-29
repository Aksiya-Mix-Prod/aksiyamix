from apps.base.exceptions import CustomExceptionError
from apps.discounts.choices import DiscountChoices


def validate_standard_discount(instance):
    if instance.discount_type == DiscountChoices.STANDARD:
        if instance.discount_value is None:
            raise CustomExceptionError(code=400, detail="Standard discount must require a discount_value")

        if instance.discount_value_is_percent and instance.discount_value:
            if not (0 <= instance.discount_value <= 100):
                raise CustomExceptionError(code=400, detail="Discount must be a percentage between 0 and 100")

def validate_free_product_discount(instance):
    if instance.discount_type == DiscountChoices.FREE_PRODUCT:
        if instance.min_quantity is None or instance.bonus_quantity is None or not instance.free_product:
            raise CustomExceptionError(code=400,
                                       detail='Free product discount requires min_quantity, bonus_quantity, and a free product.')

        elif instance.bonus_quantity > instance.min_quantity:
            raise CustomExceptionError(code=400,
                                       detail='Bonus quantity must be less than or equal to min_quantity.')

        elif instance.min_quantity <= 0 or instance.bonus_quantity <= 0:
            raise CustomExceptionError(code=400, detail='Min quantity and bonus quantity must be greater than 0.')

def validate_quantity_discount(instance):
    if instance.discount_type == DiscountChoices.QUANTITY_DISCOUNT:
        if instance.min_quantity is None:
            raise CustomExceptionError(code=400, detail='Quantity discount requires a min_quantity')

        if instance.discount_value_is_percent and instance.discount_value:
            if not (0 <= instance.discount_value <= 100):
                raise CustomExceptionError(code=400, detail="Discount must be a percentage between 0 and 100")

def validate_service_discount(instance):
    if instance.discount_type == DiscountChoices.SERVICE_DISCOUNT:
        if instance.service is None:
            raise CustomExceptionError(
                code=400,
                detail='Service discount requires a valid service.'
            )

        if instance.min_quantity is None:
            raise CustomExceptionError(
                code=400,
                detail='Service discount requires a min_quantity.'
            )
