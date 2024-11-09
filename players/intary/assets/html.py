import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

# 目标URL
base_url = 'https://chal01-kgskioca.hack-challenge.lug.ustc.edu.cn:8443/list'  # 这里替换为你要爬取的URL

# Cookie内容
cookies = {
    '_ga': 'GA1.1.2108883494.1728571359',
    '_ga_R7BPZT6779': 'GS1.1.1730520397.2.1.1730522566.60.0.123214942',
    'session': 'eyJ0b2tlbiI6IjEzNDI6TUVVQ0lCNmE5VTZuTytjVjVNWm0yNnNJWSs0N3pMdVh3YUlvbzdQdEN0TEc5U05JQWlFQTYyd2JDTVZrYzc0dVhvODZGNktiODdnNUxRQTIyayt1OU5lbGNEZlZZd2s9In0.Zyl-ew.ca47km9mBrv_4lDJU-RE-IO_-AI'
}

# 创建存储页面内容的目录
if not os.path.exists('pages'):
    os.makedirs('pages')

# 清理URL中的非法字符，生成合法的文件名
def sanitize_filename(url):
    # 只保留字母数字字符和一些常见符号（替换掉非法字符）
    return re.sub(r'[\\/*?:"<>|]', '_', url)

# 获取页面内容并保存到文件
def fetch_page(url):
    print(f"正在爬取: {url}")
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        html_content = response.text
        # 清理URL中的非法字符，作为文件名
        filename = sanitize_filename(url.split('/')[-1]) + '.html'
        filename = os.path.join('pages', filename)
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        return html_content
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None

# 解析页面中的超链接
def parse_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    absolute_links = set()

    for link in links:
        href = link['href']
        # 使用urljoin来确保URL的完整性
        full_url = urljoin(base_url, href)
        absolute_links.add(full_url)
    
    return absolute_links

# 主爬取函数
def crawl_website(start_url):
    visited_urls = set()
    to_visit_urls = {start_url}

    while to_visit_urls:
        current_url = to_visit_urls.pop()
        if current_url not in visited_urls:
            visited_urls.add(current_url)
            page_content = fetch_page(current_url)
            if page_content:
                new_links = parse_links(page_content, current_url)
                to_visit_urls.update(new_links - visited_urls)

# 开始爬取
crawl_website(base_url)
