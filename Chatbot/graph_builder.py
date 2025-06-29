from langgraph.prebuilt import ToolNode, tools_condition

from base_graph import ChatbotGraphBuilder
from node import chatbot_node, tools_node
from tools.tools import get_tools


def run_chatbot():    
    graph_builder = ChatbotGraphBuilder()
    graph_builder.add_node("llm_chatbot", chatbot_node)
    graph_builder.add_start_edge("llm_chatbot")

    graph_builder.add_end_edge("llm_chatbot")
    graph = graph_builder.compile_graph()
    graph_builder.visualize_graph()
    result = graph_builder.run_graph({"messages":"what is the recent news about AI? "})
    print(result["messages"][-1].content)


def run_tool_calling_llm():
    tools = get_tools()

    # Graph builder
    graph_builder = ChatbotGraphBuilder()
    # Add nodes
    graph_builder.add_node("tool_calling_llm", tools_node)
    graph_builder.add_node("tools", ToolNode(tools))

    # Add edges
    graph_builder.add_start_edge("tool_calling_llm")
    graph_builder.add_condition(
        "tool_calling_llm",
        # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
        # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
        tools_condition
    )
    graph_builder.add_end_edge("tools")

    # compile graph
    graph = graph_builder.compile_graph()
    graph_builder.visualize_graph()
    data = {"messages":"what is 5 multiplied by 2?"}
    result = graph_builder.get_result(data=data)


def react_agent_architecture():
    tools = get_tools()

    # Graph builder
    graph_builder = ChatbotGraphBuilder()
    # Add nodes
    graph_builder.add_node("tool_calling_llm", tools_node)
    graph_builder.add_node("tools", ToolNode(tools))

    # Add edges
    graph_builder.add_start_edge("tool_calling_llm")
    graph_builder.add_condition(
        "tool_calling_llm",
        # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
        # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
        tools_condition
    )
    graph_builder.add_edge("tools","tool_calling_llm")

    # compile graph
    graph = graph_builder.compile_graph()
    graph_builder.visualize_graph()
    data = {"messages":"what is 5 multiplied by 2?"}
    result = graph_builder.get_result(data=data)


def agent_with_memory():
    graph_builder = ChatbotGraphBuilder(memory=True)
    graph_builder.add_node("llm_chatbot", chatbot_node)
    graph_builder.add_start_edge("llm_chatbot")

    graph_builder.add_end_edge("llm_chatbot")

    graph = graph_builder.compile_graph()
    graph_builder.visualize_graph()
    config={"configurable":{"thread_id":"1"}}
    result = graph_builder.get_result(data={"messages":"Hi my name is Ritika "}, config=config)
    print(result)