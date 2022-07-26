from github import Github

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------'
            '-----------------------------------------------------')
    print('Event: {}'.format(event))
    print('Context: {}'.format(context))
    print('---------------------------------------------'        '-----------------------------------------------------')
    print('Finished functions\n---------------------------------------------'     '-----------------------------------------------------')
    return 'Hello World!'
