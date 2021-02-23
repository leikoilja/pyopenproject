import model.attachment as att
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand


class FindAll(AttachmentCommand):

    def __init__(self, connection):
        """
        Constructor for class DownloadByContext, from AttachmentCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for attachment in json_obj["_embedded"]["elements"]:
                yield att.Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error finding all attachments") from re
