import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random


def asked_artist():
    favorite_artist = input('Ki a kedvenc előadód? ')
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    results = sp.search(q=favorite_artist, limit=50, type='artist')
    artist_uri = results['artists']['items'][0]['uri']
    all_albums = sp.artist_albums(artist_uri, album_type='album')
    return all_albums


def album_names(albums):
    album_names_list = []
    for album in albums['items']:
        album_names_list.append(album['name'])
    return album_names_list


def album_guessing(album_list):
    guessed_album = random.choice(album_list)
    words = guessed_album.split()
    max_length = 0
    max_word = ''
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
    for _ in words:
        if _ != max_word:
            print(_, end=' ')
        else:
            for _ in range(len(max_word)):
                print('_', end=' ')
    print('')
    #   print(guessed_album)
    guessed_word = input('Add meg az odaillő szót! ').lower()
    if guessed_word == max_word.lower():
        print(f'Gratulálok, eltaláltad, a helyes válasz: {guessed_album}')
    else:
        print(f'Sajnos nem ez volt, a helyes válasz: {guessed_album}')


def main():
    print('Elkérem a kedvenc előadódat és egy random albumának, ki kell találnod a leghosszabb szavát.')
    album_guessing(album_names(asked_artist()))


main()
