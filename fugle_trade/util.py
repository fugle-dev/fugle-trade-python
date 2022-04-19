from getpass import getpass
from keyring import get_password, set_password
from keyrings.cryptfile.cryptfile import CryptFileKeyring
from hashlib import md5


def hash_value(val):
    # hashlib.md5("whatever your string is".encode('utf-8')).hexdigest()
    return md5(val.encode('utf-8')).hexdigest()


def ft_get_password(key, user_account):
    if is_notebook():
        kr = CryptFileKeyring()
        kr.keyring_key = hash_value(user_account)
        return kr.get_password(key, user_account)
    else:
        return get_password(key, user_account)


def ft_check_password(user_account):
    if is_notebook():
        kr = CryptFileKeyring()
        kr.keyring_key = hash_value(user_account)
        __check_password(user_account, kr.get_password, kr.set_password)
    else:
        __check_password(user_account, get_password, set_password)


def ft_set_password(user_account):
    if is_notebook():
        kr = CryptFileKeyring()
        kr.keyring_key = hash_value(user_account)
        __set_password(user_account, kr.get_password, kr.set_password)
    else:
        __set_password(user_account, get_password, set_password)


# from https://stackoverflow.com/a/39662359
def is_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


def __check_password(user_account, get_password, set_password):
    if not get_password("fugle_trade_sdk:account", user_account):
        set_password(
            "fugle_trade_sdk:account",
            user_account,
            getpass("Enter esun account password:\n"))

    if not get_password("fugle_trade_sdk:cert", user_account):
        set_password(
            "fugle_trade_sdk:cert",
            user_account,
            getpass("Enter cert password:\n"))


def __set_password(user_account,  get_password, set_password):
    set_password(
        "fugle_trade_sdk:account",
        user_account,
        getpass("Enter esun account password:\n"))
    set_password(
        "fugle_trade_sdk:cert",
        user_account,
        getpass("Enter cert password:\n"))
