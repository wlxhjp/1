from selenium import webdriver
from selenium.webdriver.edge.service 
import Servicefrom webdriver_manager.microsoft 
import EdgeChromiumDriverManager

driver = webdriver.Edge()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')from  从 selenium import  导入 webdriver
from  从 selenium.webdriver.edge.service import  导入 Service
from  从 webdriver_manager.microsoft import  导入 EdgeChromiumDriverManager
from  从 bs4 import BeautifulSoup
import  导入 requests
import  导入 os

# 创建保存目录
if not os.path.exists('shop_images'):
    os.makedirs('shop_images')

# 初始化 WebDriver
driver = webdriver.Edge()
driver.get('https://example.com')  # 替换为目标网站 URL

# 获取页面源码
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 查找所有 class="shop-img" 的图片元素
img_elements = soup.find_all('img', class_='shop-img')from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import requests
import os

# 创建保存目录
if not os.path.exists('shop_images'):
    os.makedirs('shop_images')

# 初始化 WebDriver
driver = webdriver.Edge()
driver.get('https://example.com')  # 替换为目标网站 URL

# 获取页面源码
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 查找所有 class="shop-img" 的图片元素
img_elements = soup.find_all('img', class_='shop-img')

# 下载图片
for i, img in enumerate(img_elements):
    try:
        img_url = img.get('src')
        if img_url:
            # 处理相对路径
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif img_url.startswith('/'):
                img_url = driver.current_url.split('/')[0] + '//' + driver.current_url.split('/')[2] + img_url
            
            # 下载图片
            response = requests.get(img_url)
            if response.status_code == 200:
                filename = f'shop_images/shop_img_{i+1}.jpg'
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f'已下载：{filename}')
    except Exception as e:
        print(f'下载失败：{e}')

# 关闭浏览器
driver.quit()
print(f'共下载 {len(img_elements)} 张图片')








































# 下载图片
for i, img in enumerate(img_elements):
    try:
        img_url = img.get('src')
        if  如果 img_url:
            # 处理相对路径
            if  如果 img_url.startswith('//'):
                img_url = 'https:' + img_url
        elif img_url.startswith('/'  “嘿”):
                img_url = driver.current_url.split('/')[0] + '//' + driver.current_url.split('/')[2] + img_url
            
            # 下载图片
            response = requests.get(img_url)
            if response.status_code == 200:
                filename = f'shop_images/shop_img_{i+1}.jpg'
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f'已下载：{filename}')
    except Exception as e:
        print(f'下载失败：{e}')

# 关闭浏览器
driver.quit()
print(f'共下载 {len(img_elements)} 张图片')  嘿



















