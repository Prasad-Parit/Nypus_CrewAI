from tkinter import Tk, Label, Entry, Button, Text, END
from agents import ContentCreationAgents
from tasks import ContentCreationTasks

# Instantiate the agents and tasks
content_agents = ContentCreationAgents()
content_tasks = ContentCreationTasks()

# Function to execute a task based on GUI inputs
def execute_task():
    try:
        # Get the inputs from the GUI
        target_audience = target_audience_entry.get()
        industry_context = industry_context_entry.get()
        keywords = keywords_entry.get()
        content_context = content_context_entry.get()

        # Ensure inputs are provided
        if not (target_audience and industry_context and keywords and content_context):
            results_text.delete(1.0, END)
            results_text.insert(END, "Please fill in all the fields.")
            return

        # Example: Connect inputs to ContentCreationTasks or agents
        content_tasks = ContentCreationTasks()
        trend_research_task = content_tasks.trend_research_task(
            target_audience=target_audience,
            industry_context=industry_context,
            keywords=keywords.split(", "),  # Splitting keywords into a list
            content_context=content_context,
        )

        # Example: Assign the task to the Trend Researcher agent and execute
        agents = ContentCreationAgents()
        trend_researcher = agents.trend_researcher()
        result = trend_researcher.execute(trend_research_task)

        # Display the result in the Results section
        results_text.delete(1.0, END)
        results_text.insert(END, result)

    except Exception as e:
        # Show error messages in the Results section
        results_text.delete(1.0, END)
        results_text.insert(END, f"An error occurred: {str(e)}")
 

# GUI setup
window = Tk()
window.title("Marketing Campaign Generator")

# Input fields
Label(window, text="Target Audience").pack()
target_audience_entry = Entry(window)
target_audience_entry.pack()

Label(window, text="Industry Context").pack()
industry_context_entry = Entry(window)
industry_context_entry.pack()

Label(window, text="Keywords").pack()
keywords_entry = Entry(window)
keywords_entry.pack()

Label(window, text="Content Context").pack()
content_context_entry = Entry(window)
content_context_entry.pack()

# Execute button
execute_button = Button(window, text="Execute", command=execute_task)
execute_button.pack()

# Results section
Label(window, text="Results:").pack()
results_text = Text(window, height=10, width=50)
results_text.pack()

# Run the GUI
window.mainloop()
