try:from github import Github
except ImportError:import os;os.system(f"pip install PyGithub")
from github import Github
Token="ghp_UR_Token"
repository="GIC"
path="main.py"
while True:git=Github(Token);repo=git.get_repo(f"{git.get_user().login}/{repository}");file=repo.get_contents(path);repo.update_file(file.path,repo.get_commits(path=path).get_page(0)[0].commit.message,f'{file.decoded_content.decode("utf-8")}',file.sha)
