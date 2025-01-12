import random
import time
from datetime import datetime
from pkg.Homepage import Homepage
from pkg.EventDeck import EventDeck

class Game:
    def __init__(self, playerA, playerB, board):
        self.playerA = playerA
        self.playerB = playerB
        self.board = board
        self.current_turn = playerA
        self.other_player = playerB
        self.switch_players = True
        self.prison_player = None
        self.event_deck = None

    def game_loop(self):
        while True:
            time.sleep(3)
            print("\n\n\n\n🐻  === GAME STATUS === 💰\n")
            Homepage.show_player_status(self.board)

            # Makes prison player skip one turn 
            if self.prison_player == self.current_turn:
                print(f'''\n{self.prison_player.type} {self.prison_player.name} {self.prison_player.icon} is still in PRISON!\n''')
                self.switch_players_helper()

                self.prison_player = None
                
            print(f'''\n\nYou're up {self.current_turn.type} {self.current_turn.name} {self.current_turn.icon} !''')
            Homepage.show_ingame_options()
            choice = input("\nWhat's next? ")
            is_numeric_input = Game.is_float(choice)
            if is_numeric_input == False:
                print("Not a valid option. Select again. You can exit with 6.")
                continue
            if int(choice) == 1:
                print("\nLET'S ROLE THE DICE! 🎲\n")
                die_result = self.roll_die()
                move_info = self.board.move_player(self.current_turn, die_result)
                new_field = move_info[0]
                crossed_start = move_info[1]

                if(crossed_start == True):
                    print(f"You passed START and survived another journey through Berlin.\nYou are rewarded with 10€ for your bravery. Keep going {self.current_turn.type} {self.current_turn.name} {self.current_turn.icon}!\n")
                    self.current_turn.balance += 10

                print(f"You move to the field: {new_field.name}\n")

                field_status = self.check_field_status(new_field, self.current_turn)
                game_status_continue = self.field_action(new_field, self.current_turn, field_status)
                               

                if game_status_continue == False:
                    break

                self.switch_players_helper()

            elif int(choice) == 2:
                self.board.show_board()
                continue
            elif int(choice) == 3:
                Homepage.show_player_status(self.board)
                continue
            elif int(choice) == 4:
                Homepage.show_property_status(self.board)                
                continue
            elif int(choice) == 5:
                Homepage.show_rules()                
                continue
            elif int(choice) == 6:
                print("Let's wrap it up early, thanks for playing!")
                break
            else:
                print("Not a valid option. Select again. You can exit with 6.")
                continue


    def check_field_status(self, field_object, current_player):
        name = field_object.short_name
        owner = field_object.owner 
        house_status = field_object.house

        if name in ["E1", "E2"]:
            return "event card"
        elif name == "ST": 
            return "start"
        elif name == "PR":
            return "prison"

        else: # street
            if owner == "for sale":
                print("You can buy this property!")
                return "for sale"
            elif owner == current_player.name and house_status == "  ":
                return "house to build"
            elif owner == current_player.name and house_status == "🏡":
                return "house present"
            elif owner != current_player.name:
                return "rent due"

    def field_action(self, field_object, current_player, field_status):
        price = field_object.price
        if field_status == "prison":
            print("DAMN - You hung out with the wrong crowd again and landed in prison.\nSkip one turn while your lawyer posts your bail.\n")
            self.prison_player = current_player
            return True
        
        elif field_status == "event card":
            input(f"\nTime to draw a BERLIN EVENT CARD! Good luck! Hit enter to do so.\n\n\n")

            # Check if event_deck exists and has cards
            if not self.event_deck or not self.event_deck.cards:
                print("Let's shuffle the event cards!\n")
                self.event_deck = EventDeck()
  
            event_success = current_player.draw_event_card(self.event_deck)
            if event_success == False:
                self.end_game(current_player)
                return False
            return True
        elif field_status == "for sale":
            choice = input(f"Do you want to buy this street for {price:.2f}€? (y/n) ")
            if choice == "y":
                current_player.buy_street(field_object)
            elif choice == "n":
                print("\nYou don't want to buy this street. Let's move on.")
            else:
                print("Input not valid. Let's move on then.")
            return True
        elif field_status == "house to build":
            choice = input(f"This is your street already! You can build a house for 20€ - Do you want to? (y/n) ")
            if choice == "y":
                current_player.buy_house(field_object)
            elif choice == "n":
                print("\nYou don't want to build a house here. Let's move on.")
            else:
                print("Input not valid. Let's move on then.")
                return True
        elif field_status == "house present":
            print(f"This is your street and you built a nice house already! Nothing else to do here.\n")            
        elif field_status == "rent due":
            input(f"This property belongs to the other player. You have to pay rent! Hit enter to do so.")
            rent_success = current_player.pay_rent(field_object, self.other_player)
            if rent_success == False:
                self.end_game(current_player)
                return False
            return True
        

    def roll_die(self):
        result = random.randint(1, 6)
        if result == 6:
            print(f'''Nice, {self.current_turn.type} {self.current_turn.name} {self.current_turn.icon}! A 6 means that the next turn is also yours.''')
            self.switch_players = False
        else:
            print(f"You threw a: {result}")
            self.switch_players = True

        return result
    
    def switch_players_helper(self):
        if self.switch_players == True: 
            if self.current_turn == self.playerA:
               self.current_turn = self.playerB
               self.other_player = self.playerA
            elif self.current_turn == self.playerB:
               self.current_turn = self.playerA
               self.other_player = self.playerB



    def end_game(self, current_player):
        # Determine the winner and loser
        if current_player == self.playerA:
            winner = self.playerB
            loser = self.playerA
        elif current_player == self.playerB:
            winner = self.playerA
            loser = self.playerB

        winner_balance = winner.balance

        # Print the game result
        print(f'''Sorry, {current_player.type} {current_player.name} {current_player.icon}! You ran out of money.\n''')
        print(f'''Congrats, {winner.type} {winner.name} {winner.icon}!  🥳🎉🪅🪩   You WON Berlinopoly and still have {winner_balance:.2f}€! Your success will live forever in the eternal highscores.''')

        # Prepare the highscore log entry
        date = datetime.now().strftime("%d.%m.%Y")
        highscore_entry = (
            f"{date} | {winner.type} {winner.name} won against "
            f"{loser.type} {loser.name} with {winner.balance} Euro in the bank!"
        )

        # Append the highscore entry to highscores.txt
        try:
            with open("highscores.txt", "a", encoding="utf-8") as file:
                file.write(highscore_entry + "\n")
            print("\nGame result has been logged in 'highscores.txt'.")
        except Exception as e:
            print(f"An error occurred while saving the highscore: {e}")


    # Function that returns false if the value is not numeric with deceimals separated by . 
    @staticmethod
    def is_float(input):
        try:
            float(input)
            return True
        except ValueError:
            return False