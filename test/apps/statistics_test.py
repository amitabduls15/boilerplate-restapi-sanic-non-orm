import unittest
from aiounittest import async_test
from apps.example import sql_statistics


class StatisticsTestCase(unittest.TestCase):
    @async_test
    async def test_get_statistics_desc_every_hour_by_cam_id_success(self):
        cam_id = 3
        res = await sql_statistics.get_stats_desc_every_hour_by_cam_id(cam_id)
        self.assertIsNotNone(res)

    @async_test
    async def test_get_statistics_desc_every_day_by_cam_id_success(self):
        cam_id = 3
        res = await sql_statistics.get_stats_desc_every_day_by_cam_id(cam_id)
        self.assertIsNotNone(res)

    @async_test
    async def test_get_statistics_every_hour_desc_success(self):
        res = await sql_statistics.get_stats_desc_every_hour()
        self.assertIsNotNone(res)

    @async_test
    async def test_get_statistics_every_day_desc_success(self):
        res = await sql_statistics.get_stats_desc_every_day()
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main(verbosity=2)
