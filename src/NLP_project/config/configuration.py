from src.NLP_project.utils.common import create_directories,read_yaml
from src.NLP_project.constants import *
from src.NLP_project.entity import DataIngestionConfig
from src.NLP_project.entity import DataValidationConfig,Data_transformationCofig


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
    
    def data_validation_done_config(self)->DataValidationConfig:
        validation=self.config.Data_validataion

        create_directories([validation.root_dir])

        data_validation=DataValidationConfig(
            root_dir=validation.root_dir,
            STATUS_FILE=validation.STATUS_FILE,
            ALL_REQUIRES_FILES=validation.ALL_REQUIRES_FILES
        )
        return data_validation
    
    def get_data_transformation(self)->Data_transformationCofig:
        transformation=self.config.Data_transformation

        create_directories([transformation.root_dir])

        transformation=Data_transformationCofig(
            root_dir=transformation.root_dir,
            data_path=transformation.data_path,
            tokiner_name=transformation.tokiner_name)
        return transformation