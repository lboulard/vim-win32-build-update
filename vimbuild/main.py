import calendar
import sys
from datetime import datetime, timezone
from typing import List

from .github import Tags


def main(args: List[str]):
    feed = Tags("vim", "vim").get()
    if feed.entries:
        entry = feed.entries[0]
        since, tag, updated = 0, "failed", "1970-01-01T00:00:00Z"
        try:
            if entry.link:
                tag = entry.link.split("/")[-1]
            updated = entry.updated
            # feedparser is seriously broken regarding time parsing
            dt = datetime.fromtimestamp(
                calendar.timegm(entry.updated_parsed), tz=timezone.utc
            )
            since = int((datetime.now(tz=timezone.utc) - dt).total_seconds())
        except IndexError:
            pass
        print(since, tag, updated)


def cli():
    main(sys.argv)
