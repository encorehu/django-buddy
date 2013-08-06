# -*- coding:utf8 -*-
#encoding=utf-8
#from ICTCLAS.ICTUtil import ICTUtil
import jieba

#newICT = ICTUtil()

class ChineseWordSegmentation():
    #def __init__(self):
        #self.input=words
        #self.output=newICT.ICTSeg(words)
    @staticmethod
    def seg(words):
        #output=newICT.ICTSeg(words)
        #return str(output)
        seg_list =jieba.cut(words,cut_all=True)
        return " ".join(seg_list)


def seg(words):
    #output=newICT.ICTSeg(words)
    #return output
    seg_list =jieba.cut(words,cut_all=False)
    return " ".join(seg_list)