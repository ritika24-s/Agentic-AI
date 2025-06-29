from state import State
from model_selector import ModelSelector
from tools.custom_tools import multiply
from tools.tavily import TavilyTool
from tools.tools import get_tools

from config import load_config


llm = ModelSelector().get_model(model_type="groq", model_name="compound-beta")



def chatbot_node(state: State):
    return {"messages": llm.invoke(state["messages"])}


def bind_llm_with_tools():
    tools = get_tools()
    llm_with_tool = llm.bind_tools(tools)
    return llm_with_tool


llm_with_tool = bind_llm_with_tools()


def tools_node(state:State):
    return {"messages":[llm_with_tool.invoke(state["messages"])]}