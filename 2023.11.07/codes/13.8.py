import numpy as np
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import os

text_data = []  # 包含文本的列表
labels = []      # 包含标签的列表

# 文本预处理
cnt=0
for item in os.scandir(r"data\newsgroups"):
    if item.is_dir():
        for txt in os.scandir(item):
            f=open(txt.path,encoding='ISO-8859-1')
            s=""
            for line in f:
                s+= line.strip()
            text_data.append(s)
            labels.append(item.name)
            cnt+=1
            if(cnt%1000==0):
                print("done: %f%%"%(100*cnt/15358))


print("特征提取中...")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_data)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

print("分类器训练中...")
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

print("测试中...")
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(report)
