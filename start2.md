# ![AgentNeo](https://docs.raga.ai/~gitbook/image?url=https%3A%2F%2F1811327582-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FYbIiNdp1QbG4avl7VShw%252Ficon%252FdbhstYExc7neijc5XvVC%252Flogo%2520only%2520svg%25201.png%3Falt%3Dmedia%26token%3D16999011-17eb-41c9-9ee8-26837edcf88f&width=32&dpr=1&quality=100&sign=f91ac5a2&sv=1)**AgentNeo**
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
The Tracer is a critical component of AgentNeo that facilitates the monitoring and recording of your agent's activities during execution. It provides insights into how the agent operates, allowing you to debug issues, analyze performance, and evaluate decision-making processes. 
- Trace LLM Calls: Monitor and analyze LLM calls from various providers like OpenAI and LiteLLM.
- Trace Agents and Tools: Instrument and monitor your agents and tools to gain deeper insights into their behavior.

How to Initialize and Start the Tracer
```py
tracer = Tracer(session=neo_session)
tracer.start()
```
### Example
```py
@tracer.trace_llm("my_llm_call")
async def my_llm_function():
    # Your LLM call here
    pass

@tracer.trace_tool("my_tool")
def my_tool_function():
    # Your tool logic here
    pass

@tracer.trace_agent("my_agent")
def my_agent_function():
    # Your agent logic here
    pass
```
After using execution and evalution model you have to stop tracer
Here's how to do it:
```py
tracer.stop()
```
This  method signals the end of the tracing session, ensuring that all recorded data related to your agent's execution is finalized and saved for later analysis.

## **Execution**
Utilizing the Execution class in AgentNeo provides you with a powerful way to gain insights into your application's performance and flow. By running specific metrics and retrieving detailed execution results, you can visualize how your AI agent operates under different conditions
Here's how to do it:
### Step 1. Create an Execution Instance: Initialize an Execution object by providing the session and trace ID:

```py
exe = Evaluation(session=neo_session, trace_id=tracer.trace_id)
```

session: This refers to the current session you established, ensuring that all metrics and traces are logged correctly.

trace_id: This unique identifier allows you to focus on a current  tracer within your session, providing clarity in your evaluations.


### Step 2. Retrieve and Print Results: Obtain the results of the evaluation and print them:
```py
metric_results = exe.get_results()
print(metric_results)
```
exe.get_results(): This method retrieves the evaluation results for the executed metrics, which may include numerical values, trends, or visual representations based on the metric's nature.

print(metric_results): Printing the results provides real-time insights into your AI agent's performance, helping you identify improvement areas or confirm that it meets the expected performance criteria.

## **Launch Dashboard**
```py
neo_session.launch_dashboard()
```
To visualize and analyze the performance data collected during your AI agent's execution, you can launch the interactive dashboard using the neo_session.launch_dashboard() method. This feature provides a user-friendly interface for exploring the metrics and execution traces.
