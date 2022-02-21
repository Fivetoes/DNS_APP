import requests
import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'FS server main page'

@app.route('/register')
def register():
    
    ## register the ip address with the host name
    dict = {}
    ip_address = '0.0.0.0'
    host_name = request.args.get('hostname')
    dict['name'] = host_name
    dict['address'] = ip_address
    r = requests.post('http://0.0.0.0:53533', data = dict)
    return r.text

@app.route('/fabonacci')
def fabonacci():
    x = int(request.args.get('number'))
    res = 0
    if x == 1:
        res = 1
    else:
        cache = [0] * (x + 1)
        cache[1] = 1
        for i in range(2, x + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
    res = cache[x]
    return Response("the fibo for "+str(x)+" is: "+str(res), status = 200)
    
app.run(host='0.0.0.0',
        port=9090,
        debug=True)
