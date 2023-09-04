from src.NLP_project.utils.common import  copy_file
from src.NLP_project import logger


class DataIngestion:
    def __init__(self,config):
        self.config=config

    def get_the_data(self):

        copy_file(source_path=self.config.source_dir,destination_path=self.config.data_dir)

        pass