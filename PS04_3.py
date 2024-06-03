from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def print_full_text(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    text = soup.get_text()
    print(text)
    input("Нажмите Enter для продолжения...")

def search_wikipedia():

    driver = webdriver.Chrome()

    try:
        while True:
            query = input("Введите ваш запрос: ")
            driver.get("https://ru.wikipedia.org")

            search_box = driver.find_element(By.NAME, "search")
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            time.sleep(2)

            while True:
                print("\n--- {} ---\n".format(query))
                print("1. Показать весь текст текущей статьи")
                print("2. Перейти на одну из связанных страниц")
                print("3. Выйти из программы")
                choice = input("Выберите действие (1, 2, 3): ")

                if choice == '1':
                    print_full_text(driver)
                elif choice == '2':
                    links = driver.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href and not(contains(@href, 'redlink=1'))]")
                    print("\nСвязанные страницы:")
                    for index, link in enumerate(links):
                        print(f"{index + 1}. {link.text} ({link.get_attribute('href')})")

                    link_choice = int(input("Выберите номер связанной страницы для перехода: ")) - 1
                    if 0 <= link_choice < len(links):
                        driver.get(links[link_choice].get_attribute("href"))
                        time.sleep(2)
                    else:
                        print("Некорректный выбор.")
                elif choice == '3':
                    print("Выход из программы.")
                    return
                else:
                    print("Некорректный выбор. Попробуйте снова.")
    finally:
        driver.quit()

if __name__ == "__main__":
    search_wikipedia()
