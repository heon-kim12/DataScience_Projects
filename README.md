# Machine Learning / Deep Learning - Data Science Projects

This repository contains a collection of my DS projects :) 

## Projects

#### Project 1: Sentimental Analysis - using LSTM model on NAVER movie reviews
- Description: This project involves sentiment analysis on NAVER movie reviews using LSTM models.
- Skills Used: The approach includes Long Short-Term Memory (LSTM) networks for analyzing the sentiment of the movie reviews. The model is built using TensorFlow and Keras libraries. Preprocessing steps like tokenization and padding are applied to the text data. 
- Results: The LSTM model showed promising results with an accuracy of 67% in the validation dataset. The model was trained on a split of 80% training and 20% validation data, with early stopping implemented to prevent overfitting. Despite the limited dataset of 500 sentences, the model demonstrated its potential in sentiment analysis of Korean movie reviews, indicating positive sentiment for the sample text review. The use of LSTM allowed for better handling of sequential data, contributing to the model's effectiveness in understanding the context and sentiment of the reviews.

#### Project 2: 
- Description: This study delves into the realm of predictive analytics within the wine industry, employing advanced machine learning techniques to assess the quality of wines. The objective is to predict the quality of wine based on its physicochemical properties, utilizing two different yet powerful algorithms: Random Forest and XGBoost.

- Skills Used: The analysis employs robust data preprocessing methods and exploratory data analysis (EDA) techniques using Python libraries such as pandas, numpy, matplotlib, seaborn, and machine learning frameworks scikit-learn and XGBoost. The EDA includes generating boxplots, scatter matrices, and correlation heatmaps to understand the data's underlying structure. The modeling involves Random Forest and XGBoost classifiers to handle a multi-class prediction problem, with particular attention given to class imbalance through label encoding and evaluation metrics.

- Results: The Random Forest classifier achieved an accuracy of approximately 65.94% on the test dataset. However, it struggled with minority classes, as evidenced by low precision and recall for certain quality levels. To address this, the XGBoost classifier was employed, which after label re-encoding, improved the accuracy to about 69.69%. The XGBoost model exhibited a better handling of the class imbalance, showing increased F1-scores for the majority classes and a more stable performance across different quality levels. Despite the challenges of an imbalanced dataset, indicated by the varying 'support' in the classification reports, both models demonstrated potential in predicting wine quality. The Random Forest model offered a solid baseline, while the XGBoost model provided an incremental improvement, especially in dealing with class imbalance. The findings underscore the importance of choosing the right algorithm and preprocessing steps in predictive modeling to achieve more accurate and generalizable results.

