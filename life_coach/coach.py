        4. One specific suggestion for improving tomorrow
        5. Something I should celebrate or feel good about from today
        6. Any follow-up actions or reminders I need

        Keep it encouraging but honest, and help me learn from today to make tomorrow better."""
        
        response_content = self._get_coach_response(prompt, "reasoning")
        
        return format_response(
            response_content,
            metadata={
                "type": "evening_reflection", 
                "time_context": time_context,
                "model_used": self.model_selector.select_model("reasoning")
            }
        )
    
    def handle_request(self, request: str, task_type: str = "general") -> Dict[str, Any]:
        """
        Handle any specific request or problem
        
        Args:
            request: Your request or question
            task_type: Type of task (planning, reasoning, creative, fast, general)
            
        Returns:
            Formatted response with assistance
        """
        self.logger.info(f"Handling {task_type} request...")
        
        response_content = self._get_coach_response(request, task_type)
        
        return format_response(
            response_content,
            metadata={
                "type": "custom_request",
                "task_type": task_type,
                "model_used": self.model_selector.select_model(task_type)
            }
        )
    
    def plan_travel(self, destination: str, dates: str, additional_info: str = "") -> Dict[str, Any]:
        """
        Plan travel with comprehensive research and suggestions
        
        Args:
            destination: Where you're traveling to
            dates: When you're traveling
            additional_info: Any additional context or preferences
            
        Returns:
            Formatted response with travel plan
        """
        self.logger.info(f"Planning travel to {destination}...")
        
        prompt = f"""Help me plan my trip to {destination} for {dates}.

        Please research and provide:

        1. Flight options and recommendations (if applicable)
        2. Accommodation suggestions based on location and budget
        3. Top attractions and activities for the dates I'm visiting
        4. Restaurant recommendations for different meals and budgets
        5. Transportation options in the destination
        6. Weather forecast and packing suggestions
        7. Any important local information, customs, or tips
        8. A suggested daily itinerary if staying multiple days

        Additional context: {additional_info}

        Be thorough but practical, and help me make the most of this trip!"""
        
        response_content = self._get_coach_response(prompt, "planning")
        
        return format_response(
            response_content,
            metadata={
                "type": "travel_planning",
                "destination": destination,
                "dates": dates,
                "model_used": self.model_selector.select_model("planning")
            }
        )
    
    def optimize_productivity(self, time_period: str = "this week") -> Dict[str, Any]:
        """
        Analyze and optimize your productivity patterns
        
        Args:
            time_period: Time period to analyze (this week, last month, etc.)
            
        Returns:
            Formatted response with productivity analysis
        """
        self.logger.info("Analyzing productivity patterns...")
        
        prompt = f"""I want to optimize my productivity and work patterns. Please help me analyze {time_period}.

        Please:

        1. Look at my calendar patterns and meeting distribution
        2. Identify when I seem most and least productive
        3. Spot any scheduling patterns that might be hurting my focus
        4. Suggest specific changes to my daily/weekly routine
        5. Recommend time-blocking strategies for my type of work
        6. Identify potential time-wasters or inefficiencies
        7. Suggest tools or techniques that might help my specific situation
        8. Create a plan for implementing one improvement this week

        Be specific and actionable - I want to see real improvements in how I manage my time and energy."""
        
        response_content = self._get_coach_response(prompt, "reasoning")
        
        return format_response(
            response_content,
            metadata={
                "type": "productivity_optimization",
                "time_period": time_period,
                "model_used": self.model_selector.select_model("reasoning")
            }
        )
    
    def _get_coach_response(self, prompt: str, task_type: str) -> str:
        """
        Get response from coach using specified task type and Toolhouse tools
        
        Args:
            prompt: The prompt/question for the coach
            task_type: Type of task for model selection
            
        Returns:
            Response content from the coach
        """
        # Select best model for this task type
        model = self.model_selector.select_model(task_type)
        
        messages = [
            {"role": "system", "content": self.personality},
            {"role": "user", "content": prompt}
        ]
        
        try:
            self.request_count += 1
            
            # Get tools from your Toolhouse bundle
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
            
            # Add the assistant's response to conversation
            messages.append(response.choices[0].message)
            
            # If the AI wants to use tools, let Toolhouse handle execution
            if response.choices[0].message.tool_calls:
                self.logger.info(f"Executing {len(response.choices[0].message.tool_calls)} tool calls...")
                
                # Toolhouse executes tools in their secure cloud
                tool_results = self.th.run_tools(response)
                messages.extend(tool_results)
                
                # Get final response after tool execution
                final_response = self.client.chat.completions.create(
                    model=model,
                    messages=messages,
                    tools=self.th.get_tools(bundle=self.bundle_name)
                )
                
                return final_response.choices[0].message.content
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Error with model {model}: {e}")
            
            # Try fallback model
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
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """
        Get current usage statistics
        
        Returns:
            Usage statistics dict
        """
        return {
            "requests_made_this_session": self.request_count,
            "current_model_preferences": {
                task: self.model_selector.select_model(task) 
                for task in ["planning", "reasoning", "creative", "fast", "general"]
            },
            "available_models": list(self.model_selector.get_all_models().keys()),
            "bundle_name": self.bundle_name,
            "timezone_offset": get_timezone_offset()
        }
    
    def set_custom_personality(self, personality: str) -> None:
        """
        Update the coach's personality/behavior
        
        Args:
            personality: New personality prompt
        """
        self.personality = personality
        self.logger.info("Coach personality updated")
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about available models
        
        Returns:
            Model information dict
        """
        return {
            "available_models": self.model_selector.get_all_models(),
            "current_preferences": {
                task: self.model_selector.select_model(task)
                for task in ["planning", "reasoning", "creative", "fast", "general", "coding", "multimodal"]
            }
        }
    
    def __repr__(self) -> str:
        return f"PersonalLifeCoach(bundle='{self.bundle_name}', requests={self.request_count})"
logger.info("Assistant personality updated")
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about available models"""
        return {
            "available_models": self.model_selector.get_all_models(),
            "current_preferences": {
                task: self.model_selector.select_model(task)
                for task in ["research", "analysis", "creative", "fast", "general", "coding"]
            }
        }
    
    def __repr__(self) -> str:
        return f"ResearchAnalysisAssistant(bundle='{self.bundle_name}', requests={self.request_count})"
