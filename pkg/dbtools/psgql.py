import psycopg2
# import the psycopg2 errors library
import psycopg2.errors
import psycopg2.extras
# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import extensions
from psycopg2 import pool

from sanic.log import logger


class DbPostgres:
    def __init__(self, minconn, maxconn, host, database, user, password, port, dev=True):
        self.minconn = int(minconn)
        self.maxconn = int(maxconn)
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = int(port)

        self.pconnection = None
        self.conn = None
        self.cur = None
        self.dev = dev

    def __str__(self):
        if self.pconnection is not None:
            return "Pool connection avaible from {}:{}".format(self.host, self.port)
        else:
            return "Pool connection not avaible now please make connection"

    def make_connection(self):
        logger.debug("Connection to host: {} port:{} database: {} user: {} password:{}".format(
            self.host,
            self.port,
            self.database,
            self.user,
            self.password
        ))
        self.pconnection = pool.ThreadedConnectionPool(
            self.minconn,
            self.maxconn,
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port)

        self.conn = self.pconnection.getconn()
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        logger.debug(self.__str__())

    def close_connection(self):
        self.pconnection.closeall()

    def put_connection(self):
        self.pconnection.putconn(self.conn)

    def to_string(self, list_dict):
        datas = []
        a_dict = {}
        for data in list_dict:
            for keys in data:
                a_dict.update({keys: str(data[keys])})
            datas.append(a_dict)
            a_dict = {}
        return datas

    def get_transaction_status(self):

        # print(self.conn.status)
        # print the connection status
        # logger.info("\nconn.status:", self.conn.status)

        # evaluate the status for the PostgreSQL connection
        if self.conn.status == extensions.STATUS_READY:
            logger.debug("psycopg2 status #1: Connection is ready for a transaction.")

        elif self.conn.status == extensions.STATUS_BEGIN:
            logger.debug("psycopg2 status #2: An open transaction is in process.")

        elif self.conn.status == extensions.STATUS_IN_TRANSACTION:
            logger.error("psycopg2 status #3: An exception has occured.")
            logger.debug("Use tpc_commit() or tpc_rollback() to end transaction")

        elif self.conn.status == extensions.STATUS_PREPARED:
            logger.debug("psycopg2 status #4:A transcation is in the 2nd phase of the process.")
        return self.conn.status

    def get_data(self, query, values: tuple = None):
        results = []
        if values is not None:
            query = query % values
        try:
            if self.dev:
                self.make_connection()
            self.cur.execute(query)
            results = self.cur.fetchall()
            if self.dev:
                self.put_connection()
        except Exception as e:
            err_msg = str(e)
            logger.error(str(e))
            self.cur.execute("ROLLBACK")
        if len(results) == 0:
            return []
        else:
            result = [dict(result) for result in results]
            return result

    def exec_script(self, script: str):
        sql_file = open(script, "r").read()
        err_msg = None
        try:
            if self.dev:
                self.make_connection()
            self.cur.execute(sql_file)
            self.conn.commit()
            if self.dev:
                self.put_connection()
        except Exception as e:
            err_msg = str(e)
            logger.error(str(e))
            self.cur.execute("ROLLBACK")
        return err_msg

    def post_data(self, query: str, values=None):
        if values is not None:
            sql = query % values
        else:
            sql = query
        err_msg = None
        try:
            if self.dev:
                self.make_connection()
            self.cur.execute(sql)
            self.conn.commit()
            if self.dev:
                self.put_connection()
        except Exception as e:
            err_msg = str(e)
            logger.error(str(e))
            self.cur.execute("ROLLBACK")
        return err_msg

    def post_data_ret(self, query: str, values: tuple):
        sql = query % values
        err_msg = None
        data = []
        try:
            if self.dev:
                self.make_connection()
            self.cur.execute(sql)
            data = self.cur.fetchall()
            self.conn.commit()
            if self.dev:
                self.put_connection()

        except Exception as e:
            err_msg = str(e)
            logger.error(str(e))
            self.cur.execute("ROLLBACK")

        if len(data) == 0:
            return []
        else:
            result = [dict(result) for result in data]
            return result, err_msg
