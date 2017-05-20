# xiangxing98.github.io

侯祥胡的Github 个人空间，分享一些计算机与程序设计方面的学习感悟。

hello github

This is [侯祥胡的Git Pages](https://xiangxing98.github.io "侯祥胡的Git Pages") link.

This is [Back to Xiangxing98 Github Profile](https://github.com/xiangxing98 "xiangxing98") inline link.

<h4><a href="Configuring-a-remote-for-a-fork_Syncing-a-fork.html">Configuring-a-remote-for-a-fork_Syncing-a-fork.html</a></h4>

<h4><a href="https://github.com/xiangxing98/">https://github.com/xiangxing98/</a></h4>

<h4><a href="https://www.linkedin.com/in/祥胡-侯-9703b4123">侯祥胡 linkedin Information</a></h4>

## Data Camp - data science
This is [Data camp](http://www.datacamp.com "Data camp") inline link.
- Improve your skills - and your career
- No matter what industry you’re in, learning how to analyze and understand your data is critical. 
- That’s why DataCamp provides you with the tools to learn the data science skills you need to start your own data projects.

## R Tutorials
[R Tutorials](https://www.tutorialspoint.com/r/index.htm "R Tutorials")

## git CODE
``` GIT 
echo "# learn-centos" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/xiangxing98/learn-centos.git
git push -u origin master

#SSH
echo "# learn-centos" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:xiangxing98/learn-centos.git
git push -u origin master

git clone git@github.com:xiangxing98/learn-centos.git learn-centos
git add .
git commit -m "comment here about what you
```

# Update_Forked_Project_in_Github
> [参考](https://www.zhihu.com/question/20393785/answer/30725725 "zhihu answer")

## 1.配置上游项目地址, 建立主repo的远程源
Configure remotes,When a repo is cloned, it has a default remote called origin that points to your fork on GitHub, not the original repo it was forked from. 

To keep track of the original repo, you need to add another remote named upstream:

```
cd Spoon-Knife
# Changes the active directory in the prompt to the newly cloned "Spoon-Knife" directory

git remote -v
# 首先要先确定一下是否建立了主repo的远程源

git remote add upstream https://github.com/octocat/Spoon-Knife.git
# Assigns the original repo to a remote called "upstream"
# 如果里面只能看到你自己的两个源(fetch 和 push)，那就需要添加主repo的源,git remote add upstream URL

git remote -v
# 再次确定一下是否建立了主repo的远程源，现在你就能看到upstream了,like：
# origin  git@github.com:cobish/fork-demo.git (fetch)
# origin  git@github.com:cobish/fork-demo.git (push)
# upstream    https://github.com/wabish/fork-demo.git (fetch)
# upstream    https://github.com/wabish/fork-demo.git (push)
```

## 2. 获取上游项目更新
Pull in (Fetch then merge) upstream changes. If the original repo you forked your project from gets updated, you can add those updates to your fork by running the following code:
```
git fetch upstream
# Fetches any new changes from the original repo. Pulls in changes not present in your local repository, without modifying your files. 使用 fetch 命令更新，fetch 后会被存储在一个本地分支 upstream/master 上。
```

## 3.与主repo合并
```
git merge upstream/master
# Merges any changes fetched into your working files,合并到本地分支。切换到 master 分支，合并 upstream/master 分支。
```

## 4. 提交推送
```
git push origin master
```
Test 2nd person to update
