from collections import deque
import random

class EventDeck:
    def __init__(self):
        # Initialize the queue with the provided events
        self.cards = deque([
            {"type": "Positive", "title": "BBQ Donut on Tegel Lake!", 
             "text": "Your cooking skills impress everyone, and your friends pitch in to cover costs. Collect €30.", "balance_change": 30},
            {"type": "Positive", "title": "Berghain Entry Success!", 
             "text": "The bouncer lets you in because of your outfit. Your friends pay your drinks all night and give you a thank-you. Collect €50.", "balance_change": 50},
            {"type": "Positive", "title": "Kayak Adventure!", 
             "text": "You help guide your group through a tricky water level. Receive €25 as a thank-you.", "balance_change": 25},
            {"type": "Positive", "title": "Street Food Tour!", 
             "text": "You find an incredible food stall and promote it on social media, earning a small influencer bonus. Gain €20.", "balance_change": 20},
            {"type": "Positive", "title": "Urban Fox Encounter!", 
             "text": "You report the sighting to a wildlife project, and they reward you for contributing to their data. Collect €15.", "balance_change": 15},
            {"type": "Positive", "title": "Ping-Pong Champion!", 
             "text": "Your skill at the park’s ping-pong table earns you bragging rights—and some bets. Collect €10.", "balance_change": 10},
            {"type": "Positive", "title": "Supreme Burger Delight!", 
             "text": "You recommend the perfect burger to a tourist and they thank you with a small tip. Gain €20.", "balance_change": 20},
            {"type": "Positive", "title": "Successful Flea Market Day!", 
             "text": "You sell vintage treasures at Mauerpark and make a profit. Receive €30.", "balance_change": 30},
            {"type": "Positive", "title": "Bike Tour and Beer Garden!", 
             "text": "A group of tourists you guided along the Mauerweg buys you a beer and tip you. Gain €20.", "balance_change": 20},
            {"type": "Positive", "title": "Art Sale!", 
             "text": "A Friedrichshain gallery loves your work and pays you a bonus for an exclusive deal. Gain €50.", "balance_change": 50},
            {"type": "Negative", "title": "BBQ Donut Disaster!", 
             "text": "You accidentally spill drinks all over the boat, and the rental company charges you a cleaning fee. Pay €30.", "balance_change": -30},
            {"type": "Negative", "title": "Kayak Mishap!", 
             "text": "You capsize and have to pay for repairs to the kayak’s equipment. Pay €20.", "balance_change": -20},
            {"type": "Negative", "title": "U-Bahn Ticket Fine!", 
             "text": "A BVG inspector catches you riding without a validated ticket. Pay €60.", "balance_change": -60},
            {"type": "Negative", "title": "Animal Trouble in the Forest!", 
             "text": "Feeding wild animals backfires when a wild boar damages your backpack. Pay €10 to replace it.", "balance_change": -10},
            {"type": "Negative", "title": "Street Food Overload!", 
             "text": "You splurge at a food market, buying more than you can carry. Pay €15 for the extra expense.", "balance_change": -15},
            {"type": "Negative", "title": "Cycling Crash!", 
             "text": "You hit a pothole and have to pay for bike repairs. Pay €20.", "balance_change": -20},
            {"type": "Negative", "title": "Burger Disappointment!", 
             "text": "Supreme Burger is closed, and you settle for a less tasty option. Pay €5 for the bad meal.", "balance_change": -5},
            {"type": "Negative", "title": "Parking Chaos!", 
             "text": "A racoon chews through your bike lock near a beer garden. Pay €30 for a replacement.", "balance_change": -30},
            {"type": "Negative", "title": "Winter Heizkosten Spike!", 
             "text": "Berlin’s winter heating bills hit hard. Pay €50 to the bank.", "balance_change": -50},
            {"type": "Negative", "title": "Döner Sauce Disaster!", 
             "text": "You spill garlic sauce on your coat after a long night out. Pay €15 for dry cleaning.", "balance_change": -15},
            {"type": "Neutral", "title": "Sunday Shopping Confusion!", 
             "text": "You forget everything is closed and have to order food to survive the day.", "balance_change": -20},
            {"type": "Neutral", "title": "Ping-Pong Diplomacy!", 
             "text": "You share drinks with the player on your left after a friendly park match. Pay them €10.", "balance_change": -10},
            {"type": "Neutral", "title": "Friendly Wildlife Encounter!", 
             "text": "You photograph a raccoon and sell the image to a local nature blog. Collect €15.", "balance_change": 15},
            {"type": "Neutral", "title": "Späti Generosity!", 
             "text": "You buy a round of drinks for your group at the Späti. Pay €5.", "balance_change": -5},
            {"type": "Neutral", "title": "Gentrification Fee!", 
             "text": "A protest in your neighborhood forces you to contribute to a local initiative. Pay €10 to the bank.", "balance_change": -10},
            {"type": "Neutral", "title": "Street Artist Moment!", 
             "text": "A busker asks you to join their performance, and you make a little cash. Gain €15.", "balance_change": 15}
        ])
        random.shuffle(self.cards)

