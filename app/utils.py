def validate_response(response):
    """
    Проверить, является ли ответ от API валидным.
    :param response: Ответ от API.
    :return: True, если ответ валиден, иначе False.
    """
    expected_fields = ['id', 'question', 'answer', 'created_at']
    if not isinstance(response, list) or len(response) == 0:
        return False
    if not all(field in response[0] for field in expected_fields):
        return False
    return True
