from os import environ

SESSION_CONFIGS = [
     dict(
         name='CBDC_Experiment',
         app_sequence=['survey','testquestions','Testround','Experiment'],
         num_demo_participants=2,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.15, participation_fee=6.00, doc=""
)

PARTICIPANT_FIELDS = ['payoff_euro','payoff_total_allrounds', 'payoff_plus_fee', 'payoff_anonymous_allrounds','payoff_notanonymous_allrounds', 'payoff_anonymous_euro', 'payoff_notanonymous_euro', 'payoff_anonymous_plus_fee' ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False
POINTS_CUSTOM_NAME =  'Taler'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5723496014656'
