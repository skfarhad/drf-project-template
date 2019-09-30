import random


def get_key():
    ''.join(
        random.SystemRandom().choice(
            'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        ) for i in range(50)
    )
