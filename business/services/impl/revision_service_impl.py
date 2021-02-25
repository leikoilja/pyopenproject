from business.services.impl.command.revision.find import Find
from business.services.impl.command.revision.find_by_context import FindByContext
from business.services.revision_service import RevisionService


class RevisionServiceImpl(RevisionService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, revision):
        return Find(self.connection, revision).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()
