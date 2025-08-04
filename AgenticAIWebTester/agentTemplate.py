from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import asyncio
import os


def main():
    from brightdataagenttemplate import BrightDataAgentTemplate
    bright_data = BrightDataAgentTemplate()


def run_agent(description, expected_results):
    results = asyncio.run(chat_with_agent_2(description,expected_results))
    return results

async def chat_with_agent():
    load_dotenv()
    model = ChatAnthropic(model_name="claude-3-5-sonnet-20240620")

    # tools used is bright data mcp, specify the commands to load mcp client within python script with our agent, similar to what was done in the claude desktop app
    server_params = StdioServerParameters(
        command="npx",
        env={
            "API_TOKEN": os.getenv("API_TOKEN"),
            "BROWSER_AUTH": os.getenv("BROWSER_AUTH"),
            "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
        },
        # make sure to update the full absolute path to your math_server.py file
        args=["@brightdata/mcp"],
    )
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model,tools)

            #start conversation history
            #encourages agent to use multiple of the tools
            messages = [
                {
                    "role": "system",
                    "content": "You can use multiple tools in sequence to answer complex questions. Think step by step. Act as if your a QA Tester"
                }
            ]



            print("Type 'exit' or 'quit' to end the chat.")
            while True:
                user_input=input("\nYou: ")
                if user_input.strip().lower() in {"exit", "quit"}:
                    print("Goodbye!")
                    break
                #add user history (adding more context)
                messages.append({"role": "user", "content": user_input})

                #call the agent
                agent_response = await agent.ainvoke({"messages": messages})

                #extract agents reply and add to history
                ai_message = agent_response["messages"][-1].content
                print(f"Agent: {ai_message}")


async def chat_with_agent_2(description, expected_results):
    load_dotenv()
    model = ChatAnthropic(model_name="claude-3-5-sonnet-20240620")

    # tools used is bright data mcp, specify the commands to load mcp client within python script with our agent, similar to what was done in the claude desktop app
    server_params = StdioServerParameters(
        command="npx",
        env={
            "API_TOKEN": os.getenv("API_TOKEN"),
            "BROWSER_AUTH": os.getenv("BROWSER_AUTH"),
            "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
        },
        # make sure to update the full absolute path to your math_server.py file
        args=["@brightdata/mcp"],
    )
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model,tools)

            #start conversation history
            #encourages agent to use multiple of the tools
            messages = [
                {
                    "role": "system",
                    "content": "You can use multiple tools in sequence to answer complex questions. Think step by step. After each answer determine if its PASS or FAIL or UNDETERMINED and print it as a seperate response"
                }
            ]


            user_input= "Description: " + description + " Expected results: " + expected_results
            if user_input.strip().lower() in {"exit", "quit"}:
                print("Goodbye!")

            #add user history (adding more context)
            messages.append({"role": "user", "content": user_input})

            #call the agent
            agent_response = await agent.ainvoke({"messages": messages})

            #extract agents reply and add to history
            ai_message = agent_response["messages"][-1].content
            print(f"Agent: {ai_message}")
            return ai_message

if __name__ == '__main__':
    main()