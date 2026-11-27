#!/usr/bin/env python3
# usage: python3 scripts/dsa.py [next|test|progress]
import datetime as dt
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROADMAP = json.loads((ROOT / "roadmap.json").read_text())
BY_ID = {p["id"]: p for p in ROADMAP}


def solved_dirs():
    return sorted(d for d in ROOT.glob("[0-9][0-9][0-9]-*") if (d / "solution.py").exists())


def date_added(d):
    out = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%ad", "--date=short", "--", f"{d.name}/solution.py"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()
    return out[-1] if out else dt.date.today().isoformat()


def next_problem():
    done = {int(d.name[:3]) for d in solved_dirs()}
    todo = [p for p in ROADMAP if p["id"] not in done]
    if not todo:
        print("all done")
        return
    p = todo[0]
    print(json.dumps({**p, "folder": f"{p['id']:03d}-{p['slug']}"}, indent=2))


def daily_dirs():
    # leetcode daily challenge, folders named YYYY-MM-DD-slug
    return sorted(d for d in (ROOT / "daily").glob("*") if (d / "solution.py").exists())


def daily_info(d):
    # first line of notes.md: "# 3946. Some Title (Medium)"
    first = (d / "notes.md").read_text().splitlines()[0].lstrip("# ").strip()
    num_title, _, diff = first.rpartition(" (")
    return d.name[:10], num_title, diff.rstrip(")")


def test():
    failed = []
    for d in solved_dirs() + daily_dirs():
        r = subprocess.run([sys.executable, "-I", str(d / "solution.py")], capture_output=True, text=True)
        print(("ok    " if r.returncode == 0 else "FAIL  ") + d.relative_to(ROOT).as_posix())
        if r.returncode:
            print(r.stdout + r.stderr)
            failed.append(d.name)
    sys.exit(1 if failed else 0)


def streak(dates):
    days = {dt.date.fromisoformat(x) for x in dates}
    cur = dt.date.today()
    if cur not in days:
        cur -= dt.timedelta(days=1)
    n = 0
    while cur in days:
        n += 1
        cur -= dt.timedelta(days=1)
    return n


def progress():
    rows = []
    for d in solved_dirs():
        p = BY_ID[int(d.name[:3])]
        rows.append((p, d.name, date_added(d)))

    table = [f"## Solved ({len(rows)}/{len(ROADMAP)})", "",
             "| # | Problem | Difficulty | Topic | Date |", "|---|---|---|---|---|"]
    for p, folder, day in reversed(rows):
        table.append(f"| {p['id']} | [{p['title']}]({folder}/) | {p['difficulty']} | {p['topic']} | {day} |")

    daily = [(d, *daily_info(d)) for d in daily_dirs()]
    if daily:
        table += ["", f"## LeetCode daily ({len(daily)})", "",
                  "| Date | Problem | Difficulty |", "|---|---|---|"]
        for d, day, title, diff in reversed(daily):
            table.append(f"| {day} | [{title}](daily/{d.name}/) | {diff} |")

    readme = ROOT / "README.md"
    text = readme.read_text()
    head = text.split("## Solved")[0].rstrip()
    readme.write_text(head + "\n\n" + "\n".join(table) + "\n")

    diff = Counter(p["difficulty"] for p, _, _ in rows)
    stats = {
        "solved": len(rows),
        "total": len(ROADMAP),
        "streak": streak(day for _, _, day in rows),
        "easy": diff["Easy"],
        "medium": diff["Medium"],
        "hard": diff["Hard"],
        "last_solved": rows[-1][0]["title"] if rows else None,
        "daily": len(daily),
    }
    (ROOT / "stats.json").write_text(json.dumps(stats, indent=2) + "\n")
    print(stats)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    {"next": next_problem, "test": test, "progress": progress}.get(cmd, lambda: print(__doc__ or "next | test | progress"))()
