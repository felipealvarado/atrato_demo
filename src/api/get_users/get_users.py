import requests
from pytest_check import check

class Users(object):

    def __init__(self):
        pass

    def get_info_users(self):
        url = 'http://localhost:5000/user'
        print(f"Making request for GET users")
        r_get_users = requests.get(url, headers={"content-type": "application/json"})
        check.equal(len(r_get_users.json()), 9)

    #if __name__ == "__main__":
    #   get_info_users()
