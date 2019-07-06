# Git的使用问题解决方案

##HTTP request failed

```{bash}
git push origin master
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/xiangxing98/c.git/info/refs

fatal: HTTP request failed

# 在用git上传时，发送如下错误：
[root@rhel6 git]# git push -u origin master
error: The requested URL returned error: 403 while accessing https://github.com/HangzhouSeason/test-onlyfortest.git/info/refs

fatal: HTTP request failed
```

### 解决办法：修改配置文件

输入：vi .git/config来修改配置文件：

修改前：

[remote "origin"]
     url = https://github.com/*********/test-onlyfortest.git
     fetch = +refs/heads/*:refs/remotes/origin/*

修改后：

[remote "origin"]
     url = https://你的用户名@github.com/********/test-onlyfortest.git
     fetch = +refs/heads/*:refs/remotes/origin/*

然后输入：wq保存退出

再输入：git push -u origin master 就能正确上传啦。2014年11月2日
