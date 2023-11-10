from flask import Flask
from collections import Counter
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = '사이드와인더a 사이드와인더b 사이드와인더c 사이드와인더d 사이드와인더f'
    counter = dict(Counter(user_string))
    result = json.dumps(counter)

    return result

