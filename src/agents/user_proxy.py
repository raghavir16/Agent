from autogen import UserProxyAgent

class UserProxy(UserProxyAgent):
    def __init__(self, name, llm_config, human_input_mode="NEVER"):
        system_message = """You are a User Proxy agent that represents the human user in the proposal generation process.
Your responsibilities include:
1. Gathering and providing project requirements
2. Answering questions from other agents about the project
3. Validating assumptions and constraints
4. Providing feedback on proposed solutions
5. Ensuring the final proposal meets user expectations

You should:
- Provide clear and concise information
- Ask for clarification when needed
- Validate critical assumptions
- Ensure requirements are properly understood
- Maintain consistency in communications"""

        super().__init__(
            name=name,
            system_message=system_message,
            human_input_mode=human_input_mode,
            llm_config=llm_config
        )
        
        self.project_context = {
            "requirements_validated": False,
            "assumptions_validated": False,
            "solution_approved": False,
            "costs_approved": False,
            "final_approval": False
        }

    def validate_requirements(self, requirements):
        """Validate the gathered requirements"""
        # Implementation handled through chat mechanism
        pass

    def validate_assumptions(self, assumptions):
        """Validate project assumptions"""
        # Implementation handled through chat mechanism
        pass

    def approve_solution(self, solution):
        """Approve the proposed solution"""
        # Implementation handled through chat mechanism
        pass

    def approve_costs(self, costs):
        """Approve the cost estimates"""
        # Implementation handled through chat mechanism
        pass

    def get_approval_status(self):
        """Get the current approval status"""
        return self.project_context 