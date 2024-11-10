import sqlite3

def main():
    con = sqlite3.connect("file:qrcode.db?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    res = con.execute("select raw from scans;")

    data_list = []
    while row := res.fetchone():
        data = row["raw"]
        data_list.append(data)
    assert len(data_list) == 178

    with open("secret", "wb") as f:
        for data in data_list:
            f.write(data)

main()
