
def categorize(entities):
    for token in entities:
        if token['type'] == 'ACTION':
            perform_action(token['value'])
        elif token['type'] == 'location':
            print('Location:', token['value'])
        elif token['type'] == 'datetime':
            print('Datetime:', token['value'])
        elif token['type'] == 'reminder':
            print('Reminder:', token['value'])
        elif token['type'] == 'note':
            print('Note:', token['value'])
        else:
            print('Unknown:', token['value'])

def perform_action(action):
    print('Performing action:', action)