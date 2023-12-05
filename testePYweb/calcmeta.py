from flask import Flask

app = Flask(__name)

@app.route('/')
def hello_world():
    return 'Olá, mundo! Este é um aplicativo web simples com Flask.'

if __name__ == '__main__':
    app.run()
