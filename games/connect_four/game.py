# Game: The traditional 6x7 board with pieces.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List
from joueur.base_game import BaseGame

# import game objects
from games.connect_four.game_object import GameObject
from games.connect_four.player import Player

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the ConnectFour game.

    The traditional 6x7 board with pieces.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._cols = 0
        self._game_objects = {}
        self._players = []
        self._rep_string = ""
        self._rows = 0
        self._session = ""

        self.name = "ConnectFour"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Player': Player
        }

    @property
    def cols(self) -> int:
        """int: The number of tiles on the board along the y (vertical) axis.
        """
        return self._cols

    @property
    def game_objects(self) -> Dict[str, 'games.connect_four.game_object.GameObject']:
        """dict[str, games.connect_four.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def players(self) -> List['games.connect_four.player.Player']:
        """list[games.connect_four.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def rep_string(self) -> str:
        """str: A string describing all of the information necessary to fully represent the game's state.
        """
        return self._rep_string

    @property
    def rows(self) -> int:
        """int: The number of cells on the board along the x (horizontal) axis.
        """
        return self._rows

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
