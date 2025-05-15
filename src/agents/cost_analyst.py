from autogen import AssistantAgent
import json

class CostAnalyst(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Cost and Estimate Analyst specialized in project cost analysis and estimation.
Your responsibilities include:
1. Analyzing solution designs and requirements for cost implications
2. Creating detailed cost breakdowns for resources and licenses
3. Estimating effort required for different project phases
4. Identifying cost optimization opportunities
5. Collaborating with other agents to ensure accurate cost estimates

You should:
- Provide detailed cost breakdowns
- Consider both one-time and recurring costs
- Include licensing and infrastructure costs
- Account for maintenance and support costs
- Document assumptions in cost calculations"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.cost_analysis = {
            "resource_costs": [],
            "license_costs": [],
            "infrastructure_costs": [],
            "effort_estimates": {},
            "maintenance_costs": [],
            "total_cost": 0,
            "cost_assumptions": [],
            "optimization_opportunities": []
        }

    def analyze_costs(self, solution_design, requirements):
        """Analyze costs based on solution design and requirements"""
        # Implementation handled through chat mechanism
        pass

    def get_cost_analysis(self):
        """Return the current cost analysis"""
        return self.cost_analysis

    def update_costs(self, category, costs):
        """Update specific aspects of the cost analysis"""
        if category in self.cost_analysis:
            if isinstance(self.cost_analysis[category], list):
                self.cost_analysis[category].extend(costs)
            else:
                self.cost_analysis[category].update(costs)

    def calculate_total_cost(self):
        """Calculate the total cost based on all components"""
        total = 0
        for category in ['resource_costs', 'license_costs', 'infrastructure_costs']:
            for cost in self.cost_analysis[category]:
                if isinstance(cost, dict) and 'amount' in cost:
                    total += cost['amount']
        self.cost_analysis['total_cost'] = total
        return total

    def export_analysis(self):
        """Export the cost analysis in a structured format"""
        return json.dumps(self.cost_analysis, indent=2) 