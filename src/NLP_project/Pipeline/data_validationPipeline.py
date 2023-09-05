from src.NLP_project.config.configuration import Configuration
from src.NLP_project.components.data_validation import Data_Validation


class Data_validationPipeline:
    def __init__(self):
        pass

    def main(self):
        validation_config=Configuration()
        val_config=validation_config.data_validation_done_config()

        val=Data_Validation(val_config)
        val.check_data_validation_files()
