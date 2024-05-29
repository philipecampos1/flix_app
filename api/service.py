import requests


class Auth:

    def __init__(self):
        self.__base_url = 'https://philipecampos.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_tokken(self, username, passowrd):
        auth_payload = {
            'username': username,
            'password': passowrd,
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Error to authenticate.Status code: {auth_response.status_code}'}
