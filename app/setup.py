import sqlite3

conn = sqlite3.connect('../database.db')
print("Opened database successfully")
conn.execute('drop table IF EXISTS users')
conn.execute('drop table IF EXISTS transactions')
conn.execute('drop table IF EXISTS footage')

conn.execute('CREATE TABLE users (username varchar , password varchar , role varchar )')
conn.execute('CREATE TABLE transactions (wallet varchar, name varchar, date DATE , food varchar )')
conn.execute('CREATE TABLE footage (video varchar, date DATE )')

conn.execute("insert into users values ('mongi','saidani','admin' )")
conn.execute("insert into users values ('anas','chabchoub','admin' )")
conn.execute("insert into users values ('hani','haddad','user' )")
conn.execute("insert into users values ('hadhoud','nefzi','user' )")
conn.execute("insert into users values ('omar','jabloun','user' )")

conn.execute("insert into footage values ('192.168.5.1/vidA.mp4', '2022-03-05')")
conn.execute("insert into footage values ('192.168.5.1/vidB.mp4', '2022-03-05')")
conn.execute("insert into footage values ('192.168.5.1/vidC.mp4', '2022-03-05')")
conn.execute("insert into footage values ('192.168.5.1/vidD.mp4', '2022-03-05')")

conn.execute("""INSERT INTO transactions VALUES(
    '0x4eafca2a40bccebfb7ff90e6f36ea56e3ea53a6a52cad7d714fe4a9161409e83', 
    'Amber Higgins',
    '2022-03-05',
    'Burger'
)""")

conn.execute("""INSERT INTO transactions VALUES(
    '0xa0bb67947ca4d0a48d63ae3e114c77f0355d2e5f60f56489b1624fd738180931', 
    'Ingrid Jordan',
    '2022-03-05',
    'Pizza'
)""")

conn.execute("""INSERT INTO transactions VALUES(
    '0x179a0f630a1fc22ae6b59b3d432050a7595a98a37f4f39aed8ac58163f9d4fd9', 
    'Joan Mahoney',
    '2022-03-05',
    'Pizza'
)""")

conn.execute("""INSERT INTO transactions VALUES(
    '0x0780096fdc802b82823dd01ff9750f73f4f5d9b2b2c62eba125160356e0f5a5a', 
    'Grania Mullen',
    '2022-03-05',
    'Burger'
)""")

conn.execute("""INSERT INTO transactions VALUES(
    '0x89a7e8b27b67eba3b91ee5b064d1a98a5984eb2341554deb65db268769d01025', 
    'Kay Kelly',
    '2022-03-05',
    'Pizza'
)""")

conn.execute("""INSERT INTO transactions VALUES(
    '0x3f352cea91b6c921cc18bb848d8561dc1f4963439fed75fb08a2d79a59d1bfa0', 
    'Carl Mills',
    '2022-03-05',
    'Burger'
)""")

conn.commit()
print("Table created successfully")
conn.close()
