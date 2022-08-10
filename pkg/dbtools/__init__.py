from .psgql import DbPostgres
from .asypsgql import AsyncDBPgSQL
from configs import pgsql_configs

conn_postgres = DbPostgres(minconn=pgsql_configs.min_conn, maxconn=pgsql_configs.max_conn, host=pgsql_configs.host,
                           database=pgsql_configs.db, user=pgsql_configs.uname,
                           password=pgsql_configs.password, port=pgsql_configs.port)

conn_asynpg = AsyncDBPgSQL(minconn=pgsql_configs.min_conn, maxconn=pgsql_configs.max_conn, host=pgsql_configs.host,
                           database=pgsql_configs.db, user=pgsql_configs.uname,
                           password=pgsql_configs.password, port=pgsql_configs.port)


