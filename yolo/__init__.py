# MODULE_PATH = "/Users/antonoeschmidt/PycharmProjects/solitaire-yolo/__init__.py"
MODULE_PATH = "/home/antonio/solitaire-yolo/__init__.py"
MODULE_NAME = "card1"
import importlib.util
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
from card1 import card