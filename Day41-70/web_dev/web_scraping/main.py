from bs4 import BeautifulSoup
import requests
# with open("./website.html", 'r',encoding="utf-8") as fh:
#     contents = fh.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.a.string)

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
span_tag = soup.select(selector=".titleline a")
inside_span_tag = soup.select(selector="a .sitestr")
inside_span_link_tag = soup.select(selector=".sitebit.comhead a")

unwanted_text_list = [x.get_text() for x in inside_span_link_tag]
unwanted_link_list = [x.get('href') for x in inside_span_link_tag]
# print(unwanted_text_list)
# print(unwanted_link_list)
text_tag_list = []
link_list = []
for a_tags in span_tag:
    text_tag_list.append(a_tags.get_text())
    link_list.append(a_tags.get('href'))

text_tag_list = [x for x in text_tag_list if x not in unwanted_text_list]
link_list = [x for x in link_list if x not in unwanted_link_list]
score_tag = soup.select(selector=".score")
scores_list = []
for scores in score_tag:
    scores_list.append(int(scores.get_text().strip(" points")))
# print(max(scores_list))
max_index = scores_list.index(max(scores_list))
# print(max_index)
print(scores_list[max_index], text_tag_list[max_index], link_list[max_index])
