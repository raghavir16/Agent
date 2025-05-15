from flask import Flask, render_template, request, send_file, jsonify
import os
from main import initialize_agents, generate_proposal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_requirements', methods=['POST'])
def submit_requirements():
    data = request.json
    project_overview = data.get('project_overview', '')
    
    # Initialize agents and generate proposal
    agents = initialize_agents()
    proposal_path = generate_proposal(agents, project_overview)
    
    return jsonify({
        'status': 'success',
        'message': 'Proposal generated successfully',
        'proposal_path': proposal_path
    })

@app.route('/download_proposal/<path:filename>')
def download_proposal(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True) 