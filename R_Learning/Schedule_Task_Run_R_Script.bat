echo R CMD BATCH 和 Rscript 使用前都要先添加环境变量
echo 把 C:\Program Files\R\R-3.3.0\bin; 加到"系统变量"的Path 值的最开始

echo 1. 可以用 R CMD BATCH *.r, 第一种命令适用于Windows和Mac
echo 2. 也可以用 Rscript *.r args0 args1 这个可以跟一定的参数, 第二种命令适用于Linux
echo 3. 当然也可以进入R交互环境 > source("*.r"), 第三种命令都适用，不过不能跟命令行参数

echo 如果R脚本里有函数， 函数中有参数，可以用args(function) 查看这个函数的参数
echo paramValue <- 15
echo source("myRfile.R")
echo myRfile.R 中有个参数教 paramValue， 那么可以先给paramValue 赋值，然后source R脚本
echo Rscript -e 可以直接执行R语言中 的表达式，如下
echo Rscript -e "l+4"


echo E:\03-Download\Github\xiangxing98.github.io\R_Learning
echo 1. R脚本与bat文件不在同一个文件夹
"D:\Program Files\R\R-3.3.2\bin\R.exe" CMD BATCH "C:\Users\Stone\Desktop\Test.r" test.txt
echo R脚本执行完毕，暂停
pause

echo 2. R脚本与bat文件在同一个文件夹
"D:\Program Files\R\R-3.3.2\bin\R.exe" CMD BATCH Test.r test.txt
echo R脚本执行完毕，暂停
pause

echo D:\Program Files\R\R-3.3.2\bin\R.exe
echo test.txt可以写也可以不写，如果不写的话，默认会生成一个“程序名.Rout"的文件，里面保存的是程序代码，不过最后会调用"proc.time()函数"

echo 1 Windows：
echo 键入 cd C:\Program Files\R\R-3.2.0\bin   工作目录切换到R的核心程序目录
echo 键入 R BATCH F:\Test.R 或 Rscript F:\Test.R 运行脚本
echo 前者R控制台内容记录到Test.Rout文件中，后者则将数据输出到windows控制台。二者涉及文件创建都需要权限。
echo 后者也是linux下运行R脚本的命令。

echo 2 Linux：
echo R  --no-save  <  step1.R  >temp001

echo Use  Rscript
"D:\Program Files\R\R-3.3.2\bin\x32\Rscript.exe" "C:\Users\Stone\Desktop\Test.r"
pause

echo 2. R脚本与bat文件在同一个文件夹
echo Use  Rscript
"D:\Program Files\R\R-3.3.2\bin\x32\Rscript.exe" Test.r
pause


