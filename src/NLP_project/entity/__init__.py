from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_dir:Path
    data_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE :str
    ALL_REQUIRES_FILES  :list


@dataclass(frozen=True)
class Data_transformationCofig:
    root_dir  : Path
    data_path : Path
    tokiner_name : Path