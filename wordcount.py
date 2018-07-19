# _*_ coding:utf-8 _*_

#author：'yzy'

import os, codecs
import jieba
from collections import Counter
 
def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    #print('词频度统计结果')
    file_handle=open('result.txt',mode='w')
    #for (k,v) in c.most_common(10000):
    for (k,v) in c.most_common():
        #print('%s%s %s  %d' % ('  '*(5-len(k)), k, '**', v))
        file_handle.write('%s %s  %d%s' % (k, '**', v,'\n'))
    file_handle.close()
if __name__ == '__main__':
    with codecs.open('wordtest.txt', 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt)