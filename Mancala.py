# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 11-20-2022
# Description: A text based game version of the popular board game Mancala.

print("Welcome to Mancala!\n\nThe objective of the game is to collect as many seeds as you can in your store!")
print("Players will pick up seeds from their pits and sow them to the right, placing one seed in each pit along the way.")
print("When you cross to your store, you stow away a seed but if you cross your oppenent's store, you skip over to their pit!")
print("Switch turns when you run out of seeds, if your last seed lands in your store, gain a free turn!")
print("If the last seed lands in your own own empty pit adjacent to the opponent's pit, you may capture their seeds into your pit!")
print("Good luck and have fun!\n")


class Player:
    """Class object that represents the two players playing the game."""

    def __init__(self, name):
        """Initializes Player class and name parameter that represents name of players."""
        self._name = name

    def get_name(self):
        """Get method that returns the name of players."""
        return self._name


class Board:
    """
    Class object that represents the physical aspects of the Mancala board. This includes all of its pits, player
    color/side, seeds, and storages. It is used by the MancalaGame class as an object that represents the board that
    players use for the game.
    """

    def __init__(self, seeds, pits):
        """Initializes Board class and its data members, the number of pits and seeds within the Mancala game board."""
        self._seeds = seeds
        self._pits = pits
        self._board = [seeds for _ in range(pits)]
        self._P1_store = 0
        self._P2_store = 0

    def get_seeds(self):
        """Get method for physical Mancala seeds that players move and play with."""
        return self._seeds

    def get_pits(self):
        """Get method for Mancala board pits that players use to place their seeds."""
        return self._pits

    def get_P1_store(self):
        """Get method for player1 storage. Used for point collection"""
        return self._P1_store

    def get_P2_store(self):
        """Get method for player2 storage. Used for point collection"""
        return self._P2_store

    def get_board(self):
        """Get method for the Mancala game board."""
        return self._board

    def get_seeds_in_pit(self, player_id):
        """Get method to return the number of seeds player pits"""
        for pit in self.get_pits(player_id):
            return pit.get_seeds()

    def check_pit(self, player_id):
        """
        Checks players' pits to see if they are empty or not. Returns True if the pit is empty, otherwise returns False.
        """
        if self.get_seeds_in_pit(player_id) == 0:
            return True
        else:
            return False


class Mancala:
    """
    Class object that represents the Mancala game and its mechanics/rules as well as the player information regarding
    gameplay.
    """

    def __init__(self):
        self._players = {1: None, 2: None}
        self._board = Board(seeds=4, pits=6)
        self._P1_board = Board(seeds=4, pits=6)
        self._P2_board = Board(seeds=4, pits=6)

    def create_player(self, name):
        """Method that creates a player for the Mancala game"""
        self._players[1] = Player(name)
        self._players[2] = Player(name)

    def print_board(self):
        """Prints the current board information including the number of seeds in all pits and storages."""
        store_num_one = self._P1_board.get_P1_store()
        store_num_two = self._P2_board.get_P2_store()
        print("CURRENT BOARD:\n")
        print("player1:")
        print("store: ", store_num_one)
        print(self._P1_board.get_board())
        print("\nplayer2:")
        print(self._P2_board.get_board())
        print("store: ", store_num_two)

    def new_game(self):
        """Creates fresh start for players to play the game"""
        player_one = input("Player 1, what is your name?")
        self.create_player(player_one)
        player_two = input("Player 2, what is your name?")
        self.create_player(player_two)
        self.print_board()

    def play_game(self, player_index, pit_index):
        """
        Parameters this method uses are the player_index and pit_index. Method follows the rules of the Mancala game
        and updates the number of seeds for each pit and store belonging to the players. Checks the state of the game if
        it has ended. If game has ended, returns 'Game is ended'. Returns list at the end of current seed number and
        stores indicating which player they belong to.
         """

        if self._board.end_game():
            return "Game is ended"

        if pit_index > 6 or pit_index <= 0:
            return "Invalid number for pit index"



    def store_seeds(self, seeds):
        """Method used to store the seeds in player storage."""

    def capture_seeds(self, seeds):
        """Method used for the special rule of capturing seeds"""

    def player_options(self, pits):
        """Checks board for all the legal and valid possible options they are allowed to do for their turn."""

    def move_seeds(self, seeds):
        """
        Moves seeds to each pit and/or player storage based onthe option the player chooses from the player_options
        method. Userinput will be needed in order to make moves. The player grabs all their seeds from the pit they
        have selected and then begins moving towards the right, placing a single seed in each pit for each respective
        step. If the player encounters their storage, they place a seed in that storage. Players are not allowed to
        place seeds in theiropposing player’s storage.
        """

    def end_turn(self):
        """Ends the turn of the current player and switches to the opposing/next player for them to begin their turn."""

    def return_winner(self):
        """
        When game has ended, the winner is returned. If there is a tie, returns a message indicating the game has
        ended in a tie. If the game is still running, prints a message that the game has not yet ended.
        """
        player_one_score = self._board.get_points(1)
        player_two_score = self._board.get_points(2)
        if player_one_score > player_two_score:
            return "Winner is player 1"
        elif player_two_score > player_one_score:
            return "Winner is player 2"
        elif player_one_score == player_two_score:
            return "It's a tie"

    def end_game(self):
        """Stops the game."""
        pass
