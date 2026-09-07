import os
import requests

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'DEMO_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'DEMO_CHAT_ID')


def format_alert(level: str, title: str, details: str) -> str:
    return f'[{level.upper()}] {title}\n{details}'


def send_alert(message: str) -> dict:
    if TOKEN.startswith('DEMO_') or CHAT_ID.startswith('DEMO_'):
        return {'sent': False, 'mode': 'demo', 'message': message}

    response = requests.post(
        f'https://api.telegram.org/bot{TOKEN}/sendMessage',
        json={'chat_id': CHAT_ID, 'text': message},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    print(send_alert(format_alert('info', 'Service status', 'All monitored services are healthy.')))
