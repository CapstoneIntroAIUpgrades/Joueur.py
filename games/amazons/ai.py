# This is where you build your AI for the Amazons game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Amazons. """

    @property
    def game(self) -> 'games.amazons.game.Game':
        """games.amazons.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.amazons.player.Player':
        """games.amazons.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Amazons Python Player" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        # <start row> <start col> <end row> <end col> <shoot row> <shoot col>
        self.moves_todo = {
            "q":"606354695956634352434453441757590459171819043407343532351542150422041423141514936676968696868586667766776879152515182818686968253525354535454445444344433343333433",
            "Q":"033355304050403151062846287858392949290936090817332326231316131424141303130413040504788780877787777867788878889977999897988898888988899989050605080908314131414030404140"
        }
        # <<-- /Creer-Merge: start -->>

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>

    def make_move(self) -> str:
        """This is called every time it is this AI.player's turn to make a move.

        Returns:
            str: A move that the AI wants to make. Format varies based on sub-game
        """
        # <<-- Creer-Merge: makeMove -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for makeMove
        move = self.moves_todo[self.game.rep_string.split(" ")[1]][:6]
        self.moves_todo["Q"] = self.moves_todo["Q"][6:]
        self.moves_todo["q"] = self.moves_todo["q"][6:]
        import time
        time.sleep(0.25)
        return f"{move[0]} {move[1]} {move[2]} {move[3]} {move[4]} {move[5]}"
        # <<-- /Creer-Merge: makeMove -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
