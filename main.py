import json

import requests
from bs4 import BeautifulSoup

from Offer import Offer


def get_offer_data(offer_url: str) -> str:
    response = requests.get(offer_url)
    bs_response = BeautifulSoup(response.content, "html.parser")

    # get offer requirements
    requirements = []
    for requirement in bs_response.findAll("button", attrs={"class": "text-truncate", "type": "button"}):
        requirements.append(requirement.getText(strip=True))

    offer_title = bs_response.find('h1', class_='font-weight-bold').getText(strip=True)
    offer_company = bs_response.find('a', id='postingCompanyUrl').getText(strip=True)
    offer_salary = bs_response.find('h4', class_='mb-0').getText(strip=True)
    working_place = bs_response.find('ul', class_='locations-compact').findChild().getText(strip=True)
    seniority = bs_response.find('span', attrs={"class": ["mr-10", "font-weigh-medium"]}).getText(strip=True)

    return json.dumps(
        Offer(offer_title, offer_company, working_place, requirements, offer_salary, offer_url, seniority).__dict__)


pageLink = "https://nofluffjobs.com/pl/praca-it?criteria=seniority%3Djunior&page=35"


def get_next_page(soup_response, host):
    next_page = soup_response.find('a', attrs={"aria-label": 'Next', "class": "page-link"})
    if next_page is not None:
        return host + next_page['href']
    else:
        return


def get_offers_links(starting_page_url: str, host: str) -> str:
    if starting_page_url is not None:
        host = host
        response = requests.get(starting_page_url)
        bs_response = BeautifulSoup(response.content, 'html.parser')

        for job_offer in bs_response.findAll('a', class_='posting-list-item'):
            yield host + job_offer['href']
        get_offers_links(get_next_page(bs_response, host), host)




print(get_offer_data('https://nofluffjobs.com/pl/job/senior-scala-big-data-engineer-virtuslab-remote-uui8ydmg'))
