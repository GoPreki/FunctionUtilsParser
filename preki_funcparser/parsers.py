import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o) if o % 1 != 0 else int(o)
        return super(DecimalEncoder, self).default(o)


class Parser:
    def __init__(self, data):
        self.data = data

    def to_number(self):
        return json.loads(
            json.dumps(self.data, cls=DecimalEncoder))

    def to_decimal(self):
        return json.loads(json.dumps(self.data), parse_float=Decimal)
