from datetime import datetime
from colors import prCyan, prRed, prYellow, prGreen, prLightPurple, prPurple , B , Black

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = 'Hey! I am on SpyChat & Available'


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Divam', 'Mr.', 20, 4.7)

friend_one = Spy('Amarjeet', 'Mr.', 21, 4.9)
friend_two = Spy('Anshul', 'Ms.', 21, 4.39)
friend_three = Spy('Nancy', 'Ms', 20, 4.95)
friends = [friend_one, friend_two, friend_three]


