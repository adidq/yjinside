from flask import *
from function.forms import loginForm
import function.database
import hashlib

_auth = Blueprint('auth', __name__, url_prefix="/")

#로그인
@_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    #로그인된 유저가 접속시도시 홈으로
    if 'username' in session:
        return redirect('/')
    if request.method == 'POST' and form.validate_on_submit():
        #폼에서 정보 불러오기
        user_id = request.form['user_id']
        req_password = request.form['password']
        #암호 불러오기
        hashed_password = function.database.findUserPasswordviaUserId(user_id)
        if hashed_password == False:
            #회원 존재 안함
            flash('아이디 또는 비밀번호가 일치하지 않습니다')
            return render_template('login.html', form=form)
        #암호 해쉬화
        hashed_req_password = hashlib.sha256(req_password.encode()).hexdigest()
        #검증
        if hashed_password == hashed_req_password:
            username = function.database.findUserNameviaUserId(user_id)
            session['username'] = username
            return redirect('/')
        else:
            flash('아이디 또는 비밀번호가 일치하지 않습니다')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

#회원가입
@_auth.route('/register')
def register():
    #로그인된 유저가 접속시도시 홈으로
    if 'username' in session:
        return redirect('/')
    #가입시 이메일인증
    return "개발중"

#로그아웃
@_auth.route('/logout')
def logout():
    if session:
        session.clear()
        return redirect('/')
    else:
        return redirect('/')