
"""
Simple agent using LangGraph which is given a tool
"""
from tools import get_geolocation, get_today_weather
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="gpt-4o",
    tools=[get_geolocation, get_today_weather],
    prompt="You are a helpful assistant that only uses tools at your disposal as it is always right"
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather like of Karachi? If you used a tool then tell me when you used the tool and how you used it and what was the input and output of that tool"}]}
)

print(result['messages'][-1].content)
