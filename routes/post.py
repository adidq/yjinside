from flask import *
import function.database
import function.management

_post = Blueprint('post', __name__, url_prefix="/post")

@_post.route('/article/<gall_id>', methods=['GET', 'POST'])
def article(gall_id):
    if function.database.findGall(gall_id) == False:
        return "없는 겔러리입니다."    
    lastnum = function.database.findLastArticleViaGallId(gall_id)
    if lastnum == False:
        article_id = 1
    else:
        article_id = int(lastnum)+1
    if request.method == 'POST':
        article_name = request.form['title']
        article_content = request.form['content']
        if session.get('id') == None:
            article_manager = function.management.get_client_ip()
        else:
            article_manager = session.get('id')
        function.database.postArticle(article_id, article_name, article_content, article_manager, gall_id)
        return redirect(f'/article/{gall_id}/{article_id}')
    return render_template('post/article.html', gall_id=gall_id)