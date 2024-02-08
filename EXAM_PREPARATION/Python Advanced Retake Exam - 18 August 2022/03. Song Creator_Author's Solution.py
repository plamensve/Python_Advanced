import os


def add_songs(*tuples_):
    songs = {}
    for t in tuples_:
        if t[0] not in songs:
            songs[t[0]] = []
        songs[t[0]].extend(t[1])
    result = []
    for song_title, song_lyrics in songs.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)
    return os.linesep.join(result)
