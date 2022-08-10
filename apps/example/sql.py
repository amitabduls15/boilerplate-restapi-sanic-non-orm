from pkg.dbtools import conn_asynpg


class SQLStatistics:
    def __init__(self, conn=conn_asynpg):
        self.conn = conn

    async def get_stats_desc_every_hour_by_cam_id(self, cam_id: int):
        sql = '''
        select CAST(created_date AS varchar), created_hour, sum, avg, max, min, stddev,count from  
            (select cam_id,DATE(time_in) AS created_date, extract(hour from time_in) as created_hour,
               sum(second_diff) as sum, avg(second_diff) as avg, max(second_diff) as max,
               min(second_diff) as min, stddev(second_diff) as stddev, count(second_diff) as count from
                    (select cam_id,time_in, extract(EPOCH from time_out-time_in) AS second_diff
                        from public.rec_history where time_out is not null) as table_diff 
        group by cam_id, created_date, created_hour) as table_statistics
        where cam_id = '%s'
        '''

        return await self.conn.get_data(sql, (cam_id))

    async def get_stats_desc_every_day_by_cam_id(self, cam_id: int):
        sql = '''
        select CAST(created_date AS varchar),sum, avg, max, min, stddev,count from  
            (select cam_id,DATE(time_in) AS created_date,
               sum(second_diff) as sum, avg(second_diff) as avg, max(second_diff) as max,
               min(second_diff) as min, stddev(second_diff) as stddev, count(second_diff) as count from
                    (select cam_id,time_in, extract(EPOCH from time_out-time_in) AS second_diff
                        from public.rec_history where time_out is not null) as table_diff 
        group by cam_id, created_date) as table_statistics
        where cam_id = '%s'
        '''

        return await self.conn.get_data(sql, (cam_id))

    async def get_stats_desc_every_hour(self):
        sql = '''
                select cam_id,CAST(created_date AS varchar), created_hour, sum, avg, max, min, stddev,count from  
                    (select cam_id,DATE(time_in) AS created_date, extract(hour from time_in) as created_hour,
                       sum(second_diff) as sum, avg(second_diff) as avg, max(second_diff) as max,
                       min(second_diff) as min, stddev(second_diff) as stddev, count(second_diff) as count from
                            (select cam_id,time_in, extract(EPOCH from time_out-time_in) AS second_diff
                                from public.rec_history where time_out is not null) as table_diff 
                group by cam_id, created_date, created_hour) as table_statistics
                '''

        return await self.conn.get_data(sql)

    async def get_stats_desc_every_day(self):
        sql = '''
                select cam_id, CAST(created_date AS varchar), sum, avg, max, min, stddev,count from  
                    (select cam_id,DATE(time_in) AS created_date,
                       sum(second_diff) as sum, avg(second_diff) as avg, max(second_diff) as max,
                       min(second_diff) as min, stddev(second_diff) as stddev, count(second_diff) as count from
                            (select cam_id,time_in, extract(EPOCH from time_out-time_in) AS second_diff
                                from public.rec_history where time_out is not null) as table_diff 
                group by cam_id, created_date) as table_statistics
                '''

        return await self.conn.get_data(sql)



