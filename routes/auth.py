from flask import *

_auth = Blueprint('auth', __name__, url_prefix="/")


@_auth.route('/login', methods=['GET', 'POST'])
def login():
    if session:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.form['username']
            session['username'] = username
            return redirect('/')
    return render_template('login.html')

@_auth.route('/logout')
def logout():
    if session:
        session.clear()
        return redirect('/')
    else:
        return redirect('/')