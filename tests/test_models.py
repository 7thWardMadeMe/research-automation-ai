"""
Unit tests for the AI Life Coach models module
"""

import unittest
from life_coach.models import ModelSelector, FREE_MODELS


class TestModelSelector(unittest.TestCase):
    """Test cases for ModelSelector class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.selector = ModelSelector()
    
    def test_model_selection_for_planning(self):
        """Test that planning tasks get appropriate models"""
        model = self.selector.select_model("planning")
        self.assertIn(model, FREE_MODELS)
        
        # Should prefer models good at planning
        model_info = FREE_MODELS[model]
        self.assertIn("planning", model_info["strengths"])
    
    def test_model_selection_for_reasoning(self):
        """Test that reasoning tasks get appropriate models"""
        model = self.selector.select_model("reasoning")
        self.assertIn(model, FREE_MODELS)
        
        # Should prefer models good at reasoning
        model_info = FREE_MODELS[model]
        self.assertIn("reasoning", model_info["strengths"])
    
    def test_model_selection_for_creative(self):
        """Test that creative tasks get appropriate models"""
        model = self.selector.select_model("creative")
        self.assertIn(model, FREE_MODELS)
        
        # Should prefer models good at creative tasks
        model_info = FREE_MODELS[model]
        self.assertIn("creative", model_info["strengths"])
    
    def test_fallback_model_different_from_original(self):
        """Test that fallback model is different from failed model"""
        original_model = "meta-llama/llama-4-scout:free"
        fallback_model = self.selector.get_fallback_model(original_model)
        
        self.assertNotEqual(original_model, fallback_model)
        self.assertIn(fallback_model, FREE_MODELS)
    
    def test_list_models_by_strength(self):
        """Test filtering models by strength"""
        reasoning_models = self.selector.list_models_by_strength("reasoning")
        
        # Should return list of model IDs
        self.assertIsInstance(reasoning_models, list)
        self.assertGreater(len(reasoning_models), 0)
        
        # All returned models should have reasoning strength
        for model_id in reasoning_models:
            model_info = FREE_MODELS[model_id]
            self.assertIn("reasoning", model_info["strengths"])
    
    def test_get_model_info(self):
        """Test getting model information"""
        model_id = "deepseek/deepseek-r1:free"
        info = self.selector.get_model_info(model_id)
        
        self.assertIsInstance(info, dict)
        self.assertIn("name", info)
        self.assertIn("strengths", info)
        self.assertIn("context", info)
        self.assertIn("description", info)
    
    def test_get_all_models(self):
        """Test getting all available models"""
        all_models = self.selector.get_all_models()
        
        self.assertIsInstance(all_models, dict)
        self.assertEqual(len(all_models), len(FREE_MODELS))
    
    def test_get_random_model(self):
        """Test getting a random model"""
        random_model = self.selector.get_random_model()
        
        self.assertIn(random_model, FREE_MODELS)
    
    def test_invalid_task_type_defaults_to_general(self):
        """Test that invalid task types default to general"""
        model = self.selector.select_model("invalid_task_type")
        
        # Should still return a valid model
        self.assertIn(model, FREE_MODELS)


class TestFreeModels(unittest.TestCase):
    """Test cases for FREE_MODELS configuration"""
    
    def test_all_models_have_required_fields(self):
        """Test that all models have required information fields"""
        required_fields = ["name", "strengths", "context", "description"]
        
        for model_id, model_info in FREE_MODELS.items():
            for field in required_fields:
                self.assertIn(field, model_info, 
                            f"Model {model_id} missing field: {field}")
    
    def test_model_strengths_are_lists(self):
        """Test that model strengths are provided as lists"""
        for model_id, model_info in FREE_MODELS.items():
            self.assertIsInstance(model_info["strengths"], list,
                                f"Model {model_id} strengths should be a list")
            self.assertGreater(len(model_info["strengths"]), 0,
                             f"Model {model_id} should have at least one strength")
    
    def test_model_names_are_non_empty(self):
        """Test that all models have non-empty names"""
        for model_id, model_info in FREE_MODELS.items():
            self.assertIsInstance(model_info["name"], str)
            self.assertGreater(len(model_info["name"]), 0,
                             f"Model {model_id} should have a non-empty name")
    
    def test_model_descriptions_are_non_empty(self):
        """Test that all models have non-empty descriptions"""
        for model_id, model_info in FREE_MODELS.items():
            self.assertIsInstance(model_info["description"], str)
            self.assertGreater(len(model_info["description"]), 0,
                             f"Model {model_id} should have a non-empty description")
    
    def test_all_models_have_free_suffix(self):
        """Test that all model IDs have :free suffix"""
        for model_id in FREE_MODELS.keys():
            self.assertTrue(model_id.endswith(":free"),
                          f"Model {model_id} should end with ':free'")


if __name__ == "__main__":
    unittest.main()
