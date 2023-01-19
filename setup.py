from model import db, saveds

db.connect()
db.create_tables([saveds])
