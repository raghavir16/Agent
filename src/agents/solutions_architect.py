from autogen import AssistantAgent
import json

class SolutionsArchitect(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Solutions Architect specialized in designing comprehensive technical solutions.
Your responsibilities include:
1. Analyzing requirements and creating high-level solution designs
2. Ensuring alignment with design standards and best practices
3. Creating system architecture diagrams and technical specifications
4. Evaluating technical feasibility and scalability
5. Collaborating with other agents to ensure solution viability

You should:
- Follow provided design standards
- Consider scalability, maintainability, and security
- Propose optimal technical stack and infrastructure
- Document architecture decisions and rationale
- Consider integration points and dependencies"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.solution_design = {
            "architecture": {},
            "technical_stack": [],
            "infrastructure": {},
            "integrations": [],
            "security_measures": [],
            "scalability_considerations": [],
            "design_decisions": []
        }

    def create_solution_design(self, requirements):
        """Create a solution design based on requirements"""
        # Implementation handled through chat mechanism
        pass

    def get_solution_design(self):
        """Return the current solution design"""
        return self.solution_design

    def update_design(self, category, details):
        """Update specific aspects of the solution design"""
        if category in self.solution_design:
            if isinstance(self.solution_design[category], list):
                self.solution_design[category].extend(details)
            else:
                self.solution_design[category].update(details)

    def export_design(self):
        """Export the solution design in a structured format"""
        return json.dumps(self.solution_design, indent=2) 