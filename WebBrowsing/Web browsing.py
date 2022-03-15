import webbrowser
while True:
    userName = input("Please, Enter Your First Name: ")
    if userName.isalpha():
        userName = str(userName)
        break
    else:
        print("Invalid Input")

print(f"Hello {userName}, Which Web-Site you want to visit:")
print("**********************************************************************")
print("                           [1] Facebook                               ")
print("                           [2] Twitter                                ")
print("                           [3] Google                                 ")
print("                           [4] LinkedIn                               ")
print("                           [5] Exit                                   ")
print("**********************************************************************")
print(" ")

while True:
    choise = input("Your choise is : ")
    if choise.isnumeric():
        choise=int(choise)
        break
    else:
        print("Invalid Choise")

webSitesList = ("facebook", "twitter", "google", "linkedin")

if choise == 1:
    webbrowser.open(f"https://www.{webSitesList[0]}.com", new=2)
if choise == 2:
    webbrowser.open(f"https://www.{webSitesList[1]}.com", new=2)
if choise == 3:
    webbrowser.open(f"https://www.{webSitesList[2]}.com", new=2)
if choise == 4:
    webbrowser.open(f"https://www.{webSitesList[3]}.com", new=2)
if choise == 5 :
    print("Exit .................................. !!!")
    exit()
