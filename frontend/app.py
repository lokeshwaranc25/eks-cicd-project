from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>EKS CI/CD Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 80px auto;
            background: #f4f7fb;
        }

        .card {
            background: white;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0,0,0,.08);
        }

        h1 {
            color: #2563eb;
        }

        .success {
            color: #16a34a;
            font-weight: bold;
        }

        code {
            background: #eef2ff;
            padding: 4px 8px;
        }
    </style>
</head>

<body>
<div class="card">

<h1>AWS EKS CI/CD Microservices</h1>

<p class="success">Frontend service is running ✓</p>

<h3>Backend Response</h3>

<p>Service: <code>{{ backend.service }}</code></p>
<p>Version: <code>{{ backend.version }}</code></p>
<p>Hostname: <code>{{ backend.hostname }}</code></p>

<h3>DevOps Stack</h3>

<p>
Docker • Kubernetes • AWS EKS • Terraform • Jenkins •
GitHub Actions • Helm • CloudWatch • Grafana
</p>

</div>
</body>
</html>
"""

@app.route("/")
def home():
    try:
        response = requests.get(
            f"{BACKEND_URL}/api/info",
            timeout=3
        )
        response.raise_for_status()
        backend = response.json()

    except Exception as error:
        backend = {
            "service": "Backend unavailable",
            "version": "-",
            "hostname": str(error)
        }

    return render_template_string(
        HTML,
        backend=backend
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
