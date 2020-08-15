# Hotel-Review-Classifier

## Overview
I have writen a naive Bayes classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative. We will be using the word tokens as features for classification.

Data
A top-level directory with two sub-directories, one for positive reviews and another for negative reviews (plus license and readme files which you won’t need for the exercise).
Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews.
Each of these subdirectories contains four subdirectories, called “folds”.
Each of the folds contains 80 text files with English text (one review per file).
The grading script will train your model on all of the training data, and test the model on unseen data in a similar format. The directory structure and file names of the test data will be masked so that they do not reveal the labels of the individual test files.

Programs
You will write two programs: nblearn.py will learn a naive Bayes model from the training data, and nbclassify.py will use the model to classify new data. If using Python 3, you will name your programs nblearn3.py and nbclassify3.py. The learning program will be invoked in the following way:

> python nblearn.py /path/to/input

The argument is the directory of the training data; the program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt. The format of the model is up to you, but it should follow the following guidelines:

The model file should contain sufficient information for nbclassify.py to successfully label new data.
The model file should be human-readable, so that model parameters can be easily understood by visual inspection of the file.
The classification program will be invoked in the following way:

> python nbclassify.py /path/to/input

The argument is the directory of the test data; the program will read the parameters of a naive Bayes model from the file nbmodel.txt, classify each file in the test data, and write the results to a text file called nboutput.txt in the following format:

label_a label_b path1
label_a label_b path2
⋮

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.
