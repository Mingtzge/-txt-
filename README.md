# 使用说明
这是一个在解析bag包的时候，临时写的格式转换程序。

当提取出对应话题的bag时，需要将其转化为txt文件，但是转换之后，flags和nums不对齐，可观性不好

例如：123.txt

hihasid,ashdiadh,asdhiasdh,ashidahi,asdhiasd
12341,23424,234234252,234234,23425

这个小程序实现的功能就是将其转化为：456.txt

hihasid:12341
ashdiadh:23424
asdhiasdh:234234252
ashidahi:234234
asdhiasd:23425

这个程序针对于固定的场景，及要转换的文件中，只有两行数据，第一行为标签，第二行为数值，当然，你自己也可以修改。

说一下程序的使用说明：适用版本python2,python3
在终端下使用：

python transform.py [源文件] [目的文件]

例子：

python transform.py /home/parallels/123.txt ./456.txt
