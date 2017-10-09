import os
import configparser


def read_conf(env_name):
    home = os.path.expanduser("~")
    file = '.kong'
    file_path = os.path.join(home, file)

    try:
        if os.path.exists(file_path):
            pygd_parser = configparser.ConfigParser()
            pygd_parser.read(file_path)
            return pygd_parser[env_name]
        else:
            raise FileNotFoundError
    except Exception as error:
        raise error
