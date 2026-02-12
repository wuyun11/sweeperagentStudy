"""
路径工具

为整个工程提供统一的绝对路径
"""
import os

"""
获取工程所在的根目录
:return: 字符串根目录
"""
def get_project_path() -> str:
    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前文件所在目录
    current_dir = os.path.dirname(current_file_path)
    # 获取当前目录的父目录
    parent_dir = os.path.dirname(current_dir)
    # 获取父目录的父目录
    project_path = os.path.dirname(parent_dir)
    return project_path

"""
获取相对路径的绝对路径
:param relative_path: 相对路径
:return: 绝对路径
"""
def get_abs_path(relative_path: str) -> str:
    project_path = get_project_path()
    return os.path.normpath(os.path.join(project_path, relative_path))
