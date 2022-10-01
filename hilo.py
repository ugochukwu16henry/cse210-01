@@ -25,15 +25,14 @@ def __init__(self):
<<<<<<< HEAD
self.score = 300
self.card = Card()
self.card.draw()


def start_game(self):
        """Starts the game by running the main game loop.

=======
        self.score = 300
        self.card = Card()
        self.card.draw()


    def start_game(self):
        """Starts the game by running the main game loop.
>>>>>>> f7e8445b1a26f861767fab92cf9a90a3b40bff88
        Args:
            self (Director): an instance of Director.
        """
        print("Welcome to Hilo! Each round you'll guess whether the next card will be higher or lower than the last one!\n")
        print("\nWelcome to Hilo! Each round you'll guess whether the next card will be higher or lower than the last one!")
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
@@ -48,8 +47,8 @@ def get_inputs(self):
<<<<<<< HEAD
=======
        """
>>>>>>> f7e8445b1a26f861767fab92cf9a90a3b40bff88

        last = self.card.face
        print(f"The card is: {last}")
        #make sure only h or l
        print(f"\nThe card is: {last}")


        self.choice = input("Higher or lower? [h/l] ")
        while (self.choice.lower() != "h") and (self.choice.lower() != "l"):
@@ -63,7 +62,6 @@ def do_updates(self):
            self (Director): An instance of Director.
<<<<<<< HEAD
""""""
=======
        """
>>>>>>> f7e8445b1a26f861767fab92cf9a90a3b40bff88


        self.card.draw()

        newCard = self.card.face
@@ -74,7 +72,7 @@ def do_updates(self):
<<<<<<< HEAD
newCard = self.card.face
oldCard = self.card.lastCard

print(f"The new card is: {self.card.face}")
print(f"\nThe new card is: {self.card.face}")

if newCard > oldCard:
            if self.choice.lower() == "h":
@@ -105,9 +103,9 @@ def do_outputs(self):
        # Keep playing as long the score is above 0
if self.score > 0:
=======
            newCard = self.card.face
            oldCard = self.card.lastCard

        print(f"The new card is: {self.card.face}")
        print(f"\nThe new card is: {self.card.face}")

        if newCard > oldCard:
            if self.choice.lower() == "h":
@@ -105,9 +103,9 @@ def do_outputs(self):
        # Keep playing as long the score is above 0
        if self.score > 0:
>>>>>>> f7e8445b1a26f861767fab92cf9a90a3b40bff88

            playing = input("Wanna keep playing? [y/n]")
            playing = input("Wanna keep playing? [y/n] ")
            while (playing.lower() != "y") and (playing.lower() != "n"):
                playing = input("Wanna keep playing? [y/n]")
                playing = input("Wanna keep playing? [y/n] ")
<<<<<<< HEAD
self.is_playing = (playing.lower() == "y")
pass
=======
            self.is_playing = (playing.lower() == "y")
            pass
>>>>>>> f7e8445b1a26f861767fab92cf9a90a3b40bff88
