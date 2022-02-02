from urllib.parse import urlunsplit


def github_url(path):
    return urlunsplit(("https", "github.com", path, "", ""))


def markdown_link(name, url=None):
    if url is None:
        url = github_url(name)

    return "[{}]({})".format(name, url)
