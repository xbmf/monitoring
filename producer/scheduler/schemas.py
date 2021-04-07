from marshmallow import Schema, fields


class WebsiteSchema(Schema):
    url = fields.URL()
    interval = fields.Int()  # in seconds
    regexp_rules = fields.List(fields.Str())
