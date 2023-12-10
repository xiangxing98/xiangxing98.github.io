# Git 日常发布流程

```{sh}
# 本地如果无远程代码，先做这步，不然就忽略
git clone git@github.com:heiniuhaha/heiniuhaha.github.com.git

# 定位到你blog的目录下
cd .ssh/heiniuhaha.github.com

# 配置用户名
git config --global user.name "xiangxing98"

# 配置邮箱
git config --global user.email "xiangxing985529@163.com"

# 配置项的列表
git config --list

# 创建SSH Key(添加Github远程库时需要)
# 在用户主目录下(我的win7，在C:\Users\**\下)，看看有没有.ssh目录.
# 如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，
# 如果已经有了，可直接跳到下一步。
# 如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
ssh-keygen -t rsa -C "xiangxing985529@163.com"

# Generating public/private rsa key pair.
# Enter file in which to save the key (/c/Users/xiang/.ssh/id_rsa):
# Created directory '/c/Users/xiang/.ssh'.
# Enter passphrase (empty for no passphrase):
# Enter same passphrase again:
# Your identification has been saved in /c/Users/xiang/.ssh/id_rsa.
# Your public key has been saved in /c/Users/xiang/.ssh/id_rsa.pub.
# The key fingerprint is:
# SHA256:3rno58FajjxAb39mP9WXNfmo3S0ca3zzxZuhqMUFA+4 xiangxing985529@163.com
# The key's randomart image is:
# +---[RSA 2048]----+
# |         .       |
# |        . .      |
# |         . o    .|
# |      . .   o  o.|
# |     . .SE   . .*|
# |      ..oo... oo=|
# |       o..*o = *=|
# |       ..*+o* X.O|
# |       .*=== +.*+|
# +----[SHA256]-----+

 cat /c/Users/xiang/.ssh/id_rsa.pub

```
$ ssh-keygen -t rsa -C "xiangxing985529@163.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/Administrator/.ssh/id_rsa):
Created directory '/c/Users/Administrator/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/Administrator/.ssh/id_rsa
Your public key has been saved in /c/Users/Administrator/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:g3gcgmqbB1l/ktMm9NJ/gkx2CcCBytoNBhhYNH4KOz0 xiangxing985529@163.com
The key's randomart image is:
+---[RSA 3072]----+
|+++ oo.          |
|+. + ..          |
|o.+.o...         |
| B=oo+=o. .      |
|=*Eo.B+OSo       |
|o.=...@ +.       |
| o .   o o .     |
|  .       o      |
|                 |
+----[SHA256]-----+
```


# 如果一切顺利的话，可以在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件.
# 这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，
# 可以放心地告诉任何人。
# 登陆GitHub，打开“Account settings”，“SSH Keys”页面,点“Add SSH Key”，填上任意Title，在Key文本框里粘贴公钥id_rsa.pub文件的内容.

#测试SSH 执行
ssh -T git@github.com
# 对于 oschina 的 “码云” ，执行 ssh -T git@git.oschina.net
# 对于 coding 的 “码市” ，执行 ssh -T git@git.coding.net
# The authenticity of host 'github.com (13.250.177.223)' can't be established.
# RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
# Are you sure you want to continue connecting (yes/no)? yes
# Warning: Permanently added 'github.com,13.250.177.223' (RSA) to the list of known hosts.

# Hi xiangxing98! You've successfully authenticated, but GitHub does not provide shell access.


# 显示当前的Git配置
git config --list

# 编辑Git配置文件，# .config文件在C:\Users\你的用户名\.gitconfig
git config -e --global
git config --global --edit

# 设置提交代码时的用户信息
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"


# 先同步远程文件，后面的参数会自动连接你远程的文件
git pull origin master

# 查看本地自己修改了多少文件
git status

# 添加远程不存在的git文件
git add .

# 提交到本地版本库
git commit * -m "what I want told to someone"

# 更新到远程服务器上
git push origin master
```
