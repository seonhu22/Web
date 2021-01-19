# 아주 간단한 로그인 페이지 만들기
#
# 필수 endpoints
# '/': 기본형은 'Welcome!'이 나오고 로그인 하면 'Welcome XXX!'
# '/login': GET으로 가면 로그인 페이지(아이디 비번 입력 화면), POST로 가면 아이디 비밀번호
# 받아서 로그인 후 홈으로 이동(예외 처리 필수)
# '/logout': 로그인 된 상태일 경우 로그아웃하고 홈으로 이동
# '/signup': 회원가입(예외 처리 필수)
from flask import Flask, render_template, request, flash

sign = Flask(__name__)

arr_id = []
arr_pw = []

@sign.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        signup_success = 'signup_success'
        signup_error = 'signup_error'

        if len(arr_id) == 0:
            arr_id.append(request.form['signup_id'])
            arr_pw.append(request.form['signup_pw'])
            return render_template('home.html', signup_success=signup_success)
        else:
            for i in range(len(arr_id)):
                if request.form['signup_id'] in arr_id:
                    return render_template('home.html', signup_error=signup_error)
                else:
                    arr_id.append(request.form['signup_id'])
                    arr_pw.append(request.form['signup_pw'])
                    return render_template('home.html', signup_success=signup_success)

    if request.method == 'GET':
        return render_template('home.html')

@sign.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        id = request.form['signin_id']
        pw = request.form['signin_pw']
        signin_error = 'signin error'

        for i in range(len(arr_id)):
            if arr_id[i] == id:
                if arr_pw[i] == pw:
                    return render_template('signin_home.html', id=id)
                break
        return render_template('signin.html', signin_error=signin_error)

    if request.method == 'GET':
        return render_template('signin.html')

@sign.route('/signout')
def signout():
    return render_template('signin_home.html')

@sign.route('/signup')
def signup():
    return render_template('signup.html', signup=signup)

def main():
    sign.run('127.0.0.1', 80, debug=True)

# 다른곳에서 app.py import 해도 실행안됨.
# 이 파일을 직접 실행할떄만 사용 가능
if __name__ == '__main__':
    main()