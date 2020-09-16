# coding：utf-8
import math
from itertools import chain
from collections import Counter
import numpy
import jieba

# 空文本异常
class NowordError(Exception):
    def __init__(self):
        print("该文本为空！")

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

# 计算TF-IDF
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

    # 计算tf-idf
    return tf_data * idf_data.reshape(matrix.shape[0], 1)


# 计算余弦相似度
def cos(matrix):
    m = matrix.shape[0]
    ss = numpy.sum([matrix[i][0] * matrix[i][1] for i in range(m - 1)])
    den1 = numpy.sum([pow(matrix[i][0], 2) for i in range(m - 1)])
    den2 = numpy.sum([pow(matrix[i][1], 2) for i in range(m - 1)])
    return ss / math.sqrt((den1 * den2))


def main_solve(orig_position, copy_position, ans_position):
    orig = open(orig_position, 'r', encoding='UTF-8')
    text1 = orig.read()
    orig.close()
    copy = open(copy_position, 'r', encoding='UTF-8')
    text2 = copy.read()
    copy.close()
    # 空文本检测
    if text1 == '':
        raise NowordError
    if text2 == '':
        raise NowordError

    res1, res2 = cut(text1, text2)  # 返回第一个文本和第二个文本切词后的结果
    corpus = [res1, res2]
    matrix, dictionary = word_materix(corpus)
    tfidf_matrix = tf_idf(matrix)
    sim = str('%.2f' % cos(tfidf_matrix))

    ans = open(ans_position, 'w', encoding='UTF-8')
    ans.write(sim)
    ans.close()
    print('查重结果为:', sim)
