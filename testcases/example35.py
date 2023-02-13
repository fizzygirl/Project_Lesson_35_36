# https://dumskaya.net/
# try:

def register_user():
    import time
    from factory.new_user import User
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    import os
    from selenium.webdriver.common.by import By
    from xpath.registration_page import registration
    from xpath.home_page import home
    from details.registration_page import reg_page

    my_user = User()
    options = ChromeOptions()
    foptions = FirefoxOptions()
    options.headless = False  # True False Запуск теста без включения браузера

    path = f'{os.getcwd()}/drivers/chromedriver'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://dumskaya.net/'
    e1_page = reg_page()
    driver.maximize_window()
    driver.get(url)

    enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', home.xpath_enter_button)))
    enter_button.click()
    enter_registration_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', home.xpath_enter_registration_button)))
    enter_registration_button.click()

    e1_page.email_field(driver, my_user.email)

    e1_page.nick_field(driver, my_user.nick)

    e1_page.password_field(driver, my_user.password)

    # e1_page.password2_field(driver, my_user.password)

    e1_page.female_radio(driver)

    register_gender_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(('xpath', registration.xpath_register_button)))
    register_gender_button.click()



    # n = '''Пользователь с таким ником уже зарегистрирован. Придумайте другой
    #         Укажите ник.'''

    n = '''Пароли не совпадают'''


    # time.sleep(5000)
    # login_textarea = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located(('xpath', '//tr/td/div[contains(text()," ")]')))
    # login = login_textarea.text
    # login_err = login_textarea.text
    password2_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(('xpath', '//tr/td/div[contains(text()," ")]')))
    # password2 = password2_button.text
    password2_err = password2_button.text

    driver.close()
    # if n == login_err:
    #     print('Greate!')

    if n == password2_err:
        print("Greate!")

    return n, password2_err #login_err  # 'Пользователь с таким ником уже зарегистрирован. Придумайте другой'
    # return  login_error, 'Пользователь с таким ником уже зарегистрирован. Придумайте другой'


if __name__ == '__main__':
    print(register_user())

# except BaseException:
#     print('Passwords do not match')
