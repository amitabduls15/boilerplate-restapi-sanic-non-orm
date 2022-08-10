import sanic
from sanic import Blueprint, response, HTTPResponse
from apps.example import sql_statistics
from .validator import StatsHour, StatsDay

from schematics.exceptions import DataError

stats_bp = Blueprint("Statistics", url_prefix="/stats")


@stats_bp.route("/hour", methods=['GET'])
async def stats_hour(request: sanic.Request):
    try:
        args = request.args
        args_hour = StatsHour(args)
        args_hour.validate()

        cam_id_list = args_hour.cam_id
        data = []
        if cam_id_list:
            for cam_id in cam_id_list:
                res_data = sql_statistics.get_stats_desc_every_hour_by_cam_id(cam_id=cam_id)
                data.append({'cam_id': cam_id, 'data': res_data})
        else:
            data = sql_statistics.get_stats_desc_every_hour()
        return response.json(data)
    except DataError:
        return response.text('data error', 502)


@stats_bp.route("/day", methods=['GET'])
async def stats_day(request):
    try:
        args = request.args
        args_day = StatsDay(args)
        args_day.validate()

        cam_id_list = args_day.cam_id
        data = []
        if cam_id_list:
            for cam_id in cam_id_list:
                res_data = sql_statistics.get_stats_desc_every_day_by_cam_id(cam_id=cam_id)
                data.append({'cam_id': cam_id, 'data': res_data})
        else:
            data = sql_statistics.get_stats_desc_every_day()
        return response.json(data)
    except DataError:
        return response.text('data error', 502)
