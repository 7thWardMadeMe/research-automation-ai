"""
Utility functions for the AI Life Coach
"""

import os
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict, Any


def setup_logging(level: str = "INFO") -> logging.Logger:
    """
    Set up logging configuration
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
        
    Returns:
        Configured logger
    """
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=log_format,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("life_coach.log")
        ]
    )
    return logging.getLogger("LifeCoach")


def get_time_context() -> Dict[str, Any]:
    """
    Get current time context information
    
    Returns:
        Dict with time-related context
    """
    now = datetime.now()
    
    return {
        "current_time": now.isoformat(),
        "day_of_week": now.strftime("%A"),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M"),
        "is_weekend": now.weekday() >= 5,
        "is_morning": 6 <= now.hour < 12,
        "is_afternoon": 12 <= now.hour < 18,
        "is_evening": 18 <= now.hour < 22,
        "is_night": now.hour >= 22 or now.hour < 6
    }


def validate_environment() -> Dict[str, bool]:
    """
    Validate that required environment variables are set
    
    Returns:
        Dict with validation results
    """
    required_vars = ["TOOLHOUSE_API_KEY", "OPENROUTER_API_KEY"]
    optional_vars = ["TIMEZONE_OFFSET", "USER_ID"]
    
    validation = {
        "all_required_present": True,
        "missing_required": [],
        "missing_optional": [],
        "valid": True
    }
    
    # Check required variables
    for var in required_vars:
        if not os.getenv(var):
            validation["missing_required"].append(var)
            validation["all_required_present"] = False
            validation["valid"] = False
    
    # Check optional variables
    for var in optional_vars:
        if not os.getenv(var):
            validation["missing_optional"].append(var)
    
    return validation


def format_response(content: str, metadata: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Format a response with metadata
    
    Args:
        content: Response content
        metadata: Optional metadata to include
        
    Returns:
        Formatted response dict
    """
    response = {
        "content": content,
        "timestamp": datetime.now().isoformat(),
        "word_count": len(content.split()),
        "char_count": len(content)
    }
    
    if metadata:
        response["metadata"] = metadata
    
    return response


def calculate_usage_stats(requests_made: int, daily_limit: int = 100) -> Dict[str, Any]:
    """
    Calculate API usage statistics
    
    Args:
        requests_made: Number of requests made today
        daily_limit: Daily request limit
        
    Returns:
        Usage statistics
    """
    percentage_used = (requests_made / daily_limit) * 100
    remaining = daily_limit - requests_made
    
    return {
        "requests_made": requests_made,
        "daily_limit": daily_limit,
        "remaining": remaining,
        "percentage_used": round(percentage_used, 2),
        "status": "good" if percentage_used < 80 else "warning" if percentage_used < 95 else "critical"
    }


def extract_action_items(text: str) -> list:
    """
    Extract action items from text (simple implementation)
    
    Args:
        text: Text to extract action items from
        
    Returns:
        List of potential action items
    """
    action_indicators = [
        "should", "need to", "must", "have to", "will", 
        "going to", "plan to", "remember to", "don't forget"
    ]
    
    sentences = text.split(".")
    action_items = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if any(indicator in sentence.lower() for indicator in action_indicators):
            action_items.append(sentence)
    
    return action_items


def estimate_tokens(text: str) -> int:
    """
    Rough estimation of token count (1 token ≈ 4 characters)
    
    Args:
        text: Text to estimate tokens for
        
    Returns:
        Estimated token count
    """
    return len(text) // 4


def sanitize_input(user_input: str, max_length: int = 4000) -> str:
    """
    Sanitize user input for safety
    
    Args:
        user_input: Raw user input
        max_length: Maximum allowed length
        
    Returns:
        Sanitized input
    """
    # Remove potentially harmful content
    sanitized = user_input.strip()
    
    # Truncate if too long
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "..."
    
    return sanitized


def get_timezone_offset() -> int:
    """
    Get timezone offset from environment or default
    
    Returns:
        Timezone offset in hours
    """
    try:
        return int(os.getenv("TIMEZONE_OFFSET", 0))
    except (ValueError, TypeError):
        return 0


def format_error_message(error: Exception, context: str = "") -> str:
    """
    Format error message for user display
    
    Args:
        error: Exception object
        context: Additional context about where the error occurred
        
    Returns:
        User-friendly error message
    """
    base_message = "I encountered an issue"
    
    if context:
        base_message += f" while {context}"
    
    # Don't expose sensitive error details to users
    if "API" in str(error):
        return f"{base_message}. Please check your API configuration."
    elif "network" in str(error).lower() or "connection" in str(error).lower():
        return f"{base_message}. Please check your internet connection."
    else:
        return f"{base_message}. Please try again in a moment."
