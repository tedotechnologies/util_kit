# tests/test_utils.py
import unittest
import tempfile
import logging
import yaml
from pathlib import Path
from scrip_utils import get_config, get_logger, get_kwargs


class TestUtils(unittest.TestCase):

    def test_get_config(self):
        # Создание временного YAML файла
        with tempfile.NamedTemporaryFile('w', delete=False,
                                         suffix='.yaml') as temp_file:
            yaml_content = {
                'key1': 'value1',
                'key2': {
                    'subkey1': 'subvalue1'
                }
            }
            yaml.dump(yaml_content, temp_file)
            temp_file_path = Path(temp_file.name)

        # Тестирование функции get_config
        config = get_config(temp_file_path)
        self.assertEqual(config['key1'], 'value1')
        self.assertEqual(config['key2']['subkey1'], 'subvalue1')

        # Удаление временного файла
        temp_file_path.unlink()

    def test_get_logger(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            logger = get_logger(logger_name='test_logger', path=temp_dir_path,
                                level=logging.DEBUG)

            self.assertEqual(logger.name, 'test_logger')
            self.assertEqual(logger.level, logging.DEBUG)

            # Проверка создания лог файла
            log_file = temp_dir_path / 'test_logger.log'
            self.assertTrue(log_file.exists())

            # Проверка записи логов
            logger.debug('This is a debug message')
            with open(log_file, 'r') as f:
                log_content = f.read()
            self.assertIn('This is a debug message', log_content)

    def test_get_kwargs(self):
        default_config_path = Path('/path/to/default/config.yaml')
        parser = get_kwargs(default_config_path)

        args = parser.parse_args([])
        self.assertEqual(args.config_path, default_config_path)
        self.assertEqual(args.logger_level, 20)

        args = parser.parse_args(
            ['-p', '/custom/path/config.yaml', '-l', '10']
        )
        self.assertEqual(args.config_path, Path('/custom/path/config.yaml'))
        self.assertEqual(args.logger_level, 10)


if __name__ == '__main__':
    unittest.main()
