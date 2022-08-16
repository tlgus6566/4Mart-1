from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
from selenium import webdriver

def getTopMartStoreInfo(result):
    # USB: usb_device_handle_win.cc:1049 시스템에 부착된 장치가 작동하지 않습니다.
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome('./TopMart/chromedriver.exe',options=options)


    for i in range(21010, 22150+1):
        wd.get('https://www.seowon.com/shopping/storeList')
        time.sleep(0.3)

        try:
            wd.execute_script(f"Shopping.getStoreInfo('{i}', ''); return false;")
            time.sleep(0.3) # 팝업표시 후에 크롤링이 안되서 브라우저가 닫히는 것을 방지하기 위함.
            html = wd.page_source
            soup = BeautifulSoup(html, 'html.parser')
            store_name = soup.select('div.lct-info-title > h3#storeName')[0].string
            print(store_name)
            store_address = soup.select('table.table > tbody > tr > td.border-top-0')[0].string.rstrip()
            store_contact = soup.select('table.table > tbody > tr > td#telNum')[0].string
            result.append([store_name]+[store_address]+[store_contact])
        except Exception as e:
            continue

def main():
    result = []
    print('탑마트 매장 크롤링 >>>')
    getTopMartStoreInfo(result)

    columns = ['store','address','phone']
    topmart_df= pd.DataFrame(result, columns=columns)
    topmart_df.to_csv('./topmart_shop_info.csv',index=True, encoding='utf-8')
   
    print('저장완료')

    

if __name__ == '__main__':
    main()