from pkg.env import Env


class AppsConfigs:
    _port: int
    _host: str
    _num_workers: int

    @property
    def port(self) -> int:
        return self._port

    @property
    def host(self) -> str:
        return self._host

    @property
    def num_workers(self) -> int:
        return self._num_workers

    @classmethod
    def load(cls, env: Env):
        cls._port = env.get_int("APPS_PORT", default=8000)
        cls._host = env.get_str("APPS_HOST", default='localhost')
        cls._num_workers = env.get_int("APPS_NUM_WORKER", default=1)
