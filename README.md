# Data Validator


## Windows
- Download ODBC Driver 17 from this link
- https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
****

## MacOS
### SQL Server
```sh
# https://medium.com/@jrhanso1/connecting-to-an-mssql-server-on-a-mac-27a227f43d2c

brew install freetds unixodbc

ls -l /opt/homebrew/Cellar/freetds/1.3.10
```
****


```python
>>> import pyodbc
>>> pyodbc.drivers()
```


```
╭─ 
╰─○ odbcinst -j
unixODBC 2.3.9
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /Users/rk/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8
```


[ODBC Driver 17 for SQL Server]
Description=Microsoft ODBC Driver 17 for SQL Server
Driver=/opt/homebrew/Cellar/msodbcsql17/17.9.1.1/lib
