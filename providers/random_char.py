import random
import string


def random_string(number):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(number))


def random_email(number):
    return random_string(number) + "@gmail.com"
