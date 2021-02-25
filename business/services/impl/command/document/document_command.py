from abc import abstractmethod, ABCMeta

from business.services.impl.command.command import Command


class DocumentCommand(Command):
    __metaclass__ = ABCMeta

    CONTEXT = "/api/v3/documents"

    def __init__(self, connection):
        """Constructor for class DocumentCommand, from Command.

        :param connection: The connection data
        """
        self.connection = connection

    @abstractmethod
    def execute(self): raise NotImplementedError
