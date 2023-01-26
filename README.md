# WasItRufus
Assessment for WasItRufus?

Here, I'm using one of my existing repo for test purpose: https://github.com/deepme987/Rep2Rec

Installation: `pip install GitPython`

To initialize (main): `rufus = BlameRufus(git_dir_name)`

Sample output (initial commits are from a week ago)
```angular2html
active branch: master
local changes: False
recent commit: False
blame Rufus: False
```

After making changes (no commit yet):

```angular2html
active branch: master
local changes: True
recent commit: False
blame Rufus: False
```

After committing the change, note: author tested was `"Deep"` here, not `"Rufus"`:

```angular2html
active branch: master
local changes: False
recent commit: True
blame Rufus: True
```

After changing the branch:

```angular2html
active branch: test
local changes: False
recent commit: True
blame Rufus: True
```