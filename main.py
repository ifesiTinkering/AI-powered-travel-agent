import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool, weather_tool, policies_tool, read_itinerary_tool, refine_plan_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    

llm = ChatAnthropic(model="claude-opus-4-1-20250805")
# response = llm.invoke("What is the capital of France?")
# print(response)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert travel planning assistant specializing in creating personalized trip itineraries.
            
            Your expertise includes:
            - Analyzing weather patterns and seasonal travel conditions
            - Budget optimization and cost breakdown analysis
            - Destination recommendations based on activities, climate, and preferences
            - Group travel logistics and accommodation planning
            - Activity and attraction research with timing recommendations
            - Travel plan refinement and policy compliance analysis
            
            CAPABILITIES:
            1. CREATE NEW PLANS: Research and create comprehensive travel itineraries from scratch
            2. REFINE EXISTING PLANS: Analyze and improve user-provided travel plans for policy compliance
            
            FOR NEW TRAVEL PLANS, follow this process:
            1. Search your travel policies to understand budget constraints and preferences
            2. Research weather conditions for potential destinations during travel dates
            3. Find destinations that match the weather, budget, and activity requirements
            4. Create detailed budget breakdowns following policy guidelines
            5. Recommend specific accommodations, activities, and logistics
            6. Save comprehensive travel plans using create_travel_plan_file
            
            FOR TRAVEL PLAN REFINEMENT:
            1. Use read_suggested_itinerary to analyze user's existing plan in 'suggested_itinerary.txt'
            2. Compare against your travel policies for compliance gaps
            3. Use refine_travel_plan to create an optimized version with improvements
            4. Provide detailed analysis of changes and policy compliance
            
            Focus ONLY on travel planning. Politely redirect non-travel queries to travel-related topics.
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

tools = [search_tool, wiki_tool, save_tool, weather_tool, policies_tool, read_itinerary_tool, refine_plan_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print("🌍 Welcome to your Personal Travel Planning Assistant! 🌍")
print("I specialize in creating customized trip itineraries based on weather, budget, and your preferences.")
print("Type 'quit', 'exit', or 'done' to end our session.\n")

chat_history = []

while True:
    query = input("✈️ How can I help with your travel planning today? ")
    
    # Check for exit commands
    if query.lower().strip() in ['quit', 'exit', 'done', 'no', 'goodbye', 'bye']:
        print("🎉 Happy travels! Feel free to return anytime for more trip planning assistance!")
        break
    
    if not query.strip():
        continue
    
    try:
        # Include chat history in the agent call
        response = agent_executor.invoke({
            "query": query,
            "chat_history": chat_history
        })
        
        print(f"\n{response['output']}\n")
        
        # Add to chat history for context
        chat_history.extend([
            f"Human: {query}",
            f"Assistant: {response['output']}"
        ])
        
        # Keep chat history manageable (last 10 exchanges)
        if len(chat_history) > 20:
            chat_history = chat_history[-20:]
            
        # Ask if they need more help
        more_help = input("Is there anything else I can help you plan for your travels? (yes/no): ").lower().strip()
        if more_help in ['no', 'n', 'done', 'nope', 'quit', 'exit']:
            print("🎉 Happy travels! Feel free to return anytime for more trip planning assistance!")
            break
        
    except KeyboardInterrupt:
        print("\n🎉 Happy travels! Feel free to return anytime for more trip planning assistance!")
        break
    except Exception as e:
        print(f"I encountered an error: {e}")
        print("Let's try again with your travel planning question.")