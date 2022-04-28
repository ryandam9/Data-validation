#------------------------------------------------------------------------------#
# Settings.py                                                                  #
#------------------------------------------------------------------------------#
# TGT_DB_ENGINE = "Oracle"
# TGT_PORT = "1521"
# TGT_DB = "ORCL"

# SRC_DB_ENGINE = "Postgres"
# SRC_PORT = "5432"
# SRC_DB = "postgres"

# SRC_DB_ENGINE = "SQLSERVER"
# SRC_PORT = "1433"
# SRC_DB = "AdventureWorks"

TGT_DB_ENGINE = "Postgres"
TGT_PORT = "5432"
TGT_DB = "postgres"

SRC_DB_ENGINE = "SQLSERVER"
SRC_PORT = "1433"
SRC_DB = "AdventureWorks1"

# How many records to be validated between source & target tables
DATA_VALIDATION_REC_COUNT = 1000

# How many data validation threads can run at the same time?
PARALLEL_THREADS = 50

# When true, the data validation comparison will be logged.
DEBUG_DATA_VALIDATION = True

# When set to true, interaction with DB will be logged.
SQL_ALCHEMY_ECHO_MODE = False

# Enable this when it is failing to connect to the Database.
# It shows the connecting string including the password.
SHOW_CONNECTION_STRING = False

# Update this variable to point to the Oracle Instant Client.
oracle_instant_client_path = r"C:\Users\ravis\Desktop\ravi\instantclient_21_3"
