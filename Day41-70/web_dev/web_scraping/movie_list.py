import requests
from bs4 import BeautifulSoup
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
# print(response.tex)

movie_soup = BeautifulSoup(response.text, "html.parser")
# print(movie_soup.get_text())

movie_names = movie_soup.select(selector=".article-title-description__text h3")
order_list = [x.get_text() for x in movie_names]
final_list = list(reversed(order_list))
with open("movie.txt",'w',encoding="utf-8") as file:
    for elements in final_list:
        file.write(f"{elements}\n")