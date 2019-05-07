import json
import sys
import re
from selenium import webdriver
import csv
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import datetime
import time
import urllib3
import json


print('Creating the search terms')



import sys
# name = sys.argv[1]

if len(sys.argv)>=2:
    fileName = sys.argv[1]
else:
    fileName = input('Please enter the name of keyword file: ')
print(fileName)
with open('output_for_'+fileName.split('.')[0]+'.csv','a',newline='') as csvf:
    csv_writer = csv.writer(csvf)
    csv_writer.writerow(['name','url','emails'])

with open(fileName,'r') as f:
    data = f.read()
    data = data.split('\n')

print('Beginning of scraping')

http = urllib3.PoolManager()
def wait_for_internet_connection():
    while True:
        try:
        
            response = http.request('GET', 'http://ku.edu.np')
            return
        except:
            print('No internet connection.\nTrying after 5 seconds.\n')
            sleep(5)





# with open('data_us1.csv','w',newline='') as csvf:

#     csv_writer = csv.writer(csvf)
#     csv_writer.writerow(['query','link'])
    

# os.system('cls')
print('Searching on Bing')
print(data)

start = time.time()
driver = webdriver.Firefox(executable_path='geckodriver')
count = 0
for keyword in data:
    keyword = keyword.replace(' ','+').replace('&','%26')
    print(keyword)
    temp=[]
    error=0
    data={}
    wait_for_internet_connection()
    driver.get('https://www.bing.com/search?q={}&cc=us'.format(keyword))
    
    # driver.find_element_by_xpath('//*[@id="sb_form_q"]').clear()
    # driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys(keyword)
    # input()
    # driver.find_element_by_xpath('//*[@id="id="sb_form_go""]').click()
    # input('All good?')
    
    try:
        for i in range(96):
            # os.system('clear')
            try:

                #lets parse every search result
                for n in range(1,11):
                    os.system('clear')
                    print('Looking for',keyword)
                    print('Time Passed: ',time.strftime('%H:%M:%S',time.gmtime(time.time()-start)))
                    print('Link found:',count)
                    print('\n----------------------------------------------------------\n\n')
                    # os.system('cls')
                    try:
                        url = driver.find_element_by_xpath('//li[@class="b_algo"][{}]//a'.format(n)).get_attribute('href')
                        name = driver.find_element_by_xpath('//li[@class="b_algo"][{}]//a'.format(n)).text.split('-')[0]
                        text = driver.find_element_by_xpath('//li[@class="b_algo"][{}]'.format(n)).text
                        email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
                        with open('output.csv','a',newline='') as csvf:
                            csv_writer = csv.writer(csvf)
                            csv_writer.writerow([name,url,email])

                        print(url)
                        count+=1

                    
                    except Exception as e:
                        print(e)
                        #
                        # input('Error')
          
                wait_for_internet_connection
                driver.find_element_by_xpath('//*[@title="Next page"]').click()

            except Exception as e:
                print(e)
                driver.get(driver.current_url)
                # input('Error 2')
       
                
    except Exception as e:
        
        print(e)
        print('Error in keyword')








print('Links:',count)
print('The end')
driver.close()