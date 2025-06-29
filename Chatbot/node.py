from state import State
from model_selector import ModelSelector


def chatbot_node(state: State):
    llm = ModelSelector().get_model(model_type="groq", model_name="compound-beta")
    return {"messages": llm.invoke(state["messages"])}






