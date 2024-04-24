from abc import ABC, abstractmethod


# 1 step: the ChatRoom- Publisher
class ChatRoom:
    def __init__(self):
        self.__participants = set()

    def join(self, participant):
        self.__participants.add(participant)

    def leave(self, participant):
        self.__participants.remove(participant)

    def broadcast(self, message):
        for participant in self.__participants:
            # send chat to all participants in chatroom
            participant.recieve(message)


# step 2 participant or subscriber interface
class Participant(ABC):
    @abstractmethod
    def recieve(self, message):
        pass


# step 3 : ChatMember-- concrete subscribers
class ChatMember(Participant):
    def __init__(self, name):
        self.name = name

    def recieve(self, message):
        print(f"{self.name} received: {message}")


# step 4: client
if __name__ == "__main__":
    general_chat = ChatRoom()

    # create participants
    user1 = ChatMember("Ahmad")
    user2 = ChatMember("mehmet")
    user3 = ChatMember("john")
    user4 = ChatMember("rashid khan")

    general_chat.join(user1)
    general_chat.join(user2)
    general_chat.join(user3)
    general_chat.join(user4)

    # send message to chat room
    general_chat.broadcast("Welcome to chat room")

    """
output:
Ahmad received: Welcome to chat room
rashid khan received: Welcome to chat room
mehmet received: Welcome to chat room
john received: Welcome to chat room"""
