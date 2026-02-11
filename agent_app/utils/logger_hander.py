"""
日志工具
"""
import logging
import os
from datetime import datetime

from path_tool import get_abs_path

# 日志保存的根目录
LOG_ROOT_DIR = get_abs_path("logs")

# 确保日志的文件存在
os.makedirs(LOG_ROOT_DIR, exist_ok=True)

# 日志的格式配置
DEFAULT_LOG_FORMAT = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)

"""
获取日志记录器
:param name: 日志记录器名称
:param console_level: 控制台日志级别
:param file_level: 文件日志级别
:param log_file: 日志文件路径
:return: 日志记录器
"""


def get_logger(
        name: str = "agent",
        console_level: int = logging.INFO,
        file_level: int = logging.DEBUG,
        log_file=None,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 避免重复添加Handler
    if logger.handlers:
        return logger

    # 添加控制台Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(console_handler)

    # 添加文件Handler
    if not log_file:
        # 默认文件名：name_年月日.log
        log_file = os.path.join(LOG_ROOT_DIR, f"{name}_{datetime.now().strftime('%Y%m%d')}.log")

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(file_handler)

    return logger


logger = get_logger()
