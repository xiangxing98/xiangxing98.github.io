## Git 日常发布流程
```
//本地如果无远程代码，先做这步，不然就忽略 
git clone git@github.com:heiniuhaha/heiniuhaha.github.com.git

//定位到你blog的目录下 
cd .ssh/heiniuhaha.github.com

 //先同步远程文件，后面的参数会自动连接你远程的文件
git pull origin master

//查看本地自己修改了多少文件
git status 

//添加远程不存在的git文件
git add . 

//提交到本地版本库
git commit * -m "what I want told to someone" 

//更新到远程服务器上
git push origin master
```