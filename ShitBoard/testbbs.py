import cgitb
cgitb.enable()
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.stdout.reconfigure(encoding='utf-8')
import csv
import glob

print("Content-Type: text/html; charset=utf-8")
print()
articles = []
#if os.path.isfile('../dat/dat.csv'):
#    with open("../dat/dat.csv","r") as f:
#        reader = csv.reader(f)
#        for row in reader:
#            if row:
#                articles.append(row)
dat_list = glob.glob('../dat/*.csv')
#↓なぜか動く
for i in dat_list:
    with open(i,"r") as f:
        reader = csv.reader(f)
        for num,row in enumerate(reader):
            if num == 0:
                articles.append(row)
articles_html = ''
for i in articles:
    articles_html += f'<p><a href="response.py?{i[2]}">{i[0]}:{i[1]}</a><p>'


html = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ツリー式掲示板γ</title>
    </head>
    <body>
        <div>
            <form action="test_bbs2.py" method="post">
                <input type="text" name="txt">
                <input type="submit" value = "投稿">
            </form>
        </div>
        <div>
            {articles_html}
        </div>
    </body>
</html>
'''
print(html)