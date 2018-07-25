from locust import HttpLocust, TaskSet, task
import uuid
from datetime import datetime
import json
 
headers={'authorization' : "Bearer 7a17c26f04a3acc608973b571009e64248e00713c96164406823d0b37dbc74c5"}
 
class Tasks(TaskSet):
@task()
def redeemption(self):
self.client.get("feeds/mnm", headers=headers)
self.client.get("feeds/mnm?product_id=3K", headers=headers)
 
class Tasks(HttpLocust):
task_set = Tasks
min_wait = 5000
max_wait = 9000
