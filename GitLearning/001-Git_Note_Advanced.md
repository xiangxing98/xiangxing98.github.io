# Git_Note_Advanced-tag/branch/conflict/ignore
> 2011-09-12 17:33:13 

## tag
在git中可以为任意其他对象添加tag，包括commit，tree，blob，甚至包括tag自身。git中都是用sha-1标识git对象，这是一个40个字符长度的字符串，不方便记忆，那么可为git对象添加一个tag便于标识不同对象。
```
# 添加tag
# git tag tag-name sha-1
$ git tag v1.0 bdc390c2
# 这样便为bdc390c2的对象添加了一个tag，如果不指定sha-1，会为最近的一个commit对象添加tag

# 查看tag, 使用git tag命令便能查看所有tag
$ git tag

# 当然可以筛选
$ git tag -l 'v1.*'

# 删除tag
$ git tag -d <tag-name>

# 重命名tag,重命名tag有两种方式：
# 1. 删除原tag，重新添加
# 2. git tag -f 强制替换已存在的tag后，再删除原tag
$ git tag -f <new-tag> <old-tag>
$ git tag -d <old-tag>
```

### tag的分类
轻量型标签 轻量型标签直接使用 $ git tag <tag-name> <git-object> 即可创建
标注型(annotated)标签 标注型标签可记录更多的信息，
使用 $ git tag -a <tag-name> <git-object> -m ‘tag message’即可创意一个标注性标签

## 分支
建议多使用分支来维护项目，便于保证主干的稳定性。
```
# 创建分支, git中创建分支的方法非常简单,git branch <branch-name>
$ git branch dev

# 这样便从当前分支创建了一个名为dev的分支，可以让此分支作为开发分支。
# 使用checkout <branch-name>可以很方便地在分支间进行切换：
$ git checkout master
$ git checkout dev

# 还可以直接使用checkout -b命令来创建分支后并切换到新的分支
$ git checkout -b dev

# 重命名分支
$ git branch -rm <old-branch> <new-branch>

# 远程分支

#推送本地分支到远程服务器
$ git push <remote> <branch-name>[:<remote-branch-name>]

# 远程分支名如果省略，则使用本地分支名作为远程分支名
$ git push <remote> <branch-name>

# 删除分支
# 删除分支
$ git branch -d <branch-name>

# 强制删除分支
$ git branch -D <branch-name>

# 删除远程分支
$ git push <remote> :<remote-branch-name>

# 这个命令是不是可以从推送本地分支到远程分支的命令中得到一点灵感？
# 是的，省略本地分支名后，远程分支即被删除！

# 查看分支
# 使用git branch命令可查看当前git版本库中所有分支：
$ git branch
# 查看分支,当前分支会在分支前加以星号（*）标注。

# git branch -v命令将附加显示最后一次提交相关信息的分支信息
$ git branch -v

# 查看已合并的分支
$ git branch --merge

# 查看未合并的分支
$ git branch --no-merged

# 分支合并
# 当一个分支完成预期的工作，通过测试后，便可合并到主干，作为稳定版本进行后续开发，
# 合并分支的命令非常简单：git merge branch-name
$ git merge dev

# 如果顺利，dev分支将自动地合并到当前分支。
当然很多时候会产生冲突，这个时候就需要手动坚决冲突后再进行合并。
```

## conflict冲突
conflict在git中如遇冲突，会显示冲突提示，合并会中断conflict,
此时你可以使用git mergetool命令调用merge工具进行手动合并.
```
$ git mergetool
# mergetool在配置项进行配置，以下是使用vimdiff的merge操作界面
mergetool vimdiff
```
手动解决完冲突后，还需要进行一次提交，便完成了整个手动合并过程。

## rebase
rebase亦是将分支的修改进行“合并”。
但在具体行为上略有不同，使用merge进行合并，更新部分依然会视作是从分支而来；
而rebase则是直接将更新合并到新分支，相当于是在合并分支的直接修改。
如果我们的更新是非常小，不足以作为一个分支进行合并，并且不想污染版本日志，
那么便可以使用rebase来合并更新。

## ignore
在一个git版本仓库中，有时候很多文件/目录并不需要使用git进行版本维护，
那么就可以将这些文件/目录加入.gitignore文件中，
在.gitignore文件中可定义要排除在git版本管理之外的文件/目录，
git默认会读取项目目录下的.gitignore文件。

.gitignore使用标准的shell glob模式匹配，shell glob你可以简单地理解为一种特特殊化的正则表达式，
其实要比正则表达式简单许多，语法如下：

允许使用空行，没有实际语法作用
# 开头的行视作注释
! 开头的模式会覆盖之前的定义，将匹配的对象重新加入跟踪列表
以/结尾的模式，git会屏蔽掉该目录及其所有子目录及文件（只屏蔽目录）
不以/结尾的模式，git屏蔽同名的文件名及目录（屏蔽目录和同名文件）
以/开头的模式，git只会屏蔽项目根目录下的匹配对象
示例：
#.gitignore example
.txt
.gitignore
!readme.txt
exclude/*.txt
该.gitignore中定义的屏蔽规则为：

屏蔽所有的txt文件，但是readme.txt例外；屏蔽所有的.gitignore文件；
屏蔽exclude目录下的所有txt文件（包括readme.txt）。
另外，还可以在配置项中通过core.excludesfile来指定ignore文件。

```
$ git config core.excludesfile '_myignore'
```

## git配置

git配置文件根据作用域的不同分为三种：

系统配置文件（git安装目录/gitconfig）
用户配置文件（用户主目录/.gitconfig）
项目配置文件（.git/config）
git配置项都通过git config命令写入，传入不同参数写入不同的配置文件
```
$ git config --system/--global/
git config –system 写入系统配置
git config –global 写入用户配置
git config 写入项目配置
```
具体的配置项设置参考帮助文档，`$ git config –help`

## git中的对象
git中包含4类对象：
commit 提交对象
tree 目录
blob 文件
tag 标记
git提交便产生一个commit对象，commit对象中包含一个tree对象，
tree对象中又会包含其他的tree对象或是blob对象，blob对象是最小的组成单元，即独立的文件。
每个对象都对应一个唯一的SHA-1值，只有当文件或目录有修改时这个值才会重新计算发生改变。
```
$ git log 可以查看所有commit对象
$ git ls-tree <commit> 查看commit对象中的tree对象
$ git show <blob> 查看blob的具体内容
```

## git原理
究竟git是如何工作的？打开.git目录便可一目了然。

HEAD 指向当前分支
config 项目配置文件
description 供GitWeb程序使用
hooks/ 客户端与服务端钩子脚本
info/ 忽略模式
index 暂存区域信息
objects/ 所有数据内容
refs/ 指向所有commit的指针
HEAD文件中是形如以下代码的内容：

ref: refs/heads/dev
它指向refs/heads/dev，而dev文件中代码指向当前分支最近的commit对象

objects目录中保存有所有git对象，这些对象取sha-1值的前两个字母为一个目录，
剩下的38个字符作为文件名保存，在上一节“git中对象”中能查看到的所有git对象都保存在这个目录中，
可以使用git cat-file <sha-1>来获取对象内容。
```
$ git cat-file -p 63a46849
```
不妨多使用cat-file命名多看看各种对象的内容，有助于理解git对象的结构。

refs目录中保存了git中使用的所有引用或指针，因为不可能任何时候都是用sha-1值来指代对象，
git对象也可以有“缩略名”。通常refs目录会包含以下目录：

heads 保存所有分支的HEAD指针
remotes 保存远程仓库信息
tags 保存所有tag指针
逐一地查看这些文件内容，你就什么都明白了。使用 git update-ref 命令可以直接新建一个引用。
```
$ git update-ref refs/heads/test-branch c56dce
$ git update-ref refs/tags/test-tag c56dce
```
执行上述命令，这样你的git版本库中就多了一个test-branch分支和一个名为test-tag的tag。

其他的比如git还有些底层的命令，我在文中所列举的，包括之前基础篇的都是一些高级命令。
可以使用这些底层命名直接对git库进行一些操作，有关git底层命名的详细内容，可以到网上去找找。