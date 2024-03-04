from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size, create_directories
from ..entity import DataIngestionConfig  # Update import statement
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
