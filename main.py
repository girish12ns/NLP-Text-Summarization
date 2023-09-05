from src.NLP_project import logger
from src.NLP_project.Pipeline.data_ingestionPipeline import DataIngestionPipeline
from src.NLP_project.Pipeline.data_validationPipeline import Data_validationPipeline
from src.NLP_project.Pipeline.data_transformationPipeline import Data_transformationPipline

try:
    data=DataIngestionPipeline()
    data.main()
    logger.info("Data_ingestion completed sucessully")
except Exception as e:
    raise e

try:
    data=Data_validationPipeline()
    data.main()
    logger.info("Data_validation completed sucessully")
except Exception as e:
    raise e

try:
    data=Data_transformationPipline()
    data.main()
    logger.info("Data_transformation completed sucessully")
except Exception as e:
    raise e

