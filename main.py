from CNNClassifier import logger

from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Training"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")   
except Exception as e:
    logger.exception(e)
    raise e