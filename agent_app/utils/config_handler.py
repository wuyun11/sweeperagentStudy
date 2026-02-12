"""
配置文件处理
yaml
k : v 格式
"""
import os

import yaml

from agent_app.utils.path_tool import get_abs_path

# 全局变量：定义所有配置文件的绝对路径
config_path = get_abs_path("config")
rag_config_path = os.path.join(config_path, "rag.yml")
chroma_config_path = os.path.join(config_path, "chroma.yml")
prompts_config_path = os.path.join(config_path, "prompts.yml")
agent_config_path = os.path.join(config_path, "agent.yml")

""" 
加载配置文件
:param file_path: 文件路径
:param encoding: 编码
:return: 配置字典
"""
def load_config(file_path: str, encoding="utf-8") -> dict:
    with open(file_path, "r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


""" 
加载rag配置文件
:return: 配置字典
"""
def load_rag_config() -> dict:
    return load_config(rag_config_path)


""" 
加载chroma配置文件
:return: 配置字典
"""
def load_chroma_config() -> dict:
    return load_config(chroma_config_path)


""" 
加载prompts配置文件
:return: 配置字典
"""
def load_prompts_config() -> dict:
    return load_config(prompts_config_path)


""" 
加载agent配置文件
:return: 配置字典
"""
def load_agent_config() -> dict:
    return load_config(agent_config_path)

""" 
全局变量：定义所有配置文件的配置字典
"""
rag_config = load_rag_config()
chroma_config = load_chroma_config()
prompts_config = load_prompts_config()
agent_config = load_agent_config()
