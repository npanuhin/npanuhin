from utils import markdown_link


class WatchEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        if "action" not in event["payload"]:  # GitHub, why is your API not working
            event["payload"]["action"] = "started"

        # elif event["payload"]["action"] == "deleted":  # GitHub, why is your API not working
        #     hidden_events.add(event["id"])

        self.type = "starred"
        self.valid = (event["payload"]["action"] == "started")

    def format(self, config):
        return config["messages"][self.type].format(
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        pass
