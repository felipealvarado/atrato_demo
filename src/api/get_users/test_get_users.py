import pytest
from .get_users import Users

@pytest.fixture
def get_users_instance():
    '''Returns a Risk Calculator instance'''
    return Users()

def test_get_users(get_users_instance):
    get_users_instance.get_info_users()
