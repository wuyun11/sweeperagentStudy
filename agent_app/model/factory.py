from abc import ABC, abstractmethod
from typing import Optional

from langchain_community.chat_models.tongyi import BaseChatModel, ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.embeddings import Embeddings
from langchain_ollama import OllamaEmbeddings

from agent_app.utils.config_handler import rag_config

"""  
抽象模型工厂类
"""
class BaseModelFactory(ABC):
    @abstractmethod
    def generate_model(self) -> Optional[Embeddings | BaseChatModel]:
        pass

"""  
聊天模型工厂类
"""
class ChatModelFactory(BaseModelFactory):
    def generate_model(self) -> ChatTongyi:
        return ChatTongyi(model=rag_config["chat_model_name"])


"""  
嵌入模型工厂类
"""
class EmbeddingModelFactory(BaseModelFactory):
    def generate_model(self) -> DashScopeEmbeddings:
        return DashScopeEmbeddings(model=rag_config["embedding_model_name"])

"""  
本地嵌入模型工厂类
"""
class OllamaEmbeddingsModelFactory(BaseModelFactory):
    def generate_model(self) -> OllamaEmbeddings:
        return OllamaEmbeddings(model=rag_config["local_embedding_model_name"])
        
"""
全局变量：定义所有模型
"""
chat_model: ChatTongyi = ChatModelFactory().generate_model()
embedding_model: DashScopeEmbeddings = EmbeddingModelFactory().generate_model()
ollama_embedding_model: OllamaEmbeddings = OllamaEmbeddingsModelFactory().generate_model()