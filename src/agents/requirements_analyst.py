from autogen import AssistantAgent
import json

class RequirementsAnalyst(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Requirements Analyst specialized in gathering and analyzing project requirements.
Your responsibilities include:
1. Analyzing project overviews and extracting key requirements
2. Identifying missing information and asking clarifying questions
3. Categorizing requirements into functional and non-functional
4. Ensuring all necessary project prerequisites are identified
5. Collaborating with other agents to ensure requirements are feasible

You should:
- Be thorough in requirement gathering
- Ask specific questions when information is missing
- Consider hardware, software, and infrastructure requirements
- Think about scalability and future needs
- Document assumptions and constraints"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.requirements = {
            "functional": [],
            "non_functional": [],
            "hardware": [],
            "software": [],
            "infrastructure": [],
            "assumptions": [],
            "constraints": []
        }

    def analyze_requirements(self, project_overview):
        """Analyze the project overview and extract requirements"""
        # This method would be called by the autogen framework
        # The actual analysis happens through the chat mechanism
        pass

    def get_requirements(self):
        """Return the current set of requirements"""
        return self.requirements

    def update_requirements(self, category, requirements):
        """Update requirements in a specific category"""
        if category in self.requirements:
            self.requirements[category].extend(requirements)

    def export_requirements(self):
        """Export requirements in a structured format"""
        return json.dumps(self.requirements, indent=2) 