from flask import request

def get_client_ip():
    # X-Forwarded-For 헤더 확인 (프록시 환경)
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.getlist('X-Forwarded-For')[0]
    else:
        ip = request.remote_addr
    return ip