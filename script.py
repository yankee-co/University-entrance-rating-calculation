    # pip install -r requirements.txt - Run un console to install all requirements instantly

from itertools import count
import requests, bs4, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By

# ratingScore = float(input('Enter your rating score: '))

# Enter links of specialities pages of vstup.ua site as values of the dictionary
# links = {
# 'speciality-number1':'speciality-link1',
# 'speciality-number2':'speciality-link2',
#  ...
# }

links = {
    # '121-ФІОТ':'https://vstup.osvita.ua/y2022/r27/174/986240/',
    # '121-ФПМ':'https://vstup.osvita.ua/y2022/r27/174/986241/',
    # '122':'https://vstup.osvita.ua/y2022/r27/174/1004661/',
    # '123-ФІОТ':'https://vstup.osvita.ua/y2022/r27/174/985216/',
    '123-ФПМ':'https://vstup.osvita.ua/y2022/r27/174/985217/',
    # '124':'https://vstup.osvita.ua/y2022/r27/174/984951/',
    # '125':'https://vstup.osvita.ua/y2022/r27/174/969362/',
    # '126':'https://vstup.osvita.ua/y2022/r27/174/988213/',
}

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument("--headless")


def click_button():
    try:
        time.sleep(0.2)
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, 'detail-link'))
        time.sleep(0.2)
    except Exception as _:
        pass
    return 0

for key, value in links.items():

    driver.get(value)

    for i in range(15):
        click_button()
        
    time.sleep(1)

    table = driver.find_element(By.CLASS_NAME, 'rwd-table')
    soup = bs4.BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')
    counter = 0
    tr_counter = 0
    priorities = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0
    }

    for tr in soup.findAll('tr', {'class':re.compile('rstatus')}):
        tr_counter += 1

        try:
            if float(str(tr.find('td', {'data-th':'Бал'}).text).strip()[0:7]) > 173.5:
                counter+=1

                # if '1' in tr.find('td', {'data-th':'П'}).text:
                #     priorities['1'] += 1

                # if '2' in tr.find('td', {'data-th':'П'}).text:
                #     priorities['2'] += 1

                # if '3' in tr.find('td', {'data-th':'П'}).text:
                #     priorities['3'] += 1

                # if '4' in tr.find('td', {'data-th':'П'}).text:
                #     priorities['4'] += 1

                # if '5' in tr.find('td', {'data-th':'П'}).text:
                #     priorities['5'] += 1
                if 'Рекомендовано' in tr.find('td', {'data-th':'Стан'}).text:
                    priorities['5'] += 1
            else:
                continue

        except ValueError:
            continue
    
    print(f'Speciality no. {key}')
    print(f'General place: {counter}')
    print(f'Applications: {tr_counter}')
    for key, value in priorities.items():
        print(f'Priority {key} - {value}')
    print('\n')

driver.close()