import pathlib
from loguru import logger

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG_FOLDER = PROJECT_ROOT.joinpath("logs")
LOG_FILE = LOG_FOLDER.joinpath("project_log.log")

# Ensure the log folder exists
LOG_FOLDER.mkdir(exist_ok=True)

# Configure Loguru
logger.add(LOG_FILE, level="INFO")

# Optionally, you can also log to the console
# logger.add(sys.stderr, level="DEBUG")

logger.info("Logger is ready to use.")
