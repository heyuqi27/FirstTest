# coding：utf-8
import math
from itertools import chain
from collections import Counter
import numpy
import jieba
import sys


# 分词
def cut(text1, text2):
    # 构建停用词表
    stop_words = open('stopword.txt', 'r', encoding='utf-8')
    stopwords = stop_words.read()
    result1 = ''
    result2 = ''
    words1 = jieba.cut(text1)
    words2 = jieba.cut(text2)
    for word in words1:
        if word not in stopwords:
            result1 += word
            result1 += " "
    for word in words2:
        if word not in stopwords:
            result2 += word
            result2 += " "
    return result1, result2


# 词频数矩阵
def word_materix(documents):
    docs = [d for d in documents]
    docs = [word for word in docs]
    # 得到所有的词
    words = list(set(chain(*docs)))
    # 词与ID的映射
    dictionary = dict(zip(words, range(len(words))))
    # 创建一个空矩阵
    matrix = numpy.zeros((len(words), len(docs)), dtype='float32')
    # 对两个文档进行词频计算
    for col, d in enumerate(docs):
        count = Counter(d)
        for word in count:
            id = dictionary[word]
            matrix[id, col] = count[word]
    return matrix, dictionary

# 计算每个词的TF-IDF值
def tf_idf(matrix):
    # 计算TF
    sm = numpy.sum(matrix, axis=0)
    try:
        a = matrix / sm
    except:
         print('error')
    tf_data = matrix / sm
    # 计算IDF
    Doc = matrix.shape[1]
    xy = numpy.sum(matrix, axis=1)
    idf_data = Doc / xy
    # 计算tf-idf并返回
    return tf_data * idf_data.reshape(matrix.shape[0], 1)

# 计算余弦相似度
def cos(matrix):
    m = matrix.shape[0]
    ss = numpy.sum([matrix[i][0] * matrix[i][1] for i in range(m - 1)])
    den1 = numpy.sum([pow(matrix[i][0], 2) for i in range(m - 1)])
    den2 = numpy.sum([pow(matrix[i][1], 2) for i in range(m - 1)])
    return ss / math.sqrt((den1 * den2))


if __name__ == "__main__":
    # 命令行参数读入
    d1 = open(sys.argv[1], 'r', encoding="utf-8")
    text1 = d1.read()
    d1.close()
    d2 = open(sys.argv[2], 'r', encoding="utf-8")
    text2 = d2.read()
    d2.close()

    res1, res2 = cut(text1, text2)  # 返回第一个文本和第二个文本切词后的结果
    corpus = [res1, res2]
    matrix, dictionary = word_materix(corpus)
    tfidf_matrix = tf_idf(matrix)
    sim = str('%.2f' % cos(tfidf_matrix))

    # 命令行参数输出
    output = open(sys.argv[3], 'w', encoding="utf-8")
    output.write(sim)
    output.close()