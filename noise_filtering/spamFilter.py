# Reference: https://opendatascience.com/blog/spam-detection-in-9-lines-of-code/


import pandas
import sklearn, sklearn.feature_extraction, sklearn.svm

def spamFilter(filePath):
    df = pandas.read_csv(filePath, sep="\t", header=-1)

    # convert tweets to the TF-IDF representation
    tf_transformer = sklearn.feature_extraction.text.TfidfVectorizer()
    X = tf_transformer.fit_transform(df[3])
    #y = pandas.get_dummies(df[0], drop_first=True).values.ravel()
    y = df[4]

    # perform some training using an SVM
    # and then output the accuracy of the predictions in conjunction with 5-fold cross validation
    learner = sklearn.svm.LinearSVC()
    scores = sklearn.model_selection.cross_val_score(learner, X, y, cv=5, scoring="accuracy")
    return scores.mean()


