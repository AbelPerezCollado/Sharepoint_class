from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from config import DOMAIN, USER, PWD, FOLDER_NAME, PATH

class Sharepoint():
    def __init__(self) -> None:
        self.sharepoint_url = f'https://[DOMAIN].sharepoint.com'
        self.user = f'{USER}'
        self.pwd = f'{PWD}'
        self.folder_name = f'{FOLDER_NAME}'
        self.path = f'Documentos compartidos/{self.folder_name}'

    def get_context_using_user(self):
        self.user_credentials = UserCredential(self.user , self.pwd)
        return ClientContext(self.sharepoint_url).with_credentials(self.user_credentials)

    def create_directory(self,dir_name: str):
        self.dir_name = dir_name
        if self.dir_name:
            ctx = self.get_context_using_user()
            result = ctx.web.folders.add( self.path + self.dir_name).execute_query()
        if result:
            return self.path + self.dir_name

    def upload_file(self,dir_name: str , file_name: str):
        sp_relative_url = self.create_directory(dir_name)
        ctx = self.get_context_using_user()
        target_folder = ctx.web.get_folder_by_server_relative_url(sp_relative_url)
        with open(file_name, 'rb') as content_file:
            file_content = content_file.read()
            target_folder.upload_file(file_name , file_content).execute_query()






            
