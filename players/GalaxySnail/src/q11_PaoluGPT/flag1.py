import sys
import re

import httpx
import tqdm


def main(url, token):
    client = httpx.Client()
    client.get(url, params={"token": token}, follow_redirects=True).raise_for_status()

    msgs_page = client.get(url + "list")
    msgs_page.raise_for_status()

    msgs = []
    for match in re.finditer(r'href="/(view\?conversation_id=[0-9a-f-]+)"', msgs_page.text):
        msgs.append(url + match.group(1))
    assert len(msgs) == 999

    for msg_url in tqdm.tqdm(msgs):
        response = client.get(msg_url)
        response.raise_for_status()
        for line in response.text.splitlines():
            if "flag" in line:
                print("\n" + line)
                return


main(sys.argv[1], input("token: "))
