from pkg.env import Env


class PgSQLConfigs:
    _port: int
    _host: str
    _min_conn: int
    _max_conn: int
    _uname: str
    _password: str
    _db: str

    @property
    def port(self) -> int:
        return self._port

    @property
    def host(self) -> str:
        return self._host

    @property
    def max_conn(self) -> int:
        return self._max_conn

    @property
    def min_conn(self) -> int:
        return self._min_conn

    @property
    def uname(self) -> str:
        return self._uname

    @property
    def password(self) -> str:
        return self._password

    @property
    def db(self) -> str:
        return self._db

    @classmethod
    def load(cls, env: Env):
        cls._port = env.get_int("POSTGRESQL_PORT", default=5432)
        cls._host = env.get_str("POSTGRESQL_HOST", default='localhost')
        cls._min_conn = env.get_int("POSTGRESQL_MINCONN", default=1)
        cls._max_conn = env.get_int("POSTGRESQL_MAXCONN", default=2)
        cls._db = env.get_str("POSTGRESQL_DB")

        cls._password = env.get_str("POSTGRESQL_PASSWORD", default='')
        cls._uname = env.get_str("POSTGRESQL_USER", default='postgres')
