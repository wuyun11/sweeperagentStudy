"""
配置文件处理
yaml
k : v 格式
"""
import os

import yaml

from path_tool import get_abs_path

# 全局变量：定义所有配置文件的绝对路径
config_path = get_abs_path("config")
rag_config_path = os.path.join(config_path, "rag.yml")
chroma_config_path = os.path.join(config_path, "chroma.yml")
prompts_config_path = os.path.join(config_path, "prompts.yml")
agent_config_path = os.path.join(config_path, "agent.yml")


def load_config(file_path: str, encoding="utf-8") -> dict:
    with open(file_path, "r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def load_rag_config() -> dict:
    return load_config(rag_config_path)


def load_chroma_config() -> dict:
    return load_config(chroma_config_path)


def load_prompts_config() -> dict:
    return load_config(prompts_config_path)


def load_agent_config() -> dict:
    return load_config(agent_config_path)

rag_config = load_rag_config()
chroma_config = load_chroma_config()
prompts_config = load_prompts_config()
agent_config = load_agent_config()
