
class BlameRufus:
    def __init__(self, git_dir):
        self._git_dir = git_dir

    def active_branch(self):
        head_dir = self._git_dir + "/.git/HEAD"
        with head_dir.open("r") as f:
            content = f.read().splitlines()

        for line in content:
            if line[0:4] == "ref:":
                return line.partition("refs/heads/")[2]

    def local_changes(self):

if __name__ == '__main__':
