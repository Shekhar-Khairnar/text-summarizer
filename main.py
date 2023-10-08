<<<<<<< HEAD
from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from textsummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textsummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
=======
from textsummarizer.logging import logger

logger.info('Custom logging')
>>>>>>> 631e41c49e951fe581201673a0b05d4c5eb8ba0b
