import pytest


@pytest.fixture(scope='module')
def setup():
    print('Creating DB Connection')

    yield
    print('Closing DB Connection')


@pytest.fixture(scope='function')
def before():
    print('Launching Browser')

    yield
    print('Closing Browser')


@pytest.mark.usefixtures("setup", "before")
def test_do_login():
    print('Executing login test')


@pytest.mark.usefixtures("setup", "before")
def test_user_reg():
    print('Executing user reg test')
