from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def getLotteMartStoreInfo(result):
    # USB: usb_device_handle_win.cc:1049 시스템에 부착된 장치가 작동하지 않습니다.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome('./TopMart/chromedriver.exe',options=options)


    for i in range(2, 113):
        wd.get('https://www.lotteon.com/p/lotteplus/offlinestore/offLineStoreInfo?mall_no=4')
        time.sleep(0.3)

        wd.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/div[1]/div/ul/li[1]/button').click()
        time.sleep(0.3)
        wd.find_element(By.XPATH,f'//*[@id="content"]/div/div/div[2]/div[2]/div/table/tr[{i}]/td[1]/a').click()
        time.sleep(0.3)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        store_name = soup.select('div.storeName')[0].string.strip()
        print(store_name)
        store_address = soup.select('div.branchInfo > div.content')[0].string
        print(store_address)
        store_contact = soup.select('div.branchInfo > div.content > a')[0].string
        print(store_contact)
        wd.find_element(By.XPATH,'//*[@id="modals-container"]/div/div/div[2]/div/button').click()
        time.sleep(0.3)

def main():
    result = []
    print('롯데마트 매장 크롤링 >>>')
    getLotteMartStoreInfo(result)

    # columns = ['store','address','phone']
    # topmart_df= pd.DataFrame(result, columns=columns)
    # topmart_df.to_csv('./topmart_shop_info.csv',index=True, encoding='utf-8')
   
    # print('저장완료')

    

if __name__ == '__main__':
    main()