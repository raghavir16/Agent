from autogen import AssistantAgent
import json

class SolutionDesigner(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Solution Designer specialized in creating detailed technical designs.
Your responsibilities include:
1. Creating detailed technical specifications
2. Designing system components and interfaces
3. Creating implementation plans
4. Ensuring design standards compliance
5. Collaborating with architects and other agents

You should:
- Create detailed component designs
- Define interfaces and APIs
- Specify data models and flows
- Consider security and performance
- Document design patterns and decisions"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.design_details = {
            "components": [],
            "interfaces": [],
            "data_models": [],
            "security_controls": [],
            "performance_considerations": [],
            "implementation_plan": {},
            "design_patterns": []
        }

    def create_detailed_design(self, solution_architecture):
        """Create detailed design based on solution architecture"""
        # Implementation handled through chat mechanism
        pass

    def get_design_details(self):
        """Return the current design details"""
        return self.design_details

    def update_design_details(self, category, details):
        """Update specific aspects of the design"""
        if category in self.design_details:
            if isinstance(self.design_details[category], list):
                self.design_details[category].extend(details)
            else:
                self.design_details[category].update(details)

    def validate_design(self):
        """Validate design against standards and requirements"""
        # Implementation handled through chat mechanism
        pass

    def export_design(self):
        """Export the detailed design in a structured format"""
        return json.dumps(self.design_details, indent=2) 