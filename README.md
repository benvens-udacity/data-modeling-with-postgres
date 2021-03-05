# Data Modelling with Postgres

## Contents

The project directory contains the following files:

| File | Description |
| ---- | ----------- |
| `sql_queries.py` | A python module (to be `import`'ed) that includes all SQL statements |
| `create_tables.py` | Python script to execute DDL recreate the database and empty tables from scratch. |
| `etl.ipynb` | Jupyter notebook to extract, transform and load (ETL) the data, from a subset of JSON files into the database |
| `etl.py` | The ETL script based on the previous notebook, which process all JSON files found in the `log_data` and `song_data` directories. |
| `run-postgres.sh` | Script to start local Docker container running the Postgres image. |
| `sql_queries.py` | Quaery the data in the fact table and dimension tables. |
