import cgi
import cgitb
cgitb.enable()
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
import bleach
import hashlib
from datetime import datetime

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

value = form.getvalue('txt')
cvalue = bleach.clean(value)

html =f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>投稿完了{cvalue}</title>
    </head>
    <body>
        <div>
            <p>{cvalue}</p>
        </div>
        <div>
            <a href = "testbbs.py">戻る</a>
        </div>
    </body>
</html>
'''
print(html)
response = ''
get_hash = os.environ.get('QUERY_STRING')
seed = str(datetime.now().time())
hash = hashlib.sha256(seed.encode())
hash_16 = hash.hexdigest()
if os.path.isfile(f'../dat/{get_hash}.csv'):
    with open(f"../dat/{get_hash}.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow([cvalue,datetime.now(),hash_16])