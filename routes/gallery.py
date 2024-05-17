from flask import *
import function.database

_gallery = Blueprint('gallery', __name__, url_prefix="/")

@_gallery.route('/galllist')
def galllist():
    list = function.database.findGalllist()
    return render_template('galllist.html', list=list)

@_gallery.route('/gall/<gallid>')
def gall(gallid):
    data = function.database.findGall(gallid)
    if data == False:
        return "없는 겔러리입니다."
    return render_template('gallery.html', data=data)