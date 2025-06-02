"""
Retrieve LP DAAC Data Resources GitHub Traffic Metrics. 

Author: Erik Bolch, ebolch@contractor.usgs.gov

Usage:
    python lp_repo_metrics.py --token YOUR_PAT


"""
import os
import csv
import requests
import argparse
import sys
from datetime import datetime
from pathlib import Path

BASE_URL = "https://api.github.com"

REPOSITORIES = [
    ("nasa", "AppEEARS-Data-Resources"),
    ("nasa", "ECOSTRESS-Data-Resources"),
    ("nasa", "EMIT-Data-Resources"),
    ("nasa","GEDI-Data-Resources"),
    ("nasa","HLS-Data-Resources"),
    ("nasa","LPDAAC-Data-Resources"),
    ("nasa","VITALS")
]

METRICS_DIR = Path(__file__).parent.parent.parent / '_metrics'
METRICS_DIR.mkdir(exist_ok=True)
TRAFFIC_FILE = METRICS_DIR / 'traffic_metrics.csv'
REFERRERS_FILE = METRICS_DIR / 'referrers.csv'
CONTENT_FILE = METRICS_DIR / 'popular_content.csv'


def fetch_repo_traffic(owner: str, repo: str, token: str):
    """Fetch views, clones, referrers, and popular paths from GitHub Traffic API."""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    endpoints = {
        'views': f"{BASE_URL}/repos/{owner}/{repo}/traffic/views",
        'clones': f"{BASE_URL}/repos/{owner}/{repo}/traffic/clones",
        'referrers': f"{BASE_URL}/repos/{owner}/{repo}/traffic/popular/referrers",
        'paths': f"{BASE_URL}/repos/{owner}/{repo}/traffic/popular/paths"
    }
    results = {}
    for key, url in endpoints.items():
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        results[key] = resp.json()
    return results['views']['views'], results['clones']['clones'], results['referrers'], results['paths']


def append_to_csv(path: Path, header: list, rows: list):
    """Append rows to CSV; write header if file is new."""
    exists = path.exists()
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Daily GitHub traffic metrics collector"
    )
    parser.add_argument(
        '--token', default=None,
        help='GitHub PAT with repo scope (or set GITHUB_TOKEN)'
    )
    parser.add_argument(
        '--repos', nargs='*', default=None,
        help='List of owner/repo to override defaults'
    )
    args = parser.parse_args()

    token = args.token or os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GitHub token required", file=sys.stderr)
        sys.exit(1)

    if args.repos:
        try:
            repo_list = [tuple(r.split('/', 1)) for r in args.repos]
        except ValueError:
            print("Error: repos must be owner/repo", file=sys.stderr)
            sys.exit(1)
    else:
        repo_list = REPOSITORIES

    # Track existing (date,repo) to avoid duplicates
    existing = set()
    if TRAFFIC_FILE.exists():
        with open(TRAFFIC_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            date_idx = header.index('date')
            repo_idx = header.index('repository')
            for row in reader:
                existing.add((row[date_idx], row[repo_idx]))

    metrics_rows = []
    ref_rows = []
    content_rows = []
    run_date = datetime.now().strftime('%Y-%m-%d')
    for owner, repo in repo_list:
        views, clones, referrers, paths = fetch_repo_traffic(owner, repo, token)
        repo_id = f"{owner}/{repo}"
        # Map clones by date
        clone_map = {c['timestamp'][:10]: c for c in clones}
        # Daily metrics
        for v in views:
            day = v['timestamp'][:10]
            if (day, repo_id) in existing:
                continue
            vc, vu = v.get('count', 0), v.get('uniques', 0)
            cdata = clone_map.get(day, {})
            cc, cu = cdata.get('count', 0), cdata.get('uniques', 0)
            metrics_rows.append([day, repo_id, vc, vu, cc, cu])
        # Aggregate referrers and content at run date
        for ref in referrers:
            ref_rows.append([run_date, repo_id, ref.get('referrer', ''), ref.get('count', 0)])
        for p in paths:
            content_rows.append([run_date, repo_id, p.get('path', ''), p.get('count', 0), p.get('uniques', 0)])

    # Write CSVs
    append_to_csv(
        TRAFFIC_FILE,
        ['date', 'repository', 'views', 'unique views', 'clones', 'unique clones'],
        metrics_rows
    )
    append_to_csv(
        REFERRERS_FILE,
        ['date', 'repository', 'referrer', 'count'],
        ref_rows
    )
    append_to_csv(
        CONTENT_FILE,
        ['date', 'repository', 'path', 'count', 'uniques'],
        content_rows
    )

    print(f"Updated metrics in {METRICS_DIR}")

if __name__ == '__main__':
    main()
