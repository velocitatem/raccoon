# create a langchain implementation which can visit websites
# and extract text from them


from langchain.utilities import RequestsWrapper, BashProcess
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

# load the tools


tools = load_tools(["requests", "terminal"], llm=llm)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run("http://localhost:3000/exp use this resource to find out: what is the square root of 2?")
