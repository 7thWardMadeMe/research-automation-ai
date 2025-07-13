# AI Research & Analysis Assistant 🔍📊

> Your personal AI researcher that conducts comprehensive web research, analyzes data, and builds knowledge over time using Toolhouse AI tools and free LLM models via OpenRouter.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Toolhouse](https://img.shields.io/badge/Powered%20by-Toolhouse-green.svg)](https://toolhouse.ai)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange.svg)](https://openrouter.ai)

## 🌟 What This Does

Your AI Research & Analysis Assistant is like having a brilliant research partner who never forgets anything and can process information at superhuman speed. It combines AI reasoning with real-world research tools to help you gather information, analyze data, and build knowledge systematically.

### ✨ Core Capabilities

- **🔍 Comprehensive Research**: Multi-source web research with intelligent synthesis
- **📊 Data Analysis**: Real statistical analysis using code interpreter tools  
- **🧠 Memory & Learning**: Remembers your preferences and builds knowledge over time
- **📈 Trend Tracking**: Monitors changes and patterns across any timeframe
- **🗂️ Project Research**: Handles complex multi-step research projects
- **💾 Knowledge Building**: Stores insights and preferences for future use

### 🔥 Key Features

- **💯 100% Free**: Uses OpenRouter's free tier models (DeepSeek R1, Llama 4 Scout, Mistral Small 3)
- **🧠 Smart Model Selection**: Automatically chooses the best model for research vs analysis tasks
- **🛠️ Real Research Tools**: Powered by Toolhouse for web search, code analysis, and memory
- **🔄 Fallback System**: Switches models automatically if one fails
- **🔒 Privacy-Focused**: You control your data and API keys
- **📊 Usage Tracking**: Monitor your API usage and stay within free limits

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys from Toolhouse and OpenRouter (both have generous free tiers)

### 1. Get Your API Keys

#### Toolhouse Setup (Free - 50 agent runs/month)
1. Sign up at [toolhouse.ai](https://toolhouse.ai)
2. Go to [API Keys](https://app.toolhouse.ai/settings/api-keys) and generate a new key
3. Create a [Bundle](https://app.toolhouse.ai/bundles) called `research_assistant_tools`
4. Add these essential tools to your bundle:
   - **Web search** - for gathering information from the internet
   - **Code Interpreter** - for calculations, data analysis, and processing  
   - **Memory (remember)** - for storing insights and preferences
   - **Memory (recall)** - for retrieving stored information
   - **Trends over time** - for tracking patterns and changes

#### OpenRouter Setup (Free - 50-1000 requests/day)
1. Sign up at [openrouter.ai](https://openrouter.ai)  
2. Get your API key from the dashboard
3. No additional setup needed - free models are automatically available

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/PowerUpSkills/research-automation-ai.git
cd research-automation-ai

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your API keys
# TOOLHOUSE_API_KEY=your_toolhouse_api_key_here
# OPENROUTER_API_KEY=your_openrouter_api_key_here
# TIMEZONE_OFFSET=-8  # Optional: your timezone offset
# USER_ID=your_name   # Optional: for personalized responses
```

### 4. Run Your Research Assistant

```bash
# Start the interactive CLI
python main.py
```

## 📖 Usage Guide

### Interactive CLI

The main interface provides 9 research options:

```
🔍 Research Topic (Comprehensive web research)
📊 Analyze Data (Data analysis with insights)
📈 Track Trends (Monitor changes over time)  
🗂️ Comprehensive Research Project (Multi-step analysis)
💾 Store Preference (Remember insights for future)
🧠 Recall Preferences (Get stored insights)
📋 View Usage Stats
🤖 View Model Info
❌ Exit
```

### Programmatic Usage

```python
from life_coach import ResearchAnalysisAssistant

# Initialize your research assistant
assistant = ResearchAnalysisAssistant()

# Research any topic
result = assistant.research_topic(
    "best practices for remote team management", 
    depth="comprehensive"
)

# Analyze data
analysis = assistant.analyze_data(
    "Monthly sales data showing 15% growth in Q1, 8% in Q2, 22% in Q3",
    "Calculate growth trends and predict Q4 performance"
)

# Track trends over time
trends = assistant.track_trends(
    "adoption of AI tools in software development",
    timeframe="quarterly"
)

# Store preferences for future research
assistant.remember_preference(
    "research_style", 
    "Prefer data-driven analysis with specific metrics and actionable insights"
)
```

## 🎯 Example Research Projects

### Market Research
```python
# Comprehensive market analysis
result = assistant.comprehensive_research_project("""
Research the electric vehicle charging infrastructure market:
1. Current market size and growth projections
2. Key players and their market share
3. Technology trends (fast charging, wireless, etc.)
4. Geographic expansion patterns
5. Investment flows and funding rounds
6. Regulatory impacts and government policies
7. Calculate projected market value by 2030
""")
```

### Travel Planning Research
```python
# Intelligent travel research
result = assistant.research_topic("Tokyo travel guide March 2025", "deep")

# Store your travel preferences
assistant.remember_preference(
    "travel", 
    "Prefer authentic local experiences, moderate budget, interested in food and culture"
)
```

### Personal Productivity Analysis
```python
# Analyze your productivity patterns
analysis = assistant.analyze_data(
    "Work log: 8 hours daily, focus levels 1-10 scale, task completion rates over 30 days",
    "Find peak productivity patterns and optimization opportunities"
)
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test files
python -m pytest tests/test_coach.py -v
python -m pytest tests/test_models.py -v

# Run with coverage
pip install pytest-cov
python -m pytest tests/ --cov=life_coach --cov-report=html

# View coverage report
open htmlcov/index.html  # On macOS
# or navigate to htmlcov/index.html in your browser
```

### Test Structure

```
tests/
├── test_coach.py       # ResearchAnalysisAssistant class tests
└── test_models.py      # Model selection logic tests
```

### Running Individual Tests

```bash
# Test environment validation
python -m pytest tests/test_coach.py::TestEnvironmentValidation -v

# Test model selection
python -m pytest tests/test_models.py::TestModelSelector::test_model_selection_for_planning -v

# Test with output
python -m pytest tests/ -v -s
```

## 🔧 Customization

### Adding Custom Research Personality

```python
assistant = ResearchAnalysisAssistant(
    custom_personality="""
    You are a data-driven market research specialist. 
    Always prioritize quantitative data over opinions.
    Focus on actionable business insights and ROI analysis.
    Remember industry-specific terminology and trends.
    """
)
```

### Adding More Research Tools

1. Go to your [Toolhouse Bundle](https://app.toolhouse.ai/bundles)
2. Add powerful research tools like:
   - **GitHub Repo Tool** - for analyzing open source projects
   - **LinkedIn search** - for professional and company research
   - **Document Parser** - for processing PDFs and documents
   - **Image Generation** - for creating research visualizations
   - **Perplexity search** - for academic and technical research
3. No code changes needed - your assistant automatically gains new capabilities!

### Custom Model Preferences for Research

```python
from life_coach.models import ModelSelector

# Create research-optimized model selector
selector = ModelSelector(preference_weights={
    "research": 1.5,   # Prefer research models more
    "analysis": 1.3,   # Strong preference for analysis
    "creative": 0.7    # Less creative, more factual
})

assistant = ResearchAnalysisAssistant()
assistant.model_selector = selector
```

## 📊 Free Tier Limits

| Service | Free Limit | Perfect For |
|---------|------------|-------------|
| **OpenRouter** | 50-1000 requests/day | 3-5 research projects daily |
| **Toolhouse** | 50 agent runs/month + unlimited MCP calls | Serious research work |

## 🏗️ Project Structure

```
research-automation-ai/
├── 📚 README.md              # This file
├── 📦 requirements.txt       # Python dependencies
├── 🔧 .env.example          # Environment template
├── 🚫 .gitignore            # Git ignore rules
├── ⚖️  LICENSE              # MIT license
├── 🚀 main.py               # CLI interface
├── 📁 life_coach/           # Main package
│   ├── __init__.py          # Package exports
│   ├── coach.py             # ResearchAnalysisAssistant class
│   ├── models.py            # Free model configurations
│   └── utils.py             # Utility functions
├── 📁 examples/             # Usage examples
│   ├── research_projects.py # Research project examples
│   ├── data_analysis.py     # Analysis examples
│   └── trend_tracking.py    # Trend monitoring examples
└── 📁 tests/               # Unit tests
    ├── test_coach.py        # Assistant functionality tests
    └── test_models.py       # Model selection tests
```

## 🎯 Real-World Use Cases

### Business Intelligence
- **Competitor Analysis**: Track competitor products, pricing, and market moves
- **Market Research**: Analyze industry trends, market size, growth patterns
- **Investment Research**: Evaluate companies, sectors, and investment opportunities

### Academic Research  
- **Literature Reviews**: Gather and synthesize research papers and studies
- **Data Analysis**: Process experimental data and calculate statistical insights
- **Trend Monitoring**: Track developments in your field of study

### Personal Projects
- **Purchase Research**: Compare products, read reviews, analyze value propositions
- **Travel Planning**: Research destinations, costs, activities, and optimal timing
- **Learning Projects**: Research new skills, tools, and learning resources

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/PowerUpSkills/research-automation-ai.git
cd research-automation-ai

# Create development environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8

# Run tests to ensure everything works
python -m pytest tests/ -v
```

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/amazing-research-feature

# Make your changes and test
python -m pytest tests/ -v

# Format code
black life_coach/ tests/ examples/

# Check style
flake8 life_coach/ tests/ examples/

# Commit and push
git commit -m 'Add amazing research feature'
git push origin feature/amazing-research-feature
```

## 🐛 Troubleshooting

### Common Issues

**Missing Toolhouse Bundle**
```bash
❌ Bundle 'research_assistant_tools' not found

# Solution: Create the bundle in Toolhouse dashboard
# 1. Go to https://app.toolhouse.ai/bundles
# 2. Create bundle named 'research_assistant_tools'  
# 3. Add: Web search, Code Interpreter, Memory (remember), Memory (recall), Trends over time
```

**Model Rate Limits**
```bash
❌ Error with model: Rate limit exceeded

# The system automatically tries fallback models
# Check your usage: python main.py → Option 7 (Usage Stats)
```

**Research Tool Errors**
```bash
❌ Tool execution failed

# Check your Toolhouse bundle has the required tools
# Verify your API keys are correctly set in .env
```

### Getting Help

1. **Check the [Issues](https://github.com/PowerUpSkills/research-automation-ai/issues)** for known problems
2. **Join our [Discussions](https://github.com/PowerUpSkills/research-automation-ai/discussions)** for questions
3. **Create a new issue** with:
   - Python version
   - Error messages
   - Research task you were attempting

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Toolhouse](https://toolhouse.ai)** - For providing the AI research tool execution platform
- **[OpenRouter](https://openrouter.ai)** - For free access to powerful LLM models  
- **Open Source Community** - For making AI research accessible to everyone

## 🌟 Support

If you find this helpful:

- ⭐ **Star the repository** to show support
- 🐛 **Report bugs** via [Issues](https://github.com/PowerUpSkills/research-automation-ai/issues)
- 💡 **Suggest features** via [Discussions](https://github.com/PowerUpSkills/research-automation-ai/discussions)
- 🤝 **Contribute code** via Pull Requests
- 📢 **Share with researchers** who could benefit from an AI research assistant

## 🎉 What's Next?

- 📱 **Browser extension** for instant research on any webpage
- 🔗 **Database integrations** (PostgreSQL, MongoDB for data storage)
- 📊 **Advanced visualizations** with interactive charts and graphs
- 🤝 **Team research** features for collaborative projects
- 📚 **Research paper analysis** with citation tracking

---

**Built with ❤️ for researchers, analysts, and curious minds who want AI that actually helps with real research.**

> "Research is to see what everybody else has seen, and to think what nobody else has thought." - Your AI Research Assistant
