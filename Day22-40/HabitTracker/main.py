import requests
import datetime

NAME = "binduhc"
ID = "abc"
top_ep = "https://pixe.la/v1/users/"
pixela_endpoint = "https://pixe.la/v1/users/"
pixela_data = {"token": "yes23111996", "username": NAME, "agreeTermsOfService": "yes", "notMinor": "yes"}
# response = requests.post(url=pixela_endpoint, json=pixela_data)
# print(response.json())
# inserting line

# after creating the profile commented
# creating a graph

graph_endpoint = f"{top_ep}{NAME}/graphs"
print(graph_endpoint)
graph_params = {

    "id": ID,
    "name": "first_graph",
    "unit": "commit",
    "type": "int",
    "color": "momiji",

}
graph_header = {
    "X-USER-TOKEN": "yes23111996"
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_header)
# print(response.json())

# headers - key word argument (**args)
# https://pixe.la/v1/users/binduhc/graphs/abc.html

# ?updating the pixel for the graph for a date and quantity

update_pixel_ep = f"{top_ep}{NAME}/graphs/{ID}"
#
todays_date = datetime.datetime.now()
formatted_date = todays_date.strftime("%Y%m%d")
update_pixel_params = {
    "date": formatted_date,
    "quantity": input("how many commits for the day?"),

}
response = requests.post(url=update_pixel_ep, json=update_pixel_params, headers=graph_header)
print(response.json())

#datetime module to automatic date/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

# todays_date = datetime.datetime.now()
# formatted_date = todays_date.strftime("%Y%m%d")
# update_pixel_params_put = {
#     "quantity": "45",
# }
# update_pixel_ep_put = f"{top_ep}{NAME}/graphs/{ID}/{formatted_date}"
# response = requests.put(url=update_pixel_ep_put, json=update_pixel_params_put, headers=graph_header)
# response = requests.delete(url=update_pixel_ep_put, headers=graph_header)
# print(response.json())