import argparse
import requests
import json

ISSUE_TYPE = "ISSUE_TYPE"
ISSUE_TYPE_ARTICLE = "article"
ARTICLE_DB_PATH = "../db/article.json"

url = "https://api.github.com/repos/yamamoto-yuta/hugo-docker-test/issues"


def parse_label(label_name):
    """
    Parse label to name and value

    Parameters
    ----------
    label_name: str
        label name

    Returns
    -------
    item_name: str
        item name
    item_value: str
        item value
    """
    splited_text = label_name.split(":")
    item_name = splited_text[0]
    item_value = splited_text[1].strip()
    return item_name, item_value


def identify_issue(issue_labels):
    """
    Identify issue

    Parameters
    ----------
    issue_labels: list
        label list of issue

    Returns
    -------
    issue_identifier: dict
        issue identifier
    """
    issue_identifier = {}
    for label in issue_labels:
        item_name, item_value = parse_label(label["name"])
        issue_identifier[item_name] = item_value
    return issue_identifier


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("article_db_path", help="Path of Article DB")
    args = parser.parse_args()

    data = requests.get(
        url,
        {"state": "closed"},
    )
    if data.status_code != requests.codes.ok:
        print("Error: " + data.status_code)
        exit(1)

    issue_list = data.json()

    print(len(issue_list))

    article_list = []
    for issue in issue_list:
        issue_identifier = identify_issue(issue["labels"])
        if (
            ISSUE_TYPE in issue_identifier.keys()
            and issue_identifier[ISSUE_TYPE] == ISSUE_TYPE_ARTICLE
        ):
            article_list.append(
                {
                    "number": issue["number"],
                    "title": issue["title"],
                    "date": issue["closed_at"],
                    "body": issue["body"],
                }
            )

    with open(args.article_db_path, "w") as f:
        f.write(json.dumps(article_list))
