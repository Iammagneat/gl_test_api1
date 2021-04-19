from conftest import Settings
import requests
import logging


class Api1:
    LOG = logging.getLogger(__name__)

    @staticmethod
    def get_all_users_list():
        endpoint = '/public-api/users'
        response = requests.get(Settings.base_url+endpoint)
        Api1.LOG.info('get_all_users_list')
        assert response.status_code == 200, f'{response.text}'
        return response


    @staticmethod
    def get_all_posts():
        endpoint = '/public-api/posts'
        response = requests.get(Settings.base_url + endpoint)
        Api1.LOG.info('get_all_posts')
        assert response.status_code == 200, f'{response.text}'
        return response


    @staticmethod
    def get_all_comments():
        endpoint = '/public-api/comments'
        response = requests.get(Settings.base_url + endpoint)
        Api1.LOG.info('get_all_comments')
        assert response.status_code == 200, f'{response.text}'
        return response



    @staticmethod
    def get_all_todos():
        endpoint = '/public-api/todos'
        response = requests.get(Settings.base_url + endpoint)
        assert response.status_code == 200, f'{response.text}'
        return response


    @staticmethod
    def get_all_products():
        endpoint = '/public-api/products'
        response = requests.get(Settings.base_url + endpoint)
        assert response.status_code == 200, f'{response.text}'
        return response


if __name__ == '__main__':
    print(Api1.get_all_users_list().json())
    print(Api1.get_all_posts().json())
    print(Api1.get_all_comments().json())
    print(Api1.get_all_todos().json())
    print(Api1.get_all_products().json())
