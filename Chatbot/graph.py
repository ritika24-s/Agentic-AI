from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display
from state import State

class ChatbotGraphBuilder:
    """
    This class is used to build the chatbot graph.
    """
    def __init__(self):
        self.state = State()
        self.graph_builder = StateGraph(State)
        self.graph = None
    
    def add_node(self, node_name:str, node)-> None:
        self.graph_builder.add_node(node_name, node)
    
    def add_edge(self, node_from:str, node_to:str):
        self.graph_builder.add_edge(node_from, node_to)
    
    def add_start_edge(self, node_name:str)-> None:
        self.graph_builder.add_edge(START, node_name)
    
    def add_end_edge(self, node_name:str)-> None:
        self.graph_builder.add_edge(node_name, END)

    def compile_graph(self):
        self.graph = self.graph_builder.compile()
        return self.graph

    def visualize_graph(self):
        try:
            return display(Image(self.graph.get_graph().draw_mermaid_png()))
        except Exception as e:
            print(f"Error visualizing graph: {e}")
            return None
        
    def run_graph(self, data: dict):
        return self.graph.invoke(data)
