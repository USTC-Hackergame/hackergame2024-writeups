import sys
import re

import httpx
import tqdm


def main(url):
    client = httpx.Client()
    my_answer = [0] * 500
    # my_answer[:5] = [c - 65 for c in b"flag{"]
    flag = b"flag{uno\0\0\0\0_esrever_now_U_run_MY_c\0decf\0\0\0a\0\0\0f}"
    my_answer[:len(flag)] = [c - 65 for c in flag]

    def get_score():
        r = client.post(
            url + "submit",
            files={"file": str(my_answer).encode()},
            follow_redirects=True,
        )
        r.raise_for_status()
        match = re.search(r"评测成功，你的平方差为\s(\d+)", r.text)
        assert match is not None, r.text
        return int(match.group(1))

    last_score = get_score()
    for i in range(5, 500):
        print(i, bytes(c + 65 for c in my_answer[:i]))
        if my_answer[i-1] == ord("}") - 65:
            break

        for guess in tqdm.trange(my_answer[i], 101):
            my_answer[i] = guess
            score = get_score()
            if score > last_score:
                my_answer[i] -= 1
                break
            last_score = score
        else:
            raise RuntimeError("not found")


main(sys.argv[1])
# flag{unoAAAA_esrever_now_U_run_MY_cAdecfAAAaAAAf}
