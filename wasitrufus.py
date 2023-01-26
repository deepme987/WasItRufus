
import os
import git
import datetime

REPOSITORY_DIR = "Rep2Rec"


class BlameRufus:
    def __init__(self, git_dir: str = "") -> None:
        self._git_dir = os.getcwd() + "/" + git_dir
        self.Repo = None
        assert self.is_git_repo()

    def is_git_repo(self) -> bool:
        """ Tests whether the given directory is a valid directory/ repository """
        try:
            self.Repo = git.Repo(self._git_dir)
            return True
        except git.exc.InvalidGitRepositoryError:
            print("Not a valid Git Repository")
            return False
        except git.exc.NoSuchPathError:
            print("Not a valid Path")
            return False

    def active_branch(self) -> str:
        """ Fetch the current branch from the repository """

        """
        # Archived code to manually get the branch
        head_dir = self._git_dir + "/.git/HEAD"
        with open(head_dir, "r") as f:
            content = f.read().splitlines()

        for line in content:
            if line[0:4] == "ref:":
                return line.partition("refs/heads/")[2]
        """

        return self.Repo.active_branch

    def local_changes(self) -> bool:
        """" Returns a bool for any untracked changes in local repository """
        return self.Repo.is_dirty(untracked_files=True)

    def last_commit(self) -> bool:
        """ Returns a bool to indicate whether the last local commit was made within a week """
        week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).timestamp()
        commit_date = self.Repo.commit().committed_date
        return week_ago < commit_date

    def was_it_rufus(self, name: str = "Rufus") -> bool:
        """ It was not me, IT WAS RUFUS! """
        commit = self.Repo.commit()
        # Checks for name as well as email
        return any([name.lower() in author.lower() for author in [commit.author.name, commit.author.email]])


if __name__ == '__main__':
    rufus = BlameRufus(REPOSITORY_DIR)
    print(f"active branch: {rufus.active_branch()}")
    print(f"local changes: {rufus.local_changes()}")
    print(f"recent commit: {rufus.last_commit()}")
    print(f"blame Rufus: {rufus.was_it_rufus()}")
