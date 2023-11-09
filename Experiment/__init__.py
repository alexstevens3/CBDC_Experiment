from otree.api import *
#import numpy as np
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Experiment'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10
    MAXIMUM_EM = cu(10)
    #currency_range(0, 10, 1)
    TC_MOP1 = 0.50
    TC_MOP2 = 0.38
    TC_MOP3 = 0.10
    Adoption_MOP3 = 0.40 #can be 0.2 or 0.6
     

@staticmethod
def creating_session(subsession):
    #subsession = player.subsession
    player = subsession.get_players()
    for player in subsession.get_players():
        player.prob_MOP2 = random.randint(0,100)   


    import itertools
    if subsession.round_number <=5:
        CBDC = itertools.cycle(['Account', 'Token'])
        for player in subsession.get_players():
            player.CBDC_design = next(CBDC)

    if subsession.round_number > 5:
        CBDC = itertools.cycle(['Token', 'Account'])
        for player in subsession.get_players():
            player.CBDC_design = next(CBDC)
   
        
@staticmethod
def set_payoffs(player):
    player.payoff = player.payoff_MOP1 + player.payoff_MOP2 + player.payoff_MOP3


class Subsession(BaseSubsession):
    pass
    

class Group(BaseGroup):
    nb_players_CBDC_Yes = models.FloatField()
    share_players_CBDC_Yes = models.FloatField()
    sum_MOP3 = models.FloatField()
    average_MOP3 = models.FloatField()

#class Participant(BasePlayer):
 #   payoff_total_allrounds = models.FloatField()

class Player(BasePlayer):
    MOP1 = models.IntegerField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Zahlungsmittel 1:", 
    )
    MOP2 = models.IntegerField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Zahlungsmittel 2:", 
    )
    MOP3 = models.IntegerField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Zahlungsmittel 3:", 
    )
    CBDC_Choice = models.BooleanField(
        label="Möchten Sie Zahlungsmittel 3 nutzen?", 
    )
    
    prob_MOP2 = models.IntegerField()
    CBDC_design = models.StringField()
    MOP2_accept = models.BooleanField()
    MOP3_accept = models.BooleanField()
    transaktionen_MOP1 = models.IntegerField()
    transaktionen_MOP2 = models.IntegerField()
    transaktionen_MOP3 = models.IntegerField()
    payoff_MOP1 = models.FloatField()
    payoff_MOP2 = models.FloatField()
    payoff_MOP3 = models.FloatField()
    payoff_total = models.FloatField(min=0)
    CBDC_Choice_Yes = models.IntegerField()
    payoff_total_allrounds1 = models.FloatField()
    belief1 = models.IntegerField(
        label = "",
        min=0,
        max=C.PLAYERS_PER_GROUP,
        doc="Belief about/Expected CBDC_Choice_Yes")
    belief2 = models.IntegerField(
        label = "",
        min=0,
        max=C.MAXIMUM_EM,
        doc="Belief about/Expected MOP3")
    belief3 = models.IntegerField(
        label = "",
        min=0,
        max=100,
        doc="Belief about prob. acceptance MOP3")
    last_round = models.IntegerField()
    next_round = models.IntegerField()
    #calculator_input = models.FloatField(
     #   label = "Geben Sie eine Zahl an",
      #  )
    #calculator_result = models.FloatField()
    
  
    

class Treatment(Page):
    timeout_seconds = 30

class CBDCChoice(Page):
    form_model = 'player'
    form_fields = ['CBDC_Choice']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.CBDC_Choice == 1:
            player.CBDC_Choice_Yes =1
        if player.CBDC_Choice == 0:
            player.CBDC_Choice_Yes =0

             

class PaymentChoice(Page):
    form_model = 'player'
    #form_fields = ['calculator_input', 'calculator_result']

    
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
            return 'Die Summe muss insgesamt 10 ergeben'
        if player.CBDC_Choice == False and values['MOP1'] + values['MOP2'] != C.MAXIMUM_EM:
            return 'Die Summe muss insgesamt 10 ergeben'

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.MOP2_accept=player.prob_MOP2<=81

    #@staticmethod
   # def calculate_result(player):
    #    player.calculate_result = player.calculator_input * 2

    #def vars_for_template(self):
    #    return {
     #       'example_variable': 42,  # You can pass additional variables to the template if needed.
     #   }

   # def calculator_input_error_message(self, value):
    #    if not value:
     #       return 'Please enter a valid value.'

   # def before_next_page(self):
        
     #   self.player.calculate_result()

    
    #@staticmethod
   # def vars_for_template(player):
    #    group = player.group
    #    players = group.get_players()
        
    #    for player in group.get_players():
    #        group.nb_players_CBDC_Yes = sum([player.CBDC_Choice_Yes for player in players]) 
      #      group.share_players_CBDC_Yes = (group.nb_players_CBDC_Yes /  C.PLAYERS_PER_GROUP) *100
          
      #      group.sum_MOP3 = sum([player.field_maybe_none('MOP3') for player in players if player.CBDC_Choice_Yes ==1 ]) 
        


class WaitingPage(WaitPage):
    template_name = 'Experiment\WaitingPage.html'
    wait_for_all_players = True


class Beliefs(Page):
    form_model = 'player'
    form_fields = ['belief1', 'belief2', 'belief3']

   # @staticmethod
    #def error_message(player, values):
    #    print('values is', values)
   #     if values['belief1'] > C.PLAYERS_PER_GROUP:
   #         return 'Der Wert muss zwischen 0 und 10 liegen'
   #     if values['belief2'] > 10:
   #         return 'x'
       

    @staticmethod
    def vars_for_template(player):
        player.last_round = player.round_number - 1
        player.next_round = player.round_number + 1
        if player.CBDC_Choice == False:
            player.MOP3 = 0 

        group = player.group
        #subsession=player.subsession
        #session=subsession.session
        players = group.get_players()
        
        for player in group.get_players():
            group.nb_players_CBDC_Yes = sum([player.CBDC_Choice_Yes for player in players]) 
            group.share_players_CBDC_Yes = (group.nb_players_CBDC_Yes /  C.PLAYERS_PER_GROUP) *100
          
            group.sum_MOP3 = sum([player.field_maybe_none('MOP3') for player in players if player.CBDC_Choice_Yes ==1 ]) 
            group.average_MOP3 = group.sum_MOP3 / C.PLAYERS_PER_GROUP
        

    @staticmethod
    def before_next_page(player, timeout_happened):
        group = player.group
        players = group.get_players()

        player.transaktionen_MOP1 = player.MOP1 
        if player.MOP2_accept == True:
            player.transaktionen_MOP2 = player.MOP2
        if player.MOP2_accept == False:
            player.transaktionen_MOP2 = 0
       # if player.CBDC_Choice == True and player.MOP3_accept == 1:
       #     player.transaktionen_MOP3 = player.MOP3
      #  if player.CBDC_Choice == True and player.MOP3_accept == 0:
       #     player.transaktionen_MOP3 = 0

        if player.CBDC_Choice == True and group.share_players_CBDC_Yes >= 60: 
            player.transaktionen_MOP3 = player.MOP3
        if player.CBDC_Choice == True and group.share_players_CBDC_Yes < 60:
            player.transaktionen_MOP3 = 0
        if player.CBDC_Choice == False:
            player.transaktionen_MOP3 = 0



class Trading(Page):
    timeout_seconds = 60
    @staticmethod
    def vars_for_template(player):
        
        player.payoff_MOP1 = player.transaktionen_MOP1 - (player.transaktionen_MOP1 * C.TC_MOP1)
        if player.MOP2_accept == True:
            player.payoff_MOP2= player.transaktionen_MOP2 - (player.transaktionen_MOP2 * C.TC_MOP2)
        if player.MOP2_accept == False:
            player.payoff_MOP2 = 0
        if player.CBDC_Choice == True: 
            player.payoff_MOP3= player.transaktionen_MOP3 - (player.transaktionen_MOP3 * C.TC_MOP3) - C.Adoption_MOP3
        if player.CBDC_Choice == False:
            player.payoff_MOP3 = 0
        player.payoff_total = player.payoff_MOP1 + player.payoff_MOP2 + player.payoff_MOP3
        
        if player.payoff_total < 0:
            player.payoff_total = 0

    @staticmethod
    def before_next_page(player, timeout_happened):
        set_payoffs(player)

        group = player.group
        players = group.get_players()
        
        for player in group.get_players():
            if group.share_players_CBDC_Yes >=60:
                player.MOP3_accept = 1
            if group.share_players_CBDC_Yes < 60:
                player.MOP3_accept = 0

class Total_Payoff(Page):
    @staticmethod
    def vars_for_template(player):
        if player.round_number > 1:
            player.payoff_total_allrounds1 = sum([player.payoff_total for player in player.in_all_rounds()])
        else:
            player.payoff_total_allrounds1 = player.payoff_total
   

        participant=player.participant
        if player.round_number > 1:
            participant.payoff_total_allrounds = sum([player.payoff_total for player in player.in_all_rounds()])
        else:
            participant.payoff_total_allrounds = player.payoff_total

page_sequence = [Treatment, CBDCChoice, PaymentChoice, WaitingPage, Beliefs, Trading, Total_Payoff, WaitingPage]
