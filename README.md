# util_kit
An essential utility library for Python scripts, offering robust functions for reading YAML configurations, initializing loggers, and parsing command-line arguments.

## Installation
```bash
pip install scriputils
```

## Usage in your Python script
```python
from pathlib import Path
from scriputils import get_config, get_logger, get_kwargs


if __name__ == '__main__':
    # getting default config path
    file_path = Path(__file__)
    config_path = file_path.parent / (file_path.stem + '_config.yaml')
    kwargs = get_kwargs(config_path).parse_args()
    # Read configurations from a YAML file
    
    config = get_config(kwargs.config_path)
    LOGGER = get_logger(
        logger_name=config['logger_name'],
        path=Path("logs"),
        level=kwargs.logger_level,
        add_stdout=False
    )
    LOGGER.info("Logger initialized")
```
