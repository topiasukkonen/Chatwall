from db import db
import users

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at, M.id, M.topic FROM messages M, users U WHERE M.user_id=U.id order by M.sent_at desc"
    result = db.session.execute(sql)
    return result.fetchall()

def send(content, topic):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO messages (content, user_id, sent_at, topic) VALUES (:content, :user_id, NOW(), :topic)"
    db.session.execute(sql, {"content":content, "user_id":user_id, "topic":topic})
    db.session.commit()
    return True

def send1(content, topic):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO answers (content, topic, user_id, sent_at) VALUES (:content, :topic, :user_id, NOW())"
    db.session.execute(sql, {"content":content, "topic":topic, "user_id":user_id})
    db.session.commit()
    return True