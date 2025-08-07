# Intelligent Travel Planner

An AI-powered travel planning assistant that creates personalized trip itineraries using advanced language models, vector search, and real-time data integration. This system combines conversational AI with comprehensive travel policies and industry expertise to deliver optimized travel experiences.

## Features

### AI-Powered Planning
- **Conversational Interface**: Natural language interaction using Claude (Anthropic) or OpenAI models
- **Context Awareness**: Maintains chat history for coherent multi-turn conversations
- **Intelligent Research**: Automatically searches web and Wikipedia for up-to-date travel information

### Policy-Driven Compliance  
- **Vector Search**: FAISS-powered semantic search through comprehensive travel policies
- **Budget Optimization**: Automatic allocation following industry best practices
- **Risk Management**: Built-in travel insurance and safety protocol recommendations
- **Seasonal Intelligence**: Weather-aware destination recommendations with optimal timing

### Dual Operation Modes
1. **New Plan Creation**: Generate comprehensive itineraries from user preferences
2. **Plan Refinement**: Analyze and optimize existing travel plans for compliance and value

### Real-Time Data Integration
- **Weather API**: OpenWeatherMap integration for climate-based planning
- **Web Search**: DuckDuckGo integration for current travel information
- **Wikipedia Research**: Automated destination and attraction research

## Architecture

### Core Components
- **main.py**: Primary application with conversational interface
- **tools.py**: Modular tool system for search, weather, and file operations
- **policies.txt**: Comprehensive travel policy framework

### Technology Stack
- **AI Framework**: LangChain with tool-calling agents
- **Models**: Claude (Anthropic) and OpenAI support
- **Vector Search**: FAISS with HuggingFace embeddings
- **APIs**: OpenWeatherMap, DuckDuckGo, Wikipedia

## Quick Start

### Prerequisites
- Python 3.8+
- API keys for:
  - Anthropic Claude or OpenAI
  - OpenWeatherMap

### Installation

1. **Clone and setup environment**:
```bash
git clone <repository-url>
cd intelligent-travel-planner
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**:

**IMPORTANT**: You must create a `.env` file with your API keys before running the application.

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your actual API keys
```

Your `.env` file should contain:
```bash
OPENAI_API_KEY="your_openai_api_key_here"
ANTHROPIC_API_KEY="your_anthropic_api_key_here" 
OPENWEATHERMAP_API_KEY="your_openweathermap_api_key_here"
```

**Getting API Keys:**
- **Anthropic Claude**: Sign up at https://console.anthropic.com/
- **OpenAI** (optional): Sign up at https://platform.openai.com/
- **OpenWeatherMap**: Sign up at https://openweathermap.org/api

**Note**: You need either OpenAI OR Anthropic API key (or both). The application defaults to Claude but can use OpenAI if configured.

4. **Run the application**:
```bash
python main.py
```

## Usage

### Creating New Travel Plans
```
How can I help with your travel planning today? 
> I want to plan a tropical winter vacation for 6 friends with a $5000 per person budget

[AI researches policies, weather, and destinations]
[Generates comprehensive travel plan saved to travel_plan.txt]
```

### Refining Existing Plans
```
1. Create suggested_itinerary.txt with your proposed plan
2. Ask the AI: "Please refine my suggested itinerary"
3. AI analyzes against policies and creates refined_travel_plan.txt
```

## Example Use Cases

### Planning a Group Winter Vacation
```
User: "I need to plan a 7-day tropical vacation for 6 friends. Our budget is $5000 per person and we want to travel in January. We love beaches, adventure activities, and cultural experiences."

AI Response: [Researches weather patterns, analyzes budget against policies, recommends Cancun/Riviera Maya with detailed itinerary including Chichen Itza, cenotes, and beachfront accommodations]
```

### Budget-Conscious Solo Travel
```
User: "I'm a solo traveler with a $2500 budget looking for a 10-day cultural immersion experience in Asia during spring. I prefer authentic local experiences over luxury."

AI Response: [Searches policies for economy tier guidelines, analyzes spring weather in Asia, recommends Vietnam or Nepal with detailed budget breakdown and cultural activity suggestions]
```

### Business Travel with Weekend Extension
```
User: "I have a business meeting in London for 3 days but want to extend it into a 7-day European trip. Budget is $4000 total. I'm interested in history and food."

AI Response: [Analyzes transport connections from London, recommends Paris/Amsterdam extension with historical sites, applies business travel policies, suggests optimal train routes]
```

### Family Adventure Planning
```
User: "Planning a 2-week family adventure for 2 adults and 2 teenagers. Budget $6000 per person. We want outdoor activities, wildlife, and educational experiences."

AI Response: [Searches for family-friendly adventure destinations, analyzes group accommodation options, recommends Costa Rica or New Zealand with age-appropriate activities]
```

### Refining an Existing Itinerary
```
User: "I have a rough plan for Bali but want to make sure it follows best practices and fits my budget properly."

AI Response: [Reads suggested_itinerary.txt, analyzes against comprehensive policies, identifies accommodation upgrades needed, optimizes budget allocation, creates refined plan]
```

### Last-Minute Trip Planning
```
User: "I need to book a relaxing vacation for next month. Budget is flexible around $4000. I just want beaches, good food, and minimal planning stress."

AI Response: [Searches current weather conditions, finds destinations with easy logistics, recommends all-inclusive options, applies flexible budget optimization]
```

## Project Structure

```
intelligent-travel-planner/
├── main.py                    # Main application and conversational interface
├── tools.py                   # Tool implementations and vector search
├── policies.txt               # Comprehensive travel policy framework
├── requirements.txt           # Python dependencies
├── .env.example              # Example environment file template
├── .env                       # Environment variables (create from .env.example)
├── travel_plan.txt           # Generated comprehensive travel plans
├── suggested_itinerary.txt   # User-provided plans for refinement
├── refined_travel_plan.txt   # AI-optimized refined plans
└── venv/                     # Virtual environment
```

## How It Works

### New Plan Workflow
1. **Policy Research**: Vector search retrieves relevant travel policies
2. **Weather Analysis**: Real-time weather data for destination recommendations  
3. **Budget Planning**: Automatic allocation (40% accommodation, 30% transport, etc.)
4. **Itinerary Generation**: Comprehensive plan with activities, logistics, and compliance

### Refinement Workflow  
1. **Plan Analysis**: Reads existing itinerary from suggested_itinerary.txt
2. **Policy Compliance**: Checks against comprehensive travel policies
3. **Optimization**: Budget restructuring, accommodation upgrades, timing adjustments
4. **Output**: Refined plan with detailed improvements and compliance notes

## Travel Policy Framework

The system includes comprehensive policies covering:

- **Budget Tiers**: Economy ($1.5-3K), Standard ($3-5K), Premium ($5-8K), Luxury ($8K+)
- **Allocation Rules**: 35-45% accommodation, 25-35% transport, 15-25% food, 10-20% activities
- **Accommodation Standards**: 4.0+ star ratings, WiFi/AC requirements, location proximity
- **Seasonal Planning**: Optimal timing for different destinations and climates
- **Risk Management**: Insurance requirements, passport validity, safety protocols

## Customization

### Adding New Tools
Extend the tools list in tools.py:
```python
def custom_tool_function(query: str) -> str:
    # Your implementation
    return result

custom_tool = Tool(
    name="custom_tool",
    func=custom_tool_function,
    description="Tool description"
)
```

### Modifying Policies
Edit policies.txt to customize:
- Budget frameworks
- Destination criteria  
- Accommodation standards
- Risk management protocols

## Example Outputs

### Generated Travel Plan
- Destination recommendations with weather analysis
- Detailed budget breakdown by category
- Accommodation and transportation options
- Activity suggestions with timing
- Policy compliance verification

### Refined Plan Analysis
- Original plan assessment
- Policy compliance gaps identified
- Budget optimization recommendations
- Accommodation and timing improvements
- Risk management enhancements

## Roadmap & Next Steps

### Upcoming Features

#### Wallet Integration & Secure Verification
- **Crypto Wallet Addon**: Integration with popular crypto wallets for seamless payment processing
- **zkTLS Oracle**: Zero-knowledge proof system for secure user information verification
  - Verify identity without exposing personal data
  - Authenticate travel documents (passport, visa status)
  - Confirm financial capability without revealing account balances

#### Enhanced AI Capabilities
- **Multi-modal Planning**: Image analysis for destination preferences
- **Real-time Pricing**: Dynamic budget optimization with live pricing data
- **Personalization Engine**: Learning user preferences over time
- **Group Consensus**: AI-mediated decision making for group travel

#### Communication & Sharing
- **Gmail Integration**: Automatically share generated travel plans with friends and group members
- **Smart Notifications**: Email updates for booking deadlines, weather changes, and travel alerts
- **Collaborative Planning**: Real-time plan sharing and group feedback collection
- **Calendar Integration**: Automatic calendar event creation for travel activities

#### Advanced Integrations
- **Travel Insurance**: Automated insurance recommendations and claims
- **Carbon Footprint**: Environmental impact tracking and offsetting
- **Local Guides**: Connection with verified local travel experts

### Architecture Evolution
The current system provides a solid foundation for these advanced features:
- **Modular Design**: Easy integration of new tools and APIs
- **Policy Framework**: Extensible for regulatory compliance and verification
- **Vector Search**: Scalable for larger knowledge bases
- **Agent Architecture**: Ready for multi-agent coordination

### Contributing to Development

We welcome contributions to help build the future of AI-powered travel planning:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)  
5. Open Pull Request

**Priority Areas for Contribution:**
- zkTLS integration and privacy-preserving verification
- Wallet connectivity and payment processing
- Gmail API integration for plan sharing and notifications
- Real-time data feeds and pricing APIs
- Enhanced natural language understanding
- Mobile and web interface development

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Acknowledgments

- **LangChain**: Framework for AI agent orchestration
- **Anthropic Claude**: Advanced language model capabilities
- **HuggingFace**: Embedding models for semantic search
- **OpenWeatherMap**: Real-time weather data
- **FAISS**: Efficient vector similarity search

---

**Built for intelligent travel planning**