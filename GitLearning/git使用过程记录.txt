# git使用过程记录

> 2010-08-09 16:11:04
> 参考：http://www.jifuyi.com/git-cvs-tutorial/

```{bash}
[root@slh githome]# git init --bare
Initialized empty Git repository in /home/echo/githome/
[root@slh githome]# ll
total 32
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 branches
-rw-r--r--. 1 root root   66 2010-01-05 13:46 config
-rw-r--r--. 1 root root   58 2010-01-05 13:46 description
-rw-r--r--. 1 root root   23 2010-01-05 13:46 HEAD
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 hooks
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 info
drwxr-xr-x. 4 root root 4096 2010-01-05 13:46 objects
drwxr-xr-x. 4 root root 4096 2010-01-05 13:46 refs
[root@slh githome]# cat  HEAD
ref: refs/heads/master
```

HEAD 文件中的内容其实只是包含了一个索引信息，并且，这个索引将总是指向你的项目中的当前开发分支。
master 是默认的分支。

```{bash}
[root@slh githome]# ll objects
total 8
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 info
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 pack
```

objects 子目录包含了你的项目中的所有对象

```{bash}
[root@slh githome]# ll refs
total 8
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 heads
drwxr-xr-x. 2 root root 4096 2010-01-05 13:46 tags
```

子目录 refs 包含着两个子目录叫 heads 和 tags，存放了不同的开发分支的头的索引, 或者是你用来标定版本的标签的索引。

创建一个示例文件：
```{bash}
[root@slh githome]# echo "echo example" >example
```

添加到库:
```{bash}
[root@slh githome]# git add example
fatal: This operation must be run in a work tree
# 答案：http://stackoverflow.com/questions/1456923/why-am-i-getting-the-message-fatal-this-operation-must-be-run-in-a-work-tree

```

## 以下相关于客户端操作

重新init，没有用bare参数：
```{bash}
[root@slh projects]# pwd
/home/echo/projects
[root@slh projects]# git init
Initialized empty Git repository in /home/echo/projects/.git/
[root@slh projects]# echo "example1" >example1
[root@slh projects]# git add .

# 与远程库（/home/echo/githome），用的是ssh链接
# poject 是我在本地库为远程库建的一个标识，root是我在linux上维护项目的用户名
# NAME git-remote - manage set of tracked repositories

[root@slh projects]# git remote add project ssh://root@192.168.157.128/home/echo/githome
[root@slh projects]# git config --global user.name "shulihua"
[root@slh projects]# git config --global user.email "shulihua@XXX"
[root@slh projects]# git commit -m "add example1"
[master (root-commit) bfd55ac] add example1
 1 files changed, 1 insertions(+), 0 deletions(-)
 create mode 100644 example1
[root@slh projects]# git push
fatal: No destination configured to push to.
```

## 继续Git中文教程

> http://www.bitsun.com/documents/gittutorcn.htm

### 添加文件、查看状态、修改文件、提交文件

```{bash}
[root@slh projects]# git status
# On branch master
nothing to commit (working directory clean)
[root@slh projects]# echo "change example1">>example1
[root@slh projects]# git diff
diff --git a/example1 b/example1
index e723c8f..c8ffee7 100644
--- a/example1
+++ b/example1
@@ -1 +1,2 @@
 example1
+change example1
[root@slh projects]#git commit -a -m "something changed"
[master 74603bd] something changed
 1 files changed, 1 insertions(+), 0 deletions(-)
```
 
### 分支相关：添加、删除、查看

```{bash}
[root@slh projects]# git branch echo_br
[root@slh projects]# git branchecho_br2
[root@slh projects]# git branch-D echo_br2
Deleted branch echo_br2 (was 74603bd).
[root@slh projects]# git branch
  echo_br
* master
```

如果你忘记了你现在工作在哪个分支上，运行下面的命令可以告诉你：
```{bash}
[root@slh projects]# cat .git/HEAD
ref: refs/heads/master
```

### 查看项目进展和比较差异

```{bash}
[root@slh projects]# git checkout echo_br
Switched to branch 'echo_br'
[root@slh projects]# echo "Switched to branch 'echo_br'" >>example1
[root@slh projects]# git commit -m "commit in echo_br" -iexample1
[echo_br 64c5fb9] commit in echo_br
 1 files changed, 1 insertions(+), 0 deletions(-)
[root@slh projects]# git checkout master
Switched to branch 'master'
[root@slh projects]# echo "changes in master branch" >>example1
[root@slh projects]# echo "changes in master branch" >>example3
[root@slh projects]# git commit -m "commit in master" -i example1 example3
[master fa8323d] commit in master
 1 files changed, 1 insertions(+), 0 deletions(-)
[root@slh projects]# git show-branch
! [echo_br] commit in echo_br
 * [master] commit in master
--
 * [master] commit in master
+  [echo_br] commit in echo_br
+* [master^] something changed
```

### 比较分支的差异

```{bash}
[root@slh projects]# git diff master^ echo_br
diff --git a/example1 b/example1
index c8ffee7..a2584bd 100644
--- a/example1
+++ b/example1
@@ -1,2 +1,3 @@
 example1
 change example1
+Switched to branch 'echo_br'
```


### 查看master的版本变更情况

```{bash}
[root@slh projects]# git checkout master
Already on 'master'
[root@slh projects]# git whatchanged
commit fa8323dcb9d58634a2609d79e43a1f0669fdbc24
Author: echo <shulihua@snda.com>
Date:   Tue Jan 5 15:50:45 2010 +0800
    commit in master
:100644 100644 c8ffee7... d83a91a... M  example1
......
```

### 合并分支
```{bash}
[root@slh projects]# git checkout master
Already on 'master'
[root@slh projects]# git merge "merge from echo_br to master" HEAD echo_br
Auto-merging example1
CONFLICT (content): Merge conflict in example1
Automatic merge failed; fix conflicts and then commit the result.
[root@slh projects]# cat example1
example1
change example1
<<<<<<< HEAD:example1
changes in master branch
=======
Switched to branch 'echo_br'
>>>>>>> echo_br:example1
[root@slh projects]# vi example1
<<<<<<< HEAD:example1
=======
example1
change example1
changes in master branch
this is changed in branch 'echo_br'
"example1" 4L, 86C written
[root@slh projects]# git commit -i example1
merge from echo_br to master
Conflicts:
        example1
#
# It looks like you may be committing a MERGE.
# If this is not correct, please remove the file
#       .git/MERGE_HEAD
# and try again.
#
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#       modified:   example1
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#       example
#       example3
貌似这样也提交成功了（若不加-m参数就会显示以上内容，加上则无）。

```

### 逆转与恢复：git reset--Reset current HEAD to the specified state
```{bash}
git-reset [--mixed | --soft | --hard] [<commit-ish>]
```

命令的选项：
```{bash}
--mixed
```
仅是重置索引的位置，而不改变你的工作树中的任何东西（即，文件中的所有变化都会被保留，也不标记他们为待提交状态），并且提示什么内容还没有被更新了。这个是默认的选项。

--soft
既不触动索引的位置，也不改变工作树中的任何内容，我们只是要求这些内容成为一份好的内容（之后才成为真正的提交内容）。这个选项使你可以将已经提交的东西重新逆转至“已更新但未提交（Updated but not Check in）”的状态。就像已经执行过 git-update-index 命令，但是还没有执行 git-commit 命令一样。

--hard
将工作树中的内容和头索引都切换至指定的版本位置中，也就是说自 <commit-ish> 之后的所有的跟踪内容和工作树中的内容都会全部丢失。因此，这个选项要慎用，除非你已经非常确定你的确不想再看到那些东西了。

eg.soft例子：
（1）、创建了一个 master 的拷贝分支 softreset
```{bash}
[root@slh projects]# git checkout master
Already on 'master'
[root@slh projects]# git checkout -b softreset
Switched to a new branch 'softreset'
```

两个分支是在同一起跑线上
```{bash}
[root@slh projects]# git show-branch
! [echo_br] commit in echo_br
 ! [master] merge from echo_br to master
  * [softreset] merge from echo_br to master
---
 -- [master] merge from echo_br to master
++* [echo_br] commit in echo_br
```

修改softreset分支上的文件
```{bash}
[root@slh projects]# echo "softreset" >>example1
[root@slh projects]# git commit -a -m "in softreset"
[softreset 2fd313b] in softreset
 1 files changed, 1 insertions(+), 0 deletions(-)
[root@slh projects]# git show-branch
! [echo_br] commit in echo_br
 ! [master] merge from echo_br to master
  * [softreset] in softreset
---
  * [softreset] in softreset
 -- [master] merge from echo_br to master
++* [echo_br] commit in echo_br
```

softreset 分支的头和 ORIG_HEAD 保存的索引
```{bash}
[root@slh projects]# cat .git/refs/heads/softreset .git/ORIG_HEAD
2fd313bfbfd3166f0c58551f232e1bb8d0fe54e3
fa8323dcb9d58634a2609d79e43a1f0669fdbc24

# 用 --soft 选项逆转刚才提交的内容
[root@slh projects]# git reset --soft HEAD^
[root@slh projects]# cat .git/ORIG_HEAD
2fd313bfbfd3166f0c58551f232e1bb8d0fe54e3
```
现在的 .git/ORIG_HEAD 等于逆转前的 .git/refs/heads/softreset
也就是说，git-reset --soft HEAD^ 命令逆转了刚才提交的版本进度，但是它将那次提交的对象的索引拷贝到了 .git/ORIG_HEAD 中?example1中的内容还是变了，没reset成功?

### 提取版本库中的数据，貌似就是同步为版本库中的内容
```{bash}
[root@slh projects]# echo "changes" >> example1
[root@slh projects]# cat example1
example1
change example1
changes in master branch
this is changed in branch 'echo_br'
softreset
changes
[root@slh projects]# git checkout -f example1
[root@slh projects]# cat example1
example1
change example1
changes in master branch
this is changed in branch 'echo_br'
softreset
```

注：-f  When switching branches, proceed even if the index or the working tree differs from HEAD. This is used to throw away local changes.

### 标定版本
```{bash}
NAME
       git-tag - Create, list, delete or verify a tag object signed with GPG
```

在 git 中，有两种类型的标签，“轻标签”和“署名标签”。
技术上说，一个“轻标签”和一个分支没有任何区别，只不过我们将它放在了 .git/refs/tags/ 目录，而不是 heads 目录。因此，打一个“轻标签”再简单不过了。

```{bash}
[root@slh projects]# ll .git/refs/tags
total 0
[root@slh projects]# git tag my-first-tag
[root@slh projects]# ll .git/refs/tags
total 4
-rw-r--r--. 1 root root 41 2010-01-05 17:27 my-first-tag
```

针对某个commit ID来打标签???什么是commit ID???

“署名标签”是一个真正的 git 对象，它不但包含指向你想标记的状态的指针，还有一个标记名和信息，可选的 PGP 签名。你可以通过 -a 或者是 -s 选项来创建“署名标签”。
```{bash}

-a
           Make an unsigned, annotated tag object
-s
           Make a GPG-signed tag, using the default e-mail address key
[root@slh projects]# git tag -s tag1
```

输入一些tag message

```{bash}
".git/TAG_EDITMSG" 7L, 41C written
gpg: directory `/root/.gnupg' created
gpg: new configuration file `/root/.gnupg/gpg.conf' created
gpg: WARNING: options in `/root/.gnupg/gpg.conf' are not yet active during this run
gpg: keyring `/root/.gnupg/secring.gpg' created
gpg: keyring `/root/.gnupg/pubring.gpg' created
gpg: skipped "echo <shulihua@XXX.com>": secret key not available
gpg: signing failed: secret key not available
error: gpg failed to sign the tag
error: unable to sign the tag
The tag message has been left in .git/TAG_EDITMSG
```

后记：
```{bash}
[root@slh projects]# git checkout  my-first-tag
A       example4
Note: moving to 'my-first-tag' which isn't a local branch
If you want to create a new branch from this checkout, you may do so
(now or later) by using -b with the checkout command again. Example:
  git checkout -b <new_branch_name>
HEAD is now at 7a6f47b... in softreset
```

### 合并外部版本

远程合并的无非就是“抓取（fetch）一个远程的版本库中的工作到一个临时的标签中”，然后再使用 git-merge 命令

```{bash}
[root@slh projects_bk]# git fetch root@127.0.0.1:/home/echo/projects.git
fatal: Not a git repository (or any of the parent directories): .git
```
答：当前目录必须是git库，即有.git目录的目录

```{bash}
[root@slh projects_bk]# git fetch root@192.168.157.128:/home/echo/projects.git
The authenticity of host '192.168.157.128 (192.168.157.128)' can't be established.
RSA key fingerprint is bf:58:cf:84:cd:84:49:34:b9:0f:80:cc:42:c1:5e:74.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.157.128' (RSA) to the list of known hosts.
root@192.168.157.128's password:
fatal: '/home/echo/projects.git': unable to chdir or not a git archive
fatal: The remote end hung up unexpectedly
```


# 看日记学GIT

> http://roclinux.cn/?p=184

## 1、安装了个gitk，后来又发现可以安装git-all
```{bash}
[root@slh ~]# yum install gitk
[root@slh ~]# yum install git-all
[root@slh ~]# yum list|grep ^git
git.i586                                1.6.2.5-1.fc11                 installed
git-all.noarch                          1.6.2.5-1.fc11                 installed
git-arch.noarch                         1.6.2.5-1.fc11                 installed
git-cvs.noarch                          1.6.2.5-1.fc11                 installed
git-email.noarch                        1.6.2.5-1.fc11                 installed
git-gui.noarch                          1.6.2.5-1.fc11                 installed
git-svn.noarch                          1.6.2.5-1.fc11                 installed
gitk.noarch                             1.6.2.5-1.fc11                 installed
git-cola.noarch                         1.3.8-1.fc11                   updates
git-cpan-patch.noarch                   0.2.1-1.fc11                   updates
git-daemon.i586                         1.6.2.5-1.fc11                 updates
gitg.i586                               0.0.3-1.fc11                   updates
gitosis.noarch                          0.2-8.20080825git.fc11         fedora
gitweb.noarch                           1.6.2.5-1.fc11                 updates
```
gitk包是一个带有Tcl/Tk GUI的可以用来浏览git仓库历史信息的桌面程序。

## 2、导入新的项目

配置：
```{bash}
git config --global user.name “Your Name”
git config --global user.email “you@example.com”
```

导入：
```{bash}
[root@slh echo]# mkdir gitrepo1
[root@slh echo]# cd gitrepo1
[root@slh gitrepo1]# git init
Initialized empty Git repository in /home/echo/gitrepo1/.git/
[root@slh gitrepo1]# ls -a
.  ..  .git
[root@slh gitrepo1]# git add .
fatal: pathspec '' did not match any files
[root@slh gitrepo1]# git commit
```

git add .这个命令要求git给我目前的这个项目制作一个快照snapshot（快照只是登记留名，快照不等于记录在案，git管快照叫做索引index)。快照一般会暂时存储在一个临时存储区域中。

## 3、代码修改、提交
```{bash}
[root@slh gitrepo1]# git diff--cached
```

这个git diff --cached是用来查看index file和仓库之间代码的区别的。由于我们目前只是在working tree里做了修改，还没有报告给index file，所以使用此命令显然会输出空信息。而如果省略--cached选项的话，就是比较working tree和index file的区别，由于我们的确在working tree里做了修改，所以使用git diff后会输出修改信息。
(注：三个概念：working tree、index file、仓库，省略--cached，比较前两者，加上就比较后两者)
```{bash}
[root@slh gitrepo1]# git diff
diff --git a/hello.c b/hello.c
index 848d690..6b08fcc 100644
--- a/hello.c
+++ b/hello.c
@@ -1,6 +1,7 @@
 include<stdio.h>
 int main()
  {
- printf("hello world\n");
+printf("Version:0.01\n");
+printf("hello world\n");
  return 0;
 }
 
```

还可以使用git status命令来获取整体改动的信息
```{bash}
[root@slh gitrepo1]# git status
# On branch master
# Changed but not updated:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   hello.c
#
no changes added to commit (use "git add" and/or "git commit -a")
[root@slh gitrepo1]# git commit -a
[master 5c45386]        modified:   hello.c
 1 files changed, 2 insertions(+), 1 deletions(-)
```

git commit -a，直接提交所有修改，省去了git add和git diff和git commit的工序，git commit -a无法把新增文件或文件夹加入进来，所以，如果你新增了文件或文件夹，那么就要老老实实的先git add .，再git commit喽。

查看日志：
```{bash}
[root@slh gitrepo1]# git log
commit 5c453860fbe50522ff9546e75efcb849b7fcce4f
Author: echo <shulihua@XXXX.com>
Date:   Tue Jan 5 19:40:41 2010 +0800
        modified:   hello.c
commit 1b9afca34ab5248ae6d002cb4ccbccb9873d9c6f
Author: echo <shulihua@XXXX.com>
Date:   Tue Jan 5 19:31:24 2010 +0800
        new file:   hello.c
```
注：git log -p，更详细的日志信息

## 4、分支
```{bash}
[root@slh gitrepo1]# git branch experimental
[root@slh gitrepo1]# git branch
  experimental
* master
[root@slh gitrepo1]# git checkout experimental
Switched to branch 'experimental'
```

为了方便运行，偶将hello.c重命名为main.c，结果全乱了，于是重新开始：
```{bash}
[root@slh gitrepo1]# git branch echo_br
[root@slh gitrepo1]# git checkout echo_br
[root@slh gitrepo1]# vi main.c
[root@slh gitrepo1]# git commit -a
[root@slh gitrepo1]# git checkout master
[root@slh gitrepo1]# vi main.c
[root@slh gitrepo1]# git merge echo_br
```

解决冲突：
```{bash}
[root@slh gitrepo1]# vi main.c
[root@slh gitrepo1]# git commit -a
```

这时加到服务器上，在相应的repo目录下运行gitk，终于可看到图形化界面了。。
后记：
```{bash}
[root@slh gitrepo1]# gitk
Application initialization failed: no display name and no $DISPLAY environment variable
Error in startup script: invalid command name "image"
    while executing
"image create bitmap tri-rt -background black -foreground blue -data {
    #define tri-rt_width 13
    #define tri-rt_height 13
    static unsigned cha..."
    (file "/usr/bin/gitk" line 2915)
```

查找得“That's what happens when you have a Virtual Machine WITHOUT XWindows”

注：分支experimental被偶删除了

```{bash}
[root@slh gitrepo1]# git branch -d experimental
```
在这里使用的是小写的-d，表示“在分支已经合并到主干后删除分支”。
如果使用大写的-D的话，则表示“不论如何都删除分支”，-D当然使用在“分支被证明失败”的情况下喽。
后记：貌似偶合并后用-d，结果把master上的main.c文件删除了，怪怪。

## 5、clone pull push

```{bash}
[root@slh gitrepo1]# git clone /home/echo/gitrepo1 gitrepo2
Initialized empty Git repository in /home/echo/gitrepo1/gitrepo2/.git/
```

进入/home/echo/gitrepo1/gitrepo2，修改了main.c
```{bash}
[root@slh gitrepo2]# git commit -a
[root@slh gitrepo1]# git pull /home/echo/gitrepo1/gitrepo2 master
Unpacking objects: 100% (4/4), done.
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 2), reused 0 (delta 0)
From /home/echo/gitrepo1/gitrepo2
 * branch            master     -> FETCH_HEAD
Updating 3f245e0..7adac67
Fast forward
 a.out  |  Bin 4894 -> 5385 bytes
 main.c |    4 ++--
 2 files changed, 2 insertions(+), 2 deletions(-)
```

pull命令完成了两个动作，首先从远端分支获取diff信息，第二个动作就是将改变合并到本地分支中。
//pull命令的意思是从远端git仓库中取出(git-fetch)修改的代码，然后合并(git-merge)到我（rocrocket）的项目中去

可以先fetch到一个新分支再merge到master：先修改了gitrepo2下的main.c再如下操作
```{bash}
[root@slh gitrepo1]# git fetch /home/echo/gitrepo1/gitrepo2 master:repo2_br
Unpacking objects: 100% (3/3), done.
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0)
From /home/echo/gitrepo1/gitrepo2
 * [new branch]      master     -> repo2_br
```

先比较差异：
```{bash}
[root@slh gitrepo1]# git whatchanged -p master..repo2_br
commit 81e3a782811cc0902f08debbeb706cca9c8a531d
Author: echo <shulihua@XXXX.com>
Date:   Wed Jan 6 09:46:26 2010 +0800
    in repo2
diff --git a/main.c b/main.c
index 9c819fe..9aa8f2d 100644
--- a/main.c
+++ b/main.c
@@ -13,7 +13,7 @@ printf("Day:%d\n",mylocaltime->tm_mday);
 printf("Hour:%d\n",mylocaltime->tm_hour);
 printf("Min:%d\n",mylocaltime->tm_min);
 printf("Second:%d\n",mylocaltime->tm_sec);
-printf("Version: 0.06\n");
+printf("Version: 0.07\n");
 printf("in gitrepo2!\n");
 return 0;
 }
 ```
 
再merge
```{bash}
[root@slh gitrepo1]# git checkout master
Switched to branch 'master'
[root@slh gitrepo1]# git pull . repo2_br
From .
 * branch            repo2_br   -> FETCH_HEAD
Updating 7adac67..81e3a78
Fast forward
 main.c |    2 +-
 1 files changed, 1 insertions(+), 1 deletions(-)
```

当gitrepo2想取得gitrepo1上的更新时
```{bash}
[root@slh gitrepo1]# cd gitrepo2
[root@slh gitrepo2]# git pull
From /home/echo/gitrepo1
   3f245e0..81e3a78  master     -> origin/master
 * [new branch]      repo2_br   -> origin/repo2_br
Already up-to-date.
```

但是此时的main.c还是gitrepo2时的内容，偶在gitrepo1上的

原来是忘记commit了

删除了repo2_br，再修改了gitrepo1上master的main.c后commit，再pull
```{bash}
[root@slh gitrepo2]# git pull
Unpacking objects: 100% (3/3), done.
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0)
From /home/echo/gitrepo1
```