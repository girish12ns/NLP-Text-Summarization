from src.NLP_project.utils.common import create_directories,read_yaml
from src.NLP_project.constants import *
from src.NLP_project.entity import DataIngestionConfig


class Configuration:
    def __init__(self,config=config_path_file,params=params_path_file):
        self.config=read_yaml(config)
        self.params=read_yaml(params)

        create_directories([self.config.Artifacts])

    def get_the_data_config(self)->DataIngestionConfig:
        ingestion=self.config.Data_ingestion

        create_directories([ingestion.source_dir,ingestion.data_dir])

        data_ingestion=DataIngestionConfig(
            root_dir=ingestion.root_dir,
            source_dir=ingestion.source_dir,
            data_dir=ingestion.data_dir)
        
        return data_ingestion