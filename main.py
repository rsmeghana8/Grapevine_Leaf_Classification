from CNNClassifier import logger

from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from CNNClassifier.pipeline.stage_04_data_evaluation import EvaluationPipeline


 #Uncomment the following when running first time

#STAGE_NAME="Data Ingestion Training"
#try:
#    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
#    data_ingestion = DataIngestionTrainingPipeline()
#    data_ingestion.main()
#    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")   
#except Exception as e:
#    logger.exception(e)
#    raise e

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


STAGE_NAME="Training"

try:
    logger.info(f"***************************************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Evaluation"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


