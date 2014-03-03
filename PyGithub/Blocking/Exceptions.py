# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

"""
Error handling in PyGithub is done with exceptions. All exceptions derive (indireclty) from
:class:`PyGithubException`.

@todoSomeday generate the exception hierarchy graph
"""


class PyGithubException(Exception):
    """
    Base class for all exceptions raised by PyGithub.
    """


class BadAttributeException(PyGithubException):
    """
    Raised when GitHub API v3 returns an attribute that doesn't match the expected type or format.
    """

    def __init__(self, name, type, value):
        PyGithubException.__init__(self, name, type, value)
        self.__name = name
        self.__type = type
        self.__value = value

    def __str__(self):
        if isinstance(self.__type, list):
            names = " or ".join(t.__name__ for t in self.__type)
        else:
            names = self.__type.__name__
        return "Attribute " + self.__name + " is expected to be a " + names + " but GitHub API v3 returned " + repr(self.__value)


class ClientErrorException(PyGithubException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 4XX HTTP status code.
    """


class ObjectNotFoundException(ClientErrorException):
    """
    Raised by PyGithub when GitHub API v3 returns an unexpected 404 HTTP status code.
    """


class UnauthorizedException(ClientErrorException):
    """
    Raised by PyGithub when GitHub API v3 returns a 401 HTTP status code.
    """


class ForbiddenException(ClientErrorException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 403 HTTP status code.
    """


class RateLimitExceededException(ForbiddenException):
    """
    Raised by PyGithub when GitHub API v3 returns a 403 HTTP status code and the remaining rate limit is null.
    """


class UnprocessableEntityException(ClientErrorException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 422 HTTP status code.
    """


class ServerErrorException(PyGithubException):
    """
    Base class for exceptions raised by PyGithub when GitHub API v3 returns a 5XX HTTP status code.
    """
