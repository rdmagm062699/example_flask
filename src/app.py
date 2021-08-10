from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/blah', methods=['POST'])
def blah():
    print(request.json)
    return ""