from flask import Flask, render_template, request

app = Flask(__name__)

item_list = [
    'Apple',
    'Banana',
    'Kiwi',
    'Mango',
]

@app.route('/')
def home():
    return render_template('calc.html')
# html file in templates folder
# static file in static folder(ex: css, javascript)

@app.route('/calc', methods=['Get', 'POST'])
def calc():
    if request.method == 'GET':
        return 'calculation'
    if request.method == 'POST':
        value = request.form['expr']
        result = eval(value)
        return render_template('calc.html', result=result)

@app.route('/fruits')
def show_fruits():
    return render_template('list.html', title='My fruits', items=item_list)

def main():
    app.run('127.0.0.1', 80, debug=True)

# 다른곳에서 app.py import 해도 실행안됨.
# 이 파일을 직접 실행할떄만 사용 가능
if __name__ == '__main__':
    main()