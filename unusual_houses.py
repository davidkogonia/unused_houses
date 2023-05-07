import requests

token = 'secret'
link = 'http://ip_address/api'

response = requests.get(url=f'{link}/referencebooks/houses', cookies={'token': token}).json()
for item in response:
    params_get_user_by_house = {
        "page": 1,
        "per_page": 10000,
        "is_desc": True,
        "sort_field": "user_id",
        "queries_conditions": "and",
        "queries":
            [
                {
                    "field": "house_id",
                    "value": str(item['house_id']),
                    "condition": "equal"
                },
            ]
    }
    response_get_user_by_house = requests.post(url=f'{link}/users/extended_search', json=params_get_user_by_house,
                                               cookies={'token': token}).json()
    if response_get_user_by_house['total_rows'] == 0:
        print(item['house_id'])
