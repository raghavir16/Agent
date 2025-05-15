from autogen import AssistantAgent
import json

class RiskAssessor(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Risk Assessor specialized in identifying and analyzing project risks.
Your responsibilities include:
1. Identifying potential project risks
2. Assessing risk probability and impact
3. Proposing risk mitigation strategies
4. Monitoring dependencies and assumptions
5. Collaborating with other agents to ensure comprehensive risk assessment

You should:
- Consider technical, operational, and business risks
- Provide detailed risk analysis
- Suggest practical mitigation strategies
- Monitor project dependencies
- Follow risk management standards"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.risk_assessment = {
            "technical_risks": [],
            "operational_risks": [],
            "business_risks": [],
            "dependencies": [],
            "assumptions": [],
            "mitigation_strategies": {},
            "risk_matrix": {
                "high": [],
                "medium": [],
                "low": []
            }
        }

    def assess_risks(self, solution_design, requirements):
        """Assess risks based on solution design and requirements"""
        # Implementation handled through chat mechanism
        pass

    def get_risk_assessment(self):
        """Return the current risk assessment"""
        return self.risk_assessment

    def update_risks(self, category, risks):
        """Update specific aspects of the risk assessment"""
        if category in self.risk_assessment:
            if isinstance(self.risk_assessment[category], list):
                self.risk_assessment[category].extend(risks)
            else:
                self.risk_assessment[category].update(risks)

    def categorize_risk(self, risk):
        """Categorize a risk based on probability and impact"""
        # Implementation handled through chat mechanism
        pass

    def propose_mitigation(self, risk):
        """Propose mitigation strategies for a specific risk"""
        # Implementation handled through chat mechanism
        pass

    def export_assessment(self):
        """Export the risk assessment in a structured format"""
        return json.dumps(self.risk_assessment, indent=2) 