from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'spasibo'
    PLAYERS_PER_GROUP = 8
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

   

class WinnerPage(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.id_in_group == 1 or self.id_in_group == 8
    
    
class NoWinPage(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.id_in_group != 1 and self.id_in_group != 8
    


page_sequence = [WinnerPage, NoWinPage]
