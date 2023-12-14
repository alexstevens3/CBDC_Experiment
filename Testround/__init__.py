from otree.api import *
import random

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'Testround'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    MAXIMUM_EM = cu(10)
    TC_MOP1 = 0.50
    TC_MOP2 = 0.38
    TC_MOP3 = 0.10
    Adoption_MOP3 = 0.40 #can be 0.2 or 0.6
     

@staticmethod
def creating_session(subsession):
    player = subsession.get_players()
    for player in subsession.get_players():
        player.testprob_MOP2 = random.randint(0,100)   

    import itertools
    if subsession.round_number ==1:
        testCBDC = itertools.cycle(['Account', 'Token'])
        for player in subsession.get_players():
            player.testCBDC_design = next(testCBDC)
        
#@staticmethod
#def set_payoffs(player):
 #   player.testpayoff = player.testpayoff_MOP1 + player.testpayoff_MOP2 + player.testpayoff_MOP3

class Subsession(BaseSubsession):
    pass
    
class Group(BaseGroup):
    testnb_players_CBDC_Yes = models.FloatField()
    testshare_players_CBDC_Yes = models.FloatField()


class Player(BasePlayer):
    testMOP1 = models.IntegerField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Zahlungsmittel 1:", 
    )
    testMOP2 = models.IntegerField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Zahlungsmittel 2:", 
    )
    testMOP3 = models.IntegerField(
        min=0,
        max=C.MAXIMUM_EM,
        label="Zahlungsmittel 3:", 
    )
    testCBDC_Choice = models.BooleanField(
        label="Möchten Sie Zahlungsmittel 3 nutzen?", 
    )
    
    testprob_MOP2 = models.IntegerField()
    testCBDC_design = models.StringField()
    testMOP2_accept = models.BooleanField()
    testMOP3_accept = models.BooleanField()
    testtransaktionen_MOP1 = models.IntegerField()
    testtransaktionen_MOP2 = models.IntegerField()
    testtransaktionen_MOP3 = models.IntegerField()
    testpayoff_MOP1 = models.CurrencyField()
    testpayoff_MOP2 = models.CurrencyField()
    testpayoff_MOP3 = models.CurrencyField()
    testpayoff_total = models.CurrencyField(min=0)
    testCBDC_Choice_Yes = models.IntegerField()
    
    amount1 = models.IntegerField(
        label= 'Zahlungsmittel 1:',
        min=0,
        max=10,
        blank=True)
    amount2 = models.FloatField(
        label= 'Zahlungsmittel 2:',
        min=0,
        max=10,
        blank=True)
    amount3 = models.FloatField(
        label= 'Zahlungsmittel 3:',
        min=0,
        max=10,
        blank=True)
    testpayoff_MOP3_Token = models.CurrencyField()
    testpayoff_MOP3_Account = models.CurrencyField()
    testpayoff_anonymous = models.CurrencyField()
    testpayoff_notanonymous = models.CurrencyField()
    

class Treatment(Page):
    timeout_seconds = 30

class CBDCChoice(Page):
    form_model = 'player'
    form_fields = ['testCBDC_Choice']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.testCBDC_Choice == 1:
            player.testCBDC_Choice_Yes =1
        if player.testCBDC_Choice == 0:
            player.testCBDC_Choice_Yes =0  

class PaymentChoice(Page):
    form_model = 'player'
    form_fields = ['amount1', 'amount2', 'amount3']

    @staticmethod
    def get_form_fields(player):
        if player.testCBDC_Choice == True:
            return ['testMOP1', 'testMOP2', 'testMOP3', 'amount1', 'amount2', 'amount3']
        else:
            return ['testMOP1', 'testMOP2', 'amount1', 'amount2', 'amount3']

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if player.testCBDC_Choice == True and values['testMOP1'] + values['testMOP2'] + values['testMOP3'] != C.MAXIMUM_EM:
            return 'Die Summe der Zahlungsmittel muss insgesamt 10 ergeben'
        if player.testCBDC_Choice == False and values['testMOP1'] + values['testMOP2'] != C.MAXIMUM_EM:
            return 'Die Summe der Zahlungsmittel muss insgesamt 10 ergeben'

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.testMOP2_accept=player.testprob_MOP2<=81

    @staticmethod
    def js_vars(player):
        return dict(TC1=C.TC_MOP1, TC2=C.TC_MOP2, TC3=C.TC_MOP3)

    
class WaitingPage(WaitPage):
    template_name = 'Experiment\WaitingPage.html'
    wait_for_all_players = True


class Beliefs(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player):
        if player.testCBDC_Choice == False:
            player.testMOP3 = 0 

        group = player.group
        players = group.get_players()
        
        for player in group.get_players():
            group.testnb_players_CBDC_Yes = sum([player.testCBDC_Choice_Yes for player in players]) 
            group.testshare_players_CBDC_Yes = (group.testnb_players_CBDC_Yes /  C.PLAYERS_PER_GROUP) *100
          
            #group.testsum_MOP3 = sum([player.field_maybe_none('testMOP3') for player in players if player.testCBDC_Choice_Yes ==1 ]) 
            #group.testaverage_MOP3 = group.testsum_MOP3 / C.PLAYERS_PER_GROUP

    @staticmethod
    def before_next_page(player, timeout_happened):
        group = player.group
        players = group.get_players()

        player.testtransaktionen_MOP1 = player.testMOP1 
        if player.testMOP2_accept == True:
            player.testtransaktionen_MOP2 = player.testMOP2
        if player.testMOP2_accept == False:
            player.testtransaktionen_MOP2 = 0
        if player.testCBDC_Choice == True and group.testshare_players_CBDC_Yes >= 60: 
            player.testtransaktionen_MOP3 = player.testMOP3
        if player.testCBDC_Choice == True and group.testshare_players_CBDC_Yes < 60:
            player.testtransaktionen_MOP3 = 0
        if player.testCBDC_Choice == False:
            player.testtransaktionen_MOP3 = 0

class Welcome(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Trading(Page):
   # timeout_seconds = 60
    @staticmethod
    def vars_for_template(player):

        group = player.group
        players = group.get_players()
        
        player.testpayoff_MOP1 = player.testtransaktionen_MOP1 - (player.testtransaktionen_MOP1 * C.TC_MOP1)
        if player.testMOP2_accept == True:
            player.testpayoff_MOP2= player.testtransaktionen_MOP2 - (player.testtransaktionen_MOP2 * C.TC_MOP2)
        if player.testMOP2_accept == False:
            player.testpayoff_MOP2 = 0
        if player.testCBDC_Choice == True: 
            player.testpayoff_MOP3= player.testtransaktionen_MOP3 - (player.testtransaktionen_MOP3 * C.TC_MOP3) - C.Adoption_MOP3
        if player.testCBDC_Choice == False:
            player.testpayoff_MOP3 = 0
        player.testpayoff_total = player.testpayoff_MOP1 + player.testpayoff_MOP2 + player.testpayoff_MOP3
        
        if player.testpayoff_total < 0:
            player.testpayoff_total = 0

        if player.testMOP2_accept ==1 and player.testMOP2 == 3:
            player.testpayoff_MOP2 = 1.86
            player.testpayoff_total = player.testpayoff_MOP1 + 1.86 + player.testpayoff_MOP3
        if player.testMOP2_accept ==1 and player.testMOP2 == 6:
            player.testpayoff_MOP2 = 3.72
            player.testpayoff_total = player.testpayoff_MOP1 + 3.72 + player.testpayoff_MOP3
        
        if player.testpayoff_total < 0:
            player.testpayoff_total = 0

        if player.testCBDC_design == "Token":
            player.testpayoff_MOP3_Token = player.testpayoff_MOP3
        else:
            player.testpayoff_MOP3_Token = 0
        if player.testCBDC_design == "Account":
            player.testpayoff_MOP3_Account = player.testpayoff_MOP3
        else:
            player.testpayoff_MOP3_Account = 0
        player.testpayoff_anonymous = player.testpayoff_MOP3_Token + player.testpayoff_MOP1
        player.testpayoff_notanonymous = player.testpayoff_MOP3_Account + player.testpayoff_MOP2

    
        
        if player.testpayoff_total == 0:
           player.testpayoff_anonymous = 0
           player.testpayoff_notanonymous = 0


    @staticmethod
    def before_next_page(player, timeout_happened):

        group = player.group
        players = group.get_players()
        
        for player in group.get_players():
            if group.testshare_players_CBDC_Yes >=60:
                player.testMOP3_accept = 1
            if group.testshare_players_CBDC_Yes < 60:
                player.testMOP3_accept = 0

class Total_Payoff(Page):
    pass
   

page_sequence = [Welcome, WaitingPage, Treatment, CBDCChoice, WaitingPage, PaymentChoice, WaitingPage, Beliefs, WaitingPage, Trading, Total_Payoff, WaitingPage]
