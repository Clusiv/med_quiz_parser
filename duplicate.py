from dbfile import db
from pprint import pprint
splited = db.split('@')

topics = []
duplicated = []

for t in splited:
    topic = t.split('\n')
    if topic not in topics:
        topics.append(topic)
    else:
        duplicated.append(topic)

pprint(duplicated)