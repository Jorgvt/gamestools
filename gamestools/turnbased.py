# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_turnbased.ipynb.

# %% auto 0
__all__ = ['TurnBasedGame']

# %% ../00_turnbased.ipynb 3
from abc import ABC, abstractmethod
from itertools import cycle

# %% ../00_turnbased.ipynb 4
class TurnBasedGame(ABC):
    """
    Base class for when creating turn-based games.
    Implements some basic functionality to control the current player
    and the representation of the boards.
    """
    def __init__(self,
                 n_players, # Number of players
                ):
        self.n_players = n_players
        self.current_player = self.choose_initial_player()
        self._players = cycle(range(n_players))
    
    def __repr__(self):
        """
        Representation of the game state (currently only for two players
        with one board each).
        The current player is marked with an *.
        """
        player0 = "Player 1 *" if self.current_player==0 else "Player 1"
        player1= "Player 2 *" if self.current_player==1 else "Player 2"
        
        return "\n".join([player0,
                          str(self.boards[0]),
                          player1,
                          str(self.boards[1])])

    def _change_player(self):
        """
        Changes the current player to the next.
        """
        self.current_player = next(self._players)
