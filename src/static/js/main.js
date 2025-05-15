document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('proposalForm');
    const status = document.getElementById('status');
    const downloadSection = document.getElementById('downloadSection');
    const downloadBtn = document.getElementById('downloadBtn');
    let proposalPath = '';

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const projectOverview = document.getElementById('projectOverview').value;
        
        // Disable form submission while processing
        form.querySelector('button').disabled = true;
        status.innerHTML = 'Generating proposal... This may take a few minutes.';
        status.className = 'status-container';
        downloadSection.style.display = 'none';

        try {
            const response = await fetch('/submit_requirements', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ project_overview: projectOverview }),
            });

            const data = await response.json();

            if (data.status === 'success') {
                status.innerHTML = data.message;
                status.className = 'status-container success';
                proposalPath = data.proposal_path;
                downloadSection.style.display = 'block';
            } else {
                throw new Error(data.message || 'Failed to generate proposal');
            }
        } catch (error) {
            status.innerHTML = `Error: ${error.message}`;
            status.className = 'status-container error';
        } finally {
            form.querySelector('button').disabled = false;
        }
    });

    downloadBtn.addEventListener('click', () => {
        if (proposalPath) {
            window.location.href = `/download_proposal/${proposalPath}`;
        }
    });
}); 