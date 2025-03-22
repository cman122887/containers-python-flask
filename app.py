from flask import Flask
import requests
import json
import random
from flask import request
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper!"

@app.route('/gm', methods=['POST'])
def cts():
    rj = request.json
    logger.info(json.dumps(rj))
    if rj['text'].lower().strip() == 'dice roll':
        ret_msg = {'bot_id': '7d48b603bf93154b8f4a2bee31', 'text': str(random.randint(1,6))}
        requests.post('https://api.groupme.com/v3/bots/post', json=ret_msg)
        return json.dumps({'success': True}), 201, {'ContentType':'application/json'} 
    return json.dumps(rj), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    app.run(host='0.0.0.0', port=8080)
