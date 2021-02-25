from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.delete_request import DeleteRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand


class Delete(MembershipCommand):

    def __init__(self, connection, membership):
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            DeleteRequest(self.connection, f"{self.CONTEXT}/{self.membership.id}").execute()
        except RequestError as re:
            raise BusinessError(f"Error deleting membership by id: {self.membership.id}") from re
