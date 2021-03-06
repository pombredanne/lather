# -*- coding: utf-8 -*-


class ServiceNotFound(Exception):
    pass


class ObjectDoesNotExist(Exception):
    pass


class ObjectsDoNotExist(Exception):
    pass


class MultipleObjectReturned(Exception):
    pass


class ValidationError(Exception):
    pass


class FieldException(Exception):
    pass


class InvalidBaseUrlException(Exception):
    pass


class ConnectionError(Exception):
    pass
