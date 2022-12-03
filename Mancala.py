# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 11-20-2022
# Description: A text based game version of the popular board game Mancala.

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

        # initialize self-board-list, the main data structure.
        # sample: [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        # index 0-5 will be player1's pit, index 7-12 will be player2's pit and index 6,13 will be storage
        self._playboard = [self._seeds if i % 7 != 6 else 0 for i in range((self._pits+1) * 2)]

    def get_seeds(self):
        """Get method for physical Mancala seeds that players move and play with."""
        return self._seeds

    def get_pits(self):
        """Get method for Mancala board pits that players use to place their seeds."""
        return self._pits

    def get_P1_store(self):
        """Get method for player1 storage. Used for point collection"""
        return self._playboard[6]

    def get_P2_store(self):
        """Get method for player2 storage. Used for point collection"""
        return self._playboard[13]

    def get_board(self):
        """Get method for the Mancala game board."""
        return self._playboard

    def get_P1_board(self):
        """Get method for the Mancala game board for player 1."""
        return self._playboard[0:6]

    def get_P2_board(self):
        """Get method for the Mancala game board for player 2."""
        return self._playboard[7:13]

    def get_seeds_in_pit(self, player_id):
        """Get method to return the number of seeds player pits"""
        if player_id == 1:
            return sum(self._playboard[0:6])
        if player_id == 2:
            return sum(self._playboard[7:13])

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
        self._board = Board(seeds=4, pits=6)
        self._players = []

    def create_player(self, name):
        """Method that creates a player for the Mancala game"""
        self._players.append(Player(name))

    def print_board(self):
        """Prints the current board information including the number of seeds in all pits and storages."""
        store_num_one = self._board.get_P1_store()
        store_num_two = self._board.get_P2_store()
        print("CURRENT BOARD:\n")
        print("player1:")
        print("store: ", store_num_one)
        print(self._board.get_board()[0:6])
        print("\nplayer2:")
        print(self._board.get_board()[7:13])
        print("store: ", store_num_two)

    def play_game(self, player_index, pit_index):
        """
        Parameters this method uses are the player_index and pit_index. Method follows the rules of the Mancala game
        and updates the number of seeds for each pit and store belonging to the players. Checks the state of the game if
        it has ended. If game has ended, returns 'Game is ended'. Returns list at the end of current seed number and
        stores indicating which player they belong to.
        """
        if pit_index > 6 or pit_index < 1:
            return "Invalid number for pit index"

        elif self._board.check_pit(1) or self._board.check_pit(2):
            return "Game is ended"

        else:
            # player I
            if player_index == 1:
                # declare a variable "sow" -> number of seed player get
                sow = self._board.get_board()[pit_index - 1]
                self._board.get_board()[pit_index - 1] = 0
                # set a variable save_i to record the last i in the next for loop in order to avoid referenced before assignment
                save_i = 0
                for i in range(sow):
                    self._board.get_board()[pit_index + i] += 1
                    save_i = i
                # special case 1, the final move is landed in storage
                if pit_index + save_i == 6:
                    print("player 1 takes another turn")

                # special case 2, the final move is landed in an empty pit
                elif pit_index + save_i < 6 and self._board.get_board()[pit_index + save_i] == 1:
                    self._board.get_board()[pit_index + save_i] = 0
                    self._board.get_board()[6] += 1
                    self._board.get_board()[6] += self._board.get_board()[pit_index + save_i + 7]
                    self._board.get_board()[pit_index + save_i + 7] = 0
            # player II
            else:
                sow = self._board.get_board()[pit_index - 1 + 7]
                self._board.get_board()[pit_index - 1 + 7] = 0
                for i in range(sow):
                    adjust_index = pit_index + i + 7
                    if adjust_index > 13:
                        adjust_index = adjust_index - 14
                    self._board.get_board()[adjust_index] += 1

                if adjust_index == 13:
                    print("player 2 takes another turn")
                # special case 2, the final move lands in an empty pit
                elif adjust_index > 7 and self._board.get_board()[adjust_index] == 1:
                    self._board.get_board()[adjust_index] = 0
                    self._board.get_board()[13] += 1
                    self._board.get_board()[13] += self._board.get_board()[adjust_index - 7]
                    self._board.get_board()[adjust_index - 7] = 0

        return self._board.get_board()

    def return_winner(self):
        """
        When game has ended, the winner is returned. If there is a tie, returns a message indicating the game has
        ended in a tie. If the game is still running, prints a message that the game has not yet ended.
        """
        if self._board.check_pit(1) or self._board.check_pit(2):
            player_one_score = self._board.get_P1_store()
            player_two_score = self._board.get_P2_store()
            if player_one_score > player_two_score:
                return "Winner is player 1 " + self._players[0].get_name()
            elif player_two_score > player_one_score:
                return "Winner is player 2 " + self._players[1].get_name()
            elif player_one_score == player_two_score:
                return "It's a tie"
        else:
            return "Game is not ended"


