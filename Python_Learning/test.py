# 打印左下角三角形：for i in range(10):之后，range(0,i)
# 打印右上角三角形：在左下角的基础上，将"－"变成" "空格

for i in range(10):
    for j in range(0,i):
        print("-",end=" ")

    for j in range(i,10):
        print("$", end=" ")

    print("")

print("-------------------------")
