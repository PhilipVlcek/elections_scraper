"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Filip Vlček
email: philip.vlcek@seznam.cz
discord: Filip V. Filip_#8786
"""

import csv
from requests import get
from bs4 import BeautifulSoup as BS
import sys

def get_page(url):
    """
    Function takes the data from the provided URL and parses it with BeautifulSoup.
    """
    response = get(url)
    return BS(response.text, features = "html.parser") 
    
    # možná by šlo odstanit <response> a vložit za BS přímo <get(url)>

def scrape_web(url):
    """
    Function scrapes data from a web page and puts it into a dictionary.
    """
    soup = get_page(url)
    web_data = {}
    all_tr = soup.find_all("tr")

    for tr in all_tr:

        try:
            td = tr.find('td', class_='cislo')
            code = td.find('a').string
            url = td.find('a', href = True)

            city_url = "https://volby.cz/pls/ps2017nss/" + url['href']
            city_name = tr.find('td', class_ = "overflow_name").string

            city_soup = get_page(city_url)
            td2 = city_soup.find_all("td", class_ = "cislo")
            voters_list = td2[3].string
            envelopes = td2[4].string
            valid_votes = td2[7].string

            web_data[code] = {
                "Kód obce" : code,
                "Název obce": city_name,
                "URL obce" : city_url,
                "Voliči v seznamu" : voters_list,
                "Vydané obálky" : envelopes,
                "Platné hlasy" : valid_votes,
            }

            table2 = city_soup.find_all('table', class_ = 'table')
            trs_2 = table2[1].find_all('tr') 
            trs_3 = table2[2].find_all('tr')
            
            for tr in trs_2:

                try:
                    political_party = tr.find('td',class_ = "overflow_name").text
                    votes = tr.find('td', {"class" : "cislo", "headers" : "t1sa2 t1sb3"}).text
                    web_data[code][political_party] = votes

                except AttributeError:
                    continue

            for tr in trs_3:

                try:
                    political_party = tr.find('td',class_ = "overflow_name").text
                    votes = tr.find('td', {"class" : "cislo", "headers" : "t2sa2 t2sb3"}).text
                    web_data[code][political_party] = votes

                except AttributeError:
                    continue

        except AttributeError:
            continue

    return web_data

def get_header(url):
    """
    Funkce načte záhlaví souboru CSV na základě webové stránky s výsledky voleb.
    """
    soup = get_page(url)

    try:
        city_name = soup.find('td', attrs = {'class': 'cislo', 'headers': 't1sa1 t1sb1'}).a 
                # Možná by šlo odstanit ".a"
        url_location = "https://volby.cz/pls/ps2017nss/" + city_name['href']
        soup_2 = get_page(url_location)
        political_parties = soup_2.find_all('tr')
        header = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]

    except AttributeError:
        quit()
    
    for i in political_parties:

        try:
            party = i.find('td', class_ = 'overflow_name').string
            header.append(party)

        except AttributeError:
            continue

    return list(header)

def create_csv(web_data, csv_file, url):
    """
    The function creates a CSV file and writes data to it.
    """
    with open(csv_file, mode = "w", newline = "", encoding = "utf-8") as file:

        writer = csv.writer(file)
        header = get_header(url)
        writer.writerow(header)

        for location_data in web_data.values():

            assigned_data = {key: location_data[key] for key in header}
            writer.writerow(assigned_data.values())

def arg_check(argv):
    """
    The function checks the validity of arguments entered by the user.
    """
    if len(argv) != 3:
        print("You have entered an incorrect number of arguments. There must be exactly two arguments: <URL> <file_name.csv>")
        quit()

    elif "https://volby.cz/pls/ps2017nss/" not in argv[1]:
        print("You have entered invalid URL")
        quit()

    elif not argv[2].endswith(".csv"):
        print("The file name must end with a .csv extension")
        quit()

def main(url, csv_file):
    """
    Main function.
    """
    print("\nThe scraping process has been started . . . \n")

    web_data = scrape_web(url)
    create_csv(web_data, csv_file, url)

    print(f"The obtained data was downloaded to the file: \"{csv_file}\"\n")   
    print("The process is over")

if __name__ == '__main__':

    arg_check(sys.argv)
    main(sys.argv[1], sys.argv[2])

