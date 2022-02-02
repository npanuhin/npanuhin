from requests import head as req_head
from utils import markdown_link
from copy import deepcopy


class GollumEvent:
    def __init__(self, event):
        self.event = event
        self.id = event["id"]

        self.wiki_page_obj = event["payload"]["pages"][int(event["id"][event["id"].rfind('_') + 1:])]

        if "action" not in self.wiki_page_obj:  # GitHub, why is your API not working
            self.wiki_page_obj["action"] = "created"

        self.type = "wiki_created"
        self.valid = (self.wiki_page_obj["action"] == "created")

    def format(self, config):
        return config["messages"][self.type].format(
            WIKI=markdown_link(self.wiki_page_obj["title"], self.wiki_page_obj["html_url"]),
            REPO=markdown_link(self.event["repo"]["name"])
        )

    def check(self):
        self.valid = (req_head(self.wiki_page_obj["html_url"]).status_code == 200)


def parse_gollum_events(event):
    for wiki_page in range(len(event["payload"]["pages"])):

        new_event = deepcopy(event)

        new_event["id"] = "{}_{}".format(new_event["id"], wiki_page)

        yield new_event
