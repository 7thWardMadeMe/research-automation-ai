# AI Research & Analysis Assistant 🔍📊

> Your personal AI researcher that conducts comprehensive web research, analyzes data, and builds knowledge over time using Toolhouse AI tools and free LLM models via OpenRouter.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Toolhouse](https://img.shields.io/badge/Powered%20by-Toolhouse-green.svg)](https://toolhouse.ai)
[![OpenRouter](https://img.shields.io/badge/Powered%20by-OpenRouter-orange.svg)](https://openrouter.ai)

## 🌟 What This Does

Your AI Research & Analysis Assistant is like having a brilliant research partner who never forgets anything and can process information at superhuman speed. It combines AI reasoning with real-world research tools to help you gather information, analyze data, and build knowledge systematically.

### ✨ Core Capabilities

* **🔍 Comprehensive Research**: Multi-source web research with intelligent synthesis
* **📊 Data Analysis**: Real statistical analysis using code interpreter tools
* **🧠 Memory & Learning**: Remembers your preferences and builds knowledge over time
* **📈 Trend Tracking**: Monitors changes and patterns across any timeframe
* **💂️ Project Research**: Handles complex multi-step research projects
* **📂 Knowledge Building**: Stores insights and preferences for future use

### 🔥 Key Features

* **💯 100% Free**: Uses OpenRouter's free tier models (DeepSeek R1, Llama 4 Scout, Mistral Small 3)
* **🧠 Smart Model Selection**: Automatically chooses the best model for research vs analysis tasks
* **🛠️ Real Research Tools**: Powered by Toolhouse for web search, code analysis, and memory
* **🔄 Fallback System**: Switches models automatically if one fails
* **🔐 Privacy-Focused**: You control your data and API keys
* **📊 Usage Tracking**: Monitor your API usage and stay within free limits

## 🚀 Quick Start

### Prerequisites

* Python 3.8 or higher
* API keys from Toolhouse and OpenRouter (both have generous free tiers)

### 1. Get Your API Keys

#### Toolhouse Setup (Free - 50 agent runs/month)

1. Sign up at [toolhouse.ai](https://toolhouse.ai)
2. Go to [API Keys](https://app.toolhouse.ai/settings/api-keys) and generate a new key
3. Create a [Bundle](https://app.toolhouse.ai/bundles) called `research_assistant_tools`
4. Add these essential tools to your bundle:

   * **Web search** - for gathering information from the internet
   * **Code Interpreter** - for calculations, data analysis, and processing
   * **Memory (remember)** - for storing insights and preferences
   * **Memory (recall)** - for retrieving stored information
   * **Trends over time** - for tracking patterns and changes

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

> ℹ️ **Need help with TIMEZONE\_OFFSET?**
> Set your offset from UTC (e.g., -8 for PST, +1 for CET). Unsure of yours? Use tools like [https://www.utcoffset.net](https://www.utcoffset.net) or search "current UTC offset \[your city]" on your favorite search engine.

### 💡 Running in PowerShell vs VS Code

This project was developed and tested on **Windows 11**, using **PowerShell** and **VS Code**. These instructions are beginner-friendly, but feel free to use what works best for your operating system and setup. The goal is to help other new users — this just happens to be the setup that worked for me.

#### ✅ Recommended: VS Code Terminal (Beginner Friendly)

1. **Open the project folder** in VS Code:

   * `File > Open Folder...`
   * Select: `research-automation-ai`

2. **Open the Terminal**:

   * Press \`Ctrl + \`\` (backtick)
   * OR: `View > Terminal`

3. **Activate the virtual environment**:

   ```powershell
   .\venv\Scripts\activate
   ```

4. **Run the program**:

   ```powershell
   python main.py
   ```

#### 💻 Alternative: PowerShell Standalone

If you’re outside VS Code and just using PowerShell:

1. **Navigate to the project folder**:

   ```powershell
   cd "C:\Users\7thWa\OneDrive\Desktop\local-projects\research-automation-ai"
   ```

2. **Activate the virtual environment**:

   ```powershell
   .\venv\Scripts\activate
   ```

3. **Run the program**:

   ```powershell
   python main.py
   ```

👍 Pro Tip: Always make sure you’re in the root of your project (where `main.py`, `.env`, and `requirements.txt` are located) before running commands.

### 4. Run Your Research Assistant

```bash
# Start the interactive CLI
python main.py
```

## 🧠 New User Tips (Optional but Helpful)

* 💾 **Backup Your Progress**: Push your fork to a private repo like `research-automation-ai-backup`
* 🔐 **Never Share `.env` Files**: Use `.gitignore` to keep secrets safe (already included)
* 📝 **Use `README.md` and `CHANGELOG.md`**: Track what you learn or modify
* 💻 **Try Screenshots**: Add visual walkthroughs for team sharing
* 🔍 **Don't Fear Git**: Use `git status`, `git add`, `git commit` regularly to manage changes

> 🚀 Built for learners by learners — safe, open, powerful research automation.
