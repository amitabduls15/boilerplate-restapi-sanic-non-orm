from asyncpg import connect, create_pool
import asyncio


class AsyncDBPgSQL:
    def __init__(self, minconn, maxconn, host, database, user, password, port):
        self.minconn = int(minconn)
        self.maxconn = int(maxconn)
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = int(port)

        self.conn = None
        self.pool = None
        self.cur = None

    async def make_connection(self):
        self.conn = "postgres://{user}:{password}@{host}:{port}/{database}".format(
            user=self.user, password=self.password, host=self.host,
            port=self.port, database=self.database
        )

        self.pool = await create_pool(
            dsn=self.conn,
            # in bytes
            min_size=self.minconn,
            # in bytes
            max_size=self.maxconn,
            # maximum query
            max_queries=50000,
            # maximum idle times
            max_inactive_connection_lifetime=300)
        return self.pool

    @staticmethod
    def jsonify(records):
        """
        Parse asyncpg record response into JSON format
        """
        list_return = []
        for r in records:
            items = r.items()
            list_return.append({i[0]: i[1].rstrip() if type(
                i[1]) == str else i[1] for i in items})
        return list_return

    async def get_data(self, sql, values: tuple = ()):
        await self.make_connection()
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                rows = await conn.fetch(sql % values)
                return self.jsonify(rows)

    async def post(self, sql, values: tuple = ()):
        await self.make_connection()
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                rows = await conn.execute(sql, values)
                return self.jsonify(rows)
