from os import getenv
from getpass import getpass
from keyring import get_password, set_password, set_keyring
from keyrings.cryptfile.cryptfile import CryptFileKeyring
from hashlib import md5


def setup_keyring(user_account):
    backend = getenv("PYTHON_KEYRING_BACKEND")
    if backend == "keyrings.cryptfile.cryptfile.CryptFileKeyring" or is_notebook():
        kr = CryptFileKeyring()
        kr.keyring_key = getenv("KEYRING_CRYPTFILE_PASSWORD") or hash_value(user_account)
        set_keyring(kr)


def hash_value(val):
    # hashlib.md5("whatever your string is".encode('utf-8')).hexdigest()
    return md5(val.encode('utf-8')).hexdigest()


def ft_get_password(key, user_account):
    return get_password(key, user_account)


def ft_check_password(user_account):
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


def ft_set_password(user_account):
    set_password(
        "fugle_trade_sdk:account",
        user_account,
        getpass("Enter esun account password:\n"))
    set_password(
        "fugle_trade_sdk:cert",
        user_account,
        getpass("Enter cert password:\n"))


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
