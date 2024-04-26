import os
import pkg_resources

# Get the installation directory of the package
package_path = pkg_resources.resource_filename("legent", "")
# Construct the path to the resource
resource_path = os.path.join(package_path, os.pardir, ".legent")
resource_path = os.path.abspath(resource_path)

ENV_FOLDER = f"{resource_path}/env"
ENV_DATA_FOLDER = f"{ENV_FOLDER}/env_data"
CLIENT_FOLDER = f"{ENV_FOLDER}/client"
SCENES_FOLDER = f"{resource_path}/scenes"
TASKS_FOLDER = f"{resource_path}/tasks"
DATASET_FOLDER = f"{resource_path}/dataset"
MODEL_FOLDER = f"{resource_path}/models"
EVAL_FOLDER = f"{resource_path}/eval"
ROOM_NUM = 2

# OpenAI
OPENAI_API_KEY = None
OPENAI_BASE_URL = None
MODEL_CHAT = 'gpt-4',  # 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'gpt-4-32k'
MODEL_VISION_PREVIEW = 'gpt-4-vision-preview'
