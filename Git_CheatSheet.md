<!--
/**
 * @ Title:		Git_CheatSheet.md
 * @ Authors:	siqin.hou (xiangxing985529@163.com)
 * @ Date:		2017-05-23 07:17:33
 * @ Version:	0.0.1
 */
-->

[返回xiangxing98的Github主页](https://xiangxing98.github.io/ "返回xiangxing98的Github主页")

[返回xiangxing98的Github Profile](https://github.com/xiangxing98/ "返回xiangxing98的Github Profile")

## All Git Command CheatSheet
> Gitella

## Start
Initialize a repository
```
git init
```

Clone a remote repository
```
git clone URL_REPOSITORY
```

Show files modified
```
git status
```

Add all the files your changed
```
git add --all
```

Commit changes with a message
```
git commit -m "MESSAGE" 
```

Pull changes from remotes
```
git pull origin REMOTE_BRANCH
```

## Branches

Create a local branch
```
git checkout -b LOCAL_BRANCH
```

Show the local branched list
```
git branch
```

Switch between branches
```
git checkout LOCAL_BRANCH
```

Create a local remote branch from a local one
```
git push origin LOCAL_BRANCH:REMOTE_BRANCH
```

Delete / force delete local branch
```
git branch -d LOCAL_BRANCH
git branch -D LOCAL_BRANCH
```

Delete a remote branch
```
git push origin :REMOTE_BRANCH
```

## History

History
```
git log
```

List of remote repositories
```
git remote -v
```

Pull changes from original repository to fork
```
git remote add superOrigin https://github.com/other-guy/other-guys-repo.git
git pull superOrigin REMOTE_BRANCH
```

Stash your changes without commit /Recover the files from stash
```
git stash
git stash apply
```

## Commit

Make an interactive rebase to join, rewrite, reorder commits
```
git rebase -i BRANCH/COMMIT
```

List all files for a commit
```
git diff-tree --no-commit-id --name-only -r [SHA1]
git show pretty="format:" --name-only [SHA1]
```

Show the File from Specific commit
```
git show -r [SHA1]:[filepath]
```

Search for string in all commit history
```
git log -S "[string]" --source --all
```

Undo changes of a file to a specified commit 
```
git checkout [SHA1] -- [filename]
```
