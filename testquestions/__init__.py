from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'testquestions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField(
        label= 'Wie viele Zahlungsmittel gibt es im Experiment?'
    )
    q2 = models.StringField(
        label= 'Welches Zahlungsmittel hat die höchsten Transaktionskosten?'
    )
    q3 = models.StringField(
        label= 'Welches Zahlungsmittel hat die niedrigsten Transaktionskosten?'
    )
    q4 = models.StringField(
        label= 'Wie hoch ist die Wahrscheinlichkeit, dass Zahlungsmittel 2 vom Verkäufer akzeptiert wird? (in %)'
    )
    q5 = models.StringField(
        label= 'Wie hoch muss der Anteil der Käufer mindestens sein, sodass Zahlungsmittel 3 vom Verkäufer akzeptiert wird? (in %)'
    )


class Welcome(Page):
    pass

class Questions(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Welcome, Questions, ResultsWaitPage, Results]
