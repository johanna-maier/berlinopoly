class Player:
    def __init__(self, name, type, icon):
        self.name = name
        self.type = type
        self.icon = icon
        self.balance = 150
        self.position = "Start"
        self.properties = {}

    def buy_street(self, field_object):
        price = field_object.price
        street_name = field_object.name

        if price > self.balance:
            print(f'''Sorry, {self.type} {self.name} {self.icon}, you don't have enough money.\nYou only have {self.balance:.2f}€. You need {price:.2f}€''')
        else:
            self.balance -= price
            self.properties[street_name] = ""
            field_object.owner = self.name
            print(f'''\nCONGRATS {self.type} {self.name} {self.icon} ! You are now the proud owner of: {street_name} 🔑''')
    
    def buy_house(self, field_object):
        house_price = 20 
        street_name = field_object.name

        if house_price > self.balance:
            print(f'''Sorry, {self.type} {self.name} {self.icon}, you don't have enough money.\nYou only have {self.balance:.2f}€. You need {house_price:.2f}€''')
        else:
            self.balance -= house_price
            self.properties[street_name] = "🏡"
            field_object.house = "🏡"
            print(f'''CONGRATS {self.type} {self.name} {self.icon} ! You built a new house on: {street_name} 🏡''')

    def pay_rent(self, field_object, other_player):
        house_status = field_object.house

        if house_status == "🏡":
            rent_price = field_object.rent_w_house
        else:
            rent_price = field_object.rent

        if rent_price > self.balance:
            print(f'''Sorry, {self.type} {self.name} {self.icon}, you don't have enough money.\nYou only have {self.balance:.2f}€. You need {rent_price:.2f}€''')
            print("\nYOU HAVE LOST THE GAME!")
            return False
        else:
            self.balance -= rent_price
            other_player.balance += rent_price
            print(f'''\nThanks {self.type} {self.name} {self.icon}, you PAID YOUR RENT of {rent_price:.2f}€!''')
            return True

    def draw_event_card(self, event_deck):
        # Draw the top card
        card = event_deck.cards.popleft()

        # Print event details
        print(f"{card['title'].upper()}")
        print(f"{card['text']}\n")

        if card["balance_change"] + self.balance < 0:
            print(f'''Sorry, {self.type} {self.name} {self.icon}, you don't have enough money.\nYou only have {self.balance:.2f}€. The needed balance change is {card["balance_change"]:.2f}€.''')
            print("\nYOU HAVE LOST THE GAME!")
            event_deck.cards.append(card)
            return False
        else:
            self.balance += card["balance_change"]
            print(f'''{self.type} {self.name} {self.icon}, your balance changed by {card["balance_change"]:.2f}€.''')
            # Print the player's new balance
            print(f"Your new balance is: €{self.balance}")

            # Recycle the card by adding it back to the end
            # Disabled this functionality. Game.py recreates and shuffles a new deck if the old one is empty.
            # event_deck.cards.append(card) 
            return True
        