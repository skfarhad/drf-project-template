import random


def get_key():
    return ''.join(
        random.SystemRandom().choice(
            'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        ) for i in range(50)
    )


print('New Key:' + get_key())
