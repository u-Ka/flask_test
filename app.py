from flask import Flask

# 自分自身の名前をappという変数でインスタンス化
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=False)