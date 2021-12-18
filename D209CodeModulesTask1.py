#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
%matplotlib inline
#set the plot style
plt.style.use('ggplot')
#set the figure size
plt.rcParams["figure.figsize"] = "11, 8"
#importing the dataset
dataset=pd.read_csv('/Users/Scot/OneDrive - University of Florida/School/WGU/Fall2021/D209-Data Mining 1/MedicalData/medical_clean_knn.csv',sep=',')
#Examine data types in the dataset to determine if assumptions about variable types are met.
dataset.info()
#creating predictor and response arrays
data_array=np.array(dataset)
X = data_array[1:,1:]#sets the array for the predictor variables without the header row
y = data_array[1:,0]#sets the response variable
#Indexing schema: [startrow:endrow, startcolumn:endcolumn] If you leave out the end boundaries, it continues to the last one.

#Split data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)
#The above takes the feature data (X), the target data (y), splits it using 'test_size' to indicate the percentage of data in the test bank, uses a random seed value to determine where to make the split, and tells the procedure to distribute group membership based on the target variable.

#Preprocessing the data: Standardizing and performing PCA
scaler = StandardScaler()

scaler.fit(X_train)
X_train = scaler.transform(X_train) #Standardizes the training feature data set
X_test = scaler.transform(X_test) #Standardizes the test data set

#Due to correlation between two variables and to reduce dimensionality, PCA was applied.
pca = PCA(.95) #This tells PCA to find the minimum number of factors to account for 95% of variability.
pca.fit(X_train) #PCA is fit to the training data.
print(pca.n_components_) #Tells us how many factors we are using.  In this case, 4.
#Transforms training and testing features to the PCA fit
X_train = pca.transform(X_train)
X_test = pca.transform(X_test)

#Creating accurancy charts to determine number of neighbors to use

# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 20) #sets array of number of neighbors to iterate through
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

#Once optimal number of neighbors has been identified, run model with that number of neighbors
knn = KNeighborsClassifier(n_neighbors=12) #sets the number of neighbors.  The number of neighbors was determined by accuracy chart below.
knn.fit(X_train, y_train) #fits the model to the training data
y_pred=knn.predict(X_test) #predicts using the test data
#Testing performance
knn.score(X_test, y_test)

print(confusion_matrix(y_test, y_pred))
[[1829   70]
 [  37 1064]]

print(classification_report(y_test, y_pred))
              precision    recall  f1-score   support

         0.0       0.98      0.96      0.97      1899
         1.0       0.94      0.97      0.95      1101

    accuracy                           0.96      3000
   macro avg       0.96      0.96      0.96      3000
weighted avg       0.96      0.96      0.96      3000

#Calculating AUC

y_pred_prob = knn.predict_proba(X_test)[:,1]
roc_auc_score(y_test, y_pred_prob)

0.995328580126545

#Exports testing and training datasets into csvs
pd.DataFrame(X_train).to_csv("/Users/Scot/OneDrive - University of Florida/School/WGU/Fall2021/D209-Data Mining 1/Task 1/X_train.csv")

pd.DataFrame(y_train).to_csv("/Users/Scot/OneDrive - University of Florida/School/WGU/Fall2021/D209-Data Mining 1/Task 1/y_train.csv")

pd.DataFrame(X_test).to_csv("/Users/Scot/OneDrive - University of Florida/School/WGU/Fall2021/D209-Data Mining 1/Task 1/X_test.csv")

pd.DataFrame(y_test).to_csv("/Users/Scot/OneDrive - University of Florida/School/WGU/Fall2021/D209-Data Mining 1/Task 1/y_test.csv")