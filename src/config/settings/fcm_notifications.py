import os

#   FCM SERVER KEY
FCM_SERVER_KEY = os.environ['FCM_SERVER_KEY']

FCM_DJANGO_SETTINGS = {
    #   THIS IS FCM KEY
    "FCM_SERVER_KEY": FCM_SERVER_KEY,
    #   One user is allowed more than one device
    "ONE_DEVICE_PER_USER": False,
}
