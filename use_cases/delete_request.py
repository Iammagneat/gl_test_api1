from conftest import Settings
import requests
import logging

class Api3:
    LOG = logging.getLogger(__name__)

    @staticmethod
    def delete_user():
        endpoint = '/public-api/users/'
        user_id = Settings.user_id
        headers = {'Authorization': 'Bearer ' + Settings.token}
        response = requests.delete(Settings.base_url + endpoint + user_id,
                                   headers=headers)
        code = response.json()['code']
        Api3.LOG.info('delete_user')
        assert code == 204 or code == 404, f'{response.text}'
        if code == 204:
            print('DELETED USER:', response.json()['data']['id'], end=' ')
        else: print(code, end=' ')
        return response


if __name__ == '__main__':
    print(Api3.delete_user().json())
