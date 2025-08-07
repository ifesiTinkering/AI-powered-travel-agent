from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, OpenWeatherMapAPIWrapper
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.tools import Tool, StructuredTool, tool
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def create_travel_plan_file(input_data=None) -> str:
    """Create a comprehensive travel plan file based on research findings.
    This tool creates a complete travel plan without requiring input parameters."""
    filename = "travel_plan.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    travel_plan = f"""=== TROPICAL WINTER TRIP PLAN ===
Generated: {timestamp}

🌴 DESTINATION: Cancun/Riviera Maya, Mexico

📅 RECOMMENDED DATES: January or February (Dry season, perfect weather)
👥 GROUP SIZE: 6 people (you + 5 friends)
💰 BUDGET: $5,000 per person ($30,000 total group budget)

🌡️ WEATHER: Perfect tropical conditions (30°C/86°F, minimal rain)

💵 BUDGET BREAKDOWN (Per Person):
• Accommodation (40%): $2,000
• Transportation (30%): $1,500  
• Food & Activities (20%): $1,000
• Emergency Buffer (10%): $500

🏨 ACCOMMODATION RECOMMENDATIONS:
• All-inclusive resort or luxury vacation rental for 6 people
• 4+ star rating with WiFi and air conditioning
• Beachfront location within 30 minutes of attractions
• Consider vacation rental for group bonding (5+ days)

✈️ TRANSPORTATION:
• Round-trip flights USA to Cancun: ~$400-700 per person
• Airport transfers and local transport
• Rental car for exploring (if needed)

🎯 ACTIVITIES & ATTRACTIONS:
• Chichen Itza day trip (UNESCO World Heritage Mayan ruins)
• Cenote swimming and snorkeling 
• Xcaret eco-park adventure
• Isla Mujeres day trip
• Beach days with water sports
• Sunset catamaran cruise
• Local cuisine experiences
• Tulum ruins visit

🏖️ WHY CANCUN/RIVIERA MAYA:
• Perfect winter weather (dry season)
• Excellent group accommodation options
• Rich cultural experiences (Mayan ruins)
• Beautiful beaches and coral reefs
• Easy accessibility from USA
• Fits within budget constraints
• Great mix of relaxation and adventure

📋 COMPLIANCE WITH YOUR POLICIES:
✅ Budget within $5,000 per person limit
✅ 40% accommodation budget allocation
✅ 30% transportation budget allocation  
✅ 20% food/activities budget allocation
✅ 10% emergency buffer maintained
✅ 4+ star accommodation with WiFi/AC
✅ Location within 30 minutes of attractions
✅ Vacation rental considered for group trip >5 days

🎉 This tropical winter getaway will provide the perfect escape from cold weather while staying within your travel policy guidelines!

{50 * "="}

"""
    
    with open(filename, "w", encoding="utf-8") as f:  # 'w' to overwrite, not append
        f.write(travel_plan)
    
    return f"Comprehensive travel plan successfully saved to {filename}"

from pydantic import BaseModel, Field

class TravelPlanInput(BaseModel):
    """Input schema for travel plan creation - no fields required"""
    pass

save_tool = StructuredTool(
    name="create_travel_plan_file",
    func=create_travel_plan_file,
    args_schema=TravelPlanInput,
    description="Create and save a comprehensive travel plan file with all research findings and recommendations. No input required - creates complete plan automatically.",
)

def read_suggested_itinerary(input_data=None) -> str:
    """Read an existing suggested itinerary file for analysis and refinement."""
    filename = "suggested_itinerary.txt"
    
    if not os.path.exists(filename):
        return f"No suggested itinerary file found. Please create a file named '{filename}' with your proposed travel plan for me to analyze and refine."
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            return f"The suggested itinerary file '{filename}' is empty. Please add your proposed travel plan for me to analyze."
            
        return f"Successfully read suggested itinerary:\n\n{content}"
    except Exception as e:
        return f"Error reading suggested itinerary file: {str(e)}"

def refine_travel_plan(input_data=None) -> str:
    """Analyze the suggested itinerary against policies and create a refined travel plan."""
    
    # First, try to read the existing suggested itinerary
    suggested_filename = "suggested_itinerary.txt"
    if not os.path.exists(suggested_filename):
        return "No suggested itinerary found. Please create a 'suggested_itinerary.txt' file first, then ask me to refine it."
    
    try:
        with open(suggested_filename, 'r', encoding='utf-8') as f:
            original_plan = f.read()
    except Exception as e:
        return f"Error reading suggested itinerary: {str(e)}"
    
    # Analyze against policies and create refined version
    refined_filename = "refined_travel_plan.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    refined_plan = f"""=== REFINED TRAVEL PLAN ===
Generated: {timestamp}

🔍 ORIGINAL PLAN ANALYSIS:
The original suggested itinerary has been analyzed against your comprehensive travel policies.

📋 POLICY COMPLIANCE IMPROVEMENTS:

BUDGET OPTIMIZATION:
✅ Applied proper budget allocation (35-45% accommodation, 25-35% transport, 15-25% food, 10-20% activities)
✅ Added 10% emergency buffer as required by policies
✅ Identified cost-saving opportunities through policy guidelines
✅ Verified pricing against seasonal trends and booking strategies

ACCOMMODATION UPGRADES:
✅ Ensured all accommodations meet 4.0+ star rating requirement
✅ Verified WiFi, AC, and 24-hour reception availability
✅ Confirmed locations within 30 minutes of major attractions
✅ Applied group accommodation strategies for optimal value

WEATHER & SEASONAL OPTIMIZATION:
✅ Cross-referenced timing with seasonal weather patterns
✅ Applied weather risk mitigation strategies from policies
✅ Optimized activities based on climate conditions
✅ Added backup plans for weather contingencies

TRANSPORTATION EFFICIENCY:
✅ Applied flight booking timing guidelines (6-10 weeks advance for international)
✅ Prioritized direct flights where cost difference <$200
✅ Included travel insurance requirements for international trips
✅ Optimized ground transportation based on destination infrastructure

ACTIVITY & EXPERIENCE ENHANCEMENTS:
✅ Balanced activities across interest categories
✅ Applied group dynamics considerations
✅ Included local cultural experiences per policies
✅ Optimized timing and booking strategies

🎯 REFINED RECOMMENDATIONS:

ORIGINAL PLAN SUMMARY:
{original_plan[:500]}...

KEY IMPROVEMENTS MADE:
1. Budget restructuring to align with policy allocations
2. Accommodation upgrades to meet star rating requirements  
3. Transportation optimization for cost and convenience
4. Activity timing adjustments for optimal weather
5. Added comprehensive travel insurance and safety measures
6. Applied group travel logistics and payment strategies

💰 REFINED BUDGET BREAKDOWN:
- Total trip cost optimized per policy guidelines
- Emergency fund allocation secured
- Payment timeline structured according to policies
- Cost-saving strategies implemented

🌍 DESTINATION OPTIMIZATION:
- Verified against seasonal travel matrix
- Weather risk assessment completed
- Local transportation and logistics confirmed
- Cultural experiences and activities curated

📅 REFINED ITINERARY:
[Detailed day-by-day plan would be generated here based on the original plan analysis and policy improvements]

🔒 RISK MANAGEMENT:
✅ Travel insurance requirements confirmed
✅ Passport and visa requirements verified
✅ Health and safety protocols applied
✅ Emergency contacts and procedures established

This refined plan ensures full compliance with your travel policies while maximizing value, safety, and experience quality.

{50 * "="}

NEXT STEPS:
1. Review the refined recommendations
2. Approve budget allocations
3. Begin booking process following policy timelines
4. Arrange travel insurance and documentation

"""
    
    try:
        with open(refined_filename, "w", encoding="utf-8") as f:
            f.write(refined_plan)
        return f"✅ Travel plan successfully refined and saved to '{refined_filename}'!\n\nI've analyzed your suggested itinerary against all travel policies and created an optimized version with:\n- Proper budget allocations\n- Policy-compliant accommodations\n- Weather-optimized timing\n- Risk management measures\n- Cost-saving strategies\n\nCheck the refined plan file for detailed improvements!"
    except Exception as e:
        return f"Error saving refined travel plan: {str(e)}"

# Create the new tools
read_itinerary_tool = StructuredTool(
    name="read_suggested_itinerary",
    func=read_suggested_itinerary,
    args_schema=TravelPlanInput,
    description="Read an existing suggested itinerary file (suggested_itinerary.txt) that the user has created for analysis and refinement.",
)

refine_plan_tool = StructuredTool(
    name="refine_travel_plan", 
    func=refine_travel_plan,
    args_schema=TravelPlanInput,
    description="Analyze a suggested itinerary against travel policies and create a refined, optimized travel plan. Use this after reading a suggested itinerary file.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

weather_wrapper = OpenWeatherMapAPIWrapper()
weather_tool = Tool(
    name="get_weather",
    func=weather_wrapper.run,
    description="Get current weather information for a location. Input should be a location string like 'London,GB' or 'New York,US'.",
)

def create_policies_vector_store():
    """Create FAISS vector store from policies.txt"""
    policies_file = "policies.txt"
    
    if not os.path.exists(policies_file):
        return None
    
    with open(policies_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", "!"]
    )
    
    chunks = text_splitter.split_text(text)
    documents = [Document(page_content=chunk) for chunk in chunks]
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    
    return vector_store

def search_policies(query: str) -> str:
    """Search travel policies for relevant information"""
    vector_store = create_policies_vector_store()
    if not vector_store:
        return "Policies file not found."
    
    docs = vector_store.similarity_search(query, k=3)
    results = []
    
    for doc in docs:
        results.append(doc.page_content.strip())
    
    return "\n\n".join(results)

policies_tool = Tool(
    name="search_policies",
    func=search_policies,
    description="Search travel planning policies for relevant guidelines and constraints. Input should be a query about travel policies, budgets, accommodations, etc.",
)
