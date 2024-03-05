from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValiadtion
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        CONFIG_FILE_PATH = r"C:\Users\USER\Text Summerize Project\Text-Summarization-Project\config\config.yaml"

        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH)
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()