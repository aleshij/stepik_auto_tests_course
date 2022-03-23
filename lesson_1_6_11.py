from selenium import webdriver
import time

# useragent = UserAgent()
# options.set_preference('general.useragent.override', useragent.firefox)

options = webdriver.FirefoxOptions()

options.set_preference('general.useragent.override',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0')
options.set_preference('dom.webdriver.enable', False)

# Запустить в фоне
# options.headless = True

# Используется Firefox, скачайте вебдрайвер и укажите к нему путь!
browser = webdriver.Firefox(
    executable_path="D:\\Dropbox\\Python\\Selenium\\geckodriver.exe",
    options=options
)

# команда time.sleep устанавливает паузу в N секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

link = "http://suninjuly.github.io/registration1.html" # проходит на этой страницу
# link = "http://suninjuly.github.io/registration2.html" # падает на этой странице

try:

    browser.get(link)

    # Уникальные селекторы
    input1 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
    input3.send_keys("Ivan@Petrov.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


# except Exception as ex:
#     print(ex)


finally:
    time.sleep(2)
    browser.quit()
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
