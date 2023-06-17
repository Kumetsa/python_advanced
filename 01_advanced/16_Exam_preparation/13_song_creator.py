def add_songs(*songs):
    song_dict = {}

    result = []

    for song in songs:
        if song[0] not in song_dict:
            song_dict[song[0]] = []
        song_dict[song[0]].extend(song[1])

    for song, lyrics in song_dict.items():
        result.append(f"- {song}")
        for lyric in lyrics:
            result.append(lyric)

    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
