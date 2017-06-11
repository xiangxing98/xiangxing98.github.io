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
> 参考[Git教程](http://www.runoob.com/git/git-tutorial.html)

![Git Command Flow](images/Git Command Flow.png "Git Command Flow")

## 几个专用名词：

Workspace：工作区,就是你在电脑里能看到的目录，比如我的Git文件夹就是一个工作区.

Repository：仓库区（或本地仓库）/版本库,工作区有一个隐藏目录.git，
这个不算工作区，而是Git的版本库。

Index / Stage：暂存区,Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，
还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。

Remote：远程仓库

## 实用小贴士
内建的图形化 git：`gitk`
彩色的 git 输出：`git config color.ui true`
显示历史记录时，每个提交的信息只显示一行：`git config format.pretty oneline`
交互式添加文件到暂存区：`git add -i`

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
Git的设置文件为.gitconfig，它可以在用户主目录下（全局配置），
也可以在项目目录下（项目配置）。
```
# 创建SSH Key(添加Github远程库时需要)
# 在用户主目录下(我的win7，在C:\Users\**\下)，看看有没有.ssh目录.
# 如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，
# 如果已经有了，可直接跳到下一步。
# 如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
$ ssh-keygen -t rsa -C "youremail@example.com"

# 如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件.
# 这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，
# 可以放心地告诉任何人。
# 登陆GitHub，打开“Account settings”，“SSH Keys”页面,点“Add SSH Key”，填上任意Title，在Key文本框里粘贴公钥id_rsa.pub文件的内容.

#测试SSH 执行
$ ssh -T git@github.com
# 对于 oschina 的 “码云” ，执行 ssh -T git@git.oschina.net
# 对于 coding 的 “码市” ，执行 ssh -T git@git.coding.net

# 显示当前的Git配置
$ git config --list

# 编辑Git配置文件，# .config文件在C:\Users\你的用户名\.gitconfig
$ git config -e --global
$ git config --global --edit

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
# 第一次推送master分支时，加上了-u参数，
# Git不但会把本地的master分支内容推送给远程新的master分支，
# 还会把本地的master分支和远程的master分支关联起来，
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

# 创建一个带注解的标签,我推荐一直创建带注解的标签。
# -a 选项意为"创建一个带注解的标签"。 不用 -a 选项也可以执行的，
# 但它不会记录这标签是啥时候打的，谁打的，也不会让你添加个标签的注解。 
$  git tag -a v1.0 

# 指定标签信息命令：
$ git tag -a <tagname> -m "w3cschool.cc标签"

# PGP签名标签命令：
$ git tag -s <tagname> -m "w3cschool.cc标签"

# 新建一个tag在指定commit
$ git tag [tag] [commit]

# 删除本地tag
$ git tag -d [tag]

# 删除远程tag
$ git push origin :refs/tags/[tagName]

# 查看tag信息
$ git show [tag]

# 显示某次提交的内容 git show $id
$ git show 

# 提交指定tag
$ git push [remote] [tag]

# 提交所有tag，push的时候是不包含tag的,如果想包含,可以在push时加上--tags参数.
$ git push [remote] --tags

# 新建一个分支，指向某个tag
$ git checkout -b [branch] [tag]
```

## 七、查看信息 History, show commit history of a branch/diff/log
```
# 注：最后你可能会碰到这个（END），此后你怎么点都没有用。
# 那么现在你要输入:wq或:q退出。这个命令同linux指令。

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

# 看 Git 项目中三周前且在四月十八日之后的所有提交,用了 --no-merges 选项以隐藏合并提交
$ git log --oneline --before={3.weeks.ago} --after={2010-04-18} --no-merges

# git log命令显示从最近到最远的提交日志。
# 如果嫌输出信息太多，看得眼花缭乱的，可以试试加上--pretty=oneline参数：
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

# 显示两次提交之间的差异,用如下命令预览差异
$ git diff [first-branch]...[second-branch]
$ git diff <source_branch> <target_branch>

# 显示今天你写了多少行代码
$ git diff --shortstat "@{0 day ago}"

# 显示某次提交的元数据和内容变化,显示某次提交的内容
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
# 公共钥匙生成与验证
# 本地Git仓库和GitHub仓库之间的传输是通过SSH加密，需要配置验证信息，使用以下命令生成SSH Key：
$ ssh-keygen -t rsa -C "youremail@example.com"

# 后面的 your_email@youremail.com 改为你在 github 上注册的邮箱，
# 之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。
# 成功的话会在~/下生成.ssh文件夹，进去，打开 id_rsa.pub，复制里面的 key。
# 回到 github 上，进入 Account => Settings（账户配置）。
# 左边选择 SSH and GPG keys，然后点击 New SSH key 按钮,title随便填，粘贴pub key。

# 为了验证是否成功，输入以下命令：
$ ssh -T git@github.com
# Hi tianqixin! You've successfully authenticated, but GitHub does not provide shell access.


# list, add and delete remote repository aliases.
# 因为不需要每次都用完整的url,所以Git为每一个remote repo的url都建立一个别名,
# 然后用git remote来管理这个list.
# 如果你clone一个project,Git会自动将原来的url添加进来,别名就叫做:origin.
# 列出remote aliases.
$ git remote

# 下载远程仓库的所有变动download new branches and data from a remote repository.
# fetch将会取到所有你本地没有的数据,所有取下来的分支可以被叫做remote branches,
# 它们和本地分支一样(可以看diff,log等,也可以merge到其他分支),
# 但是Git不允许你checkout到它们. 
$ git fetch [remote]

# 显示所有远程仓库List of remote repositories,可以看见每一个别名对应的实际url.
$ git remote -v

# 显示某个远程仓库的信息
$ git remote show [remote]

# 增加一个新的远程仓库，并命名
# 要添加一个新的远程仓库，可以指定一个简单的名字，别名或者短名字，以便将来引用,命令格式如下：
$ git remote add [alias/shortname] [url]
$ git remote add superOrigin https://github.com/other-guy/other-guys-repo.git

# 删除一个存在的remote alias
$ git remote rm [alias]

# 重命名一个存在的remote
$ git remote rename [old-alias] [new-alias]:

# 更新url.可以加上—push和fetch参数,为同一个别名设置不同的存取地址.
$ git remote set-url [alias] [url]:更新url. 

# 取回远程仓库的变化，并与本地分支合并Pull changes from original repository to fork
# pull == fetch + merge FETCH_HEAD, git pull会首先执行git fetch,然后执行git merge,
# 把取来的分支的head merge到当前分支.
# 这个merge操作会产生一个新的commit. 
# 如果使用--rebase参数,它会执行git rebase来取代原来的git merge.
$ git pull [remote] [branch]
$ git pull superOrigin REMOTE_BRANCH

# 上传本地指定分支到远程仓库
$ git push [remote] [branch]

# push your new branches and data to a remote repository.
git push [alias] [branch]
# 将会把当前分支merge到alias上的[branch]分支.
# 如果分支已经存在,将会更新,如果不存在,将会添加这个分支.
# 如果有多个人向同一个remote repo push代码, Git会首先在你试图push的分支上运行git log,
# 检查它的历史中是否能看到server上的branch现在的tip,
# 如果本地历史中不能看到server的tip,说明本地的代码不是最新的,Git会拒绝你的push,
# 让你先fetch,merge,之后再push,这样就保证了所有人的改动都会被考虑进来.

# 强行推送当前分支到远程仓库，即使有冲突
$ git push [remote] --force

# 推送所有分支到远程仓库
$ git push [remote] --all
```

## 九、撤销、回退
```
# 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，
# 用命令git checkout -- file。

# 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，
# 第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。

# 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，
# 参考版本回退一节，不过前提是没有推送到远程库。

# 恢复暂存区的指定文件到工作区
$ git checkout [file]

# 把readme.txt文件在工作区的修改全部撤销，丢弃工作区的修改,
# 让这个文件回到最近一次git commit或git add时的状态, 
# git checkout -- file命令中的--很重要，
# 没有--，就变成了“创建一个新分支”的命令，
# 我们在后面的分支管理中会再次遇到git checkout命令。
# git checkout其实是用版本库里的最新的版本HEAD 替换工作区的版本，
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

# 假如你想丢弃你在本地的所有改动与提交，可以到服务器上获取最新的版本历史，
# 并将你本地主分支指向它：
$ git fetch origin
$ git reset --hard origin/master

# 暂时将未提交的变化移除，稍后再移入
$ git stash
$ git stash pop

# Stash your changes without commit /Recover the files from stash
$ git stash
$ git stash apply

```

## 十、其他
```
# 显示command的help
git help <command>

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
# --rebase不会产生合并的提交,它会将本地的所有提交临时保存为补丁(patch),
# 放在”.git/rebase”目录中,然后将当前分支更新到最新的分支尖端,
# 最后把保存的补丁应用到分支上.
# rebase的过程中,也许会出现冲突,Git会停止rebase并让你解决冲突,
# 在解决完冲突之后,用git add去更新这些内容,然后无需执行commit,
# 只需要下面一句就会继续打余下的补丁.
git rebase --continue

#将会终止rebase,当前分支将会回到rebase之前的状态.
git rebase --abort
```

## Remote Repository Github & Local Repository Basic Flow
```
$ mkdir git-test                     # 创建测试目录
$ cd git-test/                       # 进入测试目录
$ touch test.txt                        # 添加文件
$ echo "# 菜鸟教程 Git 测试" >> README.md     # 创建 README.md 文件并写入内容

$ ls                                        # 查看目录下的文件
# README

$ git init                                  # 初始化
$ git add README.md                         # 添加文件
$ git commit -m "添加 README.md 文件"        # 提交并备注信息
# [master (root-commit) 0205aab] 添加 README.md 文件
#  1 file changed, 1 insertion(+)
#  create mode 100644 README.md

# 添加远端仓库，
$ git remote add origin git@github.com:xiangxing98/git-test.git

# 提交到 Github，第一次提交时 -u表示链接远端与本地的分支
$ git push -u origin master
# 以后就用下面的命令推送就OK了,将你的 [branch] 分支推送成为 [alias] 远程仓库上的 [branch] 分支
$ git push [alias] [branch]

# 从远程仓库下载新分支与数据，该命令执行完后需要执行git merge 远程分支到你所在的分支。
# 假设你配置好了一个远程仓库，并且你想要提取更新的数据，
# 你可以首先执行 git fetch [alias] 告诉 Git 去获取它有你没有的数据，
git fetch origin

# 然后你可以执行 git merge [alias]/[branch] 
# 以将服务器上的任何更新（假设有人这时候推送到服务器了）合并到你的当前分支。
git merge origin/master

# 从远端仓库提取数据并尝试合并到当前分支：
# 该命令就是在执行 git fetch 之后紧接着执行 git merge 远程分支到你所在的任意分支。
git pull

# 删除远程仓库你可以使用命令：
git remote rm [别名]

$ git remote -v
# origin  git@github.com:tianqixin/runoob-git-test.git (fetch)
# origin  git@github.com:tianqixin/runoob-git-test.git (push)

# 添加仓库 origin2
$ git remote add origin2 git@github.com:tianqixin/runoob-git-test.git

$ git remote -v
# origin  git@github.com:tianqixin/runoob-git-test.git (fetch)
# origin  git@github.com:tianqixin/runoob-git-test.git (push)
# origin2 git@github.com:tianqixin/runoob-git-test.git (fetch)
# origin2 git@github.com:tianqixin/runoob-git-test.git (push)

# 删除仓库 origin2
$ git remote rm origin2
$ git remote -v
# origin  git@github.com:tianqixin/runoob-git-test.git (fetch)
# origin  git@github.com:tianqixin/runoob-git-test.git (push)

```

## Git 服务器搭建
> [Git 服务器搭建](http://www.runoob.com/git/git-server.html)

Github 公开的项目是免费的，但是如果你不想让其他人看到你的项目就需要收费。
这时我们就需要自己搭建一台Git服务器作为私有仓库使用。

接下来我们将以 Centos 为例搭建 Git 服务器。

### 1、安装Git
```
$ yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-devel
$ yum install git
```

接下来我们 创建一个git用户组和用户，用来运行git服务：
```
$ groupadd git
$ adduser git -g git
```

### 2、创建证书登录
收集所有需要登录的用户的公钥，公钥位于id_rsa.pub文件中，
把我们的公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个。
如果没有该文件创建它：
```
$ cd /home/git/
$ mkdir .ssh
$ chmod 700 .ssh
$ touch .ssh/authorized_keys
$ chmod 600 .ssh/authorized_keys
```

### 3、初始化Git仓库
首先我们选定一个目录作为Git仓库，假定是/home/gitrepo/runoob.git，
在/home/gitrepo目录下输入命令：
```
$ cd /home
$ mkdir gitrepo
$ chown git:git gitrepo/
$ cd gitrepo

$ git init --bare runoob.git
```

Initialized empty Git repository in /home/gitrepo/runoob.git/
以上命令Git创建一个空仓库，服务器上的Git仓库通常都以.git结尾。
然后，把仓库所属用户改为git：
```
$ chown -R git:git runoob.git
```

### 4、克隆仓库
```
$ git clone git@192.168.45.4:/home/gitrepo/runoob.git
# Cloning into 'runoob'...
# warning: You appear to have cloned an empty repository.
# Checking connectivity... done.
```
192.168.45.4 为 Git 所在服务器 ip ，你需要将其修改为你自己的 Git 服务 ip。
这样我们的 Git 服务器安装就完成了，接下来我们可以禁用 git 用户通过shell登录，
可以通过编辑/etc/passwd文件完成。找到类似下面的一行：
```
git:x:503:503::/home/git:/bin/bash
```
改为：
```
git:x:503:503::/home/git:/sbin/nologin
```

## 参考资料
1. [Git 社区参考书](http://book.git-scm.com/)
2. [专业 Git](http://progit.org/book/)
3. [像 git 那样思考](http://think-like-a-git.net/)
4. [GitHub 帮助](http://help.github.com/)
5. [图解 Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)
6. [菜鸟教程-网络技术-推荐](http://www.runoob.com/)
7. [Pro Git（中文版）](http://git.oschina.net/progit/)
8. [猴子都能懂的GIT入门](http://backlogtool.com/git-guide/cn/)

======

## Git常用命令
> [Git常用命令](http://www.cnblogs.com/cspku/articles/Git_cmds.html)

### 查看、添加、提交、删除、找回，重置修改文件
```
git help <command> # 显示command的help
git show # 显示某次提交的内容 git show $id
git co -- <file> # 抛弃工作区修改
git co . # 抛弃工作区修改
git add <file> # 将工作文件修改提交到本地暂存区
git add . # 将所有修改过的工作文件提交暂存区
git rm <file> # 从版本库中删除文件
git rm <file> --cached # 从版本库中删除文件，但不删除文件
git reset <file> # 从暂存区恢复到工作文件
git reset -- . # 从暂存区恢复到工作文件
git reset --hard # 恢复最近一次提交过的状态，即放弃上次提交后的所有本次修改
git ci <file> git ci . git ci -a # 将git add, git rm和git ci等操作都合并在一起做　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　git ci -am "some comments"
git ci --amend # 修改最后一次提交记录
git revert <$id> # 恢复某次提交的状态，恢复动作本身也创建次提交对象
git revert HEAD # 恢复最后一次提交的状态
```

### 查看文件diff
```
git diff <file> # 比较当前文件和暂存区文件差异 git diff
git diff <id1><id1><id2> # 比较两次提交之间的差异
git diff <branch1>..<branch2> # 在两个分支之间比较
git diff --staged # 比较暂存区和版本库差异
git diff --cached # 比较暂存区和版本库差异
git diff --stat # 仅仅比较统计信息
```
查看提交记录
```
git log git log <file> # 查看该文件每次提交记录
git log -p <file> # 查看每次详细修改内容的diff
git log -p -2 # 查看最近两次详细修改内容的diff
git log --stat #查看提交统计信息
tig
# Mac上可以使用tig代替diff和log，brew install tig
```

### Git 本地分支管理

#### 查看、切换、创建和删除分支
```
git br -r # 查看远程分支
git br <new_branch> # 创建新的分支
git br -v # 查看各个分支最后提交信息
git br --merged # 查看已经被合并到当前分支的分支
git br --no-merged # 查看尚未被合并到当前分支的分支
git co <branch> # 切换到某个分支
git co -b <new_branch> # 创建新的分支，并且切换过去
git co -b <new_branch> <branch> # 基于branch创建新的new_branch
git co $id # 把某次历史提交记录checkout出来，但无分支信息，切换到其他分支会自动删除
git co $id -b <new_branch> # 把某次历史提交记录checkout出来，创建成一个分支
git br -d <branch> # 删除某个分支
git br -D <branch> # 强制删除某个分支 (未被合并的分支被删除的时候需要强制)
```

#### 分支合并和rebase
```
git merge <branch> # 将branch分支合并到当前分支
git merge origin/master --no-ff # 不要Fast-Foward合并，这样可以生成merge提交
git rebase master <branch> # 将master rebase到branch，相当于： git co <branch> && git rebase master && git co master && git merge <branch>
```

### Git补丁管理(方便在多台机器上开发同步时用)
```
git diff > ../sync.patch # 生成补丁
git apply ../sync.patch # 打补丁
git apply --check ../sync.patch #测试补丁能否成功
```

### Git暂存管理
```
git stash # 暂存
git stash list # 列所有stash
git stash apply # 恢复暂存的内容
git stash drop # 删除暂存区
```

### Git远程分支管理
```
git pull # 抓取远程仓库所有分支更新并合并到本地
git pull --no-ff # 抓取远程仓库所有分支更新并合并到本地，不要快进合并
git fetch origin # 抓取远程仓库更新
git merge origin/master # 将远程主分支合并到本地当前分支
git co --track origin/branch # 跟踪某个远程分支创建相应的本地分支
git co -b <local_branch> origin/<remote_branch> # 基于远程分支创建本地分支，功能同上
git push # push所有分支
git push origin master # 将本地主分支推到远程主分支
git push -u origin master # 将本地主分支推到远程(如无远程主分支则创建，用于初始化远程仓库)
git push origin <local_branch> # 创建远程分支， origin是远程仓库名
git push origin <local_branch>:<remote_branch> # 创建远程分支
git push origin :<remote_branch> #先删除本地分支(git br -d <branch>)，然后再push删除远程分支
```

### Git远程仓库管理

#### GitHub
```
git remote -v # 查看远程服务器地址和仓库名称
git remote show origin # 查看远程服务器仓库状态
git remote add origin git@ github:robbin/robbin_site.git # 添加远程仓库地址
git remote set-url origin git@ github.com:robbin/robbin_site.git # 设置远程仓库地址(用于修改远程仓库地址) git remote rm <repository> # 删除远程仓库
```

#### 创建远程仓库
```
git clone --bare robbin_site robbin_site.git # 用带版本的项目创建纯版本仓库
scp -r my_project.git git@ git.csdn.net:~ # 将纯仓库上传到服务器上
mkdir robbin_site.git && cd robbin_site.git && git --bare init # 在服务器创建纯仓库
git remote add origin git@ github.com:robbin/robbin_site.git # 设置远程仓库地址
git push -u origin master # 客户端首次提交
git push -u origin develop # 首次将本地develop分支提交到远程develop分支，并且track
git remote set-head origin master # 设置远程仓库的HEAD指向master分支
```

也可以命令设置跟踪远程库和本地库
```
git branch --set-upstream master origin/master
git branch --set-upstream develop origin/develop
```
