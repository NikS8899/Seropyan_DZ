# coding: Windows-1251


from unittest.mock import patch
from src.external_api import transaction_amount


@patch('requests.get')
def test_get_github_user_info(mock_get):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                               'info': {'timestamp': 1722102724, 'rate': 85.972867},
                                               'date': '2024-07-27', 'result': 706814.749568}

    assert transaction_amount({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }) == 706814.749568
    # mock_get.assert_called_once_with('https://api.github.com/users/testuser')
