from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import StringType, URLType, IntType, ListType


class StatsHour(Model):
    cam_id = ListType(IntType, required=False)


class StatsDay(Model):
    cam_id = ListType(StringType, required=False)
