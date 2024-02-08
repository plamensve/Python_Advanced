import os


def add_songs(*string):
    info = {}
    for s in string:
        song_name = s[0]
        song_lyrics = s[1]
        if song_name not in info:
            info[song_name] = song_lyrics
        else:
            info[song_name] += song_lyrics

    msg = []
    for tittle, song_lir in info.items():
        msg.append(f"- {tittle}")
        if song_lir:
            msg.extend(song_lir)
    return os.linesep.join(msg)