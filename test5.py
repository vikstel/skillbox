violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs = int(input("Сколько песен выбрать? "))
songs_list = []
songs_time = 0
for i in range(songs):
    song_name = input(f"Название {i + 1}-й песни: ")
    songs_list.append(song_name)
for song in range(len(violator_songs)):
    if violator_songs[song][0] in songs_list:
        songs_time += violator_songs[song][1]
print(f"Общее время звучания песен: {round(songs_time, 2)} минуты")




