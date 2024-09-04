import os
import unittest

from clear_cache import remove_python_caches

current_dir = os.path.dirname(__file__)

def process_path(directory: str) -> str:
    if directory.startswith(current_dir):
        directory = directory[len(current_dir):]

    directory = directory.replace("\\", ".").replace("/", ".")

    if directory.startswith("."):
        directory = directory[1:]

    while ".." in directory:
        directory = directory.replace("..", ".")

    if not directory.endswith("."):
        directory += "."

    return directory

def register_test(directory: str, suite: unittest.TestSuite, loader: unittest.TestLoader):
    for test_file in os.listdir(directory):
        if test_file.startswith('test') and test_file.endswith('.py'):
            suite.addTests(loader.loadTestsFromName(process_path(directory) + test_file[:-3]))

loader = unittest.TestLoader()
suite = unittest.TestSuite()
module_dir = os.path.join(current_dir, 'modules')
main_test_dir = os.path.join(current_dir, 'tests')

register_test(main_test_dir, suite, loader)

for module_name in os.listdir(module_dir):
    module_path = os.path.join(module_dir, module_name)
    if os.path.isdir(module_path) and not module_name.startswith('__'):
        tests_path = os.path.join(module_path, 'tests')
        if os.path.isdir(tests_path):
            register_test(tests_path, suite, loader)

runner = unittest.TextTestRunner(verbosity=2)
remove_python_caches()
result = runner.run(suite)
