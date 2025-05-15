import os
from dotenv import load_dotenv
import autogen
from main import initialize_agents, create_group_chat, generate_proposal

def test_agent_initialization():
    """Test if all agents can be initialized properly"""
    # Load environment variables
    load_dotenv()
    
    try:
        # Initialize all agents
        agents = initialize_agents()
        
        # Test that all required agents exist
        required_agents = [
            "user_proxy",
            "requirements_analyst",
            "solutions_architect",
            "cost_analyst",
            "solution_designer",
            "risk_assessor",
            "document_assembler",
            "proposal_manager"
        ]
        
        for agent_name in required_agents:
            print(f"Testing {agent_name}...")
            assert agent_name in agents, f"Missing agent: {agent_name}"
            agent = agents[agent_name]
            assert isinstance(agent, (autogen.AssistantAgent, autogen.UserProxyAgent)), f"{agent_name} is not an AutoGen agent"
            assert hasattr(agent, 'name'), f"{agent_name} missing 'name' attribute"
            assert hasattr(agent, 'llm_config'), f"{agent_name} missing 'llm_config' attribute"
        
        # Test group chat creation
        groupchat, manager = create_group_chat(agents)
        assert isinstance(groupchat, autogen.GroupChat), "Failed to create group chat"
        assert isinstance(manager, autogen.GroupChatManager), "Failed to create chat manager"
        
        print("All agents initialized and tested successfully!")
        return agents

    except Exception as e:
        print(f"Error during agent initialization: {str(e)}")
        raise

def test_proposal_generation():
    """Test the proposal generation process"""
    try:
        # Test with a sample project
        project_overview = "Create a small web application for task management"
        doc_path = generate_proposal(project_overview)
        
        assert doc_path is not None, "No proposal document was generated"
        assert doc_path.endswith('.docx'), "Generated document is not a Word document"
        
        print("Proposal generation test completed successfully!")
        
    except Exception as e:
        print(f"Error during proposal generation: {str(e)}")
        raise

if __name__ == "__main__":
    agents = test_agent_initialization()
    test_proposal_generation() 