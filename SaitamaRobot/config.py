class Development(Config):
    OWNER_ID =  1731486754  # your telegram ID
    OWNER_USERNAME = "rimuruslimeboy"  # your telegram username
    API_KEY = "your bot api key"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    JOIN_LOGGER = '-1001228830348' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    SUDO_USERS = [  ]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
