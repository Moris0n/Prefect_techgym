# Prefect Live Coding Session: Simplifying Workflow Orchestration

Welcome to the repository for the live coding session, **Simplifying Workflow Orchestration with Prefect**. This session introduces Prefect, a modern workflow orchestration platform, demonstrating its capabilities through hands-on examples.

---

## 📋 Session Outline

1. **Introduction to Workflow Orchestration**  
   Understand what workflow orchestration is and why it’s essential in modern data pipelines and task automation.

2. **Live Demonstrations with Prefect**  
   Learn to build, run, and monitor workflows locally:
   - From simple Python code to structured flows with tasks.
   - Working with synchronous and asynchronous workflows.
   - Understanding retries in workflows.
   - Deploying workflows to a local server using Prefect.

---

## 📁 Directory Overview

The project demonstrates the following Prefect concepts:

1. **`basics/base_code.py`**  
   A simple Python script demonstrating a workflow without Prefect.

2. **`basics/base_code_with_flows.py`**  
   The same workflow restructured with Prefect's `Flow` and `Task` components.

3. **`basics/sync_async.py`**  
   Demonstrates synchronous and asynchronous workflows, showcasing task submission and result retrieval.

4. **`basics/retries.py`**  
   Demonstrates Prefect's retry mechanism for failed tasks.

5. **`basics/deploy_code.py`**  
   A simple example of deploying a Prefect flow to a local server with a local worker.

---

## ⚙️ Setting Up the Project

Follow these steps to set up and run the project:

### 1. Install Dependencies
Navigate to the `prefect-project` directory and install dependencies using `poetry`:
```bash
cd prefect-project
poetry install
```

### 2. Start the Prefect Server
Set up and start the Prefect server:
```bash
export PREFECT_API_URL="http://127.0.0.1:4200/api"
prefect server start
```
Once started, visit [http://localhost:4200](http://localhost:4200) to access the Prefect UI.

### 3. Running Examples
Run any example script with:
```bash
python <script_name>
```

For instance:
```bash
python basics/base_code_with_flows.py
```

---

## 🖥️ Viewing Results
After running a workflow, visit the Prefect UI at [http://localhost:4200](http://localhost:4200) to monitor and manage tasks.

