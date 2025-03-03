import cgi
import cgitb
cgitb.enable()
import hashlib
import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime
import bleach

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

#元の仕様
#if not os.path.isfile('../dat/dat.csv'):
#    with open('../dat/dat.csv', 'w') as f:
#        writer = csv.writer(f)
#        writer.writerow([cvalue,datetime.now(),datetime.now().time()])
#else:
#    with open('../dat/dat.csv', 'a') as f:
#        writer = csv.writer(f)
#        writer.writerow([cvalue,datetime.now(),datetime.now().time()])
seed = str(datetime.now().time())
hash = hashlib.sha256(seed.encode())
hash_16 = hash.hexdigest()
with open(f'../dat/{hash_16}.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow([cvalue,datetime.now(),hash_16])
