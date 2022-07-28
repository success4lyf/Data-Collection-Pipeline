from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib.request
import pandas as pd
import shutil
import json
import csv
import uuid
import os
import time

class Boohoo:

    def __init__(self):      
        self.driver = webdriver.Chrome()
        self.url = 'https://www.boohoo.com/womens'
        self.action = ActionChains(self.driver)
        
    def do_something(self):
        self.driver.get(self.url)
        self.accept_cookies()
        self.create_directory()
        self.navigate()
        self.get_categories()
        self.click_category()
        self.get_details()
        self.get_images()
        self.driver.quit()

    def accept_cookies(self):
        try:
            self.accept_cookie = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="b-notification_panel-button b-button m-large"]')))
            self.accept_cookie.click()
        except:
            pass           
        
    def create_directory(self):
        cwd = os.getcwd()
        directory = ['Raw_Data', 'Images', 'Links']
        for items in directory:                   
            path = os.path.join(cwd, items)
            shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)
            print("Directory '% s' created" % directory)

    def navigate(self):
        all_clothing = self.driver.find_element(By.XPATH, '(//li/a[@class="b-menu_bar-tab_content_link m-has-submenu "])[3]')
        self.action.move_to_element(all_clothing).perform()
        time.sleep(2)

    def get_categories(self):
        self.categories = self.driver.find_elements(By.XPATH, '(//div[@aria-label="ALL CLOTHING"])[2]/div/a')
        self.category_names = []
        self.category_links = []
        with open('Links/Links.csv', 'w') as f:
            writer = csv.writer(f)
            for category in self.categories:
                try:
                    names = category.text
                    links = category.get_attribute('href')                  
                    self.category_names.append(names)
                    self.category_links.append(links)
                except NoSuchElementException:
                    continue 
            writer.writerow(self.category_names)                       
            writer.writerow(self.category_links)
            print(self.category_names)
            print(self.category_links)      

    def click_category(self):
        self.driver.get(self.category_links[1])
        time.sleep(3)

    def get_details(self):
        self.items = self.driver.find_elements(By.XPATH, '//div[@class="l-plp_grid"]/section')
        counter = 0        
        for item in self.items[:40]:
            try:
                data = {
                'ID': str(uuid.uuid4()),
                'Title': item.find_element(By.XPATH, './/a[@class="b-product_tile-link"]').text,
                'Price': item.find_element(By.XPATH, './/span[@class="b-price-item m-new"]').text,
                'Discount': item.find_element(By.XPATH, './/span[@class="b-price-discount"]').text,
                'Color': item.find_element(By.XPATH, './/img[@class="b-product_tile_swatches-swatch_image"]').get_attribute('alt')              
                }
            except NoSuchElementException:
                continue
            print(data)
            with open(f'Raw_Data/boohoo_{counter}.json', mode='w') as f:
                json.dump(data, f)
            counter += 1
            
            
    def get_images(self):       
        self.images = self.driver.find_elements(By.XPATH, '//div[@class="l-plp_grid"]/section//picture/img')
        counter = 0
        for image in self.images[:40]:   
            src = image.get_attribute('src')
            website_opener = urllib.request.build_opener()
            website_opener.addheaders = [('User-Agent', 'MyApp/1.0')]
            urllib.request.install_opener(website_opener)
            try:
                urllib.request.urlretrieve(src, f'Images/image_{counter}.png')                            
            except NoSuchElementException:
                continue              
            counter += 1
            print('image saved')            

if __name__ == '__main__':
    scraper = Boohoo()
    scraper.do_something()
    