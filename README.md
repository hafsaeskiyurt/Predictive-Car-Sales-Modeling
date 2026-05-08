# Predictive-Car-Sales-Modeling

Overview: This project involved building a complete, end-to-end data science pipeline to estimate the potential car purchasing amount of a customer based on demographic and financial variables. The goal was to transform raw customer data into actionable business intelligence that can assist sales teams in personalized pricing strategies.

Technical Execution:

➱ Data Exploration & Visualization: I performed an extensive Exploratory Data Analysis (EDA) using Pandas and Matplotlib. I focused on identifying correlations         between features like "Annual Salary" and "Age" with the final "Purchase Amount".
    
➱ Feature Engineering: To make the data model-ready, I applied StandardScaler from Scikit-learn to normalize financial figures, ensuring that features with             different scales (e.g., age vs. salary) were treated fairly by the algorithm.

➱ Deployment: I didn't stop at the code; I exported the trained model using Joblib and built a functional web interface with Streamlit, allowing users to input         data and receive real-time predictions.
