import os
import logging
import random
from typing import Any, Dict
from openai import OpenAI
from toolhouse import Toolhouse
from dotenv import load_dotenv
from .helpers import format_response, format_error_message, get_timezone_offset, save_markdown_log

load_dotenv()

class ResearchAnalysisAssistant:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

        self.th = Toolhouse()
        self.th.set_api_key(os.getenv("TOOLHOUSE_API_KEY"))
        self.th.set_provider("openai")

        self.bundle_name = "research_assistant_tools"
        self.request_count = 0
        self.logger = logging.getLogger("ResearchAssistant")

        self.model_selector = self._init_model_selector()
        self.personality = self._default_personality()

        self.th.set_metadata("timezone", get_timezone_offset())
        self.th.set_metadata("id", os.getenv("USER_ID", "research_assistant"))

    def _init_model_selector(self):
        return type("ModelSelector", (), {
            "select_model": lambda _, task: {
                "planning": "meta-llama/llama-4-scout:free",
                "reasoning": "deepseek/deepseek-r1:free",
                "creative": "google/gemini-2.0-flash-exp:free",
                "fast": "mistralai/mistral-small-3.1-24b-instruct:free",
                "general": "deepseek/deepseek-chat-v3-0324:free",
                "coding": "qwen/qwq-32b:free"
            }.get(task, "meta-llama/llama-4-scout:free"),
            "get_all_models": lambda _: {
                "planning": "meta-llama/llama-4-scout:free",
                "reasoning": "deepseek/deepseek-r1:free",
                "creative": "google/gemini-2.0-flash-exp:free",
                "fast": "mistralai/mistral-small-3.1-24b-instruct:free",
                "general": "deepseek/deepseek-chat-v3-0324:free",
                "coding": "qwen/qwq-32b:free"
            },
            "get_fallback_model": lambda _, model: "mistralai/mistral-small-3.1-24b-instruct:free"
        })()

    def _default_personality(self):
        return (
            "You are my personal research and analysis assistant. "
            "You excel at web research, data analysis, trend tracking, and memory. "
            "You always try to provide useful, fact-based, and actionable insights."
        )

    def _get_coach_response(self, prompt: str, task_type: str) -> str:
        model = self.model_selector.select_model(task_type)

        messages = [
            {"role": "system", "content": self.personality},
            {"role": "user", "content": prompt}
        ]

        try:
            self.request_count += 1

            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                tools=self.th.get_tools(bundle=self.bundle_name),
                tool_choice="auto",
                extra_headers={
                    "HTTP-Referer": "https://ai-life-coach.com",
                    "X-Title": "AI Life Coach"
                }
            )

            messages.append(response.choices[0].message)

            if response.choices[0].message.tool_calls:
                tool_results = self.th.run_tools(response)
                messages.extend(tool_results)

                final_response = self.client.chat.completions.create(
                    model=model,
                    messages=messages,
                    tools=self.th.get_tools(bundle=self.bundle_name)
                )

                return final_response.choices[0].message.content

            return response.choices[0].message.content

        except Exception as e:
            self.logger.error(f"Error with model {model}: {e}")
            fallback_model = self.model_selector.get_fallback_model(model)
            self.logger.info(f"Trying fallback model: {fallback_model}")
            try:
                response = self.client.chat.completions.create(
                    model=fallback_model,
                    messages=messages,
                    tools=self.th.get_tools(bundle=self.bundle_name)
                )
                return response.choices[0].message.content
            except Exception as fallback_error:
                self.logger.error(f"Fallback model also failed: {fallback_error}")
                return format_error_message(fallback_error, "getting your coach response")

    def handle_request(self, request: str, task_type: str = "general") -> Dict[str, Any]:
        """
        Handle a user request and save the response as markdown.
        """
        self.logger.info(f"Handling {task_type} request...")

        response_content = self._get_coach_response(request, task_type)

        formatted = format_response(
            response_content,
            metadata={
                "type": "custom_request",
                "task_type": task_type,
                "model_used": self.model_selector.select_model(task_type)
            }
        )

        save_markdown_log(
            title=request[:40] or "ai_response",
            content=formatted["response"],
            metadata=formatted["metadata"]
        )

        return formatted

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "available_models": self.model_selector.get_all_models(),
            "current_preferences": {
                task: self.model_selector.select_model(task)
                for task in ["planning", "reasoning", "creative", "fast", "general", "coding"]
            }
        }

    def __repr__(self) -> str:
        return f"ResearchAnalysisAssistant(bundle='{self.bundle_name}', requests={self.request_count})"
