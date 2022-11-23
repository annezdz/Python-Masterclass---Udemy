from data import albums

#CONSTANTE NO PYTHON

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

CHOICE_ALBUM = "Please choose your album (invalid choice exists):"
CHOICE_SONG = 'Please choose your song:'
while True:
    print(CHOICE_ALBUM)
    for index, (title, artist, year, songs) in enumerate(albums):
        print('{} : {}'
              .format(index + 1, title))

    # for index, value in enumerate(albums): outra forma de fazer o unpacking dos dados
    #     title, artist, year, sons = value
    #     print(index + 1, title, artist, year, sons)
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    elif choice == 0:
        break
    else:
        choice = 0
        print("Album doesnt exist")
        print(CHOICE_ALBUM)
        choice = int(input())
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    print(CHOICE_SONG)
    for index, (track_number, song) in enumerate(songs_list):
        print('{} : {}'.format(index + 1, song))
    choice_song = int(input())
    if 1 <= choice_song <= len(songs_list):
        song = songs_list[choice_song -1][SONG_TITLE_INDEX]
    else:
        choice_song = 0
        print('Invalid song: ')
        print(CHOICE_SONG)
        choice_song = int(input())
        song = songs_list[choice_song -1][SONG_TITLE_INDEX]
    print('Playing {}!'.format(song))
    print('*' * 20)
