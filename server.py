#모듈
import os
from flask import *

app = Flask(__name__)

#세션(로그인) 보안 키
app.secret_key = '83u2ijvfujv!ujw3jrfji!j2oifjviwj!'

#라우팅(분할)
import routes.index
app.register_blueprint(routes.index._index)
import routes.auth
app.register_blueprint(routes.auth._auth)
import routes.gallery
app.register_blueprint(routes.gallery._gallery)

if __name__ == '__main__':
    app.run(debug=True)




