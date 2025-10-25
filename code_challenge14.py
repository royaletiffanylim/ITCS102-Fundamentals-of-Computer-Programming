print ("FAVORITE ANIME LIST")
list = []
lim = True 

while lim == True:
    anime_title = input("Enter Favorite Anime Title/s Here (type 'done' to finish listing): ")
    if anime_title.lower() == 'done':
        break
    list.append(anime_title)
    print(f"'{anime_title}' Has Been Added to Your Anime List.")
print("You're Done Listing Your Favorite Animes.")
print("Your Anime List Includes the Following:")
for anime in list:
    print(f"- {anime}") 