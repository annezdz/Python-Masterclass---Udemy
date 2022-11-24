import pytest


def get_data():
    return [
        ('trainer@way2automation.com', 'teste123'),
        ('trainer@way3automation.com', 'teste321'),
        ('trainer@batata.com', 'testeteste'),
    ]


@pytest.mark.parametrize('username,password', get_data())
def test_do_login(username, password):
    print(username, ' ---- ', password)
