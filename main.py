from src.NLP_project import logger
from src.NLP_project.Pipeline.data_ingestionPipeline import DataIngestionPipeline

try:
    data=DataIngestionPipeline()
    data.main()
    logger.info("Data_ingestion completed sucessully")
except Exception as e:
    raise e
