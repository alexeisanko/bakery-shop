from django.conf import settings
import requests
import random


def send_activate_code(number_phone: str) -> tuple:
    code = _generate_code()
    url = f'https://{settings.API_SMS_LOGIN}:{settings.API_SMS_TOKEN}@gate.smsaero.ru/v2/sms/send?' \
          f'number={number_phone}' \
          f'&text={settings.TEXT_REGISTRATION_SMS} "{code}"' \
          f'&sign={settings.SIGN_NAME}'
    response = requests.get(url).json()
    success = response['success']
    return success, code
    # return True, 1234


def _generate_code() -> int:
    code = random.randint(1000, 9999)
    return code
