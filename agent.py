
"""
Simple agent using LangGraph which is given a tool
"""

from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always cold in {city}! 365 days a year"

agent = create_react_agent(
    model="gpt-4o",  
    tools=[get_weather],  
    prompt="You are a helpful assistant that only uses one of the tools at your disposal as it is always right."  
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in Brisbane"}]}
)

print(result['messages'][-1].content)
