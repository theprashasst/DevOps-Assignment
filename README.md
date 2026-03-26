# DevOps Assignment

**Submitted by:** Prashasst Dongre  
**Enrollment:** 0201AI221053  
**Semester:** 8th Sem  
**Branch:** Artificial Intelligence and Data Science

---

## Tech Stack

- **Backend:** FastAPI + Uvicorn
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## Run Locally

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000)

## Run Tests

```bash
pip install pytest httpx
pytest test_main.py -v
```

## Docker

```bash
# Build
docker build -t devops-assignment .

# Run
docker run -p 8000:8000 devops-assignment
```

## CI/CD

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs automatically on every push:

1. **Test** — Installs dependencies and runs `pytest`
2. **Build** — Builds the Docker image and verifies the container starts
