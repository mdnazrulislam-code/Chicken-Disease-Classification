from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_basemodel_config = config.get_prepare_base_model_config()
        prepare_basemodel = PrepareBaseModel(config= prepare_basemodel_config)
        prepare_basemodel.get_base_model()
        prepare_basemodel.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e 