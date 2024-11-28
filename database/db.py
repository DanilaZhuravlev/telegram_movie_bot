from peewee import SqliteDatabase, Model, IntegerField, TextField, DateTimeField
import datetime

db = SqliteDatabase('bot_history.db')


class BaseModel(Model):
    class Meta:
        database = db


class UserCommand(BaseModel):
    user_id = IntegerField()
    command = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


db.connect()
db.create_tables([UserCommand])
