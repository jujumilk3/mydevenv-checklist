#!/usr/bin/env python3
import subprocess

import iterm2


async def get_git_info(path):
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=path,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return ""

        branch = subprocess.run(
            ["git", "symbolic-ref", "--short", "HEAD"],
            cwd=path,
            capture_output=True,
            text=True,
        ).stdout.strip()

        numstat = subprocess.run(
            ["git", "diff", "HEAD", "--numstat"],
            cwd=path,
            capture_output=True,
            text=True,
        ).stdout.strip()

        inserted = deleted = 0
        for line in numstat.splitlines():
            parts = line.split("\t")
            if len(parts) >= 2:
                try:
                    inserted += int(parts[0])
                    deleted += int(parts[1])
                except ValueError:
                    pass

        diff = ""
        if inserted:
            diff += f"+{inserted}"
        if deleted:
            diff += f" -{deleted}"

        return f"⎇ {branch}  |  {diff}".strip() if diff else f"⎇ {branch}"
    except Exception:
        return "⎇"


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Git Status",
        detailed_description="Branch and diff lines",
        knobs=[],
        exemplar="⎇ main +10 -3",
        update_cadence=10,
        identifier="com.custom.gitstatus",
    )

    @iterm2.StatusBarRPC
    async def git_status_coroutine(knobs, path=iterm2.Reference("path")):
        if not path:
            return "⎇"
        return await get_git_info(path)

    await component.async_register(connection, git_status_coroutine)
    await iterm2.async_get_app(connection)


iterm2.run_forever(main)

# vim ~/Library/Application\ Support/iTerm2/Scripts/AutoLaunch/git_status.py
