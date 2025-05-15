from autogen import AssistantAgent
import json
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

class DocumentAssembler(AssistantAgent):
    def __init__(self, name, llm_config):
        system_message = """You are a Document Assembler specialized in creating professional proposal documents.
Your responsibilities include:
1. Gathering content from all agents
2. Formatting the proposal document
3. Ensuring consistent styling and branding
4. Including all required sections
5. Generating the final proposal document

You should:
- Follow document templates
- Maintain consistent formatting
- Include all required sections
- Ensure professional presentation
- Follow branding guidelines"""

        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config
        )
        
        self.document_sections = {
            "title_page": {},
            "contents": [],
            "executive_summary": "",
            "requirements": [],
            "scope": {
                "in_scope": [],
                "out_scope": []
            },
            "solution": {},
            "deliverables": [],
            "costs": {},
            "raid": {
                "risks": [],
                "assumptions": [],
                "issues": [],
                "dependencies": []
            }
        }

    def generate_document(self):
        """Generate the final proposal document"""
        doc = Document()
        self._create_title_page(doc)
        self._create_contents_page(doc)
        self._add_executive_summary(doc)
        self._add_requirements(doc)
        self._add_scope(doc)
        self._add_solution(doc)
        self._add_deliverables(doc)
        self._add_costs(doc)
        self._add_raid(doc)
        
        # Save the document
        filename = "proposal.docx"
        doc.save(filename)
        return filename

    def update_section(self, section, content):
        """Update content for a specific section"""
        if section in self.document_sections:
            self.document_sections[section] = content

    def _create_title_page(self, doc):
        """Create the title page"""
        # Implementation for creating title page
        pass

    def _create_contents_page(self, doc):
        """Create the contents page"""
        # Implementation for creating contents page
        pass

    def _add_executive_summary(self, doc):
        """Add the executive summary section"""
        # Implementation for adding executive summary
        pass

    def _add_requirements(self, doc):
        """Add the requirements section"""
        # Implementation for adding requirements
        pass

    def _add_scope(self, doc):
        """Add the scope section"""
        # Implementation for adding scope
        pass

    def _add_solution(self, doc):
        """Add the solution section"""
        # Implementation for adding solution
        pass

    def _add_deliverables(self, doc):
        """Add the deliverables section"""
        # Implementation for adding deliverables
        pass

    def _add_costs(self, doc):
        """Add the costs section"""
        # Implementation for adding costs
        pass

    def _add_raid(self, doc):
        """Add the RAID section"""
        # Implementation for adding RAID
        pass

    def export_sections(self):
        """Export the document sections in a structured format"""
        return json.dumps(self.document_sections, indent=2) 