from conftest import Settings
from use_cases.resources import Api1
from use_cases.post_requests import Api2
from use_cases.delete_request import Api3


class TestAll(Settings):

    @staticmethod
    def test_guest_can_get_all_users_list():
        Api1.get_all_users_list()


    @staticmethod
    def test_logged_user_can_create_users():
        Api2.create_new_user()


    @staticmethod
    def test_logged_user_can_delete_users():
        Api3.delete_user()