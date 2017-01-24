# Imports the Google Cloud client library
from google.cloud import datastore

# Instantiates a client
datastore_client = datastore.Client()

print("Created Client")

# The kind for the new entity
kind = 'cik-mappings'
# The name/ID for the new entity
name = 'sampletask1'
# The Cloud Datastore key for the new entity
task_key = datastore_client.key(kind, name)


print("Created Key")

# Prepares the new entity
task = datastore.Entity(key=task_key)
task['description'] = 'Buy milk'

print("Prepared Entity")

# Saves the entity
datastore_client.put(task)

print('Saved {}: {}'.format(task.key.name, task['description']))