#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import git
import os
from datetime import datetime, timedelta
import argparse

art = [
    "       ",
    " xx xx ",
    " xx xx ",
    "       ",
    " x   x ",
    "  xxx  ",
    "       ",
]  # Ascii art to be printed (space = full dark, x, nothing)


def init(folder="gitlab-history"):
    repo = git.Repo.init(os.path.join("..", folder))
    return repo


def commit_on_date(repo, date):
    actor = git.Actor("crazyiop", "crazyiop@gmail.com")
    repo.index.commit(
        ":)",
        author=actor,
        committer=actor,
        author_date=datetime(date.year, date.month, date.day, 12).strftime(
            f"%Y-%m-%dT%H:%M:%S +0200"
        ),
        commit_date=datetime(date.year, date.month, date.day, 12).strftime(
            f"%Y-%m-%dT%H:%M:%S +0200"
        ),
    )


if __name__ == "__main__":
    now = datetime.now()
    start_time = datetime(now.year, now.month, now.day) - timedelta(
        days=now.weekday() + 15 * 7 + 1  # +1 as gitlab activity start on sunday
    )

    repo = init()
    for day_offset, line in enumerate(art):
        for week_offset, char in enumerate(line):
            if char == " ":
                d = start_time + timedelta(days=day_offset + 7 * week_offset)
                print("marking", d)
                for _ in range(31):
                    commit_on_date(repo, d)
