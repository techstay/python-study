# %%
import logging
from pathlib import Path

# 创建Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建Handler

# 终端Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 文件Handler
logger_file = Path("log.log")
file_handler = logging.FileHandler(logger_file, mode="w")
file_handler.setLevel(logging.NOTSET)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加到Logger中
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# %%
# 打印日志
logger.debug("debug 信息")
logger.info("info 信息")
logger.warning("warn 信息")
logger.error("error 信息")
logger.critical("critical 信息")
logger.debug("%s 是自定义信息" % "这些东西")

# %%

# shutdown logger and then delete the logging file
logging.shutdown()
logger_file.unlink()

# %%
