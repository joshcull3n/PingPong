from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def ping_service():
  return '\nhello, I am the ping service!'

@app.route('/ping')
def do_ping():
  ping = '\nping ... '
  response = ''

  try:
    response = requests.get('http://pong-service-container:5001/pong')
  except requests.exceptions.RequestException as e:
    print('\ncannot reach the pong service. :(')
    return ping
  
  ping += response.text + '\n'
  return ping

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 5000, debug = True)