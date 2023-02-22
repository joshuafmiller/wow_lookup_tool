#make character and leaderboard requests concurent
#lookup async io python
#this is to increase performance
#teddy boy
# adding a comment

#3v3 lookup function
def character_3v3():

    while True:

        import requests
        print("")
        print("Welcome to the 3v3 lookup tool.  Please provide character name and realm.")
        print("Type home to go back to the main menu.")
        print("Type exit to leave program.")
        print("")
        user_name = input("Character name: ").lower()

        if user_name.strip() == "":
            print("No information provided, please try again.")
            continue

        if user_name.lower().strip() == "exit":
            print("Exiting program...")
            exit()
        if user_name.lower().strip() == "home":
            print("Navigating to main menu...")
            home()
        
        user_realm = input("Realm name: ").lower()

        print("Searching...")
        print("")  

        if user_realm.strip() == "":
            print("No information provided, please try again.")
            continue

        if user_realm.lower().strip() == "exit":
            print("Exiting program...")
            exit()
        if user_realm.lower().strip() == "home":
            print("Navigating to main menu...")
            home()
            

        character_url = f"https://us.api.blizzard.com/profile/wow/character/{user_realm}/{user_name}/pvp-bracket/3v3?namespace=profile-us&locale=en_US&access_token=USa64cPNwfHW4DmbGr1a4Jyeppy2KhCUeG"
        leaderboard_url = "https://us.api.blizzard.com/data/wow/pvp-season/34/pvp-leaderboard/3v3?namespace=dynamic-us&locale=en_US&access_token=USa64cPNwfHW4DmbGr1a4Jyeppy2KhCUeG"

        character_req = requests.get(character_url)
        leaderboard_req = requests.get(leaderboard_url)


        if character_req.status_code == 200:

            character = character_req.json()
            print("Results:")
            print(f"{character['character']['name']}'s 3v3 rating: {character['rating']}")
            response = set()
            if leaderboard_req.status_code == 200:
                rank = leaderboard_req.json()   

                for item in rank['entries']:
                    if user_name.lower() == item['character']['name'].lower() and user_realm.lower() == item['character']['realm']['slug'].lower():
                        print(f"Rank: {item['rank']}")
                        response = str("")
                        break
                    else:
                        response.add("Character is not high enough on ladder to have a rank.")
                        continue

                
        else:
            print("Please enter a valid name and realm.")
            response = str("")
        
        if type(response) == str:
            print(response)
        else:
            print(response.pop())
            print("")

#solo shuffle lookup function
def character_shuffle():
        while True:

            import requests
            print("")
            print("Please prvoide character name, realm, class, and spec.")
            print("Type home to go back to the main menu.")
            print("Type exit to leave program.")
            print("")
            user_name = input("Character name: ").lower()

            if user_name.strip() == "":
                print("No information provided, please try again")
                continue

            if user_name.lower().strip() == "exit":
                print("Exiting program...")
                exit()

            if user_name.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
            
                
            
            user_realm = input("Realm name: ").lower()


            if user_realm.strip() == "":
                print("No information provided, please try again")
                continue

            if user_realm.lower().strip() == "exit":
                print("Exiting program...")
                exit()

            if user_realm.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
            
            user_class = input("Class: ").lower()

            if user_class.strip() == "":
                print("No information provided, please try again")
                continue

            if user_class.lower().strip() == "exit":
                print("Exiting program...")
                exit()

            if user_class.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
            
                

            user_spec = input("Spec: ")

            if user_spec.strip() == "":
                print("No information provided, please try again")
                continue

            if user_spec.lower().strip() == "home":
                print("Navigating to main menu...")
                home()

            if user_spec.lower().strip() == "exit":
                print("Exiting program...")
                exit()
                

        
            print("Searching...")
            print("")

            solo_url = f"https://us.api.blizzard.com/data/wow/pvp-season/34/pvp-leaderboard/shuffle-{user_class}-{user_spec}?namespace=dynamic-us&locale=en_US&access_token=USa64cPNwfHW4DmbGr1a4Jyeppy2KhCUeG"
            solo_req = requests.get(solo_url)
            solo_data = solo_req.json()
            if solo_req.status_code == 200:
                for item in solo_data['entries']:
                    if user_name.lower() == item['character']['name'].lower() and user_realm.lower() == item['character']['realm']['slug'].lower():
                        print(f"Rating: {item['rating']}")
                        print(f"Rank: {item['rank']}")
                        break
            else:
                print("Please enter valid information")

#title lookup function
def character_titles():
        while True:

            import requests
            print("")
            print("Please prvoide character name and realm.")
            print("Type home to go back to the main menu.")
            print("Type exit to leave program")
            print("")
            user_name = input("Character name: ").lower()

            if user_name.strip() == "":
                print("No information provided, please try again")
                continue

            if user_name.lower().strip() == "exit":
                print("Exiting program...")
                exit()
            if user_name.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
                         
        
            user_realm = input("Realm name: ").lower()

            print("Searching...")
            print("")

            if user_realm.strip() == "":
                print("No information provided, please try again")
                continue

            if user_realm.lower().strip() == "exit":
                print("Exiting program...")
                exit()
            if user_realm.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
            
            title_url = f"https://us.api.blizzard.com/profile/wow/character/{user_realm}/{user_name}/titles?namespace=profile-us&locale=en_US&access_token=USa64cPNwfHW4DmbGr1a4Jyeppy2KhCUeG"
            title_req = requests.get(title_url)
            titles = title_req.json()

            if title_req.status_code == 200:
            
                print("This character has the following titles:")
                print("")
                for title in titles['titles']:
                    print(f"+{title['name']}")
            else:
                print("Please enter valid information")

#glad or bad lookup function
def glad_or_bad():

    while True:
            import re
            import requests
            print("")
            print("Please prvoide character name and realm.")
            print("Type home to go back to the main menu.")
            print("Type exit to leave program")
            print("")
            user_name = input("Character name: ").lower()

            if user_name.strip() == "":
                print("No information provided, please try again")
                continue

            if user_name.lower().strip() == "exit":
                print("Exiting program...")
                exit()

            if user_name.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
        
            user_realm = input("Realm name: ").lower()

            print("Searching...")
            print("")

            if user_realm.strip() == "":
                print("No information provided, please try again")
                continue

            if user_realm.lower().strip() == "exit":
                print("Exiting program...")
                exit()
            if user_realm.lower().strip() == "home":
                print("Navigating to main menu...")
                home()
            
            glad_url = f"https://us.api.blizzard.com/profile/wow/character/{user_realm}/{user_name}/achievements?namespace=profile-us&locale=en_US&access_token=USa64cPNwfHW4DmbGr1a4Jyeppy2KhCUeG"
            glad_req = requests.get(glad_url)
            glad = glad_req.json()
            response = {'', ''}
            response_if_title = ""
            if glad_req.status_code == 200:
                for item in glad['achievements']:
                    if re.search('Gladiator: ', item['achievement']['name']):
                        response.add(f"{item['achievement']['name']}")
                        response_if_title = "This character has the following Glad titles:"

                    else:
                        response.add("This character is Bad, not Glad")

                        continue
            else:
                print("Please enter valid information")

            print(response_if_title)
            print("")
            for item in sorted(response):
                if re.search('Gladiator: ', item):
                    print(item)

            if len(response) == 2:
                print("This character is Bad, not Glad")



#main menu
def home():
    while True:
        print("")
        print("Welcome to the WoW Lookup Tool!")
        print("Please select an option.")
        print("1. 3v3 PVP Stats")
        print("2. Solo Shuffle PVP Stats")
        print("3. Character Titles")
        print("4. Glad or Bad Checker")
        print("Type exit to leave the program.")
        print("")
        main_menu = input("Your selection: ")


        if main_menu.lower().strip() == "exit":
            print("Exiting program...")
            break 
        if main_menu.strip() == "1":
            character_3v3()
        if main_menu.strip() == "2":
            character_shuffle()
        if main_menu.strip() == "3":
            character_titles()
        if main_menu.strip() == "4":
            glad_or_bad()
        if main_menu.lower().strip() == "home":
            home()

        else:
            print("")
            print("Not a valid input")
            print("")
home()


