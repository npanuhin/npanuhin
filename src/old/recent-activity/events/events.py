from events.CommentEvent import CommentEvent
from events.CreateEvent import CreateEvent
from events.ForkEvent import ForkEvent
from events.GollumEvent import GollumEvent, parse_gollum_events
from events.IssuesEvent import IssuesEvent
from events.PullRequestEvent import PullRequestEvent
from events.PullRequestReviewEvent import PullRequestReviewEvent
from events.ReleaseEvent import ReleaseEvent
from events.WatchEvent import WatchEvent


def parse_event(event):
    result_events = {}
    hidden_events = set()

    def add_to_result(event):
        if event.valid:
            result_events[event.id] = event
        else:
            hidden_events.add(event.id)

    if event["type"] in ("CommitCommentEvent", "IssueCommentEvent", "PullRequestReviewCommentEvent"):
        add_to_result(CommentEvent(event))

    elif event["type"] == "CreateEvent":
        add_to_result(CreateEvent(event))

    elif event["type"] == "ForkEvent":
        add_to_result(ForkEvent(event))

    elif event["type"] == "GollumEvent":
        for event in parse_gollum_events(event):
            add_to_result(GollumEvent(event))

    elif event["type"] == "IssuesEvent":
        add_to_result(IssuesEvent(event))

    # elif event["type"] == "MemberEvent":
    #     if "action" not in event["payload"]:  # GitHub, why is your API not working
    #         event["payload"]["action"] = "added"

    #     if event["payload"]["action"] == "added":
    #         result_events[event["id"]] = {
    #             "type": "collaboration",
    #             "repo_name": event["repo"]["name"],
    #             "repo_url": github_url(event["repo"]["name"])
    #         }

    #     # elif event["payload"]["action"] == "deleted":  # GitHub, why is your API not working
    #     #     hidden_events.add(event["id"])

    elif event["type"] == "PullRequestEvent":
        add_to_result(PullRequestEvent(event))

    elif event["type"] == "PullRequestReviewEvent":
        add_to_result(PullRequestReviewEvent(event))

    elif event["type"] == "ReleaseEvent":
        add_to_result(ReleaseEvent(event))

    elif event["type"] == "WatchEvent":
        add_to_result(WatchEvent(event))

    return result_events, hidden_events
