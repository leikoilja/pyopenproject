
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.time_entry.time_entry_command import TimeEntryCommand
import model.time_entry as te


class Create(TimeEntryCommand):

    def __init__(self, connection, time_entry):
        super().__init__(connection)
        self.time_entry = time_entry

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.time_entry.__dict__).execute()
            return te.TimeEntry(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating a time entry with ID: {self.time_entry.id}") from re
