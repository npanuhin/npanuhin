from utils import markdown_link


class CommentEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]
        self.type = "comment"

        if "action" not in event["payload"]:  # GitHub, why is your API not working
            event["payload"]["action"] = "created"

        if event["payload"]["action"] == "created":
            if event["type"] == "CommitCommentEvent":
                self.name = event["payload"]["comment"]["commit_id"][-7:]
            elif event["type"] == "IssueCommentEvent":
                self.name = '#' + str(event["payload"]["issue"]["number"])
            elif event["type"] == "PullRequestReviewCommentEvent":
                self.name = '#' + str(event["payload"]["pull_request"]["number"])

        # elif event["payload"]["action"] == "deleted":  # GitHub, why is your API not working
        #     hidden_events.add(event["id"])
        #     return True

        self.type = "comment"
        self.valid = (event["payload"]["action"] == "created")

    def format(self, config):
        return config["messages"][self.type].format(
            ID=markdown_link(self.name, self.event["payload"]["comment"]["html_url"]),
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        pass
