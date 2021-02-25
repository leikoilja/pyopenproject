
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.form import Form


class UpdateForm(ProjectCommand):

    def __init__(self, connection, project):
        super().__init__(connection)
        self.project = project

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.project.id}/form",
                                   json=self.project.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating project form {self.project.name}") from re
