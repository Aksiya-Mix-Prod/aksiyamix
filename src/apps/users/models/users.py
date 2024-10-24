from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db import models

from apps.base.models import AbstractBaseModel
from apps.base.exceptions import CustomExceptionError
from apps.base.utils import Regions, District
from apps.users.utils import CustomUserManager


class CustomUser(AbstractBaseModel, AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    class Gender(models.IntegerChoices):
        MAN = 1, _('Male')
        WOMAN = 2, _('Female')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["fullname"]

    objects = CustomUserManager()

    username = models.CharField(_("username"), max_length=150, unique=True)
    fullname = models.CharField(_("full name"), max_length=150)

    phone_number = models.CharField(max_length=13, blank=True, null=True, validators=[
        RegexValidator(
            regex=r"^\+998\d{9}$",
            message="Example: +998 XXXXXXXXX",
            code="uzb_phone_number_validation"
        )
    ])
    email = models.EmailField(_("email address"), blank=True, null=True)

    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    
    birthday = models.DateField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, blank=True, null=True)
    
    region = models.PositiveSmallIntegerField(choices=Regions.choices, blank=True, null=True)
    district = models.CharField(choices=District.choices, blank=True, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_spam = models.BooleanField(default=False)
    spam_counts = models.PositiveIntegerField(default=0)

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        """Check email or phone number"""
        if not self.email and not self.phone_number:
            raise CustomExceptionError(code=400, detail='Email or phone number is required')
        
        """Saving username if not username"""
        if not self.username:
            self.username = self.phone_number or self.email

        """Saving region if exist district"""
        if self.district:
            self.region = self.district.split('X')[0]

        super().save(*args, **kwargs)
    
    class Meta:
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username