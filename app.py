from flask import Flask
import requests
import json
import random
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper!"

@app.route('/gm', methods=['POST'])
def cts():
    rj = request.json
    print(rj)
    if rj['text'].lower().strip() == 'dice roll':
        ret_msg = {'bot_id': '7d22d6aae5e37b72fbb41ef03b', 'text': str(random.randint(1,6))}
        requsts.post('https://api.groupme.com/v3/bots/post', json=ret_msg)
        return json.dumps({'success': True}), 201, {'ContentType':'application/json'} 
    return json.dumps(rj), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
