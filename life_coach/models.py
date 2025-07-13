"""
Free model configurations and selection logic for OpenRouter
"""

import random
from typing import Dict, List


# Free models available on OpenRouter (as of 2025)
FREE_MODELS = {
    "meta-llama/llama-4-scout:free": {
        "name": "Llama 4 Scout",
        "strengths": ["planning", "analysis", "multimodal"],
        "context": "10M tokens",
        "description": "Great for planning and strategic analysis"
    },
    "deepseek/deepseek-r1:free": {
        "name": "DeepSeek R1", 
        "strengths": ["reasoning", "math", "coding"],
        "context": "131K tokens",
        "description": "Excellent reasoning and problem-solving capabilities"
    },
    "mistralai/mistral-small-3.1-24b-instruct:free": {
        "name": "Mistral Small 3.1",
        "strengths": ["speed", "efficiency", "general"],
        "context": "33K tokens", 
        "description": "Fast and efficient for general tasks"
    },
    "google/gemini-2.0-flash-exp:free": {
        "name": "Gemini 2.0 Flash",
        "strengths": ["creative", "multimodal", "conversation"],
        "context": "1M tokens",
        "description": "Good for creative and conversational tasks"
    },
    "deepseek/deepseek-chat-v3-0324:free": {
        "name": "DeepSeek Chat V3",
        "strengths": ["general", "reliable", "coding"],
        "context": "131K tokens",
        "description": "Reliable general-purpose assistant"
    },
    "qwen/qwq-32b:free": {
        "name": "QwQ 32B",
        "strengths": ["reasoning", "analysis", "math"],
        "context": "131K tokens", 
        "description": "Strong reasoning and analytical capabilities"
    },
    "google/gemini-2.5-pro-exp-03-25:free": {
        "name": "Gemini 2.5 Pro",
        "strengths": ["advanced", "multimodal", "creative"],
        "context": "1M tokens",
        "description": "Advanced capabilities for complex tasks"
    }
}


class ModelSelector:
    """Smart model selection based on task types and preferences"""
    
    def __init__(self, preference_weights: Dict[str, float] = None):
        """
        Initialize model selector with optional preference weights
        
        Args:
            preference_weights: Dict mapping task types to preference multipliers
        """
        self.preference_weights = preference_weights or {}
        
        # Default task-to-model mappings based on model strengths
        self.task_preferences = {
            "planning": [
                "meta-llama/llama-4-scout:free",
                "qwen/qwq-32b:free",
                "deepseek/deepseek-r1:free"
            ],
            "reasoning": [
                "deepseek/deepseek-r1:free", 
                "qwen/qwq-32b:free",
                "meta-llama/llama-4-scout:free"
            ],
            "creative": [
                "google/gemini-2.0-flash-exp:free",
                "google/gemini-2.5-pro-exp-03-25:free",
                "meta-llama/llama-4-scout:free"
            ],
            "fast": [
                "mistralai/mistral-small-3.1-24b-instruct:free",
                "deepseek/deepseek-chat-v3-0324:free",
                "google/gemini-2.0-flash-exp:free"
            ],
            "general": [
                "deepseek/deepseek-chat-v3-0324:free",
                "mistralai/mistral-small-3.1-24b-instruct:free",
                "meta-llama/llama-4-scout:free"
            ],
            "coding": [
                "deepseek/deepseek-r1:free",
                "deepseek/deepseek-chat-v3-0324:free",
                "qwen/qwq-32b:free"
            ],
            "multimodal": [
                "meta-llama/llama-4-scout:free",
                "google/gemini-2.5-pro-exp-03-25:free", 
                "google/gemini-2.0-flash-exp:free"
            ]
        }
    
    def select_model(self, task_type: str = "general") -> str:
        """
        Select the best free model for a given task type
        
        Args:
            task_type: Type of task (planning, reasoning, creative, fast, general, etc.)
            
        Returns:
            Model identifier string for OpenRouter
        """
        # Get preferred models for this task type
        preferred_models = self.task_preferences.get(task_type, 
                                                   self.task_preferences["general"])
        
        # Apply preference weights if configured
        if task_type in self.preference_weights:
            # Weighted selection (simplified - just return first choice)
            return preferred_models[0]
        
        # Default: return the top choice for this task type
        return preferred_models[0]
    
    def get_fallback_model(self, failed_model: str) -> str:
        """
        Get a fallback model when the primary model fails
        
        Args:
            failed_model: The model that failed
            
        Returns:
            Alternative model identifier
        """
        available_models = [model for model in FREE_MODELS.keys() 
                          if model != failed_model]
        return random.choice(available_models)
    
    def list_models_by_strength(self, strength: str) -> List[str]:
        """
        Get all models that excel at a specific strength
        
        Args:
            strength: Model strength to filter by (reasoning, creative, etc.)
            
        Returns:
            List of model identifiers with that strength
        """
        return [model_id for model_id, info in FREE_MODELS.items()
                if strength in info["strengths"]]
    
    def get_model_info(self, model_id: str) -> Dict:
        """
        Get detailed information about a specific model
        
        Args:
            model_id: Model identifier
            
        Returns:
            Model information dict
        """
        return FREE_MODELS.get(model_id, {})
    
    @classmethod
    def get_all_models(cls) -> Dict[str, Dict]:
        """Get all available free models with their information"""
        return FREE_MODELS.copy()
    
    @classmethod 
    def get_random_model(cls) -> str:
        """Get a random free model"""
        return random.choice(list(FREE_MODELS.keys()))
