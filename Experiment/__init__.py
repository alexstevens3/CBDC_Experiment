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



@staticmethod
def creating_session(subsession):
    #subsession = player.subsession
    player = subsession.get_players()
    for player in subsession.get_players():
        player.prob_MOP2 = random.randint(0,100)   

    #if subsession.round_number == 1:
    import itertools
    CBDC = itertools.cycle(['Account', 'Token'])
    for player in subsession.get_players():
        player.CBDC_design = next(CBDC) 

   # if player.prob_MOP2 >= 81:
        #return player.MOP2_accept == True
        #return player.MOP2_accept == player.field_maybe_none('MOP2_accept') == True
    #    return player.field_maybe_none('MOP2_accept') == True
    #else:
    #    return player.field_maybe_none('MOP2_accept') == False
        #return player.MOP2_accept == False
        #return player.MOP2_accept == player.field_maybe_none('MOP2_accept') == False

        #player.prob_MOP2 == player.field_maybe_none('prob_MOP2') <= 81

#@staticmethod
#def decision_seller(player):
   
    #subsession = player.subsession
    #player = subsession.get_players()
    #for player in subsession.get_players():
        #if player.prob_MOP2 > 50:
            #return player.MOP2_accept == True
        #return player.MOP2_accept == player.field_maybe_none('MOP2_accept') == True
           # return player.field_maybe_none('MOP2_accept') == True
        #return player.MOP2_accept == player.field_maybe_none('MOP2_accept') == False
        #else:
            #return player.field_maybe_none('MOP2_accept') == False
            #return player.MOP2_accept == False


#    for player in subsession.get_players():
#        player.prob_MOP2 = random.randint(0,100) 
#        if player.prob_MOP2 >= 81:
#            return player.MOP2_accept == True
#        else:
#            return player.MOP2_accept == False
        

#def set_payoffs(group):
 #   for player in group.get_players():
    #players = subsession.get_players()
        #total_MOP1 = sum(player.MOP1)
  #      if player.prob_MOP2 >= 81:
   #         return player.MOP2_accept == True
    #    else:
     #       return player.MOP2_accept == False
    #for player in players:
     #   player.payoff = player.MOP1


    #for player in subsession.get_players():
     #   player.completion_code = random.randint(0,100) 
      #  if player.completion_code >= 81:
       #     player.MOP2_accept == True
        #    player.payoff = MOP_1 + MOP_2
        #else:
         #   player.MOP2_accept == False
          #  player.payoff = 0
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
    #total_MOP1 = models.CurrencyField()


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
        label="Means of Payment 3:", 
    )
    CBDC_Choice = models.BooleanField(
        label="Möchten Sie Zahlungsmittel 3 einführen?", 
    )
    PaymentChoice_Check = models.BooleanField(
        label = ""
    )
    prob_MOP2 = models.IntegerField()
    CBDC_design = models.StringField()
    MOP2_accept = models.BooleanField()
    
    
    

# PAGES
class Treatment_Token(Page):
    @staticmethod
    def is_displayed(player):
        return player.CBDC_design == 'Token'

class Treatment_Account(Page):
    @staticmethod
    def is_displayed(player):
        return player.CBDC_design == 'Account'

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

    @staticmethod
    def before_next_page(player, timeout_happened):
        #subsession = player.subsession
        #player = subsession.get_players
        #for player in subsession.get_players():
        #player = 
        #decision_seller(player)
        #player.test=player.prob_MOP2>=50
        player.MOP2_accept=player.prob_MOP2>=81
    

      #  if player.prob_MOP2 >= 81:
        #return player.MOP2_accept == True
        #return player.MOP2_accept == player.field_maybe_none('MOP2_accept') == True
       #     player.field_maybe_none('MOP2_accept') == True
        #return player.MOP2_accept == player.field_maybe_none('MOP2_accept') == False
       # else:
        #    player.field_maybe_none('MOP2_accept') == False


        #decision_seller(player)


class ResultsWaitPage(WaitPage):
    pass
    #wait_for_all_groups = True
    #after_all_players_arrive = decision_seller

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
        return player.prob_MOP2 == player.field_maybe_none('prob_MOP2') <= 81



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
        #return player.prob_MOP2 > 81
        return player.prob_MOP2 == player.field_maybe_none('prob_MOP2') > 81

class Results(Page):
    pass

    

    
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





page_sequence = [Treatment_Token, Treatment_Account, CBDCChoice, PaymentChoice, PaymentChoice_Check, Trading_MOP2accept, Trading_MOP2notaccept, ResultsWaitPage]
