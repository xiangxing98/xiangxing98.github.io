url0 = "https://www.meitulu.com/item/20984.html"
max_page_num = 20
for i in range(2,max_page_num + 1):
    print(str(i))
    urls2 = url0.replace(".html", "_" + str(i) + ".html")
    print(urls2)
