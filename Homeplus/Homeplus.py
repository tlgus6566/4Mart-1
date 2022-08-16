import time
import requests
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import pandas as pd
import matplotlib.font_manager as fm
import urllib.request


from selenium.webdriver.common.by import By
from selenium import webdriver
from matplotlib import rc
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getHomeplusStoreInfo(result):
    # USB: usb_device_handle_win.cc:1049 시스템에 부착된 장치가 작동하지 않습니다.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome('./TopMart/chromedriver.exe',options=options)

    wd.get('https://corporate.homeplus.co.kr/STORE/HyperMarket.aspx')
    time.sleep(0.3)
    
    # 서울특별시
    for i in range(1,20):
        wd.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_Region_Code"]/option[2]').click()
        time.sleep(0.3)
        wd.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_Region_Code"]/option[1]').click()
        time.sleep(0.3)
        wd.find_element(By.XPATH,f'//*[@id="content"]/div/div/div/ul/li[{i}]/div[1]/h3/span[2]/a').click()
        time.sleep(0.3)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        store_name = soup.select('div.col-lg-4 > h3.type > span.name')[0].string.strip()
        print(store_name)
        store_address = soup.select('div.tab-content > div#store_detail01 > table.table > tbody > tr > td')[0].string.rstrip()
        print(store_address)
    
        wd.find_element(By.XPATH,'//*[@id="content"]/div/div/div/div[3]/a').click()
        time.sleep(0.3)
        # result.append([store_name]+[store_address]+[store_contact])


def main():
    result = []
    print('홈플러스 매장 크롤링 >>>')
    getHomeplusStoreInfo(result)

    # columns = ['store','address','phone']
    # topmart_df= pd.DataFrame(result, columns=columns)
    # topmart_df.to_csv('./topmart_shop_info.csv',index=True, encoding='utf-8')
   
    # print('저장완료')

    

if __name__ == '__main__':
    main()