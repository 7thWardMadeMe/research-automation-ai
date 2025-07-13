#!/usr/bin/env python3
"""
AI Research & Analysis Assistant - Command Line Interface

A personal AI research assistant that helps gather information, analyze data, and track insights 
using Toolhouse and OpenRouter.
"""

import os
import sys
from datetime import datetime
from life_coach import ResearchAnalysisAssistant
from life_coach.utils import validate_environment


def print_banner():
    """Print the application banner"""
    print("🔍📊 AI Research & Analysis Assistant 📊🔍")
    print("Your personal AI researcher powered by Toolhouse & OpenRouter")
    print("=" * 70)
    print()


def print_menu():
    """Print the main menu options"""
    print("What would you like to research or analyze?")
    print()
    print("1. 🔍 Research Topic (Comprehensive web research)")
    print("2. 📊 Analyze Data (Data analysis with insights)")
    print("3. 📈 Track Trends (Monitor changes over time)")
    print("4. 🗂️  Comprehensive Research Project (Multi-step analysis)")
    print("5. 💾 Store Preference (Remember insights for future)")
    print("6. 🧠 Recall Preferences (Get stored insights)")
    print("7. 📋 View Usage Stats")
    print("8. 🤖 View Model Info")
    print("9. ❌ Exit")
    print()


def get_user_choice() -> str:
    """Get user's menu choice"""
    while True:
        choice = input("Enter your choice (1-9): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 9.")


def handle_topic_research(assistant: ResearchAnalysisAssistant):
    """Handle topic research"""
    print("🔍 Let's research a topic!")
    print()
    
    topic = input("What topic would you like to research? ").strip()
    if not topic:
        print("❌ Topic is required.")
        return
    
    depth_options = {
        '1': 'quick',
        '2': 'comprehensive', 
        '3': 'deep'
    }
    
    print()
    print("How deep should the research be?")
    for key, value in depth_options.items():
        print(f"{key}. {value.title()}")
    
    depth_choice = input("Enter choice (1-3, or press Enter for comprehensive): ").strip()
    depth = depth_options.get(depth_choice, 'comprehensive')
    
    print()
    print(f"🔍 Researching '{topic}' with {depth} depth...")
    
    try:
        result = assistant.research_topic(topic, depth)
        print("📋 Research Results:")
        print("-" * 50)
        print(result["content"])
        print()
        print(f"⏰ Completed at: {result['timestamp']}")
        print(f"📝 Words: {result['word_count']}")
    except Exception as e:
        print(f"❌ Error during research: {e}")


def handle_data_analysis(assistant: ResearchAnalysisAssistant):
    """Handle data analysis"""
    print("📊 Let's analyze some data!")
    print()
    
    data_description = input("Describe the data you want analyzed: ").strip()
    if not data_description:
        print("❌ Data description is required.")
        return
    
    analysis_goals = input("What insights are you looking for? ").strip()
    if not analysis_goals:
        print("❌ Analysis goals are required.")
        return
    
    print()
    print(f"📊 Analyzing data: {data_description[:50]}...")
    
    try:
        result = assistant.analyze_data(data_description, analysis_goals)
        print("📈 Analysis Results:")
        print("-" * 50)
        print(result["content"])
        print()
        print(f"⏰ Completed at: {result['timestamp']}")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")


def handle_trend_tracking(assistant: ResearchAnalysisAssistant):
    """Handle trend tracking"""
    print("📈 Let's track some trends!")
    print()
    
    topic = input("What trend would you like to track? ").strip()
    if not topic:
        print("❌ Topic is required.")
        return
    
    timeframe_options = {
        '1': 'recent',
        '2': 'monthly',
        '3': 'quarterly', 
        '4': 'yearly',
        '5': 'custom'
    }
    
    print()
    print("What timeframe for trend analysis?")
    for key, value in timeframe_options.items():
        print(f"{key}. {value.title()}")
    
    choice = input("Enter choice (1-5): ").strip()
    
    if choice in timeframe_options:
        timeframe = timeframe_options[choice]
        if choice == '5':
            timeframe = input("Specify custom timeframe: ").strip()
    else:
        timeframe = "recent"
        print("Using default: recent")
    
    print()
    print(f"📈 Tracking trends for '{topic}' over {timeframe} period...")
    
    try:
        result = assistant.track_trends(topic, timeframe)
        print("📊 Trend Analysis:")
        print("-" * 50)
        print(result["content"])
        print()
        print(f"⏰ Completed at: {result['timestamp']}")
    except Exception as e:
        print(f"❌ Error tracking trends: {e}")


def handle_comprehensive_research(assistant: ResearchAnalysisAssistant):
    """Handle comprehensive research project"""
    print("🗂️ Let's tackle a comprehensive research project!")
    print()
    
    print("Describe your research project in detail.")
    print("(Include what you want to research, analyze, and what outcomes you're looking for)")
    print()
    
    project_description = input("Your research project: ").strip()
    if not project_description:
        print("❌ Project description is required.")
        return
    
    print()
    print(f"🔍 Starting comprehensive research project...")
    print("This may take a moment as I use multiple research tools...")
    
    try:
        result = assistant.comprehensive_research_project(project_description)
        print("📋 Comprehensive Research Report:")
        print("-" * 60)
        print(result["content"])
        print()
        print(f"⏰ Completed at: {result['timestamp']}")
        print(f"📝 Words: {result['word_count']}")
    except Exception as e:
        print(f"❌ Error during comprehensive research: {e}")


def handle_store_preference(assistant: ResearchAnalysisAssistant):
    """Handle storing preferences"""
    print("💾 Let's store a preference for future research!")
    print()
    
    category = input("Category (e.g., travel, work, food, research): ").strip()
    if not category:
        print("❌ Category is required.")
        return
    
    preference = input("What preference or insight should I remember? ").strip()
    if not preference:
        print("❌ Preference description is required.")
        return
    
    print()
    print(f"💾 Storing preference in category '{category}'...")
    
    try:
        result = assistant.remember_preference(category, preference)
        print("✅ Preference Stored:")
        print("-" * 30)
        print(result["content"])
        print()
        print(f"⏰ Stored at: {result['timestamp']}")
    except Exception as e:
        print(f"❌ Error storing preference: {e}")


def handle_recall_preferences(assistant: ResearchAnalysisAssistant):
    """Handle recalling preferences"""
    print("🧠 Let's recall your stored preferences!")
    print()
    
    category = input("Category to recall (or press Enter for all): ").strip()
    
    print()
    if category:
        print(f"🧠 Recalling preferences for '{category}'...")
    else:
        print("🧠 Recalling all stored preferences...")
    
    try:
        result = assistant.get_remembered_preferences(category if category else None)
        print("📋 Stored Preferences:")
        print("-" * 40)
        print(result["content"])
        print()
        print(f"⏰ Retrieved at: {result['timestamp']}")
    except Exception as e:
        print(f"❌ Error recalling preferences: {e}")


def handle_usage_stats(assistant: ResearchAnalysisAssistant):
    """Display usage statistics"""
    print("📊 Usage Statistics:")
    print("-" * 40)
    
    try:
        stats = assistant.get_usage_stats()
        print(f"Requests this session: {stats['requests_made_this_session']}")
        print(f"Bundle name: {stats['bundle_name']}")
        print(f"Timezone offset: {stats['timezone_offset']}")
        print()
        print("Current model preferences:")
        for task, model in stats['current_model_preferences'].items():
            model_name = model.split('/')[-1].replace(':free', '')
            print(f"  {task.title()}: {model_name}")
        print()
        print(f"Available models: {len(stats['available_models'])}")
    except Exception as e:
        print(f"❌ Error getting usage stats: {e}")


def handle_model_info(assistant: ResearchAnalysisAssistant):
    """Display model information"""
    print("🤖 Available Models:")
    print("-" * 40)
    
    try:
        info = assistant.get_model_info()
        
        print("Free models available:")
        for model_id, model_info in info['available_models'].items():
            name = model_info['name']
            context = model_info['context'] 
            strengths = ', '.join(model_info['strengths'][:3])
            print(f"  • {name} ({context}) - Good for: {strengths}")
        
        print()
        print("Current task assignments:")
        for task, model in info['current_preferences'].items():
            model_name = model.split('/')[-1].replace(':free', '')
            print(f"  {task.title()}: {model_name}")
            
    except Exception as e:
        print(f"❌ Error getting model info: {e}")


def main():
    """Main application loop"""
    # Check environment first
    validation = validate_environment()
    if not validation["valid"]:
        print("❌ Setup Error!")
        print("Missing required environment variables:")
        for var in validation["missing_required"]:
            print(f"  - {var}")
        print()
        print("Please:")
        print("1. Copy .env.example to .env")
        print("2. Add your API keys to the .env file")
        print("3. Create 'research_assistant_tools' bundle in Toolhouse")
        print("4. Run the program again")
        sys.exit(1)
    
    if validation["missing_optional"]:
        print("⚠️  Optional variables not set:")
        for var in validation["missing_optional"]:
            print(f"  - {var}")
        print()
    
    print_banner()
    
    # Initialize the research assistant
    try:
        assistant = ResearchAnalysisAssistant()
        print("✅ AI Research & Analysis Assistant initialized successfully!")
        print("📚 Make sure you've created 'research_assistant_tools' bundle with:")
        print("   • Web search")
        print("   • Code Interpreter") 
        print("   • Memory (remember)")
        print("   • Memory (recall)")
        print("   • Trends over time")
        print()
    except Exception as e:
        print(f"❌ Failed to initialize Research Assistant: {e}")
        print("Please check your API keys and Toolhouse bundle setup.")
        sys.exit(1)
    
    # Main interaction loop
    while True:
        print_menu()
        choice = get_user_choice()
        print()
        
        if choice == '1':
            handle_topic_research(assistant)
        elif choice == '2':
            handle_data_analysis(assistant)
        elif choice == '3':
            handle_trend_tracking(assistant)
        elif choice == '4':
            handle_comprehensive_research(assistant)
        elif choice == '5':
            handle_store_preference(assistant)
        elif choice == '6':
            handle_recall_preferences(assistant)
        elif choice == '7':
            handle_usage_stats(assistant)
        elif choice == '8':
            handle_model_info(assistant)
        elif choice == '9':
            print("👋 Thanks for using AI Research & Analysis Assistant!")
            print("Keep researching and stay curious! 🌟")
            break
        
        print()
        input("Press Enter to continue...")
        print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
