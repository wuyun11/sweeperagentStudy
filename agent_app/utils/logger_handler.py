"""
日志工具
"""
import logging
import os
import sys
from datetime import datetime

from agent_app.utils.path_tool import get_abs_path

# 日志保存的根目录
LOG_ROOT_DIR = get_abs_path("logs")

# 确保日志的文件存在
os.makedirs(LOG_ROOT_DIR, exist_ok=True)

# 控制台按级别着色（ANSI 码，Windows 10+ / 现代终端均支持）
_COLORS = {
    logging.DEBUG: "\033[36m",    # 青色
    logging.INFO: "\033[0m",      # 默认（黑/白）
    logging.WARNING: "\033[33m",  # 黄色
    logging.ERROR: "\033[31m",    # 红色
    logging.CRITICAL: "\033[35m", # 紫红
}
_RESET = "\033[0m"


class ColoredConsoleFormatter(logging.Formatter):
    """控制台用：按日志级别给整行上色。"""

    def format(self, record: logging.LogRecord) -> str:
        raw = super().format(record)
        color = _COLORS.get(record.levelno, _RESET)
        return f"{color}{raw}{_RESET}"


# 日志格式（文件用纯文本，控制台用彩色）
LOG_FMT = "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
DEFAULT_LOG_FORMAT = logging.Formatter(LOG_FMT)

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

    # 输出到 stdout，避免 PyCharm 把 stderr 整段标红；颜色由 ANSI 码控制
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(ColoredConsoleFormatter(LOG_FMT))

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


"""  
全局变量：定义日志记录器
"""
logger = get_logger()
