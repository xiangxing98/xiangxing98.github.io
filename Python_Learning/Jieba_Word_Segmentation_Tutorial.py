# coding: utf-8

# ###jieba特性介绍
# 支持三种分词模式：
# 精确模式，试图将句子最精确地切开，适合文本分析；
# 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
# 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
# 支持繁体分词。
# 支持自定义词典。
# MIT 授权协议。

# ###分词速度
# 1.5 MB / Second in Full Mode
# 400 KB / Second in Default Mode
# 测试环境: Intel(R) Core(TM) i7-2600 CPU @ 3.4GHz；《围城》.txt

# #一、 第一部分

# ##Part 1. 分词

# jieba.cut 方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型。
# jieba.cut_for_search 方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细。
# 待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8。
# jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用
# jieba.lcut 以及 jieba.lcut_for_search 直接返回 list。
# jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器，所有全局分词相关函数都是该分词器的映射。

# In[1]:

import jieba
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式


# In[15]:

seg_list = jieba.cut("我来到北京清华大学", cut_all = False)
print("Precise Mode: " + "/".join(seg_list))  #精确模式，默认状态下也是精确模式


# In[16]:

seg_list = jieba.cut("他来到网易杭研大厦。")
print("Default Mode: " + "/".join(seg_list))


# In[14]:

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造。")  #搜索引擎模式
print("Search Mode: " + "/".join(seg_list))


# ##Part 2. 添加自定义词典

# ###载入词典
# 开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率。
# 用法： jieba.load_userdict(file_name) # file_name 为自定义词典的路径。
# 词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频（可省略），最后为词性（可省略），用空格隔开。
# 词频可省略，使用计算出的能保证分出该词的词频。
# 更改分词器的 tmp_dir 和 cache_file 属性，可指定缓存文件位置，用于受限的文件系统。

# In[5]:

seg_list = jieba.cut("李小福是创新办主任也是云计算方面的专家。")
print("Origin: " + "/".join(seg_list))


# In[6]:

jieba.load_userdict("C:\\Users\\Luo Chen\\Desktop\\lixiaofu.txt")
seg_list = jieba.cut("李小福是创新办主任也是云计算方面的专家。")
print("Revise: " + "/".join(seg_list))


# ###调整词典

# 使用 add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
# 使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
# 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。

# In[7]:

print("/".join(jieba.cut("如果放到post中将出错。", HMM = False)))


# In[8]:

#利用调节词频使“中”，“将”都能被分出来
jieba.suggest_freq(("中", "将"), tune = True)


# In[9]:

print("/".join(jieba.cut("如果放到post中将出错。", HMM = False)))


# In[16]:

Original = "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。", HMM = False))
print "Original: " + Original


# In[21]:

jieba.add_word("江大桥", freq = 20000, tag = None)
print "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。"))


# In[20]:

jieba.load_userdict("C:\\Users\\Luo Chen\\Desktop\\shizhang.txt")
print "Revise: " + "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。", HMM = False))


# ##Part 3. 词性标注

# jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。jieba.posseg.dt 为默认词性标注分词器。
# 标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。

# In[22]:

import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门。")
for w in words:
    print("%s %s" %(w.word, w.flag))


# ##Part 4. 关键词提取

# ###基于 TF-IDF 算法的关键词提取

# import jieba.analyse
# jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())
# sentence:待提取的文本。
# topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
# withWeight:是否一并返回关键词权重值，默认值为False。
# allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。
# jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件。

# optparse模块OptionParser学习
# optparse是专门在命令行添加选项的一个模块。

# In[2]:

from optparse import OptionParser
MSG_USAGE = "myprog[ -f ][-s ] arg1[,arg2..]"
optParser = OptionParser(MSG_USAGE)
#以上，产生一个OptionParser的物件optParser。传入的值MSG_USAGE可被调用打印命令时显示出来。

optParser.add_option("-f","--file",action = "store",type="string",dest = "fileName")
optParser.add_option("-v","--vison", action="store_false", dest="verbose",default='gggggg',
                     help="make lots of noise [default]")
#调用OptionParser.add_option()添加选项，add_option()参数说明：
#action:存储方式，分为三种store, store_false, store_true
#type:类型
#dest:存储的变量
#default:默认值
#help:帮助信息

fakeArgs = ['-f','file.txt','-v','good luck to you', 'arg2', 'arge']
options, args = optParser.parse_args(fakeArgs)
print options.fileName
print options.verbose
print options
print args
#调用OptionParser.parse_args()剖析并返回一个directory和一个list
#parse_args()说明:
#如果没有传入参数，parse_args会默认将sys.argv[1:]的值作为默认参数。这里我们将fakeArgs模拟输入的值。
#从返回结果中可以看到，
#options为是一个directory,它的内容fakeArgs为“参数/值 ”的键值对。
#args 是一个list，它的内容是fakeargs除去options后，剩余的输入内容。
#options.version和options.fileName都取到与options中的directory的值。

print optParser.print_help()
#输出帮助信息
#optParser.print_help()说明：
#1、最开始的的MSG_USAGE的值:在这个地方显示出来了。
#2、自动添加了-h这个参数。


# In[14]:

import jieba.analyse as anl
f = open("C:\\Users\\Luo Chen\\Desktop\\demo.txt", "r").read()
seg = anl.extract_tags(f, topK = 20, withWeight = True)
for tag, weight in seg:
    print "%s %s" %(tag, weight)


# 关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径。
# jieba.analyse.set_idf_path(file_name) #file_name为自定义语料库的路径
# 如：jieba.analyse.set_idf_path("../extra_dict/idf.txt.big")
# .big文件一般是游戏中的文件，比较常见的用途是装载游戏的音乐、声音等文件。
#
# 关键词提取所使用停用词（Stop Words）文本语料库可以切换成自定义语料库的路径。
# jieba.analyse.set_stop_words(file_name) #file_name为自定义语料库的路径。
# 如：jieba.analyse.set_stop_words("../extra_dict/stop_words.txt")

# ###基于 TextRank 算法的关键词提取

# 基本思想:
# 将待抽取关键词的文本进行分词；
# 以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图；
# 计算图中节点的PageRank，注意是无向带权图。
# jieba.analyse.textrank(sentence, topK = 20, withWeight = False, allowPOS = ('ns', 'n', 'v', 'nv')) 注意默认过滤词性。
# jieba.analyse.TextRank() 新建自定义TextRank实例。

# In[16]:

s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.textrank(s, topK = 5, withWeight = True):
    print("%s %s" % (x, w))


# ##Part 5. 并行分词（多进程分词）

# 原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升。
# 基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows。
# 用法：
# jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
# jieba.disable_parallel() # 关闭并行分词模式
# 实验结果：在 4 核 3.4GHz Linux 机器上，对金庸全集进行精确分词，获得了 1MB/s 的速度，是单进程版的 3.3 倍。
# 注意：并行分词仅支持默认分词器 jieba.dt 和 jieba.posseg.dt。

# ##Part 6. Tokenize: 返回词语在原文的起止位置

# 注意：输入参数只接受 unicode
# 两种模式：默认模式、搜索模式。

# ###默认模式

# In[19]:

result = jieba.tokenize(u"永和服装饰品有限公司")
for tk in result:
    print("%s \t start at: %d \t end at: %d" %(tk[0], tk[1], tk[2]))


# ###搜索模式
# 把句子中所有的可以成词的词语都扫描出来并确定位置。

# In[20]:

result = jieba.tokenize(u"永和服装饰品有限公司", mode = "search")
for tk in result:
    print("%s \t start at: %d \t end at: %d" % (tk[0], tk[1], tk[2]))


# ##Part 7. 延迟加载机制
# jieba 采用延迟加载，import jieba 和 jieba.Tokenizer() 不会立即触发词典的加载，一旦有必要才开始加载词典构建前缀字典。如果你想手工初始 jieba，也可以手动初始化。
# import jieba
# jieba.initialize()  #手动初始化（可选）

# 在 0.28 之前的版本是不能指定主词典的路径的，有了延迟加载机制后，你可以改变主词典的路径:
# jieba.set_dictionary("data/dict.txt.big")
# 也可以下载你所需要的词典，然后覆盖jieba/dict.txt即可。

# #二、 第二部分

# ##Part 1. 词频统计、降序排序

# In[21]:

article = open("C:\\Users\\Luo Chen\\Desktop\\demo_long.txt", "r").read()
words = jieba.cut(article, cut_all = False)
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x: x[1], reverse = True)

max_number = int(raw_input(u"需要前多少位高频词？ "))

for word, freq in freq_word[: max_number]:
    print word, freq


# ##Part 2. 人工去停用词

# 标点符号、虚词、连词不在统计范围内。

# In[22]:

stopwords = []
for word in open("C:\\Users\\Luo Chen\\Desktop\\stop_words.txt", "r"):
    stopwords.append(word.strip())
article = open("C:\\Users\\Luo Chen\\Desktop\\demo_long.txt", "r").read()
words = jieba.cut(article, cut_all = False)
stayed_line = ""
for word in words:
    if word.encode("utf-8") not in stopwords:
        stayed_line += word + " "
print stayed_line


# ##Part 3. 合并同义词

# 将同义词列举出来，按下Tab键分隔，把第一个词作为需要显示的词语，后面的词语作为要替代的同义词，一系列同义词放在一行。
# 这里，“北京”、“首都”、“京城”、“北平城”、“故都”为同义词。

# In[24]:

combine_dict = {}

for line in open("C:\\Users\\Luo Chen\\Desktop\\tongyici.txt", "r"):
    seperate_word = line.strip().split("\t")
    num = len(seperate_word)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]

jieba.suggest_freq("北平城", tune = True)
seg_list = jieba.cut("北京是中国的首都，京城的景色非常优美，就像当年的北平城，我爱这故都的一草一木。", cut_all = False)
f = ",".join(seg_list)
result = open("C:\\Users\\Luo Chen\\Desktop\\output.txt", "w")
result.write(f.encode("utf-8"))
result.close()

for line in open("C:\\Users\\Luo Chen\\Desktop\\output.txt", "r"):
    line_1 = line.split(",")

final_sentence = ""
for word in line_1:
    if word in combine_dict:
        word = combine_dict[word]
        final_sentence += word
    else:
        final_sentence += word
print final_sentence


# ##Part 4. 词语提及率

# 主要步骤：分词——过滤停用词（略）——替代同义词——计算词语在文本中出现的概率。

# In[31]:

origin = open("C:\\Users\\Luo Chen\\Desktop\\tijilv.txt", "r").read()
jieba.suggest_freq("晨妈妈", tune = True)
jieba.suggest_freq("大黑牛", tune = True)
jieba.suggest_freq("能力者", tune = True)
seg_list = jieba.cut(origin, cut_all = False)
f = ",".join(seg_list)

output_1 = open("C:\\Users\\Luo Chen\\Desktop\\output_1.txt", "w")
output_1.write(f.encode("utf-8"))
output_1.close()

combine_dict = {}
for w in open("C:\\Users\\Luo Chen\\Desktop\\tongyici.txt", "r"):
    w_1 = w.strip().split("\t")
    num = len(w_1)
    for i in range(0, num):
        combine_dict[w_1[i]] = w_1[0]

seg_list_2 = ""
for i in open("C:\\Users\\Luo Chen\\Desktop\\output_1.txt", "r"):
    i_1 = i.split(",")
    for word in i_1:
        if word in combine_dict:
            word = combine_dict[word]
            seg_list_2 += word
        else:
            seg_list_2 += word
print seg_list_2


# In[35]:

freq_word = {}
seg_list_3 = jieba.cut(seg_list_2, cut_all = False)
for word in seg_list_3:
    if word in freq_word:
        freq_word[word] += 1
    else:
        freq_word[word] = 1

freq_word_1 = []
for word, freq in freq_word.items():
    freq_word_1.append((word, freq))
freq_word_1.sort(key = lambda x: x[1], reverse = True)
for word, freq in freq_word_1:
    print word, freq

total_freq = 0
for i in freq_word_1:
    total_freq += i[1]

for word, freq in freq_word.items():
    freq = float(freq) / float(total_freq)
    print word, freq


# ##Part 5. 按词性提取

# In[36]:

import jieba.posseg as pseg
word = pseg.cut("李晨好帅，又能力超强，是“大黑牛”，也是一个能力者，还是队里贴心的晨妈妈。")
for w in word:
    if w.flag in ["n", "v", "x"]:
        print w.word, w.flag