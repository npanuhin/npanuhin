from requests import head as req_head
from utils import markdown_link

from os import environ as os_environ


class PullRequestReviewEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        if "action" not in event["payload"]:  # GitHub, why is your API not working
            event["payload"]["action"] = "created"

        # elif event["payload"]["action"] == "deleted":  # GitHub, why is your API not working
        #     hidden_events.add(event["id"])

        self.type = "changes_{}".format("approved" if event["payload"]["review"]["state"] == "approved" else "requested")
        self.valid = (
            event["payload"]["action"] == "created" and
            event["payload"]["review"]["state"] in ("approved", "changes_requested")
        )

    def format(self, config):
        return config["messages"][self.type].format(
            ID=markdown_link(
                '#' + str(self.event["payload"]["pull_request"]["number"]),
                self.event["payload"]["review"]["html_url"]
            ),
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        self.valid = (req_head(
            "https://api.github.com/repos/{}/pulls/{}/reviews/{}".format(
                self.event["repo"]["name"],
                self.event["payload"]["pull_request"]["number"],
                self.event["payload"]["review"]["id"]
            ),
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": "token {}".format(os_environ["GITHUB_TOKEN"])
            }
        ).status_code == 200)
