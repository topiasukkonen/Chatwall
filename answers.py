from db import db

def get():
    sql = "SELECT topic, content, id, user_id, sent_at FROM messages"
    result = db.session.execute(sql)
    message = result.fetchall()
    return message
def list():
    sql = "SELECT a.content, a.user_id, a.sent_at, a.topic, u.username FROM answers a, users u WHERE a.user_id=u.id"
    result = db.session.execute(sql)
    answers = result.fetchall()
    return answers