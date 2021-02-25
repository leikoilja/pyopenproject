
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.project.project_command import ProjectCommand
from model.form import Form


class CreateForm(ProjectCommand):

    def __init__(self, connection, form):
        super().__init__(connection)
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/form",
                                   json=self.form.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating project form: {self.form.name}") from re
