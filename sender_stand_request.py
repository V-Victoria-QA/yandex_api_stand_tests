import configuration
import requests
import data
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=user_body,
                         headers=data.headers)  # а здесь заголовки
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
# response = post_new_user(data.user_body);
# response = post_products_kits(data.product_ids);
# print(response.status_code)
# print(response.json())







