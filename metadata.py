import requests
from bs4 import BeautifulSoup as bs


all_games = []

def get_url():
    url = "https://store.playstation.com/en-us/grid/STORE-MSF77008-PS4ALLGAMESCATEG/"
    response = requests.get(url)

    return response



def get_soup():
    response = get_url()#call the get_url function
    return response



def get_soup():
    response = get_url()#call the get_url function
    soup = bs(response.content, 'html.parser')#parse page source to bs4

    title = soup.title.string#for the page title

    game_class = "grid-cell grid-cell--game"#class for the game cards

    games = soup.find_all("div",{"class":game_class})

    for game in games:
        name = game.find("div", {"class":"grid-cell__title"})
        #print(name.text)

        link = game.find('a', href=True)
        link = link['href']

        game_link = "http://store.playstation.com"+str(link)

        all_games.append(game_link)

        print(game_link)


def get_game():

    for link in all_games:
        response = requests.get(link)

        game_page = bs(response.content, 'html.parser')

        title = game_page.title.string

        print(title)




get_soup()
get_game()
