import autogen
import os
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables
load_dotenv()

def create_agent_config():
    """Create the configuration for agents"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your environment or .env file.")

    return {
        "config_list": [{
            "model": "gpt-4",
            "api_key": api_key
        }],
        "temperature": 0.7,
        "timeout": 600
    }

def initialize_agents():
    """Initialize all agents with proper AutoGen configuration"""
    config = create_agent_config()

    # Create the user proxy agent that will coordinate with human
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        system_message="You are a user proxy that coordinates between the human user and the AI agents. You gather requirements and provide feedback.",
        human_input_mode="TERMINATE",  # Only ask for human input when needed
        code_execution_config={"work_dir": "workspace"},
        llm_config=config
    )

    # Create the requirements analyst
    requirements_analyst = autogen.AssistantAgent(
        name="requirements_analyst",
        system_message="""You are a Requirements Analyst. You analyze project requirements and create detailed specifications.
Focus on:
1. Gathering clear requirements
2. Identifying missing information
3. Categorizing requirements
4. Documenting assumptions""",
        llm_config=config
    )

    # Create the solutions architect
    solutions_architect = autogen.AssistantAgent(
        name="solutions_architect",
        system_message="""You are a Solutions Architect. You design high-level technical solutions.
Focus on:
1. Creating system architecture
2. Selecting technologies
3. Ensuring scalability
4. Documenting design decisions""",
        llm_config=config
    )

    # Create the cost analyst
    cost_analyst = autogen.AssistantAgent(
        name="cost_analyst",
        system_message="""You are a Cost Analyst. You estimate and analyze project costs.
Focus on:
1. Resource cost estimation
2. License cost analysis
3. Infrastructure costs
4. Maintenance costs""",
        llm_config=config
    )

    # Create the solution designer
    solution_designer = autogen.AssistantAgent(
        name="solution_designer",
        system_message="""You are a Solution Designer. You create detailed technical designs.
Focus on:
1. Component design
2. Interface specifications
3. Data models
4. Implementation details""",
        llm_config=config
    )

    # Create the risk assessor
    risk_assessor = autogen.AssistantAgent(
        name="risk_assessor",
        system_message="""You are a Risk Assessor. You identify and analyze project risks.
Focus on:
1. Risk identification
2. Impact assessment
3. Mitigation strategies
4. Dependency analysis""",
        llm_config=config
    )

    # Create the document assembler
    document_assembler = autogen.AssistantAgent(
        name="document_assembler",
        system_message="""You are a Document Assembler. You create the final proposal document.
Focus on:
1. Document structure
2. Content formatting
3. Consistency checking
4. Quality assurance""",
        llm_config=config
    )

    # Create the proposal manager
    proposal_manager = autogen.AssistantAgent(
        name="proposal_manager",
        system_message="""You are a Proposal Manager. You coordinate the entire proposal process.
Focus on:
1. Process coordination
2. Quality control
3. Timeline management
4. Team communication""",
        llm_config=config
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

def create_group_chat(agents: Dict[str, Any]):
    """Create a group chat with all agents"""
    groupchat = autogen.GroupChat(
        agents=list(agents.values()),
        messages=[],
        max_round=50,
        speaker_selection_method="round_robin",  # Agents take turns speaking
        allow_repeat_speaker=False,  # Prevent the same agent from speaking twice in a row
    )
    
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=create_agent_config()
    )

    return groupchat, manager

def generate_proposal(project_overview: str):
    """Generate a proposal based on the project overview"""
    # Initialize agents
    agents = initialize_agents()
    
    # Create group chat
    groupchat, manager = create_group_chat(agents)
    
    # Start the conversation with the project overview
    user_proxy = agents["user_proxy"]
    
    # Initiate the chat with a clear task description
    user_proxy.initiate_chat(
        manager,
        message=f"""Please create a comprehensive proposal for the following project:

Project Overview:
{project_overview}

Please follow this process:
1. Requirements Analyst: Gather and analyze requirements
2. Solutions Architect: Create high-level solution design
3. Solution Designer: Create detailed technical design
4. Cost Analyst: Estimate costs and resources
5. Risk Assessor: Identify and analyze risks
6. Document Assembler: Create the proposal document
7. Proposal Manager: Review and finalize

Each agent should wait for the previous agent to complete their task before starting.
"""
    )

    # The document path will be available in the chat history
    # Find the last message from document_assembler
    for message in reversed(groupchat.messages):
        if message.get("sender") == "document_assembler" and "proposal.docx" in message.get("content", ""):
            return "proposal.docx"
    
    return None

if __name__ == "__main__":
    # Example usage
    project_overview = "Create a cloud-based inventory management system for a retail chain"
    doc_path = generate_proposal(project_overview)
    print(f"Proposal generated: {doc_path}") 