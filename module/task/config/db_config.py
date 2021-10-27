import sys
sys.path.append("....")
from common.db.db_sqlite import db 
from datetime import datetime

# 模型( model )定義
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)


    def __init__(self, name, status):
        self.name = name
        self.status = status
        db.create_all()
        db.session.commit()

    def deleteTable(self):
        db.drop_all()

if __name__ == '__main__':
    task = Task(db.Model)