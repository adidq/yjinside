import psycopg2
from dotenv import dotenv_values, load_dotenv

# 데이터베이스 설정
load_dotenv()
env_values = dotenv_values()
db_host = env_values.get('DB_HOST')
db_password = env_values.get('DB_PASSWORD')
db_username = env_values.get('DB_USERNAME')
db_name = env_values.get('DB_NAME')

def findUserPasswordviaUserId(user_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT user_password FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return False

def findUserNameviaUserId(user_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT user_name FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return False

def findUserIdviaUserEmail(user_email):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE user_email = %s", (user_email,))
    result = cur.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return False
    
def findUserEmailviaUserId(user_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT user_email FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return False

def makeUserAccount(user_id, user_name, user_email, user_password):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (user_id, user_name, user_email, user_perm, user_password) VALUES (%s, %s, %s, %s, %s)", (user_id, user_name, user_email, 1, user_password))
    conn.commit()
    cur.close()
    conn.close()
    return

def findGalllist():
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM gallery")
    result = cur.fetchall()
    conn.close()
    return result

def findGall(gall_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM gallery WHERE gall_id = %s", (gall_id,))
    result = cur.fetchall()
    conn.close()
    if result:
        return result[0]
    else:
        return False

def findArticleviaArticleIdandGallId(gall_id, article_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM article WHERE article_gall = %s AND article_id = %s", (gall_id, article_id))
    result = cur.fetchall()
    conn.close()
    if result:
        return result[0]
    else:
        return False
    
def findArticleListviaGallId(gall_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM article WHERE article_gall = %s", (gall_id,))
    result = cur.fetchall()
    conn.close()
    if result:
        return result
    else:
        return False

def updateArticle(title, content, id, gall_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("UPDATE article SET article_name = %s, article_content = %s WHERE article_id = %s AND article_gall = %s", (title, content, id, gall_id))
    conn.commit()
    cur.close()
    conn.close()
    return


def findLastArticleViaGallId(gall_id):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("SELECT MAX(article_id) FROM article WHERE article_gall = %s", (gall_id))
    result = cur.fetchall()[0][0]
    conn.close()
    if result is not None:
        return result
    else:
        return False
    
def postArticle(article_id, article_name, article_content, article_manager, article_gall):
    conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name)
    cur = conn.cursor()
    cur.execute("INSERT INTO article (article_id, article_name, article_gall, article_managers, article_content) VALUES (%s, %s, %s, %s, %s)", (article_id, article_name, article_gall, article_manager, article_content))
    conn.commit()
    cur.close()
    conn.close()
    return