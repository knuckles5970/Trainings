import bottle
import pymongo

@bottle.route('/')
def index():
    con = pymongo.MongoClient('localhost', 27017)
    db = con.test
    names = db.names 
    item = names.find_one()
    return '<b>Hello %s</b>' % item['name']

bottle.debug(True)
bottle.run(host='localhost', port='8080')