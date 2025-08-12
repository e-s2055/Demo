#beginnier python project - Madlibs - Kylie Ying 
# String Concat such as "Sub to ___"

#Var 1
#youtuber = "Momo" #string var
#print("Subscribe to " + youtuber)

#Var 2
#print("Subscribe to {}".format(youtuber)) # .format() fills in whatever is in the {}s

#Var 3 - cleanest way
#print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
famous_person =input("Famous Person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)