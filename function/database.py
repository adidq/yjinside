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
    #갤러리 게시글 15개 조회
    result = cur.fetchall()
    conn.close()
    if result:
        return result[0]
    else:
        return False