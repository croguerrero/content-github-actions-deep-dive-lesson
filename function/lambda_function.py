from tkinter import EventType
from github import Github

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n------------------------------------------------------')
    
    if event["imput"] == "hello":
        return "World!"
    else: 
        raise Exception("Invalid input")
        
