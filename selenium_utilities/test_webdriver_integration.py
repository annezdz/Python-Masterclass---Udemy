import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


def get_data():
    return [
        ('trainer@way2automation.com', 'teste123'),
        ('trainer@way3automation.com', 'teste321'),
        ('trainer@batata.com', 'testeteste'),
    ]


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='do_login',
                      attachment_type=AttachmentType.PNG)


@pytest.mark.usefixtures('log_on_failure')
@pytest.mark.parametrize('username,password', get_data())
def test_do_login(username, password, get_browser):
    driver = get_browser
    driver.find_element(By.ID, 'email').send_keys(username)
    driver.find_element(By.ID, 'pass').send_keys(password)
    # assert 1 == 2 - PARA FALHAR - SCREENSHOT TESTE

    # incluir screenshot no AllureReports
    # allure.attach(driver.get_screenshot_as_png(), name='do_login',
    #               attachment_type=AttachmentType.PNG)

# para rodar o testes em Paralell mode, instalar -> pip install pytest-xdist
# para instalar o html reports -> pip install pytest-html

# para rodar o Allure Reports
# Configurar ele nas variaveis de ambiente
# instalar ele em Settings - Project > Python Interpreter

# pytest test_webdriver_integration.py --alluredir="./allurereports"
# Gerar o Allure Reports
# allure serve ./allurereports

# pimeiro rodar os testes e depois rodar o Allure serve
# pytest -s -v --alluredir "./allurereports" e depois allure serve ./allurereports
