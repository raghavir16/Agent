from autogen import AssistantAgent
import json

class ProposalManager(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Proposal Manager responsible for coordinating the entire proposal generation process.
Your responsibilities include:
1. Coordinating between all agents
2. Ensuring all sections are completed
3. Managing the proposal timeline
4. Validating proposal quality
5. Facilitating communication between agents

You should:
- Track progress of all sections
- Ensure consistency across sections
- Validate completeness
- Coordinate revisions
- Maintain quality standards"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.proposal_status = {
            "requirements_complete": False,
            "solution_design_complete": False,
            "cost_analysis_complete": False,
            "risk_assessment_complete": False,
            "document_assembly_complete": False,
            "sections_reviewed": [],
            "pending_revisions": [],
            "final_review_complete": False
        }

    def coordinate_proposal(self):
        """Coordinate the proposal generation process"""
        # Implementation handled through chat mechanism
        pass

    def update_status(self, section, status):
        """Update the status of a proposal section"""
        if section in self.proposal_status:
            self.proposal_status[section] = status

    def get_status(self):
        """Get the current proposal status"""
        return self.proposal_status

    def add_revision(self, section, revision_details):
        """Add a revision request for a section"""
        self.proposal_status["pending_revisions"].append({
            "section": section,
            "details": revision_details
        })

    def mark_section_reviewed(self, section):
        """Mark a section as reviewed"""
        if section not in self.proposal_status["sections_reviewed"]:
            self.proposal_status["sections_reviewed"].append(section)

    def is_proposal_complete(self):
        """Check if the proposal is complete"""
        return all([
            self.proposal_status["requirements_complete"],
            self.proposal_status["solution_design_complete"],
            self.proposal_status["cost_analysis_complete"],
            self.proposal_status["risk_assessment_complete"],
            self.proposal_status["document_assembly_complete"],
            self.proposal_status["final_review_complete"]
        ])

    def export_status(self):
        """Export the proposal status in a structured format"""
        return json.dumps(self.proposal_status, indent=2) 