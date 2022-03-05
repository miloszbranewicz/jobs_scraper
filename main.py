import json

import requests
from bs4 import BeautifulSoup

from Offer import Offer


def getOfferData(offerURL):
    response = requests.get(offerURL)
    bs_response = BeautifulSoup(response.content, "html.parser")

    # get offer requirements
    requirements = []
    for requirement in bs_response.findAll("button", attrs={"class": "text-truncate", "type": "button"}):
        requirements.append(requirement.getText(strip=True))

    offer_title = bs_response.find('h1', class_='font-weight-bold').getText(strip=True)
    offer_company = bs_response.find('a', id='postingCompanyUrl').getText(strip=True)
    offer_salary = bs_response.find('h4', class_='mb-0').getText(strip=True)
    working_place = bs_response.find('ul', class_='locations-compact').findChild().getText(strip=True)

    return json.dumps(Offer(offer_title, offer_company, working_place, requirements, offer_salary, offerURL).__dict__)
