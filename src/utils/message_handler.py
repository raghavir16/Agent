import json
from datetime import datetime
from .document_generator import ProposalDocumentGenerator

class MessageHandler:
    @staticmethod
    def handle_requirements_message(content):
        """Handle messages for requirements analyst"""
        try:
            # Extract requirements from the message
            requirements = {
                "functional": [],
                "non_functional": [],
                "hardware": [],
                "software": [],
                "assumptions": []
            }
            
            lines = content.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                if line.lower().startswith('functional requirements:'):
                    current_section = 'functional'
                elif line.lower().startswith('non-functional requirements:'):
                    current_section = 'non_functional'
                elif line.lower().startswith('hardware requirements:'):
                    current_section = 'hardware'
                elif line.lower().startswith('software requirements:'):
                    current_section = 'software'
                elif line.lower().startswith('assumptions:'):
                    current_section = 'assumptions'
                elif line.startswith('- ') and current_section:
                    requirements[current_section].append(line[2:])
            
            return json.dumps(requirements)
        except Exception as e:
            return f"Error processing requirements: {str(e)}"

    @staticmethod
    def handle_solution_message(content):
        """Handle messages for solution architect"""
        try:
            # Extract solution design from the message
            solution = {
                "architecture": {},
                "technical_stack": [],
                "infrastructure": {},
                "security_measures": []
            }
            
            lines = content.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                if line.lower().startswith('architecture:'):
                    current_section = 'architecture'
                elif line.lower().startswith('technical stack:'):
                    current_section = 'technical_stack'
                elif line.lower().startswith('infrastructure:'):
                    current_section = 'infrastructure'
                elif line.lower().startswith('security:'):
                    current_section = 'security_measures'
                elif line.startswith('- ') and current_section:
                    if isinstance(solution[current_section], list):
                        solution[current_section].append(line[2:])
                    else:
                        key_value = line[2:].split(':')
                        if len(key_value) == 2:
                            solution[current_section][key_value[0].strip()] = key_value[1].strip()
            
            return json.dumps(solution)
        except Exception as e:
            return f"Error processing solution: {str(e)}"

    @staticmethod
    def handle_costs_message(content):
        """Handle messages for cost analyst"""
        try:
            # Extract costs from the message
            costs = {
                "resource_costs": [],
                "license_costs": [],
                "infrastructure_costs": [],
                "total": 0
            }
            
            lines = content.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                if line.lower().startswith('resource costs:'):
                    current_section = 'resource_costs'
                elif line.lower().startswith('license costs:'):
                    current_section = 'license_costs'
                elif line.lower().startswith('infrastructure costs:'):
                    current_section = 'infrastructure_costs'
                elif line.startswith('- ') and current_section:
                    item = {}
                    parts = line[2:].split('|')
                    if current_section == 'resource_costs':
                        item = {
                            'resource': parts[0].strip(),
                            'quantity': int(parts[1].strip()),
                            'unit_cost': float(parts[2].strip().replace('$', '')),
                            'total': float(parts[3].strip().replace('$', ''))
                        }
                    elif current_section == 'license_costs':
                        item = {
                            'name': parts[0].strip(),
                            'type': parts[1].strip(),
                            'amount': float(parts[2].strip().replace('$', ''))
                        }
                    costs[current_section].append(item)
            
            return json.dumps(costs)
        except Exception as e:
            return f"Error processing costs: {str(e)}"

    @staticmethod
    def handle_risks_message(content):
        """Handle messages for risk assessor"""
        try:
            # Extract risks from the message
            risks = {
                "risks": [],
                "assumptions": [],
                "dependencies": []
            }
            
            lines = content.split('\n')
            current_section = None
            
            for line in lines:
                line = line.strip()
                if line.lower().startswith('risks:'):
                    current_section = 'risks'
                elif line.lower().startswith('assumptions:'):
                    current_section = 'assumptions'
                elif line.lower().startswith('dependencies:'):
                    current_section = 'dependencies'
                elif line.startswith('- ') and current_section:
                    if current_section == 'risks':
                        parts = line[2:].split('|')
                        risk = {
                            'description': parts[0].strip(),
                            'impact': parts[1].strip(),
                            'probability': parts[2].strip(),
                            'mitigation': parts[3].strip()
                        }
                        risks[current_section].append(risk)
                    else:
                        risks[current_section].append(line[2:])
            
            return json.dumps(risks)
        except Exception as e:
            return f"Error processing risks: {str(e)}"

    @staticmethod
    def generate_document(requirements, solution, costs, risks):
        """Generate the final proposal document"""
        try:
            generator = ProposalDocumentGenerator()
            
            # Create title page
            generator.create_title_page(
                "Project Proposal",
                "Client Company",
                datetime.now().strftime("%B %d, %Y")
            )
            
            # Add requirements section
            generator.add_section("Requirements", json.loads(requirements))
            
            # Add solution section
            generator.add_section("Solution", json.loads(solution))
            
            # Add costs section
            generator.add_costs_section(json.loads(costs))
            
            # Add RAID section
            generator.add_raid_section(json.loads(risks))
            
            # Save the document
            return generator.save()
            
        except Exception as e:
            return f"Error generating document: {str(e)}" 