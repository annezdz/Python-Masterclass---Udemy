import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# para usar mais de um browser ao mesmo tempo, ou seja, testando com
# chrome, firefox e edge
@pytest.fixture(params=['chrome', 'firefox', 'edge'], scope='function')
# PODE MUDAR PARA  session ou function - se for session abre uma vez o
# navegador, se for por function abre o x de testes (massa)

def get_browser(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
    elif request.param == 'firefox':
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
    elif request.param == 'edge':
        driver = webdriver.Edge(
            executable_path=EdgeChromiumDriverManager().install())
    driver.get('https://www.facebook.com')
    driver.maximize_window()
    yield driver
    driver.quit()

# def tear_down_function():
#     driver.quit()
