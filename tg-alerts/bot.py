import os
import requests

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')
DRY_RUN = os.getenv('DRY_RUN', '1') == '1'


def format_alert(level: str, title: str, details: str) -> str:
    return f'[{level.upper()}] {title}\n{details}'


def send_alert(message: str) -> dict:
    if DRY_RUN or not TOKEN or not CHAT_ID:
        return {'sent': False, 'mode': 'dry_run', 'message': message}

    response = requests.post(
        f'https://api.telegram.org/bot{TOKEN}/sendMessage',
        json={'chat_id': CHAT_ID, 'text': message},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    msg = format_alert('info', 'Service status', 'All monitored services are healthy.')
    print(send_alert(msg))
