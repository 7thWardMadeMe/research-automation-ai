. Suggest ways to batch similar tasks
    6. Recommend tools for better focus and time management
    
    I typically work on software development, have many meetings, and struggle with context switching.
    """
    
    result = coach.handle_request(request, "reasoning")
    
    print("⚡ Schedule Optimization Suggestions:")
    print("-" * 40)
    print(result["content"])
    print()
    print(f"🎯 Task type: {result['metadata']['task_type']}")
    print(f"🤖 Model used: {result['metadata']['model_used']}")


def focus_improvement_plan():
    """
    Create a personalized focus improvement plan
    """
    print("🎯 Focus Improvement Plan")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    request = """
    I've been struggling with focus and getting distracted easily. Help me create a plan to improve:
    
    1. Identify my biggest distraction sources
    2. Suggest techniques for deep work sessions
    3. Recommend apps or tools that could help
    4. Create a daily routine that supports better focus
    5. Set up environmental changes for my workspace
    6. Develop strategies for handling interruptions
    7. Create a 30-day focus improvement challenge
    
    I work from home and have trouble with social media, notifications, and procrastination.
    """
    
    result = coach.handle_request(request, "planning")
    
    print("🧠 Your Focus Improvement Plan:")
    print("-" * 40)
    print(result["content"])
    
    # Save the plan
    date_str = datetime.now().strftime("%Y-%m-%d")
    with open(f"focus_improvement_plan_{date_str}.txt", "w") as f:
        f.write(f"Focus Improvement Plan - {date_str}\n")
        f.write("=" * 50 + "\n\n")
        f.write(result["content"])
        f.write(f"\n\nGenerated at: {result['timestamp']}")
    
    print(f"\n💾 Plan saved to focus_improvement_plan_{date_str}.txt")


def energy_management_analysis():
    """
    Analyze energy patterns and suggest optimization
    """
    print("⚡ Energy Management Analysis")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    request = """
    Help me understand and optimize my energy patterns throughout the day:
    
    1. Analyze when I typically have high vs low energy
    2. Suggest how to align my tasks with my energy levels
    3. Recommend strategies for maintaining energy throughout the day
    4. Identify energy drains I should minimize
    5. Suggest nutrition and lifestyle changes for better energy
    6. Create an energy-optimized daily schedule template
    7. Recommend recovery activities for when I'm drained
    
    I usually feel energetic in the morning but crash after lunch, and I have trouble with late-day motivation.
    """
    
    result = coach.handle_request(request, "reasoning")
    
    print("⚡ Your Energy Management Strategy:")
    print("-" * 40)
    print(result["content"])


def productivity_habits_tracker():
    """
    Create a system for tracking productivity habits
    """
    print("📋 Productivity Habits Tracker")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    request = """
    Help me create a simple but effective system for tracking and improving my productivity habits:
    
    1. Identify the top 5 habits that would most impact my productivity
    2. Create a simple daily tracking method
    3. Suggest weekly review questions
    4. Design a reward system for consistency
    5. Plan how to gradually add new habits
    6. Set up accountability measures
    7. Create troubleshooting strategies for when I fall off track
    
    I want something sustainable that doesn't become another source of stress or perfectionism.
    """
    
    result = coach.handle_request(request, "planning")
    
    print("📊 Your Habits Tracking System:")
    print("-" * 40)
    print(result["content"])
    
    # Create a simple habits template
    template = """
# Daily Productivity Habits Tracker

Date: ___________

## Core Habits (✓ = Done, ✗ = Missed, ~ = Partial)
□ Morning planning session (10 min)
□ Deep work block (2+ hours)
□ Inbox zero before lunch
□ Afternoon review (5 min)
□ No social media during work hours

## Energy & Focus
Morning energy (1-10): ___
Afternoon energy (1-10): ___
Focus quality today (1-10): ___

## Wins & Lessons
Biggest accomplishment: ________________
What drained my energy: ________________
Tomorrow's top priority: ________________

## Notes
_________________________________
_________________________________
"""
    
    with open("daily_habits_template.txt", "w") as f:
        f.write(template)
    
    print(f"\n📝 Habits template saved to daily_habits_template.txt")


def weekly_productivity_review():
    """
    Conduct a comprehensive weekly productivity review
    """
    print("📅 Weekly Productivity Review")
    print("=" * 50)
    
    coach = PersonalLifeCoach()
    
    # Get the previous week's date range
    today = datetime.now()
    last_monday = today - timedelta(days=today.weekday() + 7)
    last_sunday = last_monday + timedelta(days=6)
    
    request = f"""
    Help me conduct a comprehensive productivity review for the week of {last_monday.strftime('%B %d')} - {last_sunday.strftime('%B %d, %Y')}:
    
    1. Review my calendar and identify what went well vs. poorly
    2. Analyze my task completion rate and quality
    3. Identify patterns in my energy and focus levels
    4. Spot time-wasters and productivity killers
    5. Evaluate my work-life balance this week
    6. Assess progress toward my larger goals
    7. Create specific improvements for next week
    8. Set 3 priorities for the coming week
    
    Please ask me clarifying questions if you need more information to provide actionable insights.
    """
    
    result = coach.handle_request(request, "reasoning")
    
    print("📊 Your Weekly Review:")
    print("-" * 40)
    print(result["content"])
    
    # Save the review
    week_str = last_monday.strftime("%Y-W%W")
    with open(f"weekly_review_{week_str}.txt", "w") as f:
        f.write(f"Weekly Productivity Review - Week {week_str}\n")
        f.write(f"({last_monday.strftime('%B %d')} - {last_sunday.strftime('%B %d, %Y')})\n")
        f.write("=" * 60 + "\n\n")
        f.write(result["content"])
        f.write(f"\n\nGenerated at: {result['timestamp']}")
    
    print(f"\n💾 Review saved to weekly_review_{week_str}.txt")


def main():
    """
    Productivity optimization examples menu
    """
    examples = {
        '1': ('Weekly Pattern Analysis', analyze_weekly_patterns),
        '2': ('Daily Schedule Optimization', optimize_daily_schedule),
        '3': ('Focus Improvement Plan', focus_improvement_plan),
        '4': ('Energy Management Analysis', energy_management_analysis),
        '5': ('Habits Tracking System', productivity_habits_tracker),
        '6': ('Weekly Review', weekly_productivity_review)
    }
    
    print("📈 Productivity Optimization Examples")
    print("=" * 50)
    print("Choose an example:")
    
    for key, (name, _) in examples.items():
        print(f"{key}. {name}")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice in examples:
        print("\n")
        _, function = examples[choice]
        try:
            function()
        except Exception as e:
            print(f"❌ Error running example: {e}")
    else:
        print("❌ Invalid choice")


if __name__ == "__main__":
    main()
