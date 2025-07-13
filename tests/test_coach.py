"""
Unit tests for the AI Life Coach main module
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import os
from life_coach.coach import PersonalLifeCoach
from life_coach.utils import validate_environment


class TestPersonalLifeCoach(unittest.TestCase):
    """Test cases for PersonalLifeCoach class"""
    
    @patch.dict(os.environ, {
        'TOOLHOUSE_API_KEY': 'test_toolhouse_key',
        'OPENROUTER_API_KEY': 'test_openrouter_key',
        'TIMEZONE_OFFSET': '-8',
        'USER_ID': 'test_user'
    })
    @patch('life_coach.coach.OpenAI')
    @patch('life_coach.coach.Toolhouse')
    def setUp(self, mock_toolhouse, mock_openai):
        """Set up test fixtures with mocked dependencies"""
        # Mock Toolhouse
        self.mock_th = Mock()
        self.mock_th.get_tools.return_value = [{"type": "function", "function": {"name": "test_tool"}}]
        self.mock_th.run_tools.return_value = [{"role": "tool", "content": "test result"}]
        mock_toolhouse.return_value = self.mock_th
        
        # Mock OpenAI client
        self.mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response"
        mock_response.choices[0].message.tool_calls = None
        self.mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = self.mock_client
        
        # Create coach instance
        self.coach = PersonalLifeCoach()
    
    def test_initialization(self):
        """Test that PersonalLifeCoach initializes correctly"""
        self.assertIsNotNone(self.coach.client)
        self.assertIsNotNone(self.coach.th)
        self.assertIsNotNone(self.coach.model_selector)
        self.assertEqual(self.coach.bundle_name, "life_coach_tools")
        self.assertEqual(self.coach.request_count, 0)
    
    def test_daily_check_in_structure(self):
        """Test that daily check-in returns proper structure"""
        result = self.coach.daily_check_in()
        
        # Check response structure
        self.assertIsInstance(result, dict)
        self.assertIn("content", result)
        self.assertIn("timestamp", result)
        self.assertIn("word_count", result)
        self.assertIn("metadata", result)
        
        # Check metadata
        metadata = result["metadata"]
        self.assertEqual(metadata["type"], "daily_check_in")
        self.assertIn("time_context", metadata)
        self.assertIn("model_used", metadata)
    
    def test_evening_reflection_structure(self):
        """Test that evening reflection returns proper structure"""
        result = self.coach.evening_reflection()
        
        # Check response structure
        self.assertIsInstance(result, dict)
        self.assertIn("content", result)
        self.assertIn("metadata", result)
        
        # Check metadata
        metadata = result["metadata"]
        self.assertEqual(metadata["type"], "evening_reflection")
    
    def test_handle_request_structure(self):
        """Test that handle_request returns proper structure"""
        result = self.coach.handle_request("Test request", "general")
        
        # Check response structure
        self.assertIsInstance(result, dict)
        self.assertIn("content", result)
        self.assertIn("metadata", result)
        
        # Check metadata
        metadata = result["metadata"]
        self.assertEqual(metadata["type"], "custom_request")
        self.assertEqual(metadata["task_type"], "general")
    
    def test_plan_travel_structure(self):
        """Test that plan_travel returns proper structure"""
        result = self.coach.plan_travel("Paris", "next week", "romantic trip")
        
        # Check response structure
        self.assertIsInstance(result, dict)
        self.assertIn("content", result)
        self.assertIn("metadata", result)
        
        # Check metadata
        metadata = result["metadata"]
        self.assertEqual(metadata["type"], "travel_planning")
        self.assertEqual(metadata["destination"], "Paris")
        self.assertEqual(metadata["dates"], "next week")
    
    def test_request_count_increment(self):
        """Test that request count increments with each request"""
        initial_count = self.coach.request_count
        
        self.coach.handle_request("Test request")
        
        self.assertEqual(self.coach.request_count, initial_count + 1)
    
    def test_get_usage_stats(self):
        """Test getting usage statistics"""
        stats = self.coach.get_usage_stats()
        
        self.assertIsInstance(stats, dict)
        self.assertIn("requests_made_this_session", stats)
        self.assertIn("current_model_preferences", stats)
        self.assertIn("available_models", stats)
        self.assertIn("bundle_name", stats)
    
    def test_get_model_info(self):
        """Test getting model information"""
        info = self.coach.get_model_info()
        
        self.assertIsInstance(info, dict)
        self.assertIn("available_models", info)
        self.assertIn("current_preferences", info)
    
    def test_set_custom_personality(self):
        """Test setting custom personality"""
        new_personality = "You are a strict productivity coach."
        self.coach.set_custom_personality(new_personality)
        
        self.assertEqual(self.coach.personality, new_personality)
    
    @patch('life_coach.coach.OpenAI')
    @patch('life_coach.coach.Toolhouse')
    def test_toolhouse_integration(self, mock_toolhouse_class, mock_openai_class):
        """Test that Toolhouse is properly integrated"""
        # Verify Toolhouse was initialized with correct parameters
        mock_toolhouse_class.assert_called_with(
            api_key=os.getenv("TOOLHOUSE_API_KEY"),
            provider="openai"
        )
        
        # Verify metadata was set
        self.mock_th.set_metadata.assert_any_call("timezone", -8)
        self.mock_th.set_metadata.assert_any_call("id", "test_user")


class TestEnvironmentValidation(unittest.TestCase):
    """Test cases for environment validation"""
    
    @patch.dict(os.environ, {
        'TOOLHOUSE_API_KEY': 'test_key',
        'OPENROUTER_API_KEY': 'test_key'
    }, clear=True)
    def test_valid_environment(self):
        """Test validation with all required variables"""
        validation = validate_environment()
        
        self.assertTrue(validation["valid"])
        self.assertTrue(validation["all_required_present"])
        self.assertEqual(len(validation["missing_required"]), 0)
    
    @patch.dict(os.environ, {
        'TOOLHOUSE_API_KEY': 'test_key'
    }, clear=True)
    def test_missing_required_variable(self):
        """Test validation with missing required variable"""
        validation = validate_environment()
        
        self.assertFalse(validation["valid"])
        self.assertFalse(validation["all_required_present"])
        self.assertIn("OPENROUTER_API_KEY", validation["missing_required"])
    
    @patch.dict(os.environ, {
        'TOOLHOUSE_API_KEY': 'test_key',
        'OPENROUTER_API_KEY': 'test_key',
        'TIMEZONE_OFFSET': '-8'
    }, clear=True)
    def test_partial_optional_variables(self):
        """Test validation with some optional variables missing"""
        validation = validate_environment()
        
        self.assertTrue(validation["valid"])
        self.assertIn("USER_ID", validation["missing_optional"])
        self.assertNotIn("TIMEZONE_OFFSET", validation["missing_optional"])


if __name__ == "__main__":
    unittest.main()
