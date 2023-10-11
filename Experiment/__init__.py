from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    MAXIMUM_EM = cu(10)
    currency_range(0, 10, 1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    MOP1 = models.CurrencyField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Means of Payment 1:", 
    )
    MOP2 = models.CurrencyField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Means of Payment 2:", 
    )
    MOP3 = models.CurrencyField(
        min=0,
        max=C.MAXIMUM_EM,
        #doc="""x""",
        label="Means of Payment 3:", 
    )
    CBDC_Choice = models.BooleanField(
        label="Möchten Sie Zahlungsmittel 3 einführen?", 
    )
    PaymentChoice_Check = models.BooleanField(
        label = ""
    )

# PAGES
class Treatment(Page):
    pass

class CBDCChoice(Page):
    form_model = 'player'
    form_fields = ['CBDC_Choice']

class PaymentChoice(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.CBDC_Choice == True:
            return ['MOP1', 'MOP2', 'MOP3']
        else:
            return ['MOP1', 'MOP2']

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if player.CBDC_Choice == True and values['MOP1'] + values['MOP2'] + values['MOP3'] != C.MAXIMUM_EM:
            return 'The numbers must add up to 10'
        if player.CBDC_Choice == False and values['MOP1'] + values['MOP2'] != C.MAXIMUM_EM:
            return 'The numbers must add up to 10'


    #Validating multiple fields together, see documentation forms; MOP 1 + MOP 2 + MOP 3 = N, if not: error message

class PaymentChoice_Check(Page):
    form_model = 'player'
    form_fields = ['PaymentChoice_Check']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Treatment, CBDCChoice, PaymentChoice, PaymentChoice_Check, ResultsWaitPage, Results]
