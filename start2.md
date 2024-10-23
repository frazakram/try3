![AgentNeo](https://docs.raga.ai/~gitbook/image?url=https%3A%2F%2F1811327582-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FYbIiNdp1QbG4avl7VShw%252Ficon%252FdbhstYExc7neijc5XvVC%252Flogo%2520only%2520svg%25201.png%3Falt%3Dmedia%26token%3D16999011-17eb-41c9-9ee8-26837edcf88f&width=32&dpr=1&quality=100&sign=f91ac5a2&sv=1)**AgentNeo**

## Introduction
### **Observability and Evaluation of AI Agentic applications**
AgentNeo helps AI engineers build better AI from development through deployment.AgentNeo include:
- [**Creating session**](#creatingsession)
- [**Tracer**](#Tracer)
- [**Execution**](#Execution)
- [**Evaluation**](#Evaluation)
## Get started with our guides
### Step 1: Install the AgentNeo Package
Run the following command to install the agentneo package:

```bash
pip install agentneo
```
### Step 2: Import Necessary Modules
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
## **Creating session**
Initialize AgentNeo Session
The first step in using AgentNeo is to set up a session, which serves as the foundation for managing your project, tracing executions, and evaluating performance. Initializing a session ensures that AgentNeo can track all relevant data and interactions during the runtime of your agent.

Here’s how to initialize a session and create a project:
```py 
neo_session = AgentNeo(session_name="my_session")
neo_session.create_project(project_name="my_project")
```
## **Tracer**
The Tracer is a critical component of AgentNeo that facilitates the monitoring and recording of your agent's activities during execution. It provides insights into how the agent operates, allowing you to debug issues, analyze performance, and evaluate decision-making processes. By implementing tracing, you can capture detailed logs of your agent's interactions with various components, such as external APIs or internal functions.

How to Initialize and Start the Tracer
```py
tracer = Tracer(session=neo_session)
tracer.start()
```
