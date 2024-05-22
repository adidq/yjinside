from flask import *
import function.database

_gallery = Blueprint('gallery', __name__, url_prefix="/")

@_gallery.route('/galllist')
def galllist():
    list = function.database.findGalllist()
    return render_template('gall/galllist.html', list=list)

@_gallery.route('/gall/<gallid>')
def gall(gallid):
    galldata = function.database.findGall(gallid)
    if galldata == False:
        return "없는 겔러리입니다."
    articlelist = function.database.findArticleListviaGallId(gallid)
    return render_template('gall/gallery.html', galldata=galldata, articlelist=articlelist)

@_gallery.route('/article/<gallid>/<articleid>')
def article(gallid, articleid):
    if articleid == None:
        return redirect(f'/gall/{gallid}')
    galldata = function.database.findGall(gallid)
    if galldata == False:
        return "없는 겔러리입니다."
    articledata = function.database.findArticleviaArticleIdandGallId(gallid, articleid)
    if articledata == False:
        return "없는 게시글입니다."
    return render_template('gall/article.html', galldata=galldata, articledata=articledata)
