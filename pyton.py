from flask import Flask

app = Flask(__jerlin__)

@app.route('/')
def home():
    return "Hello, jerlin! This is my first pyton file."

if __jerlin__ == '__main__':
    app.run(host='0.0.0.0', port=5000)