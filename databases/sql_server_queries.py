sqlserver_queries = {}

# Get Primary key
sqlserver_queries[
    "get_primary_key"
] = """
WITH temp AS (
    <temp_placeholder>
)
SELECT
	TEMP.schema_name
  , TEMP.table_name
  , C.COLUMN_NAME 
FROM  
	INFORMATION_SCHEMA.TABLE_CONSTRAINTS T
  , INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE C   
  , TEMP 
WHERE
	T.CONSTRAINT_TYPE = 'PRIMARY KEY' 
AND T.TABLE_SCHEMA = TEMP.schema_name
AND T.TABLE_NAME   = TEMP.table_name
AND C.TABLE_SCHEMA = TEMP.schema_name
AND C.TABLE_NAME   = TEMP.table_name
AND C.CONSTRAINT_NAME = T.CONSTRAINT_NAME
ORDER BY
	1, 2, 3
"""