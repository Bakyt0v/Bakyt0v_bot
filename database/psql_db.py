import psycopg2
from config_bot import URI, bot
database = psycopg2.connect(URI, sslmode="require")
cursor = database.cursor()

