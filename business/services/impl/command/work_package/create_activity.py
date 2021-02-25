import model.activity as activity
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from util.URL import URL
from util.URLParameter import URLParameter


class CreateActivity(WorkPackageCommand):

    def __init__(self, connection, work_package, comment, notify):
        super().__init__(connection)
        self.work_package = work_package
        self.comment = {
            "comment": {
                "raw": f"{comment}"
            }
        }
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=str(URL(f"{self.CONTEXT}{self.work_package.id}/activities",
                                                   [
                                                       URLParameter("notify", self.notify)
                                                   ])),
                                   json=self.comment).execute()
            return activity.Activity(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating activity for the work package {self.work_package.id}") from re
