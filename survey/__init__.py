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
    age = models.IntegerField(label='Wie alt sind Sie?', min=16, max=125)
    gender = models.StringField(
        choices=[['Weiblich', 'Weiblich'], ['Männlich', 'Männlich'], ['Divers', 'Divers']],
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
    )
    education = models.StringField(
        label = 'Welches ist der höchste Abschluss, den Sie erreicht haben?',
        choices = ['Keinen Schulabschluss', 'Schulabschluss oder gleichwertiger Abschluss', 'Bachelor', 'Master oder Staatsexamen', 'Promotion' ],
        widget=widgets.RadioSelect,
    )
    degree = models.StringField(
        label = 'Bitte nennen Sie den Studiengang in dem Sie eingeschrieben sind:',
    )
    semester = models.StringField(
        label = 'Im wievieltem Semester studieren Sie?',
    )
    risk1 =  models.IntegerField(
        label = "",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
    )
    cbdc1 = models.StringField(
        label = 'Was glauben Sie, worum es in diesem Experiment ging?',
    )
    cbdc2 = models.StringField(
        label = 'Haben Sie bereits vor dem Experiment von digitalem Zentralbankgeld gehört bzw. darüber gelesen?',
        choices = ['ja', 'nein' ],
        widget=widgets.RadioSelect,
    )
    cbdc3 = models.StringField(
        label = 'Wie wahrscheinlich ist es, dass Sie nach einer Einführung den digitalen Euro nutzen würden?',
        choices = ['sehr wahrscheinlich', 'wahrscheinlich', 'unentschieden', 'unwahrscheinlich', 'sehr unwahrscheinlich' ],
        widget=widgets.RadioSelect,
    )
    cbdc4 =  models.IntegerField(
        label = 'Wenn der digitale Euro eingeführt werden würde, welche der folgenden Eigenschaften wäre Ihnen am wichtigsten?',
        choices = ['Anonymität der Zahlungen', 'Sicherheit in Bezug auf Datenschutz', 'kostenfreie Nutzung', 'bequeme Nutzung' ],
        widget=widgets.RadioSelect,
    )
    cbdc5 =  models.IntegerField(
        label = 'Sehen Sie den digitalen Euro als Alternative zum Bargeld oder als Alternative zu unbaren Zahlungsmitteln (z.B. Zahlung mit Debitkarte, Kreditkarte)? Der äußerste Kreis links bedeutet "nur als Alternative zu Bargeld", der äußerste Kreis rechts bedeutet "nur als Alternative zu unbaren Zahlungsmitteln".',
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelectHorizontal,
    )
    Bargeld = models.BooleanField(blank=True)
    Girocard_kontaktlos = models.BooleanField(blank=True)
    Girocard_einschieben = models.BooleanField(blank=True)
    Kreditkarte_kontaktlos = models.BooleanField(blank=True)
    Kreditkarte_einschieben = models.BooleanField(blank=True)
    Smartphone_Debit = models.BooleanField(blank=True)
    Smartphone_Kredit = models.BooleanField(blank=True)
    Anderes_Zahlungsmittel = models.BooleanField(blank=True)
# PAGES
class AnonymityPreferences(Page):
    pass

class CBDCQuestions(Page):
   form_model = 'player'
   form_fields = ['cbdc1', 'cbdc2', 'cbdc3', 'cbdc4', 'cbdc5'
     'Bargeld', 'Girocard_kontaktlos', 'Girocard_einschieben', 'Kreditkarte_kontaktlos', 
     'Kreditkarte_einschieben', 'Smartphone_Debit', 'Smartphone_Kredit', 'Anderes Zahlungsmittel']

class Risk1(Page):
    form_model = 'player'
    form_fields = ['risk1']

class Risk2(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'Vollzeiterwerbstätig', 'Teilzeiterwerbstätig',
     'Geringfügig_erwerbstätig', 'Minijob', 'Ruhestand', 'Studentin_oder_Student', 
     'Selbstständig', 'Nicht_erwerbstätig_und_Arbeitssuchend', 'Nicht_erwerbstätig_und_nicht_Arbeitssuchend', 'education']

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
        

class Demographics_degree(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.Studentin_oder_Student == 1

    form_model = 'player'
    form_fields = ['degree', 'semester']


class Auszahlungsseite(Page):
    @staticmethod
    def vars_for_template(player):
        participant=player.participant
        session=player.session
        participant.payoff_euro = participant.payoff_total_allrounds * session.config['real_world_currency_per_point']
        participant.payoff_plus_fee = participant.payoff_euro + session.config['participation_fee']
        


page_sequence = [CBDCQuestions, Risk1, Risk2, Demographics, Demographics_degree, Auszahlungsseite]
