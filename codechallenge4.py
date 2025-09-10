print ("Welcome to the World of Manga")
print ("Please, answer few questions to find new read.")

genre = input("What genre of Manga do you want to watch? (romantic, adventure, horror)")
length = input("How long would you like your Manga be? (short, medium, long) ")
year = input("Which Year? (2000s or 2010s)")

if genre == 'romantic':
    if year == '2000s':
        if length == 'short':
            print ("RECOMMENDED MANGA: Absulote Boyfriend")
        elif length == 'medium':
            print ("RECOMMENDED MANGA: Parfair Tic!")    
        elif length == 'long':
             print ("RECOMMENDED MANGA: Boys Over Flower")
    if year == '2010s':
        if length == 'short':
            print ("RECOMMENDED MANGA: Ano Ko no, Toriko")
    if length == 'medium': 
        print ("RECOMMENDED MANGA: Strobe Edge")
    elif length == 'long':
         print ("RECOMMENDED MANGA: Spice And Wolf ")
        
if genre == 'adventure':
    if year == '2000s':
        if length == 'short':
            print ("RECOMMENDED MANGA: Adventure Boys")
        elif length == 'medium':
            print ("RECOMMENDED MANGA: Samorai Deeper Kyo")    
        elif length == 'long':
             print ("RECOMMENDED MANGA: Rave Master")
    if year == '2010s':
        if length == 'short':
            print ("RECOMMENDED MANGA:Noah's Notes")
        if length == 'medium': 
            print ("RECOMMENDED MANGA: Blue Exorcist")
        elif length == 'long':
             print ("RECOMMENDED MANGA: Black Clover")
        

if genre == 'horror':
    if year == '2000s':
        if length == 'short':
            print ("RECOMMENDED MANGA: Octopus Girl ")
        elif length == 'medium':
            print ("RECOMMENDED MANGA: Mail ")    
        elif length == 'long':
             print ("RECOMMENDED MANGA: Gantz")
    if year == '2010s':
        if length == 'short':
            print ("RECOMMENDED MANGA: Hide Out ")
        if length == 'medium': 
            print ("RECOMMENDED MANGA: Kasane ")
        elif length == 'long':
            print ("RECOMMENDED MANGA: High School Of The Dead")
    