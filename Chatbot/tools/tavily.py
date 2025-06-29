from langchain_tavily import TavilySearch


class TavilyTool:
    def __init__(self):
        self.tavily_search = TavilySearch(max_results=2)

    def invoke(self, query: str):
        return self.tavily_search.invoke(query)
