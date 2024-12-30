from requests import head as req_head
from utils import markdown_link


class PullRequestEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        if "action" not in event["payload"]:  # GitHub, why is your API not working x3
            event["payload"]["action"] = "opened"

        # elif event["payload"]["action"] == "deleted":  # GitHub, why is your API not working
        #     hidden_events.add(event["id"])

        self.type = "pr_{}".format(
            "merged" if event["payload"]["pull_request"]["merged"] else event["payload"]["action"]
        )
        self.valid = (event["payload"]["action"] in ("opened", "reopened", "closed"))

    def format(self, config):
        return config["messages"][self.type].format(
            ID=markdown_link(
                '#' + str(self.event["payload"]["pull_request"]["number"]),
                self.event["payload"]["pull_request"]["html_url"]
            ),
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        self.valid = (req_head(self.event["payload"]["pull_request"]["html_url"]).status_code == 200)
