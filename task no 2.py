import os
songs =[{'title': 'shape of u', 'artist':
'ed sheeran'},


        {'title': 'blinding lights','artist':
'the weaknd'         }


       ]


def filter_songs_by_artist(songs,artist):
    return list(filter(lambda songs: songs['artist'] == artist , songs))

def convert_title_uppercase(songs):
    return list(map(lambda songs:songs['title'].upper(),songs))
artist='ed sheeran'
filtered_songs= filter_songs_by_artist(songs,'artist A')
uppercase_titles= convert_title_uppercase(filtered_songs)



print("filtered songs:",
filtered_songs)
print("uppercase titles:",
uppercase_titles)      


