from requests import head as req_head
from utils import markdown_link


class ReleaseEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        if "action" not in event["payload"]:  # GitHub, why is your API not working
            event["payload"]["action"] = "published"

        # elif event["payload"]["action"] == "deleted":  # GitHub, why is your API not working
        #     hidden_events.add(event["id"])

        self.type = "released"
        self.valid = (event["payload"]["action"] == "published")

    def format(self, config):
        return config["messages"][self.type].format(
            ID=markdown_link(
                self.event["payload"]["release"]["name"],
                self.event["payload"]["release"]["html_url"]
            ),
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        self.valid = (req_head(self.event["payload"]["release"]["html_url"]).status_code == 200)
