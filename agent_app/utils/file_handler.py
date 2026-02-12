"""
文件处理工具
"""

import hashlib
import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

from agent_app.utils.logger_handler import logger

"""
获取文件的MD5值
:param file_path: 文件路径
:return: 文件的MD5值
"""


def get_file_md5_hex(file_path: str) -> str | None:
    if not os.path.exists(file_path):
        logger.error(f"[md5计算]文件不存在: {file_path}")
        return None
    if not os.path.isfile(file_path):
        logger.error(f"[md5计算]文件路径不是文件: {file_path}")
        return None
    md5_obj = hashlib.md5()

    chunk_size = 4096

    try:
        with open(file_path, "rb") as f:
            """
            chunk = f.read(chunk_size)
            while chunk:
                md5_obj.update(chunk)
                chunk = f.read(chunk_size)
            """
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"[md5计算]文件计算md5值失败: {str(e)}")
        return None


""" 
列出指定目录下所有允许的文件
:param dir_path: 目录路径
:param allowed_type: 允许的文件类型
:return: 文件列表
"""


def list_dir_with_allowed_type(dir_path: str, allowed_type: tuple[str, ...]) -> tuple[str, ...]:
    files: list[str] = []
    if not os.path.isdir(dir_path):
        logger.error(f"[文件列表]目录不存在: {dir_path}")
        return tuple()
    for f in os.listdir(dir_path):
        if f.endswith(allowed_type):
            files.append(os.path.join(dir_path, f))
    return tuple(files)


""" 
加载pdf文件
:param file_path: 文件路径
:param password: 密码
:return: Document列表
"""


def pdf_loader(file_path: str, password: str = None) -> list[Document]:
    return PyPDFLoader(file_path, password=password).load()


""" 
加载txt文件
:param file_path: 文件路径
:return: Document列表
"""


def txt_loader(file_path: str, encoding: str = "utf-8") -> list[Document]:
    return TextLoader(file_path, encoding=encoding).load()
