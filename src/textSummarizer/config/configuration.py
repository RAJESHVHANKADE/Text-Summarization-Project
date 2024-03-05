from textSummarizer.logging import logger
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from pathlib import Path
import yaml

class ConfigurationManager:
    def __init__(self, config_filepath):
        self.config = self.read_yaml(config_filepath)
        create_directories([self.config['artifacts_root']])

    def read_yaml(self, filepath):
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        create_directories([config['root_dir']])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config['root_dir']),
            source_URL=config['source_URL'],
            local_data_file=Path(config['local_data_file']),
            unzip_dir=Path(config['unzip_dir'])
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config['data_validation']

        create_directories([config['root_dir']])

        data_validation_config = DataValidationConfig(
            root_dir=config['root_dir'],
            STATUS_FILE=config['STATUS_FILE'],
            ALL_REQUIRED_FILES=config['ALL_REQUIRED_FILES']
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.get('data_transformation', {})  # Use .get() to handle missing keys

        create_directories([config.get('root_dir', '')])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.get('root_dir', ''),
            data_path=config.get('data_path', ''),
            tokenizer_name=config.get('tokenizer_name', '')
        )

        return data_transformation_config
