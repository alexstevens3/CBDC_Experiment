from otree.api import *
#import numpy as np
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    MAXIMUM_EM = cu(10)
    currency_range(0, 10, 1)
    payment_MOP1 = 1 
    payment_MOP2 = 1
    payment_MOP3 = 1
    #prob_MOP2 = random.randint(0,100)


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import random

    for player in subsession.get_players():
        player.completion_code = random.randint(0,100)

    #def decision_seller(subsession: Subsession):
    #    prob_MOP2 = random.randint(0,100)
    #        if prob_MOP2 >= 81
    #            return 'MOP2_accepted'
    #        else:
    #            return 'MOP2_not_accepted'

    #def decision_seller(subsession):
    #    prob_MOP2 = random.randint(0,100)       

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
    completion_code = models.IntegerField()
    

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


class PaymentChoice_Check(Page):
    form_model = 'player'
    form_fields = ['PaymentChoice_Check']

class ResultsWaitPage(WaitPage):
    pass

class Trading_MOP2accept(Page):
    #@staticmethod
    #def vars_for_template(player):
    #    prob_MOP2 = random.randint(0,100)
    #    return dict(
    #        prob = prob_MOP2
    #)

    @staticmethod
    def is_displayed(player):
        #prob_MOP2 = random.randint(0,100)
        return player.completion_code <= 81

    #@staticmethod
    #def is_displayed(player):
        #prob_MOP2 = random.randint(0,100)
    #    return subsession.decision_seller <= 81

class Trading_MOP2notaccept(Page):
    #@staticmethod
    #def vars_for_template(player):
    #    prob_MOP2 = random.randint(0,100)
    #    return dict(
    #        prob = prob_MOP2
    #)

    @staticmethod
    def is_displayed(player):
        #prob_MOP2 = random.randint(0,100)
        return player.completion_code > 81
    
    #def prob_MOP2(player):
     #   prob_MOP2 = random.randint(0,100)
    #prob = random.randint(0,100)

    #@staticmethod
    #def vars_for_template(player: Player):
    #    prob = random.randint(0,100)
        #if prob <= 81:
        #    return dict(
        #        MOP = MOP 1, MOP 2, MOP 3)
        #else:
        #    return dict(
        #        MOP = MOP 1, MOP 3)
        
    
    #@staticmethod
    #def decision_seller(player: Player):
    #    prob_MOP2 = random.randint(0,100)
    #    if prob <= 81:
    #        return 'All 3 MOP accepted' 
    #    else:
    #        return 'MOP 1,3'

    #accepted_MOP = random.randint()
    #prob_accept_MOP2 = 0.81
    #prob_accept_MOP1 = 1 



page_sequence = [Treatment, CBDCChoice, PaymentChoice, PaymentChoice_Check, ResultsWaitPage, Trading_MOP2accept, Trading_MOP2notaccept]
