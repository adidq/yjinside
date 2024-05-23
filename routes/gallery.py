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
        return "없는 갤러리입니다."
    articlelist = function.database.findArticleListviaGallId(gallid)

    #값 없으면 정렬안함
    if articlelist is not False:
        articlelist.sort(key=lambda x: x[5], reverse=True)
    return render_template('gall/gallery.html', galldata=galldata, articlelist=articlelist)

@_gallery.route('/article/<gallid>/<articleid>')
def article(gallid, articleid):
    if articleid == None:
        return redirect(f'/gall/{gallid}')
    #galldata = function.database.findGall(gallid)
    #if galldata == False:
    #    return "없는 갤러리입니다."
    articledata = function.database.findArticleviaArticleIdandGallId(gallid, articleid)
    if articledata == False:
        return "없는 게시글입니다."
    return render_template('gall/article.html', articledata=articledata)
