import subprocess
import os

project_path = "/Users/francescapanteli/Desktop/CodingNomads-python-301"

# Path to PyCharm app (adjust if your version is different)
pycharm_app_path = "/Applications/PyCharm.app"

# Open the project
subprocess.run(["open", "-a", pycharm_app_path, project_path])