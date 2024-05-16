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