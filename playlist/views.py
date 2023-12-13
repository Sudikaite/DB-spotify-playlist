from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Įrašoma savo Spotify paskyros "client_id" ir "client_secret" kodai.
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=' ', client_secret=' '))

def index(request):
    return render(request, 'playlist.html', context=context)

def get_spotify_tracks(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    found_artist_list = results['artists']['items']
    track_spotify_links= []

    if len(found_artist_list) > 0:
        artist = found_artist_list[0]
        artist_id = artist["id"]
        artist_name = artist["name"]
        tracks = sp.artist_top_tracks(artist_id, country='US')

        for track in tracks['tracks']:
            track_spotify_link = track['external_urls']['spotify']
            track_spotify_link = (track_spotify_link.replace("track", "embed/track") +
                                  "?utm_source=generator")
            track_spotify_links.append(track_spotify_link)
    return track_spotify_links, artist_name

def spotify_tracks(request):
    artist_name = request.GET.get('query')
    if artist_name is None:
 #įrašomas norimo playlist'o pavadinimas, kuris atsiranda pirminiu puslapio paleidimu.
        artist_name = "King Gizzard and the Lizard wizard"
    track_spotify_links, found_artist_name = get_spotify_tracks(artist_name)
    return render(request, 'playlist.html', {'track_spotify_links':
                                                 track_spotify_links, 'artist_name':found_artist_name})



