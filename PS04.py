from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random
"""
Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.

1. Спрашивать у пользователя первоначальный запрос.

2. Переходить по первоначальному запросу в Википедии.

3. Предлагать пользователю три варианта действий:

листать параграфы текущей статьи;
перейти на одну из связанных страниц — и снова выбор из двух пунктов:
- листать параграфы статьи;

- перейти на одну из внутренних статей.

выйти из программы.
В поле для ответа загрузи ссылку на Git.
"""
print("Википедия-версия консольного режима")
Request =input("Что хотите найти?")

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")



assert "Википедия" in browser.title
#time.sleep(10)
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(Request)
search_box.send_keys(Keys.RETURN)
job = True
while job:
    if "Результаты для" in browser.title:
        paragraphs = browser.find_elements(By.CLASS_NAME, "mw-search-result-heading")
    else:
        paragraphs = browser.find_elements(By.TAG_NAME, "p")

    for paragraph in paragraphs:
       print(paragraph.text)
       #link = paragraph.find_element(By.TAG_NAME, "a").get_attribute("href")
       #print(link)
       comand = input("Введите команду(n/c/e) (n - перейти на следующую статью (next), c - выбрать статью (Choose), e - выход (Exit) :")
       if comand == "c":
        link = paragraph.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        break
       elif comand == "e":
        job = False
        break
       elif comand == "n":
        pass
       else:
        print("Неверная команда")

#mw-search-result-heading















#browser = webdriver.Chrome()
#browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")


#hatnotes = []

#for element in browser.find_elements(By.TAG_NAME, "div"):
#    print(element.get_attribute("class"))
#    cl = element.get_attribute("class")
#    if cl == "hatnote navigation-not-searchable":
#        hatnotes.append(element)


#print(hatnotes)
#hatnotes = random.choice(hatnotes)

#link = hatnotes.find_element(By.TAG_NAME, "a").get_attribute("href")
#print(link)
#browser.get(link)
#browser.save_screenshot()
#time.sleep(30)

#paragraphs = browser.find_elements(By.TAG_NAME, "p")

#for paragraph in paragraphs:
#    print(paragraph.text)
#    input()

#assert "Википедия" in browser.title
#time.sleep(10)
#search_box = browser.find_element(By.ID, "searchInput")
#search_box.send_keys("Солнечная система")
#search_box.send_keys(Keys.RETURN)

#time.sleep(10)
#a = browser.find_element(By.LINK_TEXT, "Солнечная система")
#a.click()
#browser.quit()