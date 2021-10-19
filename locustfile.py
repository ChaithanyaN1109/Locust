from locust import HttpUser,TaskSet,task
import json
import locust.stats
locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 1 second
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 60 # Determines how often the data is flushed to disk, default is 10 seconds


class Test_1(HttpUser):
    @task

    def users(self):
        f = open("data.json")
        data = json.load(f)
        response=self.client.post("/posts",name="demo_RestAPi",json=data
    
    )
        print(response.text)

class UserBehaviour(Test_1)   :
    #task_set=Test_1
    min_wait=5000
    max_wait=9000
    host="https://jsonplaceholder.typicode.com/"
