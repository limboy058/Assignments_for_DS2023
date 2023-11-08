from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
text=['This is the first document.',
    'This is the second second document.',
    'And the third one. Is this',
    'Is this the first document?']

v=cv.fit_transform(text)
print(v)
print(cv.get_feature_names_out())
print(v.toarray())