"""
Selenium 爬虫示例：爬取网站信息
本案例演示如何使用 Selenium 库自动化浏览器并提取网页数据
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ============== 基础配置 ==============
def setup_driver():
    """
    配置并启动 Chrome 浏览器驱动
    """
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # 无头模式（不显示浏览器界面）
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')
    
    # 初始化驱动（需要安装 chromedriver）
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# ============== 示例 1: 简单页面访问与信息提取 ==============
def basic_scraping_example(url):
    """
    基础爬虫示例：访问页面并提取基本信息
    """
    driver = setup_driver()
    
    try:
        # 访问目标网站
        driver.get(url)
        
        # 等待页面加载
        time.sleep(2)
        
        # 获取页面标题
        page_title = driver.title
        print(f"页面标题：{page_title}")
        
        # 获取页面源代码
        # page_source = driver.page_source
        
        # 通过 ID 查找元素
        try:
            search_box = driver.find_element(By.ID, "search-box")
            print(f"找到搜索框：{search_box}")
        except:
            print("未找到 ID 为 'search-box' 的元素")
        
        # 通过 Class Name 查找元素
        elements_by_class = driver.find_elements(By.CLASS_NAME, "content")
        print(f"找到 {len(elements_by_class)} 个 class='content' 的元素")
        
        # 通过 Tag Name 查找所有链接
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"页面共有 {len(links)} 个链接")
        
        # 打印前 5 个链接的文本和 href
        for i, link in enumerate(links[:5]):
            text = link.text.strip()
            href = link.get_attribute("href")
            if text:
                print(f"  链接 {i+1}: {text} -> {href}")
        
    finally:
        driver.quit()

# ============== 示例 2: 使用 XPath 和 CSS 选择器 ==============
def advanced_element_finding(url):
    """
    高级元素定位示例：使用 XPath 和 CSS 选择器
    """
    driver = setup_driver()
    
    try:
        driver.get(url)
        time.sleep(2)
        
        # 使用 XPath 定位元素
        # 查找包含特定文本的按钮
        buttons = driver.find_elements(By.XPATH, "//button[contains(text(), '提交')]")
        print(f"找到 {len(buttons)} 个包含'提交'的按钮")
        
        # 使用 CSS 选择器
        # 查找所有 class 为 item 的 div 元素
        items = driver.find_elements(By.CSS_SELECTOR, "div.item")
        print(f"找到 {len(items)} 个 div.item 元素")
        
        # 提取元素的属性
        for i, item in enumerate(items[:3]):
            text = item.text
            class_attr = item.get_attribute("class")
            id_attr = item.get_attribute("id")
            print(f"  元素 {i+1}: 文本='{text}', class='{class_attr}', id='{id_attr}'")
        
    finally:
        driver.quit()

# ============== 示例 3: 表单填写与提交 ==============
def form_submission_example(url, username, password):
    """
    表单操作示例：填写并提交登录表单
    """
    driver = setup_driver()
    
    try:
        driver.get(url)
        time.sleep(2)
        
        # 查找用户名输入框并输入
        username_input = driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(username)
        
        # 查找密码输入框并输入
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)
        
        # 点击登录按钮
        login_button = driver.find_element(By.ID, "login-btn")
        login_button.click()
        
        # 等待页面跳转
        time.sleep(3)
        
        # 检查是否登录成功
        current_url = driver.current_url
        print(f"登录后 URL: {current_url}")
        
    finally:
        driver.quit()

# ============== 示例 4: 显式等待与动态内容 ==============
def wait_for_dynamic_content(url):例
    """
    driver = setup_driver()
    
    try:
        driver.get(url)
        
        # 使用显式等待（推荐方式）
        wait = WebDriverWait(driver, 10)  # 最多等待 10 秒
        
        # 等待某个元素出现
        try:
            element = wait.until(
                EC.presence_of_element_located((By.ID, "dynamic-content"))
            )
            print(f"动态内容已加载：{element.text}")
        except:
            print("等待超时，元素未出现")
        
        # 等待元素可点击
        try:
            clickable_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit"))
            )
            clickable_button.click()
            print("按钮已点击")
        except:
            print("按钮不可点击或等待超时")
        
    finally:
        driver.quit()

# ============== 示例 5: 爬取列表数据 ==============
def scrape_list_data(url):
    """
    爬取列表数据示例：提取表格或列表中的信息
    """
    driver = setup_driver()
    
    try:
        driver.get(url)
        time.sleep(2)
        
        # 假设要爬取一个产品列表
        products = driver.find_elements(By.CSS_SELECTOR, "div.product-item")
        
        product_list = []
        for product in products:
            try:
                # 提取产品名称
                name_elem = product.find_element(By.CSS_SELECTOR, "h3.product-name")
                name = name_elem.text.strip()
                
                # 提取产品价格
                price_elem = product.find_element(By.CSS_SELECTOR, "span.price")
                price = price_elem.text.strip()
                
                # 提取产品链接
                link_elem = product.find_element(By.TAG_NAME, "a")
                link = link_elem.get_attribute("href")
                
                product_info = {
                    "name": name,
                    "price": price,
                    "link": link
                }
                product_list.append(product_info)
                
            except Exception as e:
                print(f"提取产品信息时出错：{e}")
                continue
        
        # 打印结果
        print(f"\n共爬取到 {len(product_list)} 个产品:")
        for i, p in enumerate(product_list[:10], 1):
            print(f"{i}. {p['name']} - {p['price']}")
            print(f"   链接：{p['link']}")
        
        return product_list
        
    finally:
        driver.quit()

# ============== 示例 6: 处理弹窗和模态框 ==============
def handle_modals(url):
    """
    处理弹窗示例
    """
    driver = setup_driver()
    
    try:
        driver.get(url)
        time.sleep(2)
        
        # 切换到 alert 弹窗
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert 文本：{alert_text}")
            # alert.accept()  # 点击确定
            # alert.dismiss()  # 点击取消
        except:
            print("没有找到 alert 弹窗")
        
        # 切换到 iframe
        try:
            driver.switch_to.frame("iframe-id-or-name")
            # 在 iframe 内操作...
            driver.switch_to.default_content()  # 切回主文档
        except:
            print("未找到指定的 iframe")
        
    finally:
        driver.quit()

# ============== 示例 7: 截图保存 ==============
def save_screenshot(url, filename="screenshot.png"):
    """
    保存页面截图
    """
    driver = setup_driver()
    
    try:
        driver.get(url)
        time.sleep(2)
        
        # 保存整个页面截图
        driver.save_screenshot(filename)
        print(f"截图已保存到：{filename}")
        
    finally:
        driver.quit()

# ============== 主函数 ==============
if __name__ == "__main__":
    # 示例用法
    
    # 1. 基础爬取示例
    print("=" * 50)
    print("示例 1: 基础页面信息提取")
    # basic_scraping_example("https://www.example.com")
    
    # 2. 高级元素定位
    print("\n" + "=" * 50)
    print("示例 2: 高级元素定位 (XPath/CSS)")
    # advanced_element_finding("https://www.example.com")
    
    # 3. 表单提交
    print("\n" + "=" * 50)
    print("示例 3: 表单填写与提交")
    # form_submission_example("https://example.com/login", "your_username", "your_password")
    
    # 4. 等待动态内容
    print("\n" + "=" * 50)
    print("示例 4: 等待动态内容")
    # wait_for_dynamic_content("https://example.com/dynamic")
    
    # 5. 爬取列表数据
    print("\n" + "=" * 50)
    print("示例 5: 爬取列表数据")
    # scrape_list_data("https://example.com/products")
    
    # 6. 处理弹窗
    print("\n" + "=" * 50)
    print("示例 6: 处理弹窗和模态框")
    # handle_modals("https://example.com")
    
    # 7. 截图保存
    print("\n" + "=" * 50)
    print("示例 7: 保存页面截图")
    # save_screenshot("https://www.example.com", "example_screenshot.png")
    
    print("\n所有示例已完成！取消注释相应函数调用来运行具体示例。")








































































































































































    """
    等待动态内容加载示








































































































































