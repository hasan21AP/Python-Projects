from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
import csv

anime_titles = []
anime_scores = []

url = requests.get("https://myanimelist.net/topanime.php")

con = url.content 
soup = BeautifulSoup(con,"lxml")
anime_title = soup.find_all("div",{"class":"di-ib clearfix"})
anime_score = soup.find_all("div",{"js-top-ranking-score-col di-ib al"})

file_list = [anime_titles,anime_scores]
ed = zip_longest(*file_list)

for i in range(len(anime_title)):
    anime_titles.append(anime_title[i].text)
    anime_scores.append(anime_score[i].text)


with open("C:/Users/hasan/Desktop/anime.csv","w") as anime_file:
    wr = csv.writer(anime_file)
    wr.writerow(["Anime","Score"])
    wr.writerows(ed)