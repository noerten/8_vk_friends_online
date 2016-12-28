try:
    import config
except ImportError:
    pass
import getpass

import vk


APP_ID = '5798454'


def get_user_login():
    user_login = input("Enter your login or press 'Enter' to get it from"
                       " config.py, that is placed in the script's folder: ")
    if not user_login:
        user_login = config.USER_LOGIN
    return user_login


def get_user_password():
    user_password = getpass.getpass("Enter your password or press 'Enter' to "
                                    "get it from config.py, that is placed in "
                                    "the folder with script: ")
    if not user_password:
        user_password = config.USER_PASSWORD
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
        )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_online_ids)
    return friends_online


def output_friends_to_console(friends_online):
    print('Friends online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
