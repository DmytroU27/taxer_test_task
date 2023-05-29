from pages.base_page import BasePage
from src.locators import BasePageLocators
from src.enums.global_enums import GlobalErrorMessages
from utils import utils
from configuration import BASE_PAGE_URL, TEST_DATA_FOLDER_PATH
import pytest



@pytest.mark.parametrize("file_name", [
    'cert',
    'cert2',
    'czo_2017',
    'ekpp_sign_2014',
    'idd_2019',
    'privat_2018',
    'Нестеренко_Володимир_Борисович_(Тест)-8101916',
    'Сухаренко_Олег_Андрiйович_(Тест)-8101900',
    'Таксер Тест Тестович',
    'Тестовий_платник_4_(Тест)-8101906',
    'Тестувальник Tellipse 1111'
])
def test_that_common_name_in_table_same_as_in_list(browser, file_name):
    page = BasePage(browser, BASE_PAGE_URL)
    page.open()
    page.accept_project()
    path = TEST_DATA_FOLDER_PATH + f'{file_name}.cer'
    page.drag_and_drop_file(path)
    assert page.browser.find_element(*BasePageLocators.CERT_IN_LIST).text == \
           page.browser.find_element(*BasePageLocators.COMMON_NAME_DATA).text, GlobalErrorMessages.COMMON_NAME_ERROR.value


@pytest.mark.parametrize("file_name", [
    'cert',
    'cert2',
    'czo_2017',
    'ekpp_sign_2014',
    'idd_2019',
    'privat_2018',
    'Нестеренко_Володимир_Борисович_(Тест)-8101916',
    'Сухаренко_Олег_Андрiйович_(Тест)-8101900',
    'Таксер Тест Тестович',
    'Тестовий_платник_4_(Тест)-8101906',
    'Тестувальник Tellipse 1111'
])
def test_that_the_subject_common_name_in_table_is_correct(browser, file_name):
    page = BasePage(browser, BASE_PAGE_URL)
    page.open()
    page.accept_project()
    path = TEST_DATA_FOLDER_PATH + f'{file_name}.cer'
    page.drag_and_drop_file(path)
    assert page.browser.find_element(*BasePageLocators.COMMON_NAME_DATA).text == utils.parsing_cert(file_name)[0], \
        GlobalErrorMessages.SUBJECT_CN_ERROR.value


@pytest.mark.parametrize("file_name", [
    'cert',
    'cert2',
    'czo_2017',
    'ekpp_sign_2014',
    'idd_2019',
    'privat_2018',
    'Нестеренко_Володимир_Борисович_(Тест)-8101916',
    'Сухаренко_Олег_Андрiйович_(Тест)-8101900',
    'Таксер Тест Тестович',
    'Тестовий_платник_4_(Тест)-8101906',
    'Тестувальник Tellipse 1111'
])
def test_that_the_issuer_common_name_in_table_is_correct(browser, file_name):
    page = BasePage(browser, BASE_PAGE_URL)
    page.open()
    page.accept_project()
    path = TEST_DATA_FOLDER_PATH + f'{file_name}.cer'
    page.drag_and_drop_file(path)
    assert page.browser.find_element(*BasePageLocators.ISSUER_CN_DATA).text == utils.parsing_cert(file_name)[1], \
        GlobalErrorMessages.ISSUER_CN_ERROR.value


@pytest.mark.parametrize("file_name", [
    'cert',
    'cert2',
    'czo_2017',
    'ekpp_sign_2014',
    'idd_2019',
    'privat_2018',
    'Нестеренко_Володимир_Борисович_(Тест)-8101916',
    'Сухаренко_Олег_Андрiйович_(Тест)-8101900',
    'Таксер Тест Тестович',
    'Тестовий_платник_4_(Тест)-8101906',
    'Тестувальник Tellipse 1111'
])
def test_that_the_valid_from_data_in_table_is_correct(browser, file_name):
    page = BasePage(browser, BASE_PAGE_URL)
    page.open()
    page.accept_project()
    path = TEST_DATA_FOLDER_PATH + f'{file_name}.cer'
    page.drag_and_drop_file(path)
    data_from_parser = str(utils.parsing_cert(file_name)[2])
    data_from_table = page.browser.find_element(*BasePageLocators.VALID_FROM_DATA).text
    assert data_from_parser[:10] == data_from_table[:10], GlobalErrorMessages.VALID_FROM_DATA_ERROR.value


@pytest.mark.parametrize("file_name", [
    'cert',
    'cert2',
    'czo_2017',
    'ekpp_sign_2014',
    'idd_2019',
    'privat_2018',
    'Нестеренко_Володимир_Борисович_(Тест)-8101916',
    'Сухаренко_Олег_Андрiйович_(Тест)-8101900',
    'Таксер Тест Тестович',
    'Тестовий_платник_4_(Тест)-8101906',
    'Тестувальник Tellipse 1111'
])
def test_that_the_valid_till_data_in_table_is_correct(browser, file_name):
    page = BasePage(browser, BASE_PAGE_URL)
    page.open()
    page.accept_project()
    path = TEST_DATA_FOLDER_PATH + f'{file_name}.cer'
    page.drag_and_drop_file(path)
    data_from_parser = str(utils.parsing_cert(file_name)[3])
    data_from_table = page.browser.find_element(*BasePageLocators.VALID_TILL_DATA).text
    assert data_from_parser[:10] == data_from_table[:10], GlobalErrorMessages.VALID_TILL_DATA_ERROR.value



