import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import helpers

config_file = './firebase_config.json'

cred = credentials.Certificate(config_file)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://jobs-scraper-310b3-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference("/offers")
junior_offers_url = 'https://nofluffjobs.com/pl/praca-it?criteria=seniority%3Djunior&page=35'
offers_links = [offer_link for offer_link in helpers.get_offers_links(junior_offers_url)]

print(offers_links)
