from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=16, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Diverse', 'Diverse']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )   


# PAGES
class AnonymityPreferences(Page):
    pass

class CBDCquestions(Page):
    pass

class RiskPreferences(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class ResultsWaitPage(WaitPage):
    pass


page_sequence = [Demographics]
