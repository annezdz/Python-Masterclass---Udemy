from unittest import TestCase

import pytest


# class Teste(TestCase):
#
#     def test_validate_titles(self):
#         expected_title = 'Google.com'
#         actual_title = 'Gmail.com'
#
#         # if actual_title == expected_title:
#         #     print('Test case pass')
#         # else:
#         #     print('Test case fail')
#         self.assertEqual(expected_title, actual_title)

def test_validate_titles():
    expected_title = 'Google.com'
    actual_title = 'Gmail.com'
    title = 'This is Gmail website'

    # if actual_title == expected_title:
    #     print('Test case pass')
    # else:
    #     print('Test case fail')
    print('Beginning')
    assert expected_title == actual_title, "Titles are not matching"
    assert 'Gmails' in title, 'Gmail does not exists in the title'
    assert False, 'Forcefully failing the test'
    print('Ending')

#pip install pytest-soft-assertions

#rodar com soft asserts
#pytest test_validate_titles.py -s -v --soft-asserts
