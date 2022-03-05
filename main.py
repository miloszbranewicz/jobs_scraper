import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

config_file = './firebase_config.json'

cred = credentials.Certificate(config_file)
firebase_admin.initialize_app(cred, {"databaseURL":"https://jobs-scraper-310b3-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/offers")
ref.set({'test':'test'})