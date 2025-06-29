from tools.custom_tools import multiply
from tools.tavily import TavilyTool


class ToolsManager:
    def __init__(self):
        self.tools = []

    def get_tools(self)-> list:
        print(self.tools)
        return self.tools
    
    def add_tools(self, tool)-> None:
        self.tools.append(tool)


def get_tools()-> list:
    tools_manager = ToolsManager()
    tavily_tool = TavilyTool()
    tools_manager.add_tools(tavily_tool.tavily_search)
    tools_manager.add_tools(multiply)
    return tools_manager.get_tools()




