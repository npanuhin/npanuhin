from urllib.parse import urlparse, parse_qs
from os.path import isfile as os_isfile
from os import environ as os_environ
from requests import get as req_get
import json
import yaml
# import re

from events.events import parse_event


if os_isfile("GITHUB_TOKEN.txt"):
    with open('GITHUB_TOKEN.txt', 'r', encoding="utf-8") as file:
        GITHUB_TOKEN = file.read().strip()
else:
    GITHUB_TOKEN = os_environ["GITHUB_TOKEN"]


def test_events():
    print("Test mode")
    with open("config.yml", 'r', encoding="utf-8") as file:
        config = yaml.safe_load(file)

    with open("tests/events_test.json", 'r', encoding="utf-8") as file:
        events = json.load(file)

    print("Parsing events...")
    result_events = {}

    for event in events:
        new_result_events, new_hidden_events = parse_event(event)
        result_events.update(new_result_events)

    print("Checking events...")
    for event_id, event in list(result_events.items()):
        event.check()
        if not event.valid:
            del result_events[event_id]

    with open("tests/events_test_result.md", 'w', encoding="utf-8") as file:
        for event_id, event in result_events.items():
            assert event.valid is True
            print(event.format(config).replace(".github/icons/", "../../icons/"), end='\n\n', file=file)


def main():
    with open("config.yml", 'r', encoding="utf-8") as file:
        config = yaml.safe_load(file)

    with open("data.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
    # print("ETag:", data["etag"])
    data["etag"] = None  # Debug

    r = req_get(
        "https://api.github.com/users/{}/events/public".format(config["settings"]["username"]),
        headers={
            "accept": "application/vnd.github.v3+json",
            "Authorization": "token {}".format(GITHUB_TOKEN),
            "If-None-Match": data["etag"]
        },
        params={"per_page": 100}
    )
    data["etag"] = r.headers["etag"]

    # with open("page.json", 'w', encoding="utf-8") as file:
    #     json.dump(json.loads(r.text), file, ensure_ascii=False, indent=4)

    if r.status_code == 304:
        print("Activity unchanged")
        return None

    last_page = int(parse_qs(urlparse(r.links["last"]["url"]).query)["page"][0]) if "last" in r.links else 1
    # last_page = re.search(
    #     r"<https:\/\/api\.github\.com\/user\/\d+\/events\/public\?per_page=\d+&page=(\d+)>;\s*rel=\"last\"",
    #     r.headers["Link"],
    #     re.IGNORECASE
    # ).group(1)

    events = []
    for page in range(1, last_page + 1):
        print("Retrieving page {}...".format(page))

        events += json.loads(req_get(
            "https://api.github.com/users/{}/events/public".format(config["settings"]["username"]),
            headers={
                "accept": "application/vnd.github.v3+json",
                "Authorization": "token {}".format(GITHUB_TOKEN)
            },
            params={"per_page": 100, "page": page}
        ).text)

    if not events:
        print("Activity unchanged")
        return None

    result_events = data["events"]
    hidden_events = set()

    for event in events:
        new_result_events, new_hidden_events = parse_event(event)
        result_events.update(new_result_events)
        hidden_events.union(new_hidden_events)

    for event_id in hidden_events:
        del result_events[event_id]

    data["events"] = result_events

    print("Checking...")
    for event_id, event in list(result_events.items()):
        event.check()
        if not event.valid:
            del result_events[event_id]

    recent_events = [event for event_id, event in reversed(sorted(result_events.items()))]

    print("\nRecent events:")  # For debug only (private data)
    for event in recent_events:
        print(event.format(config))

    # with open("data.json", 'w', encoding="utf-8") as file:
    #     json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # test_events()
    main()
