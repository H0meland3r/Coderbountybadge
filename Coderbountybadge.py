import requests

def create_coderbounty_badge(user, repo, issue_number):
    url = f"https://coderbounty.com/create_badge/{user}/{repo}/{issue_number}"
    badge_url = requests.get(url).text
    return badge_url

user = "username"
repo = "repo"
issue_number = "1"
badge_url = create_coderbounty_badge(user, repo, issue_number)
print(badge_url)
