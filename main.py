import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://ratsinfo.gelsenkirchen.de"

def get_person_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    details = {}

    h3_tags = soup.find_all('h3', {'class': 'right'})
    
    name = h3_tags[0].get_text(strip=True) if h3_tags else 'N/A'
    party = h3_tags[1].get_text(strip=True) if len(h3_tags) > 1 else 'N/A'
    
    details['Name'] = name
    details['Party'] = party

    memberships_table = soup.find('table', {'class': 'tablecss'})
    memberships = []
    if memberships_table:
        membership_rows = memberships_table.find_all('tr')[1:]  
        for row in membership_rows:
            cells = row.find_all('td')
            if len(cells) >= 3: 
                memberships.append({
                    'Committee': cells[0].get_text(strip=True),
                    'Role': cells[1].get_text(strip=True),
                    'Since': cells[2].get_text(strip=True)
                })
    details['Memberships'] = memberships

    return details

def scrape_ratsinfo():
    url = base_url + "/ratsinfo/gelsenkirchen/Person.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    person_rows = soup.find_all('tr', {'class': ['tableAlt2', 'tableAlt1']})

    person_details = []

    for row in person_rows:
        cells = row.find_all('td')
        person_link = cells[0].find('a')['href'] if cells[0].find('a') else None

        if person_link:
            details = get_person_details(base_url + person_link)
            person_details.append(details)

    with open('person_details.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'Party', 'Memberships']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(person_details)

if __name__ == '__main__':
    scrape_ratsinfo()

