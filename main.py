from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import seaborn as sns

# Define the TitanicRegression global variable
titanic_regression = None

# Define the TitanicRegression class
class TitanicRegression:
    def __init__(self):
        self.dt = None
        self.logreg = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.encoder = None

    def initTitanic(self):
        titanic_data = sns.load_dataset('titanic')
        # clean data


    def runDecisionTree(self):
        # more code here

    def runLogisticRegression(self):
        # more code here

def initTitanic():
    global titanic_regression
    titanic_regression = TitanicRegression()
    titanic_regression.initTitanic()

# From API
def predictSurvival(passenger):
    # more code here
    # interact with 
    return predict


# Sample usage without API
if __name__ == "__main__":
    # Initialize the Titanic model
    initTitanic()
