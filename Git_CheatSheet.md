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

> 参考 [常用 Git 命令清单--阮一峰](http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html "常用 Git 命令清单--阮一峰")

![Git Command Flow](images/Git Command Flow.png "Git Command Flow")

几个专用名词：
Workspace：工作区,就是你在电脑里能看到的目录，比如我的Git文件夹就是一个工作区.
Repository：仓库区（或本地仓库）/版本库,工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。
Index / Stage：暂存区,Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。
Remote：远程仓库

## All Git Command CheatSheet
> Gitella

## 一、新建代码库 Start
Initialize a repository
```
# 目录操作并切换到工作目录,注：Windows下，路径名不要包含中文，因为Git对中文支持不给力！
$ cd /d e:/github
$ mkdir MyGitRepo001
$ cd MyGitRepo001

# 显示当前的路径,当前路径下的所有东西
$ pwd //显示当前的路径
$ ls -al

# 在当前目录新建一个Git代码库
$ git init

# 新建一个目录，将其初始化为Git代码库
$ git init [project-name]

# 下载一个项目和它的整个代码历史 Clone a remote repository
$ git clone [url]
$ git clone URL_REPOSITORY
```

## 二、配置
Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），也可以在项目目录下（项目配置）。
```
# 创建SSH Key
# 在用户主目录下(我的win7，在C:\Users\**\下)，看看有没有.ssh目录.
# 如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果已经有了，可直接跳到下一步。
# 如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
$ ssh-keygen -t rsa -C "youremail@example.com"
# 如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件.
# 这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。
# 登陆GitHub，打开“Account settings”，“SSH Keys”页面,点“Add SSH Key”，填上任意Title，在Key文本框里粘贴公钥id_rsa.pub文件的内容.

# 显示当前的Git配置
$ git config --list

# 编辑Git配置文件
$ git config -e [--global]

# 设置提交代码时的用户信息
$ git config [--global] user.name "[name]"
$ git config [--global] user.email "[email address]"
```

## 三、增加/删除文件
```
# 添加指定文件到暂存区
$ git add [file1] [file2] ...

# 添加指定目录到暂存区，包括子目录
$ git add [dir]

# 添加当前目录的所有文件到暂存区Add all the files your changed
$ git add .
$ git add --all

# 添加每个变化前，都会要求确认
# 对于同一个文件的多处变化，可以实现分次提交
$ git add -p

# 删除工作区文件，并且将这次删除放入暂存区,以备提交更改git commit
$ git rm [file1] [file2] ...

# 停止追踪指定文件，但该文件会保留在工作区
$ git rm --cached [file]

# 改名文件，并且将这个改名放入暂存区
$ git mv [file-original] [file-renamed]

# Show files modified
$ git status
```

## 四、代码提交
```
# 提交暂存区到仓库区Commit changes with a message
$ git commit -m [message]
$ git commit -m "MESSAGE" 

# 提交暂存区的指定文件到仓库区
$ git commit [file1] [file2] ... -m [message]

# 提交工作区自上次commit之后的变化，直接到仓库区=git add +git commit -m
$ git commit -am

# 提交时显示所有diff信息
$ git commit -v

# 使用一次新的commit，替代上一次提交
# 如果代码没有任何新变化，则用来改写上一次commit的提交信息
$ git commit --amend -m [message]

# 重做上一次commit，并包括指定文件的新变化
$ git commit --amend [file1] [file2] ...
```

## 五、分支 Branches
```
# 列出所有本地分支Show the local branched list
$ git branch

# 列出所有远程分支
$ git branch -r

# 列出所有本地分支和远程分支
$ git branch -a

# 新建一个分支，但依然停留在当前分支
$ git branch [branch-name]

# 新建一个分支，并切换到该分支Create a local branch
$ git checkout -b [branch]
$ git checkout -b LOCAL_BRANCH

# 新建一个分支，指向指定commit
$ git branch [branch] [commit]

# 新建一个分支，与指定的远程分支建立追踪关系
$ git branch --track [branch] [remote-branch]

# 从本地分支创建远程分支 Create a local remote branch from a local one
$ git push origin LOCAL_BRANCH:REMOTE_BRANCH

# 切换到指定分支，并更新工作区Switch between branches
$ git checkout [branch-name]
$ git checkout LOCAL_BRANCH

# 切换到上一个分支
$ git checkout -

# 建立追踪关系，在现有分支与指定的远程分支之间
$ git branch --set-upstream [branch] [remote-branch]

# 合并指定分支到当前分支
$ git merge [alias]/[branch]

# 选择一个commit，合并进当前分支
$ git cherry-pick [commit]

# 删除分支 Delete / force delete local branch
$ git branch -d [branch-name]
$ git branch -d LOCAL_BRANCH
$ git branch -D LOCAL_BRANCH

# 删除远程分支 Delete a remote branch
$ git push origin --delete [branch-name]
$ git push origin :REMOTE_BRANCH
$ git branch -dr [remote/branch]

# 远程分支推送与关联
# 第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送给远程新的master分支，还会把本地的master分支和远程的master分支关联起来，
$  git push -u origin master

# 在以后的推送或者拉取时就可以简化远程推送命令推送最新修改
# git push origin master
```

## 六、标签
```
# 列出所有tag
$ git tag

# 新建一个tag在当前commit
$ git tag [tag]

# 新建一个tag在指定commit
$ git tag [tag] [commit]

# 删除本地tag
$ git tag -d [tag]

# 删除远程tag
$ git push origin :refs/tags/[tagName]

# 查看tag信息
$ git show [tag]

# 提交指定tag
$ git push [remote] [tag]

# 提交所有tag，push的时候是不包含tag的,如果想包含,可以在push时加上--tags参数.
$ git push [remote] --tags

# 新建一个分支，指向某个tag
$ git checkout -b [branch] [tag]
```

## 七、查看信息 History, show commit history of a branch
```
# 注：最后你可能会碰到这个（END），此后你怎么点都没有用。那么现在你要输入:wq或:q退出。这个命令同linux指令。

# 显示有变更的文件
$ git status

# 显示当前分支的版本历史History
$ git log

# 显示commit历史，以及每次commit发生变更的文件
$ git log --stat

# 显示特定分支的log,commit历史
$ git log branchname

# 显示出tag信息.
$ git log --decorate

# 可以指定作者的提交历史
$ git log --author=[author name]

# 根据提交时间筛选log
$ git log --since --before --until --after

# git log命令显示从最近到最远的提交日志。如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数：
$ git log --pretty=oneline

# 搜索提交历史，根据关键词
$ git log -S [keyword]

# 显示某个commit之后的所有变动，每个commit占据一行
$ git log [tag] HEAD --pretty=format:%s

# 显示某个commit之后的所有变动，其"提交说明"必须符合搜索条件
$ git log [tag] HEAD --grep feature

# 显示某个文件的版本历史，包括文件改名
$ git log --follow [file]
$ git whatchanged [file]

# 显示指定文件相关的每一次diff
$ git log -p [file]

# 显示过去5次提交
$ git log -5 --pretty --oneline

# 显示所有提交过的用户，按提交次数排序
$ git shortlog -sn

# 显示指定文件是什么人在什么时间修改过
$ git blame [file]

# 显示暂存区和工作区的差异
$ git diff

# 显示暂存区和上一个commit的差异
$ git diff --cached [file]

# 显示工作区与当前分支最新commit之间的差异
$ git diff HEAD

# 查看readme.txt工作区和版本库里面最新版本的区别
$ git diff HEAD -- readme.txt

# 显示两次提交之间的差异
$ git diff [first-branch]...[second-branch]

# 显示今天你写了多少行代码
$ git diff --shortstat "@{0 day ago}"

# 显示某次提交的元数据和内容变化
$ git show [commit]

# 显示某次提交发生变化的文件
$ git show --name-only [commit]

# 显示某次提交时，某个文件的内容
$ git show [commit]:[filename]

# 显示当前分支的最近几次提交,记录了每一次命令
$ git reflog
```

## 八、远程同步
```
# list, add and delete remote repository aliases.
# 因为不需要每次都用完整的url,所以Git为每一个remote repo的url都建立一个别名,然后用git remote来管理这个list.如果你clone一个project,Git会自动将原来的url添加进来,别名就叫做:origin.
# 列出remote aliases.
$ git remote

# 下载远程仓库的所有变动download new branches and data from a remote repository.
# fetch将会取到所有你本地没有的数据,所有取下来的分支可以被叫做remote branches,它们和本地分支一样(可以看diff,log等,也可以merge到其他分支),但是Git不允许你checkout到它们. 
$ git fetch [remote]

# 显示所有远程仓库List of remote repositories,可以看见每一个别名对应的实际url.
$ git remote -v

# 显示某个远程仓库的信息
$ git remote show [remote]

# 增加一个新的远程仓库，并命名
$ git remote add [alias] [url]
$ git remote add [shortname] [url]
$ git remote add superOrigin https://github.com/other-guy/other-guys-repo.git

# 删除一个存在的remote alias
$ git remote rm [alias]

# 重命名一个存在的remote
$ git remote rename [old-alias] [new-alias]:

# 更新url.可以加上—push和fetch参数,为同一个别名设置不同的存取地址.
$ git remote set-url [alias] [url]:更新url. 

# 取回远程仓库的变化，并与本地分支合并Pull changes from original repository to fork
# pull == fetch + merge FETCH_HEAD, git pull会首先执行git fetch,然后执行git merge,把取来的分支的head merge到当前分支.
#这个merge操作会产生一个新的commit. 如果使用--rebase参数,它会执行git rebase来取代原来的git merge.
$ git pull [remote] [branch]
$ git pull superOrigin REMOTE_BRANCH

# 上传本地指定分支到远程仓库
$ git push [remote] [branch]

# push your new branches and data to a remote repository.
git push [alias] [branch]
#将会把当前分支merge到alias上的[branch]分支.如果分支已经存在,将会更新,如果不存在,将会添加这个分支.
#如果有多个人向同一个remote repo push代码, Git会首先在你试图push的分支上运行git log,检查它的历史中是否能看到server上的branch现在的tip,如果本地历史中不能看到server的tip,说明本地的代码不是最新的,Git会拒绝你的push,让你先fetch,merge,之后再push,这样就保证了所有人的改动都会被考虑进来.

# 强行推送当前分支到远程仓库，即使有冲突
$ git push [remote] --force

# 推送所有分支到远程仓库
$ git push [remote] --all
```

## 九、撤销、回退
```
# 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file。
# 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。
# 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

# 恢复暂存区的指定文件到工作区
$ git checkout [file]

# 把readme.txt文件在工作区的修改全部撤销，丢弃工作区的修改,
# 让这个文件回到最近一次git commit或git add时的状态, git checkout -- file命令中的--很重要，
# 没有--，就变成了“创建一个新分支”的命令，我们在后面的分支管理中会再次遇到git checkout命令。
# git checkout其实是用版本库里的版本替换工作区的版本，
# 无论工作区是修改还是删除，都可以“一键还原”。
$ git checkout -- readme.txt

# 恢复某个commit的指定文件到暂存区和工作区
$ git checkout [commit] [file]

# 恢复暂存区的所有文件到工作区
$ git checkout .

# 重置暂存区的指定文件，与上一次commit保持一致，但工作区不变
$ git reset [file]

# 重置暂存区与工作区，与上一次commit保持一致
$ git reset --hard

# 重置当前分支的指针为指定commit，同时重置暂存区，但工作区不变
$ git reset [commit]

# 回退到上一个版本的命令git reset
$ git reset --hard HEAD^

# 重置当前分支的HEAD为指定commit，同时重置暂存区和工作区，与指定commit一致
$ git reset --hard [commit]

# 重置当前HEAD为指定commit，但保持暂存区和工作区不变
$ git reset --keep [commit]

# 新建一个commit，用来撤销指定commit
# 后者的所有变化都将被前者抵消，并且应用到当前分支
$ git revert [commit]

# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop

# Stash your changes without commit /Recover the files from stash
$ git stash
$ git stash apply

```

## 十、其他
```
# 生成一个可供发布的压缩包
$ git archive

# 查看文件命令cat readme.txt:
$ cat readme.txt

# Make an interactive rebase to join, rewrite, reorder commits
$ git rebase -i BRANCH/COMMIT

# List all files for a commit
$ git diff-tree --no-commit-id --name-only -r [SHA1]
$ git show pretty="format:" --name-only [SHA1]

# Show the File from Specific commit
$ git show -r [SHA1]:[filepath]

# Search for string in all commit history
$ git log -S "[string]" --source --all

# Undo changes of a file to a specified commit 
$ git checkout [SHA1] -- [filename]

# 变基，打补丁
$ git rebase
--rebase不会产生合并的提交,它会将本地的所有提交临时保存为补丁(patch),放在”.git/rebase”目录中,然后将当前分支更新到最新的分支尖端,最后把保存的补丁应用到分支上.
rebase的过程中,也许会出现冲突,Git会停止rebase并让你解决冲突,在解决完冲突之后,用git add去更新这些内容,然后无需执行commit,只需要:
git rebase --continue就会继续打余下的补丁.
git rebase --abort将会终止rebase,当前分支将会回到rebase之前的状态.
```
