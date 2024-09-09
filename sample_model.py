from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import numpy as np

# Load the iris dataset
info = load_wine()
X = info.data
y = info.target

# Train-test splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Decision Trees": DecisionTreeClassifier(),
    "Random Forests": RandomForestClassifier(),
    "SVM": SVC(),
    "k-Nearest Neighbors": KNeighborsClassifier(),
    "Naive Bayes": GaussianNB(),
    "Gradient Boosting Machines": GradientBoostingClassifier(),
    "Neural Networks": MLPClassifier()
}

# Calculate accuracies
accuracies = {}
for name, classifier in classifiers.items():
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(name,acc)
    accuracies[name] = acc

best_model = max(accuracies, key=accuracies.get)

# Plotting the results in a pie chart
plt.figure(figsize=(8, 8))
plt.pie(accuracies.values(), labels=accuracies.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Accuracy of Classification Algorithms on Dataset')
plt.axis('equal')  
plt.annotate(f'Best Model: {best_model} ({accuracies[best_model]*100:.2f}%)', xy=(0,1.05), fontsize=12, color='black', ha='center')
plt.savefig('E:\spot check\webapp\\response\classification_chart.png')  # Save the plot
plt.show()

print("Best Model:", best_model)
