"""
    ToDo: DocString
"""
import sys
from pathlib import Path


ROOT_DIRECTORY = str(Path(__file__).parents[5])
sys.path.append(f"{ROOT_DIRECTORY}/src/")
