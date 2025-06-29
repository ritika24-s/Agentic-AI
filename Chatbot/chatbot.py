from graph import ChatbotGraphBuilder
from node import chatbot_node


def run_chatbot():    
    graph_builder = ChatbotGraphBuilder()
    graph_builder.add_node("llm_chatbot", chatbot_node)
    graph_builder.add_start_edge("llm_chatbot")
    graph_builder.add_end_edge("llm_chatbot")
    graph = graph_builder.compile_graph()
    graph_builder.visualize_graph()
    result = graph_builder.run_graph({"messages":"Hi"})
    print(result["messages"][-1].content)




