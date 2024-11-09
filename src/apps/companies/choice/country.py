from django.db import models


class Country(models.IntegerChoices):
    TASHKENT = 0, "Tashkent"
    FERGANA = 1, "Fergana"
    SAMARKAND = 2, "Samarkand"
    BUKHARA = 3, "Bukhara"
    ANDIJAN = 4, "Andijan"
    NAVOI = 5, "Navoi"
    QARSHI = 6, "Qarshi"
    JIZZAKH = 7, "Jizzakh"
    KHOREZM = 8, "Khorezm"
    KOKAND = 9, "Kokand"
    TERMEZ = 10, "Termez"
    OTHER = 11, "Other"
