#This is a super basic script to help me understand what scripting is

import requests #requests is in a library of tools; requests specifically handles HTTP requests

def fetch_data(): #This is a function. We named it fetch_data because the code below it will use a get request
	response = requests.get("https://totallylegitjson.randomstuff.com") #We add quotes to make it a string. This is an example so don't actually go to a website
	tasks = response.json() #For legit json responses, we use this to organize the JSON into a python list
	return tasks
	
def process_data(tasks): #This function is designed to filter tasks that are actually completed
	completed_tasks = [task for task in tasks if task['completed']]
	return completed_tasks
	
def main():
	tasks = fetch_data() #This will fetch all tasks from the API
	completed_tasks = process_data(tasks) #This helps find completed tasks 
	#The below print jobs will display the results 
	print(f"Total number of tasks: {len(tasks)}")
	print(f"Number of completed tasks: {len(completed_tasks)}")
	
if __name__ == "__main__": #This is a little confusing, but it allows you to isolate the main body of code, so you can resuse functions in other scripts 
	main()