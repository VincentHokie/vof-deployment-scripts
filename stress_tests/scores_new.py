from locust import HttpLocust, TaskSet
import learners_urls, program_urls, urls
import urllib3
urllib3.disable_warnings()

# script used to reproduce the ZeroDivisionError bug
# that was plagueing the production environment
# documented here 
# (https://docs.google.com/document/d/1GflqDwDJh8JNTBBu6MfaZwszzsK7V9tiU81G1Sw05KM/edit?usp=sharing)


class UserBehavior(TaskSet):

    def on_start(self):
        self.client.verify = False

    tasks = {
        learners_urls.post_add_scores: 1
    }


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10
    max_wait = 10
