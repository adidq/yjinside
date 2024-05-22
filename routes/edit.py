from flask import *
import function.database

_edit = Blueprint('edit', __name__, url_prefix="/edit")

@_edit.route('/article/<gall_id>/<article_id>', methods=['GET', 'POST'])
def article(gall_id, article_id):
    #게시글 정보조회
    articledata = function.database.findArticleviaArticleIdandGallId(gall_id, article_id)

    #정보가 없으면
    if articledata == False:
        return "없는 게시글입니다."
    #post요청 처리
    if request.method == 'POST':
        #유저정보 확인
        if articledata[4] is not session.get('id'):
            return f"게시글을 수정할 권한이 없습니다. 작성자:{articledata[4][0]}"
        
        title = request.form['title']
        content = request.form['content']
        function.database.updateArticle(title, content, article_id, gall_id)
        return redirect(f'/article/{gall_id}/{article_id}')
    #유저정보 확인
    if articledata[4] == session.get('id'):
        return render_template('edit/article.html', articledata=articledata)
    else:
        return f"게시글을 수정할 권한이 없습니다. 작성자:{articledata[4][0]}"