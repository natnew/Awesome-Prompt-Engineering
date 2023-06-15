## 10 Essential Machine Learning Algorithms - Cheat Sheet


### Linear Regression (Supervised learning - Regression)
A supervised learning algorithm used for predicting a continuous output variable based on one or more input variables.
Used for predicting real-valued outputs, such as predicting housing prices based on features like square footage and number of bedrooms.<br><br>
Linear Regression: Linear regression is a type of regression model that assumes a linear relationship between the input features and the output variable. The model consists of a set of coefficients (or weights) that are multiplied by each input feature to produce a prediction of the output variable. 
During training, the model learns these coefficients by minimizing the difference between its predicted outputs and the actual outputs on a training set.<br>
Paper: "Gradient descent algorithm and its variants for linear regression," by Sanjay Mishra and Priyanka Mishra [Here](https://ieeexplore.ieee.org/document/8689082)
```
# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Create some sample data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([3, 5, 7])

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[10, 11, 12]])
prediction = model.predict(new_data)

# Print the coefficients and the predicted output
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction:", prediction)
```

### Logistic Regression (Supervised learning - Classification)
A supervised learning algorithm used for binary classification problems, where the output is a probability between 0 and 1.
Used for binary classification problems, such as predicting whether a customer will buy a product or not based on their demographic information.<br><br>
Logistic Regression: Logistic regression is a type of classification model that uses a logistic function to produce binary output predictions. The model consists of a set of coefficients (or weights) that are multiplied by each input feature, and these weighted inputs are passed through the logistic function to produce a probability estimate of the positive class. 
During training, the model learns these coefficients by maximizing the likelihood of the observed labels on a training set.<br>
Paper: "A comparison of numerical optimizers for logistic regression," by S. van der Walt, S. C. Colbert, and G. Varoquaux [Here](https://www.sciencedirect.com/science/article/pii/S0925231217309868)
```
# Import necessary libraries
import numpy as np
from sklearn.linear_model import LogisticRegression

# Create some sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0, 0, 1, 1])

# Create a logistic regression model and fit it to the data
model = LogisticRegression()
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[9, 10]])
prediction = model.predict(new_data)

# Print the coefficients and the predicted output
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction:", prediction)
```

### Decision Trees (Classification and Regression)
A supervised learning algorithm used for both classification and regression problems, which creates a tree-like model of decisions and their possible consequences.
Used for classification problems, such as predicting whether a patient has a certain disease based on their symptoms.<br><br>
Decision Trees: Decision trees are a type of tree-based model that consists of a hierarchical set of decision rules that are used to classify or predict new data points based on their input features. The model consists of a set of nodes that represent decision points, where each node tests the value of a specific input feature, and a set of branches that represent the possible outcomes of the test. 
During training, the model learns the optimal decision rules by recursively partitioning the input space into increasingly pure subsets of the target variable.<br>
Paper: "Classification and regression trees," by Leo Breiman, Jerome Friedman, Richard Olshen, and Charles Stone [Here](https://www.taylorfrancis.com/books/9780429500486)
```
# Import necessary libraries
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Create some sample data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
y = np.array([0, 0, 1, 1])

# Create a decision tree model and fit it to the data
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[5, 6]])
prediction = model.predict(new_data)

# Print the predicted output
print("Prediction:", prediction)
```

### Random Forest (Classification and Regression)
An ensemble learning method that builds multiple decision trees and combines their outputs to improve predictive accuracy and reduce overfitting.
Used for classification and regression problems, such as predicting which products a customer is likely to buy based on their purchase history.<br><br>
Random Forest: Random forests are an ensemble method that combines multiple decision tree models to improve their accuracy and generalization ability. The model consists of a set of decision trees that are trained on randomly sampled subsets of the training data, and each tree produces a prediction for a new data point. 
During training, the model selects the optimal subset of features and tree parameters to minimize the error rate of the ensemble on a training set.<br>
Paper: "Random forests," by Leo Breiman [Here](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf)
```
# Import necessary libraries
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Create some sample data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
y = np.array([0, 0, 1, 1])

# Create a random forest model and fit it to the data
model = RandomForestClassifier()
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[5, 6]])
prediction = model.predict(new_data)

# Print the predicted output
print("Prediction:", prediction)
```

### Support Vector Machines (SVM - Supervised learning - Classification and Regression)
A supervised learning algorithm used for classification and regression problems, which tries to find the best hyperplane that separates the data into different classes.
Used for classification and regression problems, such as predicting whether a customer will churn based on their behavior and demographics.<br><br>
Support Vector Machines (SVM): Support vector machines are a type of linear classification model that aims to find the hyperplane that maximally separates the positive and negative class examples in the input feature space. The model consists of a set of support vectors that lie closest to the decision boundary, and a set of coefficients that determine the orientation and position of the hyperplane. 
During training, the model learns these coefficients by maximizing the margin between the support vectors and the decision boundary on a training set.<br>
Paper:"A tutorial on support vector machines for pattern recognition," by Christopher J. C. Burges [Here](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/svmtutorial.pdf)```
```
# Import necessary libraries
import numpy as np
from sklearn.svm import SVC

# Create some sample data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
y = np.array([0, 0, 1, 1])

# Create an SVM model and fit it to the data
model = SVC(kernel='linear')
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[5, 6]])
prediction = model.predict(new_data)

# Print the predicted output
print("Prediction:", prediction)
```

### Naive Bayes (Classification)
A probabilistic algorithm used for classification problems, which predicts the probability of each class based on the input features using Bayes' theorem.
Used for classification problems, such as predicting whether an email is spam or not based on its content.<br><br>
Naive Bayes: Naive Bayes is a type of probabilistic classification model that uses Bayes' theorem to compute the probability of the positive class given the input features. The model assumes that the input features are conditionally independent given the target class, which simplifies the computation of the posterior probability. 
During training, the model learns the class conditional probability distributions of the input features and the prior probability of the classes on a training set.<br>
Paper: "An empirical study of smoothing techniques for language modeling," by Stanley F. Chen and Ronald Rosenfeld [Here](https://dl.acm.org/doi/10.5555/972525.972557)
```
# Import necessary libraries
import numpy as np
from sklearn.naive_bayes import GaussianNB

# Create some sample data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
y = np.array([0, 0, 1, 1])

# Create a Naive Bayes model and fit it to the data
model = GaussianNB()
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[5, 6]])
prediction = model.predict(new_data)

# Print the predicted output
print("Prediction:", prediction)
```

### K-Nearest Neighbors (KNN - Supervised learning - Classification) 
A lazy learning algorithm used for classification and regression problems, which assigns a new data point to the class of its K nearest neighbors in the training set.
Used for classification and regression problems, such as predicting the price of a house based on the prices of similar houses in the same neighborhood.<br><br>
K-Nearest Neighbors (KNN): K-nearest neighbors is a type of lazy classification model that classifies a new data point based on the majority class of its k-nearest neighbors in the input feature space. The model does not learn a parametric model of the input-output relationship, but instead stores the entire training set in memory for fast lookup during testing. 
During training, the model simply memorizes the training examples and their labels.<br>
Paper:  "Estimating the number of clusters in a dataset via the gap statistic," by Robert Tibshirani, Guenther Walther, and Trevor Hastie [Here](https://statweb.stanford.edu/~gwalther/gap)
```
# Import necessary libraries
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Create some sample data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
y = np.array([0, 0, 1, 1])

# Create a KNN model and fit it to the data
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict a new output based on the input
new_data = np.array([[5, 6]])
prediction = model.predict(new_data)

# Print the predicted output
print("Prediction:", prediction)
```

### Neural Networks  (Supervised learning, Unsupervised learning, and Reinforcement learning - Classification and Regression)
A class of algorithms inspired by the structure and function of the human brain, used for classification, regression, and other problems, which learn complex patterns by adjusting the strengths of connections between neurons.
Used for a wide variety of problems, such as image classification, speech recognition, and natural language processing.<br><br>
Neural Networks: Neural networks are a type of nonlinear model that consists of a set of interconnected nodes, or neurons, arranged in layers. Each neuron receives input from the previous layer, applies a nonlinear activation function to the weighted sum of its inputs, and passes its output to the next layer. The model can have many layers and nonlinear activation functions, and can learn complex input-output relationships through a process of backpropagation, 
where the error gradient is propagated backwards through the network to adjust the weights and biases of the neurons.<br>
Paper: "Deep learning," by Yann LeCun, Yoshua Bengio, and Geoffrey [Here](Hinton https://www.nature.com/articles/nature14539)
```
# Import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create some sample data
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
y = np.array([0, 0, 1, 1])

# Create a neural network model
model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model to the data
model.fit(X, y, epochs=100, batch_size=2)

# Predict a new output based on the input
new_data = np.array([[5, 6]])
prediction = model.predict(new_data)

# Print the predicted output
print("Prediction:", prediction)
```

### Gradient Boosting Machines (GBM - Supervised Learning, Regression and Classification)  
An ensemble learning method that combines multiple weak models into a single strong model, by iteratively training each new model to correct the errors of the previous ones.
Used for classification and regression problems, such as predicting which ads a user is likely to click on based on their browsing history.<br><br>
Gradient Boosting Machines (GBM): GBM is an ensemble model that combines multiple weak prediction models, usually decision trees, to create a strong predictive model. The architecture of GBM involves a sequential and iterative approach. It starts with an initial weak model, 
often a shallow decision tree, and subsequently adds new models to the ensemble to correct the errors made by the previous models.<br>
Paper: "Greedy Function Approximation: A Gradient Boosting Machine" Authors: Jerome H. Friedman [Here](https://statweb.stanford.edu/~jhf/ftp/trebst.pdf)

```
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Assuming you have a labeled dataset with features X and corresponding labels y

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a GBM classifier
gbm = GradientBoostingClassifier()

# Train the GBM model
gbm.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gbm.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

### Principal Component Analysis (PCA - Unsupervised learning - Dimensionality reduction) 
An unsupervised learning algorithm used for dimensionality reduction and feature extraction, which transforms the input data into a lower-dimensional space while retaining the most important information.
Used for dimensionality reduction and feature extraction, such as reducing the number of variables needed to represent a dataset while retaining most of the important information.<br><br>
Principal Component Analysis (PCA): Principal Component Analysis is a type of unsupervised learning model that reduces the dimensionality of a dataset by projecting it onto a lower-dimensional space while retaining the maximum amount of variance in the data. The model computes the principal components, which are linear combinations of the original features, that capture the most significant sources of variation in the data. During training, 
the model learns the principal components by diagonalizing the covariance matrix of the data and selecting the top k components that explain the most variance.<br>
Paper: "Principal component analysis," by I.T. Jolliffe [Here](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118445112.stat05324)
```
# Import necessary libraries
import numpy as np
from sklearn.decomposition import PCA

# Create some sample data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a PCA model with 2 components
pca = PCA(n_components=2)

# Fit the model to the data
pca.fit(X)

# Transform the data into 2 principal components
X_transformed = pca.transform(X)

# Print the transformed data
print("Original data shape:", X.shape)
print("Transformed data shape:", X_transformed.shape)
print("Transformed data:")
print(X_transformed)
```

## Supervised learning vs Unsupervised learning

Supervised learning is typically used when we have a labeled dataset, and we want to predict the output for new input data based on this labeled dataset. For example, if we have a dataset of images labeled with their corresponding object classes, we can train a supervised learning model to classify new images based on the learned relationship between the input features and output labels. 
Supervised learning is also used for regression tasks where we want to predict a continuous output based on the input features.<br><br>

Unsupervised learning, on the other hand, is typically used when we don't have a labeled dataset or we want to discover patterns and relationships in the data that may not be immediately apparent. 
For example, clustering algorithms can be used to group similar data points together based on their similarities. Unsupervised learning is also used for dimensionality reduction, where we want to reduce the number of features in the data while retaining as much information as possible.<br><br>


## Model evaluation metrics
* Mean squared error (MSE): A measure of the average squared difference between the predicted values and the actual values in a regression problem.

>MSE = (1/n) * Σi=1:n (yi - ŷi)^2

where n is the number of observations, yi is the actual value of the i-th observation, and ŷi is the predicted value of the i-th observation. MSE is calculated as the average of the squared differences between the actual and predicted values.
<br>
<br>

* Root mean squared error (RMSE): The square root of MSE, giving a measure of the average difference between the predicted values and actual values in a regression problem.

>RMSE = sqrt(MSE)

where MSE is the mean squared error. RMSE is the square root of MSE, giving a measure of the average difference between the predicted values and actual values in a regression problem.
<br>
<br>

* R-squared (R2): A measure of how well the predicted values match the actual values in a regression problem, ranging from 0 (no correlation) to 1 (perfect correlation).

>R2 = 1 - (SSres / SStot)

where SSres is the sum of squared residuals (i.e., the sum of squared differences between the actual and predicted values), and SStot is the total sum of squares (i.e., the sum of squared differences between the actual values and the mean of the actual values). R2 ranges from 0 (no correlation) to 1 (perfect correlation), and indicates how well the predicted values match the actual values in a regression problem.
<br>
<br>

* Accuracy: The number of correct predictions divided by the total number of predictions in a classification problem.

>Accuracy = (TP + TN) / (TP + TN + FP + FN)

where TP is the number of true positive predictions, TN is the number of true negative predictions, FP is the number of false positive predictions, and FN is the number of false negative predictions. Accuracy is the proportion of correct predictions out of all predictions made in a classification problem.
<br>
<br>

* Precision: The proportion of true positive predictions out of all the positive predictions made in a classification problem.

Precision = TP / (TP + FP)

where TP is the number of true positive predictions, and FP is the number of false positive predictions. Precision is the proportion of true positive predictions out of all the positive predictions made in a classification problem.
<br>
<br>

* Recall: The proportion of true positive predictions out of all the actual positive cases in a classification problem.

>Recall = TP / (TP + FN)

where TP is the number of true positive predictions, and FN is the number of false negative predictions. Recall is the proportion of true positive predictions out of all the actual positive cases in a classification problem.
<br>
<br>

* F1-score: A measure that combines precision and recall in a classification problem.

>F1-score = 2 * ((precision * recall) / (precision + recall))

where precision is the precision of the classifier, and recall is the recall of the classifier. The F1-score is a measure that combines precision and recall in a classification problem.
<br>
<br>

* ROC curve: A graphical representation of the trade-off between true positive rate and false positive rate for different classification thresholds.

>A ROC curve is a plot of true positive rate (TPR) versus false positive rate (FPR) for different classification thresholds. TPR is the proportion of true positive predictions out of all the actual positive cases, and FPR is the proportion of false positive predictions out of all the actual negative cases.
<br>
<br>

* AUC (Area Under the ROC Curve): A measure of the overall performance of a classification model based on the ROC curve.


>AUC is the area under the ROC curve. AUC ranges from 0.5 (random classifier) to 1 (perfect classifier), and measures the overall performance of a classification model based on the ROC curve.
<br>
<br>

* Silhouette score: A measure of how well-defined the clusters are in a clustering problem.
>Silhouette score = (b - a) / max(a, b)

where a is the mean distance between a sample and all other points in the same cluster, and b is the mean distance between a sample and all other points in the next nearest cluster. The silhouette score ranges from -1 to 1, and measures how well-defined the clusters are in a clustering problem.
<br>
<br>

* Inertia: The sum of squared distances of samples to their closest cluster center in a clustering problem.

>Inertia is the sum of squared distances of samples to their closest cluster center. Inertia measures the compactness of the clusters in a clustering problem.
<br>
<br>

* Dunn index: A measure of cluster separation and compactness in a clustering problem.


>Dunn Index = min (diameter of cluster i + diameter of cluster j) / distance between the centroids of cluster i and j, for all i ≠ j

where the diameter of a cluster is the maximum distance between any two points within the cluster, and the distance between the centroids of two clusters is the Euclidean distance between them.











