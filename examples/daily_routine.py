#!/usr/bin/env python3
"""
Daily Routine Example - Morning check-in and evening reflection

This example shows how to create automated daily routines with your AI Life Coach.
Perfect for setting up as cron jobs or scheduled tasks.
"""

import sys
import os
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from life_coach import PersonalLifeCoach


def morning_routine():
    """
    Automated morning check-in routine
    """
    print("🌅 Starting Morning Routine...")
    print("=" * 50)
    
    try:
        coach = PersonalLifeCoach()
        result = coach.daily_check_in()
        
        print("📋 Your Daily Briefing:")
        print("-" * 30)
        print(result["content"])
        print()
        print(f"✅ Completed at: {result['timestamp']}")
        
        # Optionally save to file
        date_str = datetime.now().strftime("%Y-%m-%d")
        with open(f"daily_briefing_{date_str}.txt", "w") as f:
            f.write(f"Daily Briefing - {date_str}\n")
            f.write("=" * 40 + "\n\n")
            f.write(result["content"])
            f.write(f"\n\nGenerated at: {result['timestamp']}")
        
        print(f"💾 Briefing saved to daily_briefing_{date_str}.txt")
        
    except Exception as e:
        print(f"❌ Morning routine failed: {e}")


def evening_routine():
    """
    Automated evening reflection routine
    """
    print("🌙 Starting Evening Routine...")
    print("=" * 50)
    
    try:
        coach = PersonalLifeCoach()
        result = coach.evening_reflection()
        
        print("🤔 Your Evening Reflection:")
        print("-" * 30)
        print(result["content"])
        print()
        print(f"✅ Completed at: {result['timestamp']}")
        
        # Optionally save to file
        date_str = datetime.now().strftime("%Y-%m-%d")
        with open(f"evening_reflection_{date_str}.txt", "w") as f:
            f.write(f"Evening Reflection - {date_str}\n")
            f.write("=" * 40 + "\n\n")
            f.write(result["content"])
            f.write(f"\n\nGenerated at: {result['timestamp']}")
        
        print(f"💾 Reflection saved to evening_reflection_{date_str}.txt")
        
    except Exception as e:
        print(f"❌ Evening routine failed: {e}")


def main():
    """
    Main routine selector
    """
    if len(sys.argv) < 2:
        print("Usage: python daily_routine.py [morning|evening]")
        print()
        print("Examples:")
        print("  python daily_routine.py morning   # Morning check-in")
        print("  python daily_routine.py evening   # Evening reflection")
        return
    
    routine_type = sys.argv[1].lower()
    
    if routine_type == "morning":
        morning_routine()
    elif routine_type == "evening":
        evening_routine()
    else:
        print(f"❌ Unknown routine type: {routine_type}")
        print("Use 'morning' or 'evening'")


if __name__ == "__main__":
    main()
