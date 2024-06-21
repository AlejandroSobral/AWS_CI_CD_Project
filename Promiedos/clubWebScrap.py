from get_trph import get_trph
from split_name_year import split_name_year
from bs4 import BeautifulSoup
import requests

def clubWebScrap(url):      
    try: 
        nac_titles = []
        int_titles = []
        loc_titles = [] 
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        div_tag = soup.find('div', class_='clubizq')
        div_name_tag = soup.find('div', class_='clubder')
        club = div_name_tag.contents[6].text
        nac_titles = get_trph(div_tag, "NAC")
        nac_titles = split_name_year(nac_titles, "NAC")
        int_titles = get_trph(div_tag, "INT")
        int_titles = split_name_year(int_titles, "INT")
        loc_titles = get_trph(div_tag, "LOC")
        loc_titles = split_name_year(loc_titles, "LOC")
        
        club_data = {
                "club": club[1:],
                "nac_titles": nac_titles,
                "int_titles": int_titles,
                "loc_titles": loc_titles
            }
    except Exception as error:
        print(f"Failed Web Scraping, falló para URL {url} con error {error}.")
    
    return club_data