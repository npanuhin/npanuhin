from utils import markdown_link, github_url
from requests import head as req_head


class CreateEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        self.type = "repo_created"
        self.valid = (event["payload"]["ref_type"] == "repository")

    def format(self, config):
        return config["messages"][self.type].format(
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        self.valid = (req_head(github_url(self.event["repo"]["name"])).status_code == 200)
