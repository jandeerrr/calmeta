from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    meta_financeira = float(request.form['meta_financeira'])
    economia_mensal = float(request.form['economia_mensal'])
    tempo_necessario = meta_financeira / economia_mensal
    return f'Com uma economia mensal de R$ {economia_mensal}, você atingirá sua meta de R$ {meta_financeira} em {tempo_necessario:.2f} meses.'

if __name__ == '__main__':
    app.run()
