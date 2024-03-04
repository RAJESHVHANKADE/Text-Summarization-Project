from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        CONFIG_FILE_PATH = r"C:\Users\USER\Text Summerize Project\Text-Summarization-Project\config\config.yaml"

        config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH)
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()