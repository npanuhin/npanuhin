from utils import markdown_link, github_url
from requests import head as req_head


class ForkEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        self.type = "repo_forked"
        self.valid = True

    def format(self, config):
        return config["messages"][self.type].format(
            FORK=markdown_link(self.event["payload"]["forkee"]["full_name"]),
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        self.valid = (req_head(github_url(self.event["payload"]["forkee"]["full_name"])).status_code == 200)
