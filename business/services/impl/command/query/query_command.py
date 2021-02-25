from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class QueryCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/queries"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
