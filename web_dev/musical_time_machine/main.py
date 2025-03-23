import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
spotify_client_id = os.environ.get("SPOTIFY_CLIENT_ID")
spotify_client_secret_key = os.environ.get("SPOTIFY_CLIENT_KEY")
spotify_redirect_uri = "http://127.0.0.1:9090/"
print("Enter the date of your choice to build musical files on that date.")
date_input = input("enter the date")
month_input = input("enter the month")
year_input = input("enter the year")
url = "https://www.billboard.com/charts/hot-100/" + year_input + "-" + month_input + "-" + date_input + "/"
response = requests.get(url)

musical_html = BeautifulSoup(response.text, "html.parser")
names_of_songs = musical_html.select(selector="li.lrv-u-width-100p ul li h3")

# authenticate spotify account
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret_key,
                                               redirect_uri=spotify_redirect_uri,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="x.txt"))

user_id = sp.current_user()["id"]
print(user_id)
song_list = []
song_uris = []
for names in names_of_songs:
    song_list.append(names.get_text().strip())
for songs in song_list:
    print(songs)
    result = sp.search(q=f"track:{songs} year:{year_input}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        # print(songs, uri)
    except IndexError:
        # print(f"{songs} is not present.")
        pass
playlist_name = f"my billboard for {year_input}-{month_input}-{date_input}"
spotify_playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
print(spotify_playlist['id'])
playlist_added_id = sp.playlist_add_items(spotify_playlist['id'], song_uris)
print(playlist_added_id)
