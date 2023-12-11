from otree.api import *
import random

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    showup = 6
    survey_fee = 1
    CHOICES = ['Anonymität der Zahlungen', 'Sicherheit in Bezug auf Datenschutz', 'Kostenfreie Nutzung', 'Einfache Nutzbarkeit']
    CHOICESmop = ['Bargeld', 'Kontaktlos mit Girocard', 'Einschieben der Girocard in das Terminal und PIN oder Unterschrift', 'Kontaktlos mit Kreditkarte', 'Einschieben der Kreditkarte in das Terminal und PIN oder Unterschrift', 'Bezahlen mit dem Smartphone' ]

@staticmethod
def creating_session(subsession):
    player = subsession.get_players()
    for player in subsession.get_players():
        player.risk_payoffrelevant = random.choice(['risk1', 'risk2', 'risk3', 'risk4', 'risk5', 'risk6', 'risk7', 'risk8', 'risk9', 'risk10', 'risk11'])


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def make_rank_field(label):
    return models.StringField(choices=C.CHOICES, label=label)

def make_rank_field2(label):
    return models.StringField(choices=C.CHOICESmop, label=label)

class Player(BasePlayer):
    risk_payoffrelevant= models.StringField()
    age = models.IntegerField(label='Wie alt sind Sie?', min=15, max=125)
    gender = models.StringField(
        choices=['Weiblich', 'Männlich', 'Divers'],
        label='Welches Geschlecht haben Sie?',
        widget=widgets.RadioSelect,
    )   
    Vollzeiterwerbstätig = models.BooleanField(blank=True)
    Teilzeiterwerbstätig = models.BooleanField(blank=True)
    Geringfügig_erwerbstätig = models.BooleanField(blank=True)
    Minijob= models.BooleanField(blank=True)
    Ruhestand = models.BooleanField(blank=True)
    Studentin_oder_Student = models.BooleanField(blank=True)
    Selbstständig = models.BooleanField(blank=True)
    Nicht_erwerbstätig_und_Arbeitssuchend = models.BooleanField(blank=True)
    Nicht_erwerbstätig_und_nicht_Arbeitssuchend = models.BooleanField(blank=True)

    income = models.StringField(
        label = 'Wie hoch ist Ihr persönliches Nettoeinkommen pro Monat?',
        choices = ['unter 500 Euro', '500 bis 999 Euro', '1000 bis 1499 Euro', '1500 bis 1999 Euro', '2000 bis 2499 Euro', '2500 bis 2999 Euro', '3000 bis 3499 Euro', '3500 bis 3999 Euro', '4000 bis 4499 Euro', '4500 bis 4999 Euro', 'über 5000 Euro'],
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        label = 'Welches ist der höchste Abschluss, den Sie bisher erreicht haben?',
        choices = ['Keinen Schulabschluss', 'Schulabschluss oder gleichwertiger Abschluss', 'Bachelor', 'Master oder Staatsexamen', 'Promotion' ],
        widget=widgets.RadioSelect,
    )
    degree = models.StringField(
        label = 'Was studieren Sie?',
        choices = ['Volkswirtschaftslehre', 'Betriebswirtschaftslehre', 'Biologie, Biochemie, Chemie oder Physik', 
        'Sprachwissenschaften', 'Finanz- und Versicherungsmathematik', 'Geschichte', 'Informatik', 'Kommunikations- und Medienwissenschaft', 'Mathematik', 'Medizin oder Pharmazie', 'Politik- oder Sozialwissenschaften', 'Psychologie', 'Rechtswissenschaften', 'Anderer Studiengang']
    )
    semester = models.IntegerField(
        label = 'Im wievieltem Semester studieren Sie?',
        blank = True
    )
    grade = models.FloatField(
        label= 'Was ist Ihre aktuelle Durchschnittsnote?',
        blank = True
    )
    risk =  models.IntegerField(
        label = "",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
    )
    cbdc1 = models.LongStringField(
        label = 'Was glauben Sie, worum es in diesem Experiment ging?',
    )
    cbdc2 = models.BooleanField(
        label = 'Haben Sie bereits vor dem Experiment von dem digitalen Zentralbankgeld gehört?',
    )
    cbdc3 = models.StringField(
        label = 'Wie wahrscheinlich ist es, dass Sie nach einer Einführung das digitale Zentralbankgeld nutzen würden?',
        choices = ['sehr wahrscheinlich', 'wahrscheinlich', 'unentschieden', 'unwahrscheinlich', 'sehr unwahrscheinlich' ],
        widget=widgets.RadioSelectHorizontal,
    )
    #cbdc4 =  models.StringField(
       # label = 'Wenn das digitale Zentralbankgeld eingeführt werden würde, welche der folgenden Eigenschaften wäre Ihnen am wichtigsten?',
       # choices = ['Anonymität der Zahlungen', 'Sicherheit in Bezug auf Datenschutz', 'Kostenfreie Nutzung', 'Bequeme Nutzung' ],
       # widget=widgets.RadioSelect,
    #)
    cbdc5 =  models.IntegerField(
        label = 'Sehen Sie das digitale Zentralbankgeld als Alternative zum Bargeld oder als Alternative zu unbaren Zahlungsmitteln (z.B. Zahlung mit Debitkarte, Kreditkarte)? Der äußerste Kreis links bedeutet "nur als Alternative zu Bargeld", der äußerste Kreis rechts bedeutet "nur als Alternative zu unbaren Zahlungsmitteln".',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
    )
    anonymity = models.StringField(
        label = "",
        choices = [[1, 'Ich mache mir große Sorgen in Bezug auf die Weitergabe meiner persönlichen Daten.'], 
        [2, 'Ich mache mir Sorgen in Bezug auf die Weitergabe meiner persönlichen Daten.'], 
        [3,'Ich mache mir etwas Sorgen in Bezug auf die Weitergabe meiner persönlichen Daten.'],
        [4, 'Ich mache mir keine Sorgen in Bezug auf die Weitergabe meiner persönlichen Daten.']],
        widget=widgets.RadioSelect,
    )
    #Bargeld = models.BooleanField(blank=True)
    #Girocard_kontaktlos = models.BooleanField(blank=True)
    #Girocard_einschieben = models.BooleanField(blank=True)
    #Kreditkarte_kontaktlos = models.BooleanField(blank=True)
    #Kreditkarte_einschieben = models.BooleanField(blank=True)
   # Smartphone = models.BooleanField(blank=True)
    #Anderes_Zahlungsmittel = models.BooleanField(blank=True)

    rank1_cbdc4 = make_rank_field("Erste Wahl")
    rank2_cbdc4  = make_rank_field("Zweite Wahl")
    rank3_cbdc4  = make_rank_field("Dritte Wahl")
    rank4_cbdc4  = make_rank_field("Vierte Wahl")

    rank1_cbdc6 = make_rank_field2("Erste Wahl")
    rank2_cbdc6 = make_rank_field2("Zweite Wahl")
    rank3_cbdc6 = make_rank_field2("Dritte Wahl")
    rank4_cbdc6 = make_rank_field2("Vierte Wahl")
    rank5_cbdc6 = make_rank_field2("Fünfte Wahl")
    rank6_cbdc6 = make_rank_field2("Sechste Wahl")

    risk1 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk2 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk3 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk4 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk5 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk6 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk7 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk8 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk9 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk10 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])
    risk11 = models.StringField(widget=widgets.RadioSelectHorizontal, choices=['A', 'B'])

    payoff_risk = models.FloatField()

class Anonymity(Page):
    form_model = 'player'
    form_fields = ['anonymity']

class CBDC1(Page):
    form_model = 'player'
    form_fields = ['cbdc1']

class CBDC2(Page):
    form_model = 'player'
    form_fields = ['cbdc2']

class CBDC3(Page):
    form_model = 'player'
    form_fields = ['cbdc3']

class CBDC4(Page):
    form_model = 'player'
    form_fields = ['rank1_cbdc4', 'rank2_cbdc4', 'rank3_cbdc4', 'rank4_cbdc4']

    @staticmethod
    def error_message(player: Player, values):
        choices = [values['rank1_cbdc4'], values['rank2_cbdc4'], values['rank3_cbdc4'], values['rank4_cbdc4'],]
        if len(set(choices)) != len(choices):
            return "Sie können dieselbe Eigenschaft nicht mehrfach auswählen"

class CBDC5(Page):
    form_model = 'player'
    form_fields = ['cbdc5']
       
class CBDC6(Page):
    form_model = 'player'
    form_fields = ['rank1_cbdc6', 'rank2_cbdc6', 'rank3_cbdc6', 'rank4_cbdc6', 'rank5_cbdc6', 'rank6_cbdc6']
   # form_fields = ['Bargeld', 'Girocard_kontaktlos', 'Girocard_einschieben', 'Kreditkarte_kontaktlos', 'Kreditkarte_einschieben', 'Smartphone', 'Anderes_Zahlungsmittel']

    @staticmethod
    def error_message(player: Player, values):
        choices2 = [values['rank1_cbdc6'], values['rank2_cbdc6'], values['rank3_cbdc6'], values['rank4_cbdc6'], values['rank5_cbdc6'], values['rank6_cbdc6']]
        if len(set(choices2)) != len(choices2):
            return "Sie können dasselbe Zahlungsmittel nicht mehrfach auswählen"

class Risk1(Page):
    form_model = 'player'
    form_fields = ['risk']

class Risk2(Page):
    form_model = 'player'
    form_fields = ['risk1', 'risk2', 'risk3', 'risk4', 'risk5', 'risk6', 'risk7', 'risk8', 'risk9', 'risk10', 'risk11']

class Welcome(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'Vollzeiterwerbstätig', 'Teilzeiterwerbstätig',
     'Geringfügig_erwerbstätig', 'Minijob', 'Ruhestand', 'Studentin_oder_Student', 
     'Selbstständig', 'Nicht_erwerbstätig_und_Arbeitssuchend', 'Nicht_erwerbstätig_und_nicht_Arbeitssuchend', 'education', 'income']

    def before_next_page(player, timeout_happened):
        if player.field_maybe_none("Vollzeiterwerbstätig") == None:
            player.Vollzeiterwerbstätig = 0
        if player.field_maybe_none("Teilzeiterwerbstätig") == None:
            player.Teilzeiterwerbstätig = 0
        if player.field_maybe_none("Geringfügig_erwerbstätig") == None:
            player.Geringfügig_erwerbstätig = 0
        if player.field_maybe_none("Minijob") == None:
            player.Minijob = 0
        if player.field_maybe_none("Ruhestand") == None:
            player.Ruhestand = 0
        if player.field_maybe_none("Studentin_oder_Student") == None:
            player.Studentin_oder_Student = 0
        if player.field_maybe_none("Selbstständig") == None:
            player.Selbstständig = 0
        if player.field_maybe_none("Nicht_erwerbstätig_und_Arbeitssuchend") == None:
            player.Nicht_erwerbstätig_und_Arbeitssuchend = 0
        if player.field_maybe_none("Nicht_erwerbstätig_und_nicht_Arbeitssuchend") == None:
            player.Nicht_erwerbstätig_und_nicht_Arbeitssuchend = 0

        if player.risk_payoffrelevant == 'risk1':
            if player.risk1 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk1 == 'B':
                player.payoff_risk = 1

        if player.risk_payoffrelevant == 'risk2':
            if player.risk2 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk2 == 'B':
                player.payoff_risk = 1.50

        if player.risk_payoffrelevant == 'risk3':
            if player.risk3 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk3 == 'B':
                player.payoff_risk = 2
            
        if player.risk_payoffrelevant == 'risk4':
            if player.risk4 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk4 == 'B':
                player.payoff_risk = 2.50

        if player.risk_payoffrelevant == 'risk5':
            if player.risk5 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk5 == 'B':
                player.payoff_risk = 3

        if player.risk_payoffrelevant == 'risk6':
            if player.risk6 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk6 == 'B':
                player.payoff_risk = 3.50

        if player.risk_payoffrelevant == 'risk7':
            if player.risk7 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk7 == 'B':
                player.payoff_risk = 4

        if player.risk_payoffrelevant == 'risk8':
            if player.risk8 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk8 == 'B':
                player.payoff_risk = 4.50

        if player.risk_payoffrelevant == 'risk9':
            if player.risk9 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk9 == 'B':
                player.payoff_risk = 5

        if player.risk_payoffrelevant == 'risk10':
            if player.risk10 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk10 == 'B':
                player.payoff_risk = 5.50

        if player.risk_payoffrelevant == 'risk11':
            if player.risk11 == 'A':
                player.payoff_risk = random.choice([1, 6])
            if player.risk11 == 'B':
                player.payoff_risk = 6

class Demographics_degree(Page):
    @staticmethod
    def is_displayed(player):
        return player.Studentin_oder_Student == 1

    form_model = 'player'
    form_fields = ['degree', 'semester', 'grade']

class WaitingPage(WaitPage):
    template_name = 'Experiment\WaitingPage.html'
    wait_for_all_players = True

class Auszahlungsseite(Page):
    @staticmethod
    def vars_for_template(player):
        participant=player.participant
        session=player.session
        participant.payoff_euro = participant.payoff_total_allrounds * session.config['real_world_currency_per_point']
        participant.payoff_plus_fee = participant.payoff_euro + session.config['participation_fee'] + C.survey_fee + player.payoff_risk
        
page_sequence = [Welcome, WaitingPage, Risk1, Risk2, CBDC1, CBDC2, CBDC3, CBDC4, CBDC5, CBDC6, Anonymity, Demographics, Demographics_degree, Auszahlungsseite]
