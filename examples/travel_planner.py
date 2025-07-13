#!/usr/bin/env python3
"""
Travel Planner Example

This example demonstrates using the AI Life Coach for comprehensive travel planning.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from life_coach import PersonalLifeCoach


def plan_business_trip():
    """
    Example: Planning a business trip
    """
    print("✈️ Planning Business Trip Example")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    # Business trip to Austin
    result = coach.plan_travel(
        destination="Austin, Texas",
        dates="next Tuesday to Thursday",
        additional_info="""
        Business trip for client meetings. Need:
        - Hotel near downtown area
        - Good restaurants for client dinners
        - Reliable WiFi for working
        - Transportation from airport
        - Backup plans in case of weather delays
        """
    )
    
    print("🗺️ Business Trip Plan:")
    print("-" * 30)
    print(result["content"])
    print()
    print(f"📊 Plan details: {result['metadata']}")


def plan_vacation():
    """
    Example: Planning a vacation
    """
    print("🏖️ Planning Vacation Example")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    # Vacation to Japan
    result = coach.plan_travel(
        destination="Tokyo, Japan",
        dates="December 15-25",
        additional_info="""
        First time visiting Japan. Interested in:
        - Traditional culture and temples
        - Amazing food experiences
        - Some modern tech/gaming attractions
        - Budget: moderate to high-end
        - Staying in central Tokyo but open to day trips
        """
    )
    
    print("🗾 Vacation Plan:")
    print("-" * 30)
    print(result["content"])
    print()
    print(f"📊 Plan details: {result['metadata']}")


def plan_weekend_getaway():
    """
    Example: Planning a weekend getaway
    """
    print("🌄 Planning Weekend Getaway Example")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    # Weekend trip to Napa Valley
    result = coach.plan_travel(
        destination="Napa Valley, California",
        dates="this weekend",
        additional_info="""
        Weekend wine country escape. Looking for:
        - Scenic wineries with tastings
        - Romantic dinner spots
        - Spa or relaxation activities
        - Beautiful drive routes
        - Charming accommodation (B&B or boutique hotel)
        """
    )
    
    print("🍷 Weekend Getaway Plan:")
    print("-" * 30)
    print(result["content"])
    print()
    print(f"📊 Plan details: {result['metadata']}")


def interactive_travel_planner():
    """
    Interactive travel planning session
    """
    print("🗺️ Interactive Travel Planner")
    print("=" * 50)
    
    # Get user input
    destination = input("Where would you like to travel? ").strip()
    dates = input("When are you traveling? ").strip()
    
    print("\nTell me about your trip preferences:")
    print("(Travel style, budget, interests, special requirements, etc.)")
    additional_info = input("> ").strip()
    
    print(f"\n🔍 Planning your trip to {destination}...")
    
    try:
        coach = PersonalLifeCoach()
        result = coach.plan_travel(destination, dates, additional_info)
        
        print("\n✈️ Your Custom Travel Plan:")
        print("-" * 40)
        print(result["content"])
        
        # Save the plan
        filename = f"travel_plan_{destination.replace(' ', '_').replace(',', '')}_{dates.replace(' ', '_')}.txt"
        with open(filename, "w") as f:
            f.write(f"Travel Plan: {destination}\n")
            f.write(f"Dates: {dates}\n")
            f.write("=" * 50 + "\n\n")
            f.write(result["content"])
            f.write(f"\n\nGenerated at: {result['timestamp']}")
        
        print(f"\n💾 Plan saved to: {filename}")
        
    except Exception as e:
        print(f"❌ Error planning travel: {e}")


def main():
    """
    Travel planner examples menu
    """
    examples = {
        '1': ('Business Trip (Austin)', plan_business_trip),
        '2': ('Vacation (Tokyo)', plan_vacation),
        '3': ('Weekend Getaway (Napa Valley)', plan_weekend_getaway),
        '4': ('Interactive Planner', interactive_travel_planner)
    }
    
    print("🌍 Travel Planning Examples")
    print("=" * 40)
    print("Choose an example:")
    
    for key, (name, _) in examples.items():
        print(f"{key}. {name}")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice in examples:
        print("\n")
        _, function = examples[choice]
        function()
    else:
        print("❌ Invalid choice")


if __name__ == "__main__":
    main()
