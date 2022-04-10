from urllib.parse import quote

import feedparser

GITHUB_URL = "https://github.com"


class Tags:
    def __init__(self, user: str, project: str, base: str = GITHUB_URL):
        user, project = quote(user), quote(project)
        self.atom_url = "%s/%s/%s/tags.atom" % (base, user, project)

    def get(self) -> feedparser.FeedParserDict:
        return feedparser.parse(self.atom_url)
