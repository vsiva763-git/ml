#Import Necessary Libraries
#We import the libraries to help us with text vectorization, model training, and evaluation.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Prepare the Data
#Next, we need to create a dataset of texts and their corresponding labels. Each text is either related to technology ("tech") or not ("non-tech").

texts = [
  'I love programming.', 'Python is amazing.',
  'I enjoy machine learning.', 'The weather is nice today.', 'I like algo.',
  'Machine learning is fascinating.', 'Natural Language Processing is a part of AI.'
]

labels = [
  'tech', 'tech', 'tech', 'non-tech', 'tech', 'tech', 'tech'
]

#Convert Text to Numerical Data
#We will use CountVectorizer to convert our text data into a matrix of tokens.

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

#Split the Data into Training
#The train_test_split function splits the data into training and testing sets.

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

#Train the Naive Bayes Classifier
#Next, use the MultinomialNB classifier to train the model on our training data.

model = MultinomialNB()
model.fit(x_train, y_train)

#Make Predictions on the Test Set
#Then, use the trained model to predict the labels for the test set.
y_pred = model.predict(x_test)

#Evaluate the Model's Accuracy
#Finally, calculate and print the accuracy of our model by comparing the predicted labels with the actual labels in the test set.

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)