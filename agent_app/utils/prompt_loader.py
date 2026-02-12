from agent_app.utils.config_handler import prompts_config
from agent_app.utils.path_tool import get_abs_path
from agent_app.utils.logger_handler import logger

"""
根据配置项加载提示词文件
:param config_key: 配置中的路径键名（如 main_prompt_path）
:param prompt_name: 提示词名称，用于日志（如「系统提示词」）
:return: 提示词内容
"""
def load_prompt(config_key: str, prompt_name: str) -> str:
    try:
        prompt_path = get_abs_path(prompts_config[config_key])
    except KeyError as e:
        logger.error(f"[提示词加载]在配置文件中未找到{config_key}配置项: {str(e)}")
        raise e
    try:
        return open(prompt_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[提示词加载]加载{prompt_name}失败: {str(e)}")
        raise e

"""
加载系统提示词
:return: 系统提示词
"""
def load_system_prompt() -> str:
    return load_prompt("main_prompt_path", "系统提示词")

"""
加载 rag 总结提示词
:return: rag 总结提示词
"""
def load_rag_summarize_prompt() -> str:
    return load_prompt("rag_summarize_prompt_path", "rag总结提示词")

"""
加载报告提示词
:return: 报告提示词
"""
def load_report_prompt() -> str:
    return load_prompt("report_prompt_path", "报告提示词")
