# startup guide

## Introduction
### **Observability and Evaluation of AI Agentic applications**
AgentNeo helps AI engineers build better AI from development through deployment.AgentNeo include:
- [**Creating session**](#creatingsession)
- [**Tracer**](#Tracer)
- [**Execution**](#Execution)
- [**Evaluation**](#Evaluation)
## **Creating session**
Initialize AgentNeo Session
To start using AgentNeo, you'll need to initialize the session. Here’s an example that shows how to initialize an AgentNeo session:
```py 
neo_session = AgentNeo(session_name="my_session")
neo_session.create_project(project_name="my_project")
```
## Step 1: Install the AgentNeo Package
Run the following command to install the agentneo package:

```py
pip install agentneo
```
## Step 2: Import Necessary Modules
Now that you've installed agentneo and set up your environment variables, it's time to import the required modules. Here's how to proceed:
```py 
# Import modules from agentneo
from agentneo import AgentNeo, Tracer, Evaluation, launch_dashboard
```
Here’s a brief overview of what each module does:

- AgentNeo: This class will be used to initialize and manage your AI agent.
- Tracer: The tracer will allow you to trace the execution of the agent's actions.
- Evaluation: This might be used to evaluate the performance of the agent based on metrics or goals.
- launch_dashboard: This function launches a dashboard to visualize and monitor the agent’s performance in real-time.

## Creating session
AgentNeo may require environment variables for configuration, such as API keys or other credentials. You'll likely use the python-dotenv package to load variables from a .env file.

Ensure you have python-dotenv installed:
```py
pip install python-dotenv

```
Then, create a .env file in your project directory with your environment variables, such as:
```py
# .env file
OPENAI_API_KEY=your_api_key_here
```
Now, you can load the .env variables in your Python script like this:

```py
from dotenv import load_dotenv
import os

load_dotenv("your env file path")
# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
```
## Step 4: Initialize AgentNeo Session
To start using AgentNeo, you'll need to initialize the session. Here’s an example that shows how to initialize an AgentNeo session:
```py 
neo_session = AgentNeo(session_name="my_session")
neo_session.create_project(project_name="my_project")
```
## **Tracer**

Tracing allows you to log and track the flow of the agent's actions and decisions for debugging and evaluation.
```py
tracer = Tracer(session=neo_session)
tracer.start()
```
