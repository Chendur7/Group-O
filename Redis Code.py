import redis

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Namespace for storing irrigation method data
irrigation_method_namespace = 'IrrigationSchedule'

# Create operation
def create_irrigation_method(method, days_of_week, location):
    key = f"{irrigation_method_namespace}:{method}"
    data = {'days_of_week': days_of_week, 'location': location}
    r.hmset(key, data)
    print(f"Irrigation method '{method}' created.")

# Read operation
def read_irrigation_method(method):
    key = f"{irrigation_method_namespace}:{method}"
    data = r.hgetall(key)
    if data:
        return data
    else:
        return f"Irrigation method '{method}' not found."

# Update operation
def update_irrigation_method(method, days_of_week=None, location=None):
    key = f"{irrigation_method_namespace}:{method}"
    existing_data = r.hgetall(key)
    if not existing_data:
        return f"Irrigation method '{method}' not found."
    
    if days_of_week:
        r.hset(key, 'days_of_week', days_of_week)
    if location:
        r.hset(key, 'location', location)
    
    print(f"Irrigation method '{method}' updated.")

# Delete operation
def delete_irrigation_method(method):
    key = f"{irrigation_method_namespace}:{method}"
    deleted = r.delete(key)
    if deleted:
        print(f"Irrigation method '{method}' deleted.")
    else:
        print(f"Irrigation method '{method}' not found.")

# Example usage
create_irrigation_method('Drip Irrigation', 'Monday, Wednesday, Friday', 'Paris, France')
print(read_irrigation_method('Drip Irrigation'))
update_irrigation_method('Drip Irrigation', days_of_week='Tuesday, Thursday, Saturday')
print(read_irrigation_method('Drip Irrigation'))
delete_irrigation_method('Drip Irrigation')
print(read_irrigation_method('Drip Irrigation'))
