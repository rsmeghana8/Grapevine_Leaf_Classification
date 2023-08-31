from CNNClassifier import logger

from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data Ingestion Training"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")   
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Prepare Base Model"
try:
    logger.info("*******************************************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")   
except Exception as e:
    logger.exception(e)
    raise e


