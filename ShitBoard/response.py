import cgi
import cgitb
cgitb.enable()
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
#すんげえ要る　環境依存かもしれん
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import csv
thread = ''
response = ''
get_hash = os.environ.get('QUERY_STRING')

if os.path.isfile(f'../dat/{get_hash}.csv'):
    with open(f"../dat/{get_hash}.csv","r") as f:
        reader = csv.reader(f)
        for num,row in enumerate(reader):
            #謎の空白対策
            if row:
                if num == 0:
                    thread = f'<p>{row[0]}:{row[1]}</p>'
                else:
                    response += f'<li>{row[0]}:{row[1]}</li>'
#ここに書き込みを入れたかった；；；
#else:

print("Content-Type: text/html")
print()

html = f'''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{thread}</title>
    </head>
    <body>
        <div>
            <form action="battle.py?{get_hash}" method="post">
                <input type="text" name="txt">
                <input type="submit" value = "返信">
            </form>
        </div>
        <div>
            {thread}
        </div>
        <div>
            <ul>
                {response}
            </ul>
        </div>
        <div>
            <a href= "testbbs.py">戻る</a>
        </div>
    </body>
</html>
'''
print(html)