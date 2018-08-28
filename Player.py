import abc


class player(object):
    __metaclass__ = abc.ABCMeta

    @property
    def player_symbol(self):
        return self._player_symbol

    @player_symbol.setter
    def player_symbol(self, player_symbol):
        self._player_symbol = player_symbol

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def __init__(self, player_symbol):
        self._player_symbol = player_symbol

    @abc.abstractmethod
    def next_column(self, game_board):
        return