# SMS-Spam/Ham-Classification
This project demonstrates how to classify text messages as spam or ham (not spam) using the Naive Bayes algorithm. The dataset used for this project is the "SMS Spam Collection" dataset, which can be downloaded from this [kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

The code for this project is written in Python, and the necessary libraries used are nltk, pandas, matplotlib, seaborn, sklearn.

# Project Structure
- spam.csv: Dataset file
- README.md: Project information and instructions
- spam_classification.ipynb: Jupyter Notebook containing code for the project

# Project Setup

- Clone the project repository to your local machine using the command git clone <repository-url> 
- Install the necessary libraries using the command pip install -r requirements.txt
- Run the Jupyter Notebook spam_classification.ipynb to see the code for the project

# Data Cleaning
  
The dataset contains two columns: label and message. The label column contains the classification of the message as spam or ham, and the message column contains the actual text message. The following steps were taken to clean the data:

- Remove any missing values in the dataset using the dropna() function.
- Rename the columns to label and message using the columns attribute of the dataframe.
- Create a new column called label_num that maps the ham label to 0 and the spam label to 1.
- Create a new column called message_len that contains the length of each message.
- Remove any stop words and punctuation from the messages using the text_process() function.

# Data Visualization

The distribution of message lengths for spam and ham messages was visualized using a histogram. This was done using the matplotlib and seaborn libraries.

# Data Preprocessingh

The dataset was split into training and testing sets using the train_test_split() function from the sklearn library. The training set was used to train the Naive Bayes algorithm, while the testing set was used to evaluate its performance.

The CountVectorizer() function from sklearn was used to create a document-term matrix of the training set. The TfidfTransformer() function was then used to transform the matrix into a term-frequency inverse-document-frequency (tf-idf) matrix.

# Model Training and Evaluation
The Naive Bayes algorithm was trained on the tf-idf matrix using the MultinomialNB() function from sklearn. The performance of the model was evaluated using the classification report, which shows the precision, recall, and F1 score for each class (spam and ham).

A pipeline was created using the Pipeline() function from sklearn to simplify the preprocessing and training steps. The pipeline contains three steps: CountVectorizer(), TfidfTransformer(), and MultinomialNB(). The pipeline was then used to train and evaluate the Naive Bayes model.

# Conclusion
 
The Naive Bayes algorithm was found to perform well on the task of spam classification, with an F1 score of 0.98 for the spam class and 0.99 for the ham class. Also the accuracy of the model was found to be 98%. The use of a pipeline also simplified the preprocessing and training steps, making the code easier to read and understand.
 
  **Classification Report**
  
               precision    recall  f1-score   support

           0       0.99      0.99      0.99      1213
           1       0.95      0.91      0.93       180

    accuracy                           0.98      1393

