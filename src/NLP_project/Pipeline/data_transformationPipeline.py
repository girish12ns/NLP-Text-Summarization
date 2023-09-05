from src.NLP_project.components.data_transformation import Data_transformation
from src.NLP_project.config.configuration import Configuration



class Data_transformationPipline:
    def __init__(self):
        pass

    def main(self):
        data_trans_config=Configuration()

        data_config=data_trans_config.get_data_transformation()

        transformations=Data_transformation(data_config)

        transformations.convert()
