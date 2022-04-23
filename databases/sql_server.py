import warnings

import pandas as pd
import pyodbc
import sqlalchemy
from settings import SQL_ALCHEMY_ECHO_MODE
from sqlalchemy import exc as sa_exc
from sqlalchemy.exc import SQLAlchemyError
from src.utils import print_messages
from tabulate import tabulate


def sqlserver_table_to_df(config, query, params):
    """
    For this function to work, first download ODBC Driver from this
    link:
    https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

    """
    host = config["host"]
    port = config["port"]
    service = config["service"]
    user = config["user"]
    password = config["password"]

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)

        engine = sqlalchemy.create_engine(
            f"mssql+pyodbc://{user}:{password}@{host}:{port}/{service}?driver=ODBC Driver 17 for SQL Server")

        if params is None:
            df = pd.read_sql(query, engine)
            return df
        else:
            df = pd.read_sql(query, engine, params=params)
            return df

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise e
