from locust import HttpUser,TaskSet,task
import json


class Test_1(HttpUser):
    @task

    def users(self):
        f = open("C:/Users/cnaga1/Locust/Locust_demo/data.json")
        data = json.load(f)
        response=self.client.post("/posts",name="demo_RestAPi",json=data
    
    )
        print(response.text)

class UserBehaviour(Test_1)   :
    #task_set=Test_1
    min_wait=5000
    max_wait=9000
    host="https://jsonplaceholder.typicode.com/"
   
    
  

      
        
    

        


