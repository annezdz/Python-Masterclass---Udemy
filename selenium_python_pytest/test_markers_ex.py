import pytest


# incluindo tags por ambiente/teste
@pytest.mark.functional
def test_login():
    print('Executing login test')


@pytest.mark.regression
def test_user_reg():
    print('Executing User reg test')


@pytest.mark.functional
def test_compose_email():
    print('Executing compose email test')


# pytest test_markers_ex.py -s -v -k login
# para rodar um teste via cmd

# pytest test_markers_ex.py -s -v -k "not login"
# para NÃO rodar um teste

# para rodar os testes por tag / marcação  -> 2 passed, 1 deselected, 3 warnings in 0.87s
# pytest test_markers_ex.py -s -v -k functional

# Para pular uma tag - marcação -> 1 passed, 2 deselected in 0.05s
# pytest test_markers_ex.py -s -v -k "not functional"

#Skipped: unconditional skip -> ======================== 3 passed, 1 skipped in 0.91s =========================
@pytest.mark.skip
def test_skip():
    print('skipping test')
