import requests
from django.conf import settings


def telepush_send(order_data: dict) -> None:
    """
    Отправляет сообщение с информацией о заявке в инстанс telepush (Telegram).
    :param order_data: Словарь с сериализованными данными полученными из заявки.
    :return: None.
    """
    telepush_url = settings.TELEPUSH_URL
    recipient_token = settings.RECIPIENT_TOKEN

    message = "Клиент не оставил сообщения"
    if order_data.get("message"):
        message = f"Клиент оставил сообщение: {order_data.get('message')}"

    data = {"text": f"*С сайта kajimacode.ru поступила новая заявка!*\n"
                    f"Имя: {order_data.get('name')}\n"
                    f"Почта: {order_data.get('mail')}\n"
                    f"{message}"}
    url = f"{telepush_url}/api/messages/{recipient_token}"
    response = requests.post(
        url, json=data, headers={"Content-Type": "application/json"}
    )
