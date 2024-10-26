from apps.users.models import CustomUser


usernames = [
    '+998999999998',
    '+998999999997',
    '+998999999996',
    '+998999999995',
    '+998999999994',
    '+998999999993',
    '+998999999992',
    '+998999999991',
    '+998999999990',
    '+998999999989'
             ]

def generate_users(usernames):
    users = []
    for username in usernames:
        user = CustomUser(username=username, phone_number=username, fullname='Test User')
        users.append(user)
    CustomUser.objects.bulk_create(users)