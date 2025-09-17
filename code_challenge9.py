print ("🦜 PARROT SIMULATOR - THE ECHO CHAMBER") 
word = input("What do you want your Parrot to say? ")
squawk  = eval(input("How many times should the Parrot squawk it? ")) 

print ("Listen to your Parrot:")
for s in range (squawk, 0, -1) :
    print ("🦜 SQUAWK!", word,"!")