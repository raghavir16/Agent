import autogen
import os
from dotenv import load_dotenv
from agents.requirements_analyst import RequirementsAnalyst
from agents.solutions_architect import SolutionsArchitect
from agents.cost_analyst import CostAnalyst
from agents.user_proxy import UserProxy
from agents.solution_designer import SolutionDesigner
from agents.risk_assessor import RiskAssessor
from agents.document_assembler import DocumentAssembler
from agents.proposal_manager import ProposalManager

# Load environment variables
load_dotenv()

def initialize_agents():
    # Get API key from environment
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your environment or .env file.")

    config_list = [
        {
            "model": "gpt-4",
            "api_key": api_key
        }
    ]

    # Initialize all agents
    user_proxy = UserProxy(
        name="user_proxy",
        llm_config={"config_list": config_list},
        human_input_mode="NEVER"
    )

    requirements_analyst = RequirementsAnalyst(
        name="requirements_analyst",
        llm_config={"config_list": config_list}
    )

    solutions_architect = SolutionsArchitect(
        name="solutions_architect",
        llm_config={"config_list": config_list}
    )

    cost_analyst = CostAnalyst(
        name="cost_analyst",
        llm_config={"config_list": config_list}
    )

    solution_designer = SolutionDesigner(
        name="solution_designer",
        llm_config={"config_list": config_list}
    )

    risk_assessor = RiskAssessor(
        name="risk_assessor",
        llm_config={"config_list": config_list}
    )

    document_assembler = DocumentAssembler(
        name="document_assembler",
        llm_config={"config_list": config_list}
    )

    proposal_manager = ProposalManager(
        name="proposal_manager",
        llm_config={"config_list": config_list}
    )

    return {
        "user_proxy": user_proxy,
        "requirements_analyst": requirements_analyst,
        "solutions_architect": solutions_architect,
        "cost_analyst": cost_analyst,
        "solution_designer": solution_designer,
        "risk_assessor": risk_assessor,
        "document_assembler": document_assembler,
        "proposal_manager": proposal_manager
    }

def generate_proposal(agents, project_overview):
    # Create a group chat for all agents
    groupchat = autogen.GroupChat(
        agents=list(agents.values()),
        messages=[],
        max_round=50
    )
    
    manager = autogen.GroupChatManager(groupchat=groupchat)

    # Start the conversation with project overview
    user_proxy = agents["user_proxy"]
    user_proxy.initiate_chat(
        manager,
        message=f"Please analyze this project overview and create a proposal: {project_overview}"
    )

    # The document assembler will generate the final document
    document_path = agents["document_assembler"].generate_document()
    return document_path

if __name__ == "__main__":
    agents = initialize_agents()
    # For testing purposes
    generate_proposal(agents, "Sample project overview") 