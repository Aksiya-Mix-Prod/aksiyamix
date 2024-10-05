from django.db import models


class District(models.IntegerChoices):
    # Tashkent Districts
    TASHKENT_CITY = 0, 'Tashkent City'
    YUNUSABAD = 1, 'Yunusabad'
    MIRABAD = 2, 'Mirabad'
    CHILANZAR = 3, 'Chilanzar'

    # Fergana Districts
    FERGANA_CITY = 4, 'Fergana City'
    KUVA = 5, 'Kuva'
    RISHTAN = 6, 'Rishtan'

    # Samarkand Districts
    SAMARKAND_CITY = 7, 'Samarkand City'
    URGUT = 8, 'Urgut'
    KATTALIK = 9, 'Kattalik'

    # Bukhara Districts
    BUKHARA_CITY = 10, 'Bukhara City'
    JONDOR = 11, 'Jondor'
    GIDRO = 12, 'Gidro'

    # Andijan Districts
    ANDIJAN_CITY = 13, 'Andijan City'
    ASAKA = 14, 'Asaka'
    KURGANTEPA = 15, 'Kurgantepa'

    # Navoi Districts
    NAVOI_CITY = 16, 'Navoi City'
    ZARAFSHAN = 17, 'Zarafshan'
    UCHKUDUK = 18, 'Uchkuduk'

    # Qashqadaryo Districts
    QARSHI = 19, 'Qarshi'
    KOSON = 20, 'Koson'
    SHAKHRISABZ = 21, 'Shakhrisabz'

    # Jizzakh Districts
    JIZZAKH_CITY = 22, 'Jizzakh City'
    PASTDARGOM = 23, 'Pastdargom'
    FORISH = 24, 'Forish'

    # Khorezm Districts
    URGENCH = 25, 'Urgench'
    KHIVA = 26, 'Khiva'
    YANGIYER = 27, 'YangiYer'

    # Kokand Districts
    KOKAND_CITY = 28, 'Kokand City'
    RUSTAMYON = 29, 'Rustamyon'
    FAYZABAD = 30, 'Fayzabad'

    # Termez Districts
    TERMEZ_CITY = 31, 'Termez City'
    BOYSUN = 32, 'Boysun'
    SHERABAD = 33, 'Sherabad'

    OTHER = 34, 'Other'  # Option for any other district not listed