import requests

FB_AUTH_URL = 'https://graph.accountkit.com/v1.1/me?access_token='


def get_validated_phone(access_token):
    try:
        resp = requests.get(FB_AUTH_URL + access_token).json()
        phone = resp['phone']['number']
        return phone
    except Exception as e:
        return None