from move import Move
import random

class Player:

    PLAYER_MARKER = "X"   #define class atributes
    COMPUTER_MARKER = "O" #define class atributes

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:    # jesli is_human jest True wtedy maker zwraca marker przypisany do human czyli "X
            self._marker = Player.PLAYER_MARKER
        else: # jesli is_human jest False to maker zwraca marker przypisany do computera czyl "O"
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:  # Tworzymy loop w ktorym pytamy o ruch usera i sprawdzamy czy jest valid, jesli jest valid to wychodzimy z loppy jesli jest nieprawidlowy to loop sie powtarza
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter an intiger between 1 - 9")
        return move


    def get_computer_move(self): # towrzymy metode ktora bedzie nam zwracac wartosc ktora wybral komputer. jest ona random
        random_choice = random.choice(range(1,10))
        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move




