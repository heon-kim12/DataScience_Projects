# Machine Learning / Deep Learning - Data Science Projects

This repository contains a collection of my DS projects :) 

## Projects

#### Project 1: Sentimental Analysis - using LSTM model on NAVER movie reviews
- Description: This project involves sentiment analysis on NAVER movie reviews using LSTM models.
- Skills Used: The approach includes Long Short-Term Memory (LSTM) networks for analyzing the sentiment of the movie reviews. The model is built using TensorFlow and Keras libraries. Preprocessing steps like tokenization and padding are applied to the text data. 
- Results: The LSTM model showed promising results with an accuracy of 67% in the validation dataset. The model was trained on a split of 80% training and 20% validation data, with early stopping implemented to prevent overfitting. Despite the limited dataset of 500 sentences, the model demonstrated its potential in sentiment analysis of Korean movie reviews, indicating positive sentiment for the sample text review. The use of LSTM allowed for better handling of sequential data, contributing to the model's effectiveness in understanding the context and sentiment of the reviews.

#### Project 2: Enhancing Wine Quality Prediction: Comparative Analysis of Random Forest and XGBoost Algorithms
- Description: This study delves into the realm of predictive analytics within the wine industry, employing advanced machine learning techniques to assess the quality of wines. The objective is to predict the quality of wine based on its physicochemical properties, utilizing two different yet powerful algorithms: Random Forest and XGBoost.

- Skills Used: The analysis employs robust data preprocessing methods and exploratory data analysis (EDA) techniques using Python libraries such as pandas, numpy, matplotlib, seaborn, and machine learning frameworks scikit-learn and XGBoost. The EDA includes generating boxplots, scatter matrices, and correlation heatmaps to understand the data's underlying structure. The modeling involves Random Forest and XGBoost classifiers to handle a multi-class prediction problem, with particular attention given to class imbalance through label encoding and evaluation metrics.

- Results: The Random Forest classifier achieved an accuracy of approximately 65.94% on the test dataset. However, it struggled with minority classes, as evidenced by low precision and recall for certain quality levels. To address this, the XGBoost classifier was employed, which after label re-encoding, improved the accuracy to about 69.69%. The XGBoost model exhibited a better handling of the class imbalance, showing increased F1-scores for the majority classes and a more stable performance across different quality levels. Despite the challenges of an imbalanced dataset, indicated by the varying 'support' in the classification reports, both models demonstrated potential in predicting wine quality. The Random Forest model offered a solid baseline, while the XGBoost model provided an incremental improvement, especially in dealing with class imbalance. The findings underscore the importance of choosing the right algorithm and preprocessing steps in predictive modeling to achieve more accurate and generalizable results.

#### Project 3: Trigram Models for Text Prediction and Essay Scoring
- Description: The project employs trigram models to enhance text prediction and score essays, using NLP techniques to process and understand language patterns.
- Skills Used: Python’s data structures and NLP fundamentals enable efficient computation of n-gram probabilities and perplexity measures, essential for the model's predictions.
- Results: The model was adept at assessing essay quality, indicated by its ability to differentiate between high and low-quality essays based on perplexity scores, showcasing improved handling of language data sparsity.

#### Project 4: Predictive Modeling for Long-Term Contract Viability
- Description: This project develops a predictive model tailored to evaluate the viability of long-term contracts by analyzing historical data and identifying key performance indicators that influence contract sustainability.
- Skills Used: The approach integrates data preprocessing, exploratory data analysis, and advanced statistical modeling within a Python environment, utilizing libraries such as pandas, numpy, and scikit-learn. The model accounts for various features that may impact the likelihood of a contract's long-term success.
- Results: The constructed model, trained on a comprehensive dataset, reveals critical insights into factors that contribute to the longevity of contracts. By assessing the model's accuracy and applying it to a test set, we demonstrate its capability to forecast the outcome of new contracts with a high degree of confidence.

#### Project 5: Data Science Job Market Explorer: Unveiling Entry-Level Opportunities through NLP and EDA
- Description: The project delves into the data science job market, employing NLP and EDA techniques to analyze job listings. Key insights include the prevalence of certain skills like 'data', 'machine learning', and 'python' in job descriptions, underscoring their importance in the industry. The analysis also differentiates entry-level positions from senior roles, offering clarity on the opportunities available for newcomers. Furthermore, the transformation of salary data into numerical scores provides valuable insights into compensation trends for entry-level roles. The frequency of specific skills in job listings also guides job seekers on the most sought-after competencies in the field.
- Skills Used: The project extensively uses Python and its libraries such as pandas, numpy, seaborn, matplotlib, and scikit-learn for data manipulation, visualization, and analysis. Techniques include text processing with regular expressions, keyword frequency analysis, normalization of keyword and salary scores, and the application of NLP methods for text analysis.
- Results: The project successfully identifies and evaluates entry-level data science job listings, highlighting the key skills and salary ranges. This analysis not only offers a comprehensive overview of the entry-level job market but also serves as a guide for aspiring data scientists on which areas to focus their learning and development efforts.
