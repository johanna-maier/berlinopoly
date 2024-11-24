class Homepage:
    def show_homepage(): 
        print("\n === 🐻 WELCOME TO BERLINOPOLY 💰 ===  ")
        print("----------------------------------------")
        print("|  1.   New Game   |  2.   High Scores |")
        print("----------------------------------------")
        print("|  3.   Show Rules |  4.   Exit        |")
        print("----------------------------------------\n")
    
    def choose_player():
        player_data = {
            "Hipster": "🧢",
            "Influencer": "🤳",
            "Bear": "🐻",
            "Döner": "🥙",
            "Entrepreneur": "💡",
            "Politician": "💼",
            "Tourist": "🌍",
            "Techno Fan": "🎶",
            "Vegan": "🥑",
            "Punk": "🏴",
            "Artist": "🎨",
            "Biker": "🚲",
            "Skater": "🛹",
            "Biergarten Lover": "🍺",
            "BVG Employee": "🚇"
        }


        # Display the available player types
        print("Choose your player type:")
        for i, (role, emoji) in enumerate(player_data.items(), 1):
            print(f"{i}. {role} {emoji}")

        # Get the player's choice
        while True:
            try:
                choice = int(input("\nEnter the number corresponding to your choice: "))
                if 1 <= choice <= len(player_data):
                    player_type = list(player_data.keys())[choice - 1]
                    player_icon = player_data[player_type]
                    break
                else:
                    print("Invalid choice, please choose a number from the list.")
            except ValueError:
                print("Please enter a valid number.")

        # Get the player's name
        player_name = input("Enter your player name: ")

        print(f"\nYou have chosen: {player_type} {player_icon}  as your player type.")
        print(f"Your player name is: {player_name}")

        player_info = [player_name, player_type, player_icon]

        return player_info

        
    def show_ingame_options():
        print("-------------------------------------------------")
        print("|  1.   Roll Die       |  2.   Show Board       |")
        print("-------------------------------------------------")
        print("|  3.   Show Players   |  4.   Show Properties  |")
        print("-------------------------------------------------")
        print("|  5.   Show Rules     |  6.   Stop Playing     |")
        print("-------------------------------------------------")

    def show_player_status(current_board):
        # Access players from the board
        players = [current_board.playerA, current_board.playerB]

        # Column headers
        headers = ["Name", "Type", "Icon", "Position", "Balance", "Properties"]

        # Prepare player data for column width calculations
        player_data = [
            {
                "Name": player.name,
                "Type": player.type,
                "Icon": player.icon,
                "Position": str(player.position),  # Convert position to string
                "Balance": f"{player.balance}€",
                "Properties": ", ".join(f"{key} ({value})" for key, value in player.properties.items()) if player.properties else "None"
            }
            for player in players # syntax: list comprehension > means that the same dictionary structure is appended for each player in players 
        ]

        # Calculate column widths
        column_widths = {
            header: max(len(header), *(len(data[header]) for data in player_data))
            for header in headers
        }

        # Print header row
        header_row = " | ".join(f"{header:<{column_widths[header]}}" for header in headers)
        # print("\nPlayers:")
        print(header_row)
        print("-" * (sum(column_widths.values()) + 3 * (len(headers) - 1)))

        # Print each player's data
        for data in player_data:
            row = " | ".join(f"{data[header]:<{column_widths[header]}}" for header in headers)
            print(row)

    def show_property_status(current_board):
        print("\n=== Property Status ===\n")

        # Prepare data
        fields = [
            {
                "Name": field.name,
                "Short Name": field.short_name,
                "House": "built" if field.house == "🏡" else "not built" if field.house != "--" else "--",
                "Price": f"{field.price}€",
                "Rent": f"{field.rent_w_house}€" if field.house == "🏡" else f"{field.rent}€",
                "Owner": field.owner if field.owner else "None",
                "Player Present": field.player_present if field.player_present else "",
            }
            for field in current_board.board_fields
        ]


        # Column headers
        headers = ["Name", "Short Name", "House", "Price", "Rent", "Owner", "Player Present"]

        # Calculate column widths
        column_widths = {
            header: max(len(header), *(len(str(field[header])) for field in fields))
            for header in headers
        }

        # Print header row
        header_row = " | ".join(f"{header:<{column_widths[header]}}" for header in headers)
        print(header_row)
        print("-" * (sum(column_widths.values()) + 3 * (len(headers) - 1)))

        # Print each field's data
        for field in fields:
            row = " | ".join(f"{field[header]:<{column_widths[header]}}" for header in headers)
            print(row)
        input("\nPress Enter to return to the main menu...")


    def show_rules():
        print("\n       === 🐻 BERLINOPOLY 💰 ===       ")
        print("----------------------------------------")
        print("              GAME RULES              ")
        print("----------------------------------------\n")
        
        print("** GAME OBJECTIVE **")
        print("The goal of the game is to bankrupt your opponent by buying and developing streets in Berlin.")
        print("You start with 100€ and take turns rolling a single die. Move along the streets and make strategic decisions to gain advantage!")
        print("\n** HOW TO PLAY **")
        print("1. Roll the die (1-6) and move your token accordingly.")
        print("2. If you land on a street, you can choose to purchase it.")
        print("3. You can build a house on your street for 20€, which will double its rent value.")
        print("4. If your opponent lands on a street you own, they must pay you rent.")
        print("5. If you land on an event field, you’ll draw a random event card with a surprise!")
        print("6. If you land on the ‘Prison’ field, you will be in prison for 1 round and skip this turn.")
        print("7. If you pass ‘Start’, you’ll receive 10€ from the bank!\n")
        
        print("** GAME FIELDS **")
        print("The board consists of 16 fields, arranged in a fixed sequence. Here’s a breakdown of each field:")

        print("\n--- CORNER FIELDS ---")
        print("Start (Alexanderplatz) - You start the game here and earn 10€ when passing.")
        print("Prison (Berghain Club) - If you land here, you must sit out for 1 round while your lawyer posts bail.")
        
        print("\n--- STREET FIELDS ---")
        print("Each street can be bought for a price between 5€ and 40€, and you can build one house on it for 20€. A house doubles the rent value of the street.")
        print("The streets are:")
        print("1. Kottbusser Tor (KT) - Buy for 5€, Rent: 4€ (with house: 8€)")
        print("2. Wittenau (WT) - Buy for 10€, Rent: 6€ (with house: 12€)")
        print("3. Alt-Tegel (AT) - Buy for 15€, Rent: 10€ (with house: 20€)")
        print("4. Tempelhofer Feld (TF) - Buy for 20€, Rent: 12€ (with house: 24€)")
        print("5. Friedrichstraße (FS) - Buy for 25€, Rent: 14€ (with house: 28€)")
        print("6. Museumsinsel (MI) - Buy for 30€, Rent: 16€ (with house: 32€)")
        print("7. Brandenburger Tor (BT) - Buy for 35€, Rent: 18€ (with house: 36€)")
        print("8. Kurfürstendamm (KD) - Buy for 40€, Rent: 20€ (with house: 40€)")

        print("\n--- EVENT FIELDS ---")
        print("There are two special event fields where you will draw an event card.")
        print("Event cards can have different effects, such as changing your money balance!")
        
        print("\n** RULES FOR MOVEMENT & ACTIONS **")
        print("1. Players start with 150€ each.")
        print("2. On your turn, roll the die and move forward by the number rolled.")
        print("3. If you land on an owned street, you must pay the owner rent (based on the street’s value).")
        print("4. If you land on an unowned street, you may purchase it for the listed price.")
        print("5. If you have enough money, you may build a house for 20€ on your owned street. This doubles the rent value.")
        print("6. If you roll a 6, you get another turn!")
        print("7. If a player runs out of money, they lose the game.\n")

        print("** END OF GAME **")
        print("The game ends when one player runs out of money. The remaining player wins!\n")

        print("Now you're ready to play! Enjoy Berlinopoly! 🎲💰\n")
        input("\nPress Enter to return to the main menu...")

    def show_highscores():
        try:
            with open("highscores.txt", "r") as file:
                print("\n=== 🐻 BERLINOPOLY HIGHSCORES 💰 ===")
                print(file.read())
        except FileNotFoundError:
            print("Highscores file not found. No scores to display.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        input("\nPress Enter to return to the main menu...")
