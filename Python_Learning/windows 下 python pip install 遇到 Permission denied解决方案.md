# windows 下 python pip install 遇到 Permission denied

windows 下 python pip install 遇到 Permission denied

## 现象：报错1

python -m pip install autopep8
error: could not create 'C:\Program Files\Python37\Lib\site-packages\autopep8.py': Permission denied

## 现象：报错2

C:\Users\xiang>pip install yapf
Collecting yapf
  Downloading https://files.pythonhosted.org/packages/7c/21/534d143afd3df9cae9b21674fcc32207cb80cfb3de56b89ef7a37c746cca/yapf-0.29.0-py2.py3-none-any.whl (185kB)
     |████████████████████████████████| 194kB 12kB/s
Installing collected packages: yapf
ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 拒绝访问。: 'c:\\program files\\python37\\Lib\\site-packages\\yapf'
Consider using the `--user` option or check the permissions.

WARNING: You are using pip version 19.3; however, version 20.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

## 方案1 进入命令行 cmd 

键入runas /profile /user:{user} "{cmd}" 

如：runas /profile /user:Administrator "pip install pylab" 

表示用 Administrator 运行 pip install pylab。 回车后会提示输入密码。

runas /profile /user:Administrator "python -m pip install autopep8" 
runas /profile /user:xiangxing985529@163.com "python -m pip install autopep8"

## 方案2 CMD 以管理员身份运行

以管理员身份运行后，权限问题就解决啦
随便安装了

python -m pip install autopep8



## python的代码错误检查 & 自动格式化代码

autopep8

python的代码错误检查通常用pep8、pylint和flake8，自动格式化代码通常用autopep8、yapf、black。

这些工具均可以利用pip进行安装，这里介绍传统的利用pip.exe安装和在VScode中安装两种方式。

【温馨提醒】
要使用flake8或要想flake8等工具起作用，前提是必须把settings.json文件中的"python.linting.enabled"值设为“true”，否则即使安装了这些工具，也起不到代码的错误提醒。


### 【传统安装方式】

以安装flake8为例，其余类似

方法一：
1.打开命令行窗口（同时按Win+R，输入cmd）
2.输入：python -m pip install flake8，回车运行等待结果即可
【注意】前提是必须将python的路径添加至环境变量。

方法二：
1.打开命令行窗口（同时按Win+R，输入cmd）
2.将pip.exe直接拖进cmd窗口
3.输入：pip install flake8，回车等待运行结果即可

方法三：
1.在pip.exe所在的目录，按Shift+鼠标右键，打开PowerShell窗口（win10以前的版本是可以直接打开命令行窗口）
2.输入：cmd，回车运行
3.输入：pip install flake8，回车等待运行结果即可

### 【在Vscode中安装】

代码错误工具以flake8为例：

1.在VScode中打开设置，搜索python.linting.flake8enabled
2.在Settings界面中勾选

 Whether to lint Python files using flake8
或者在User Settings.json文件中，
点击左侧默认用户设置"python.linting.flake8Enabled: false的笔形图形，选择true；或者直接在右侧栏自定义设置中，添加"python.linting.flake8Enabled": true
3.右下角会弹出配置通知，点Install安装
4.在终端界面会出现下载成功

# Recommended
name = 'John Smith'
first_name, last_name = name.split()
print(last_name, first_name, sep=', ')
# 'Smith, John'
