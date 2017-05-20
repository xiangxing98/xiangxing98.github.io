/**
 * @ Title:		Update_Forked_Project_in_Github.md
 * @ Authors:	siqin.hou (xiangxing985529@163.com)
 * @ Date:		2017-05-20 13:13:55
 * @ Version:	
 */
---

<!-- MarkdownTOC -->

- Update_Forked_Project_in_Github
    - 1.配置上游项目地址, 建立主repo的远程源
    - 2. 获取上游项目更新
    - 3.与主repo合并
    - 4. 提交推送
- Markdown语法示例
- 这是高阶标题（效果和一级标题一样 ）
    - 这是次阶标题（效果和二级标题一样）
    - 这是二级标题
    - 分割线

<!-- /MarkdownTOC -->

---

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



# Markdown语法示例

这是高阶标题（效果和一级标题一样 ）
========

这是次阶标题（效果和二级标题一样）
--------------

## 这是二级标题

### 这是三级标题

#### 这是四级标题

##### 这是五级标题

###### 这是六级标题

> 这是一级引用
>>这是二级引用
>>> 这是三级引用
>这是一级引用

```javascript 
var canvas = document.getElementById("canvas"); 
var context = canvas.getContext("2d"); 
```

使用导入图片
![Alt text](/path/to/img.jpg "Optional title")
![Markdown](http://images.cnitblog.com/blog/404392/201501/122257231047591.jpg)

1. 第一点
2. 第二点
4. 第三点

+ 呵呵
    * 嘉嘉
    - 嘻嘻
    - 吼吼
        - 嘎嘎
        + 桀桀
* 哈哈

 **粗体1**    __粗体2__
 *斜体1*    _斜体2_

 * ------:为右对齐。 
* :------为左对齐。 
* :------:为居中对齐。 
* -------为使用默认居中对齐。

|         序号    |    交易名    |    交易说明    |    备注    |
|    ------: |    :-------:    |    :---------   |    ------    |
|    1    |    prfcfg    |    菜单配置    |    可以通过此交易查询到所有交易码和菜单的对应关系    |
|    2    |    gentmo    |    编译所有交易    |    |
|    100000    |    sysdba    |    数据库表模型汇总    |    |

分割线
---
***
* * *

例1：行内链接

这就是我们常用的地址：[Baidu](www.baidu.com "百度一下，你就知道" )
这就是我们常用的地址：Baidu

例2：参考式链接

这就是我们常用的地址：[Baidu][1]
[1]:www.baidu.com "百度一下，你就知道" 

标签: 数学 英语
Tags: 数学 英语

这是一个注脚测试[^footer1]。
[^footer1]: 这是一个测试，用来阐释注脚。