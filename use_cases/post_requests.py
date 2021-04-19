from conftest import Settings
import requests
import logging
import random

class Api2:
    LOG = logging.getLogger(__name__)
    random_num = random.randint(1,500)

    @staticmethod
    def create_new_user():
        endpoint = '/public-api/users'
        gender = random.choice(['Male', 'Female'])
        name = f'TestUser{Api2.random_num}'
        status = random.choice(['Active', 'Inactive'])
        email = f'{name}@email.com'
        userdata = {
            'name':name,
            'gender':gender,
            'email': email,
            'status': status}
        headers = {'Authorization': 'Bearer ' + Settings.token}
        response = requests.post(Settings.base_url + endpoint,
                                 headers=headers, data=userdata)
        Api2.LOG.info('create_new_user')
        assert response.json()['code'] == 201, f'{response.text}'
        print('NEW USER ID:', response.json()['data']['id'], end=' ')
        return response


    @staticmethod
    def create_user_post():
        endpoint = f'/public-api/users/{Settings.user_id}/posts'
        data = {
            'title': 'Qwert',
            'body': 'Oh, La-la!'}
        headers = {'Authorization': 'Bearer ' + Settings.token}
        response = requests.post(Settings.base_url + endpoint,
                                 headers=headers, data=data)
        Api2.LOG.info('create_user_post')
        return response


if __name__ == '__main__':
    print(Api2.create_new_user().json())
    print(Api2.create_user_post().json())
