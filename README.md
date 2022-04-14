# GH Repos

This script can be used to pull repo information from the GH API. There are two ways to use it:

### With Search Criteria (for name only)

`python main.py <search-term>`

Example: `python main.py collector`

### Pull All Repos

`python main.py`

### Results

Currently, this script is set up to retrieve the full name of the repo, the description (if applicaple), and the URL to the repo. If any additional information is required, please reach out to the developer to request additional fields. The list of available fields can be seen below in the `Additional Available Fields` section.

```json
[
  {
    "full_name": "string",
    "description": "string",
    "html_url": "string"
  }
]
```

### Additional Available Fields
```json
{
    "id": 12345678,
    "node_id": "string",
    "name": "string",
    "full_name": "string",
    "private": true,
    "owner": {
        "login": "string",
        "id": 987654321,
        "node_id": "string",
        "avatar_url": "string",
        "gravatar_id": "string",
        "url": "string",
        "html_url": "string",
        "followers_url": "string",
        "following_url": "string",
        "gists_url": "string",
        "starred_url": "string",
        "subscriptions_url": "string",
        "organizations_url": "string",
        "repos_url": "string",
        "events_url": "string",
        "received_events_url": "string",
        "type": "string",
        "site_admin": false
    },
    "html_url": "string",
    "description": "string",
    "fork": false,
    "url": "string",
    "forks_url": "string",
    "keys_url": "string",
    "collaborators_url": "string",
    "teams_url": "string",
    "hooks_url": "string",
    "issue_events_url": "string",
    "events_url": "string",
    "assignees_url": "string",
    "branches_url": "string",
    "tags_url": "string",
    "blobs_url": "string",
    "git_tags_url": "string",
    "git_refs_url": "string",
    "trees_url": "string",
    "statuses_url": "string",
    "languages_url": "string",
    "stargazers_url": "string",
    "contributors_url": "string",
    "subscribers_url": "string",
    "subscription_url": "string",
    "commits_url": "string",
    "git_commits_url": "string",
    "comments_url": "string",
    "issue_comment_url": "string",
    "contents_url": "string",
    "compare_url": "string",
    "merges_url": "string",
    "archive_url": "string",
    "downloads_url": "string",
    "issues_url": "string",
    "pulls_url": "string",
    "milestones_url": "string",
    "notifications_url": "string",
    "labels_url": "string",
    "releases_url": "string",
    "deployments_url": "string",
    "created_at": "string",
    "updated_at": "string",
    "pushed_at": "string",
    "git_url": "string",
    "ssh_url": "string",
    "clone_url": "string",
    "svn_url": "string",
    "homepage": null,
    "size": 42,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "string",
    "has_issues": true,
    "has_projects": false,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "archived": true,
    "disabled": false,
    "open_issues_count": 0,
    "license": null,
    "allow_forking": true,
    "is_template": false,
    "topics": [
        "string",
        "string",
        "string"
    ],
    "visibility": "string",
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "string",
    "permissions": {
        "admin": false,
        "maintain": false,
        "push": false,
        "triage": false,
        "pull": true
    }
}
```
