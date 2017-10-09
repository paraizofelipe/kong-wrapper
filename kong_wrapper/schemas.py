from marshmallow import Schema, fields


class ApiSchema(Schema):

    id = fields.String()
    name = fields.String()
    hosts = fields.List(fields.String())
    uris = fields.String()
    methods = fields.String()
    upstream_url = fields.String()
    strip_uri = fields.Boolean()
    preserve_host = fields.Boolean()
    retries = fields.Integer()
    upstream_connect_timeout = fields.Integer()
    upstream_send_timeout = fields.Integer()
    upstream_read_timeout = fields.Integer()
    https_only = fields.Boolean()
    http_if_terminated = fields.Boolean()
    created_at = fields.Integer()


class ComsumersSchema(Schema):

    id = fields.String()
    usernam = fields.String()
    custom_id = fields.String()
    created_at = fields.Integer()


class PluginSchema(Schema):

    id = fields.String()
    api_id = fields.String()
    consumer_id = fields.String()
    name = fields.String()
    config = fields.Dict()
    enabled = fields.Boolean()
    created_at = fields.Integer()


class SniSchema(Schema):

    name = fields.String()
    ssl_certificate_id = fields.String()
    created_at = fields.Integer()


class CertificateSchema(Schema):

    id = fields.String()
    cert = fields.String()
    key = fields.String()
    snis = fields.Nested(SniSchema)
    created_at = fields.Integer()


class UpstreamSchema(Schema):

    id = fields.String()
    name = fields.String()
    orderlist = fields.List(fields.Integer())
    slots = fields.Integer()
    created_at = fields.Integer()


class TargetSchema(Schema):

    id = fields.String()
    target = fields.String()
    weight = fields.Integer()
    upstream_id = fields.String()
    created_at = fields.Integer()
