from .pgsql import PgSQLConfigs
from .apps import AppsConfigs
from pkg.env import Env

pgsql_configs = PgSQLConfigs()
apps_configs = AppsConfigs()
env_file = '.env'

env = Env(env_file)
pgsql_configs.load(env)
apps_configs.load(env)
