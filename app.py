import os
import platform
import sys

from databases.sql_server import sqlserver_table_to_df
from settings import (SRC_DB, SRC_DB_ENGINE, SRC_PORT, TGT_DB, TGT_DB_ENGINE,
                      TGT_PORT, oracle_instant_client_path)
from src.data_validation import data_validation
from src.utils import get_project_root, get_tables_to_validate

# ------------------------------------------------------------------------------#
# Get the table list that need to be validated.                                 #
# ------------------------------------------------------------------------------#
tables_to_validate = get_tables_to_validate()

if len(tables_to_validate) == 0:
    print("-> No tables to validate")
    sys.exit(0)

# ------------------------------------------------------------------------------#
# Check the DB Connection properties.                                           #
# ------------------------------------------------------------------------------#
src_host = os.environ["SRC_HOST"] if "SRC_HOST" in os.environ else None
src_user = os.environ["SRC_USER"] if "SRC_USER" in os.environ else None
src_pwd = os.environ["SRC_PWD"] if "SRC_PWD" in os.environ else None

tgt_host = os.environ["TGT_HOST"] if "TGT_HOST" in os.environ else None
tgt_user = os.environ["TGT_USER"] if "TGT_USER" in os.environ else None
tgt_pwd = os.environ["TGT_PWD"] if "TGT_PWD" in os.environ else None

if (
    SRC_DB_ENGINE is None
    or len(SRC_DB_ENGINE) == 0
    or src_host is None
    or len(src_host) == 0
    or SRC_PORT is None
    or len(SRC_PORT) == 0
    or SRC_DB is None
    or len(SRC_DB) == 0
    or src_user is None
    or len(src_user) == 0
    or src_pwd is None
    or len(src_pwd) == 0
) or (
    TGT_DB_ENGINE is None
    or len(TGT_DB_ENGINE) == 0
    or tgt_host is None
    or len(tgt_host) == 0
    or TGT_PORT is None
    or len(TGT_PORT) == 0
    or TGT_DB is None
    or len(TGT_DB) == 0
    or tgt_user is None
    or len(tgt_user) == 0
    or tgt_pwd is None
    or len(tgt_pwd) == 0
):
    print("-> Please set the DB Configuration in settings.py")
    print(
        "-> Please set the envioronment variables: SRC_HOST, SRC_USER, SRC_PWD, TGT_HOST, TGT_USER, TGT_PWD"
    )
    sys.exit(1)

src_config = {
    "db_engine": SRC_DB_ENGINE,
    "host": src_host,
    "port": SRC_PORT,
    "service": SRC_DB,
    "user": src_user,
    "password": src_pwd,
}

tgt_config = {
    "db_engine": TGT_DB_ENGINE,
    "host": tgt_host,
    "port": TGT_PORT,
    "service": TGT_DB,
    "user": tgt_user,
    "password": tgt_pwd,
}

# ------------------------------------------------------------------------------#
# Create following directories                                                  #
# ------------------------------------------------------------------------------#
root_dir = get_project_root()

if not os.path.exists(f"{root_dir}/logs"):
    os.mkdir(f"{root_dir}/logs")

if not os.path.exists(f"{root_dir}/data_validation_reports"):
    os.mkdir(f"{root_dir}/data_validation_reports")

# Using cx_Oracle requires Oracle Client libraries to be installed.
# These provide the necessary network connectivity allowing cx_Oracle to access
# an Oracle Database instance.
current_platform = platform.system().lower()

if "windows" in current_platform:
    current_path = os.environ["PATH"]
    updated_path = oracle_instant_client_path + ";" + current_path
    os.environ["PATH"] = updated_path

    client_path = updated_path.split(";")[0]
    print(f"-> PATH is set to: {client_path}")

# Invoke validation
data_validation(tables_to_validate, src_config, tgt_config)
