import unittest
from aiounittest import async_test

from pkg.dbtools import conn_asynpg


class MyTestCase(unittest.TestCase):
    @async_test
    async def test_connection(self):
        conn = await conn_asynpg.make_connection()
        self.assertIsNotNone(conn)

    @async_test
    async def test_get(self):
        await conn_asynpg.make_connection()
        data = await conn_asynpg.get("select * from rec_history where cam_id = '%s'", 3)
        # print(data)

    @async_test
    async def test_post(self):
        await conn_asynpg.make_connection()
        data = await conn_asynpg.get('''
        insert into reff_cam (name, location, status, created_at)
            values ('%s', '%s', '%s', NOW()) returning cam_id
        ''', ('test_async', 0, True))
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
