from flask import *

_index = Blueprint('index', __name__, url_prefix="/")

@_index.route('/')
def index():
    return render_template('index.html')