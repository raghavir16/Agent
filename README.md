# Autogen Proposal Generator

This project implements an AI-powered proposal generation system using AutoGen. The system consists of multiple specialized agents that collaborate to create comprehensive project proposals.

## Agents
- Requirements Analyst
- Solutions Architect
- Cost and Estimate Analyst
- User Proxy Agent
- Solution Designer
- Risk Assessor
- Document Assembler
- Proposal Manager

## Setup

1. Clone the repository
2. Create a `.env` file in the root directory with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
python src/main.py
```

## Features
- Interactive requirement gathering
- Automated proposal generation
- Web-based user interface
- Document download functionality
- Design standards integration
- Multi-agent collaboration

## Project Structure
- `src/agents/`: Contains all agent implementations
- `src/templates/`: HTML templates for proposal sections
- `src/static/`: Static files (CSS, JS, images)
- `src/utils/`: Utility functions
- `src/config/`: Configuration files
- `tests/`: Test files

## Environment Variables
The application requires the following environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4 access

You can set these by creating a `.env` file in the root directory or by setting them in your environment directly. 