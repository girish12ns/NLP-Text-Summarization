from src.NLP_project.config.configuration import Configuration
from src.NLP_project.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config_data=Configuration()
        data_ingestion_config=config_data.get_the_data_config()

        ingestion=DataIngestion(data_ingestion_config)
        ingestion.get_the_data()
        pass
