from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class ActivityCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/activities"

    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
