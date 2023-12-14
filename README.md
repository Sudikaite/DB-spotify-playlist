# Django and Spotify API Project

## About the Project

This project is created in the Python programming language, using Django, to integrate the Spotify API and allow users to search for artists and view their playlists.

## Features

- Users can open the page and enter the desired artist in the search field.
- By clicking the search button, the system will use the Spotify API to search for the artist.
- The found artist will be presented to the user, along with their playlist.
  
## Technologies

- Django: A web framework based on Python.
- Spotify API: Used for artist search and playlist retrieval.
  
## How to Run the Project

- Ensure that you have Python and Django installed.
- Create a new virtual environment and activate it.
- Install the required dependencies

## Register on the Spotify Developer platform and obtain API keys.

- SPOTIFY_CLIENT_ID=Your_Client_ID
- SPOTIFY_CLIENT_SECRET=Your_Client_Secret

## Run migrations and start the server.

- python manage.py migrate
- python manage.py runserver
  
Open your browser and go to http://localhost:8000
