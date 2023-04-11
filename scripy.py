import requests as requests
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # 定义浏览器，可以是移动端浏览器
    browser_type = p.chromium
    # 调用浏览器的launch方法，headless=False是显示浏览器窗口
    browser = browser_type.launch(headless=False)
    # 打开一个新的窗口
    page = browser.new_page()
    # 调用goto方法进入想要进去的网站
    page.goto('https://news.ycombinator.com/item?id=35371750&p=1')
    # 调用screenshot方法截图
    # page.screenshot(path=f'screenshot-{browser_type.name}.png')
    element = page.query_selector('#hnmain > tbody > tr:nth-child(3)')
    content = element.inner_text()
    time.sleep(1)

    print(content)
    browser.close()
    # 将内容保存到本地HTML文件
    with open('means.html', 'w', encoding='utf-8') as file:
        # 将内容写入文件
        file.write('<html><body>')
        file.write('<div id="my-div">')  # 用于存放内容的 div 标签
        file.write(content)
        file.write('</div></body></html>')