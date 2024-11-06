import random
import string


def generate_unique_id():
    """ Generate a unique id for the Order model """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))
