# Configuring_a_Remote_for_a_Forked_Repository_And_Synchronization
> Stone Hou 2017-05-30

## configuring-a-remote-for-a-fork & syncing-a-fork
关于fork同步的参考文章：
[configuring-a-remote-for-a-fork](https://help.github.com/articles/configuring-a-remote-for-a-fork/ "configuring-a-remote-for-a-fork")
[syncing-a-fork](https://help.github.com/articles/syncing-a-fork/ "syncing-a-fork")
[ysc:如何更新自己Fork的代码](https://github.com/ysc/APDPlat/wiki/%E5%A6%82%E4%BD%95%E6%9B%B4%E6%96%B0%E8%87%AA%E5%B7%B1Fork%E7%9A%84%E4%BB%A3%E7%A0%81 "如何更新自己Fork的代码")

## 1. 给fork配置远程库 Configuring a remote for a fork
### Step 1.0 检出自己在github上fork的Repository的分支
在更新自己Fork的代码之前，需要先把自己在本地的更改进行提交。 
检出自己在github上fork的Repository的分支到本地的文件夹。
如果已经从Repository中检出了代码，则此步骤为切换到本地的Repository根目录然后执行下一步。 
```
git clone https://github.com/appframe/APDPlat.git
cd APDPlat
```

### Step 1.1 从自己fork之后的版本库Clone--git clone -o <name>
```
# git clone -o <name>
# Instead of using the remote name origin to keep track of 
# the upstream repository, use <name>.
git clone -o chucklu https://github.com/chucklu/Hearthstone-Deck-Tracker.git
```

### Step 1.2 Open Git Bash, use git remote check remote status
```
# List the current configured remote repository for your fork.
# 使用git remote -v查看远程状态git remote -v
git remote -v 
# origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
# origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
# 以上表明，origin这个repository对应的是远端的https开头的这个链接指向的repository，
# 即自己fork出的repository.
```

### Step 1.3 再将别人的版本库(源分支地址)git remote add [shortname/alias] [url/path]
```
# Add remote upstream for syncing to your fork
# Specify a new remote upstream repository that will be synced with the fork.
# 增加源分支地址到你项目远程分支列表中，先得将原来的仓库指定为upstream(上游源头) 
git remote add APDPlat-ysc https://github.com/ysc/APDPlat.git
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
git remote add epix37 https://github.com/Epix37/Hearthstone-Deck-Tracker.git
```

### Step 1.4 再次使用git remote -v查看远程状态，确认是否配置成功。
```
git remote -v 
# origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)  
# origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)  
# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)  
# upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)

#下面是举例的例子的，upstream为epix37,别名或者简称
# chucklu https://github.com/chucklu/Hearthstone-Deck-Tracker.git (fetch)
# chucklu https://github.com/chucklu/Hearthstone-Deck-Tracker.git (push)
# epix37 https://github.com/Epix37/Hearthstone-Deck-Tracker.git (fetch)
# epix37 https://github.com/Epix37/Hearthstone-Deck-Tracker.git (push)

# 如果之前用的是git clone命令的话，可以用rename来进行重命名远端
# 重新命名远端git remote rename oldname newname
```

## 2. 同步fork来的仓库（Repository）

### Step 2.1 把远程原始分支的代码拉到本地
```
# 从上游仓库 fetch 分支和提交点，提交给本地 master
# 并会被存储在一个本地分支 upstream/master 
git fetch upstream
# remote: Counting objects: 75, done.  
# remote: Compressing objects: 100% (53/53), done.  
# remote: Total 62 (delta 27), reused 44 (delta 9)  
# Unpacking objects: 100% (62/62), done.  
# From https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY  
#  * [new branch]      master     -> upstream/master
```
以上表明，远程的原repository上确实有一些更新，现在它们已经被download到本地的.git文件夹下了， 
但是还没有合并到本地的代码中。

### Step 2.2 切换到本地主分支(如果不在的话) 
这是保证切换到本地的repository的master上，如果本来就在，那么这一步不是必须的。
```
git checkout master
```

### Step 2.3 把 upstream/master 分支合并到本地 master 上
这样就完成了同步，并且不会丢掉本地修改的内容。  
运行`git merge upstream/master`命令，将upstream/master上的更新合并到本地的master上， 
其实就是将第三步中download到.git文件夹下的那些改变合并到本地的主分支master中。 
```
git merge upstream/master
# Updating a422352..5fdff0f  
# Fast-forward  
#  README                    |    9 -------  
#  README.md                 |    7 ++++++  
#  2 files changed, 7 insertions(+), 9 deletions(-)  
#  delete mode 100644 README  
#  create mode 100644 README.md
```

### Step 2.4 解决冲突
如果本地有自己独立的更新，而又会引起冲突的话，则要解决冲突，再commit.
关于解决冲突，如果明确所有冲突都是使用upstream/master上的来override自己的，
那么可以直接运行如下命令，则无需解决冲突了：
```
git merge -X theirs upstream/master  
```

### Step 2.5 更新最新的代码到自己Github的远程仓库
如果想更新到GitHub的fork上，直接`git push origin master`就好了
注意，以上2.4步骤结束后，仅仅是本地的fork出的repository和原repository取得了同步，
如果想让远程的fork出的repository也同样取得同步，必须再git push上去。
```
git push origin master
```

### Step 2.6 给远程的原始仓库发送推送请求Pull Request，贡献代码
```
# 用自己的github账号登陆github网站，
# 打开自己Fork来的仓库的地址，例如：https://github.com/appframe/APDPlat
# 点击Pull Request
# 点击New Pull Request
# 输入Title简要描述你改进的功能
# 输入详细的功能说明
# 点击Send pull request
# 这样就把你的所有commit发送给远程的原始仓库APDPlat-ysc了
```
