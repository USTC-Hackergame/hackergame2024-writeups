import sys
import httpx

def main(url):
    client = httpx.Client()
    r = client.post(
        url + "submit",
        files={"file": ("../web/app.py", open("app.py", "rb"), "text/plain")},
        follow_redirects=True,
    )
    r.raise_for_status()

main(sys.argv[1])
