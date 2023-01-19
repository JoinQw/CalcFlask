import os

from peewee import Model, CharField, FloatField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class saveds(Model):
    code = CharField(max_length=255, unique=True)
    value = FloatField()
    value2 = FloatField()
    value3 = FloatField()

    class Meta:
        database = db
