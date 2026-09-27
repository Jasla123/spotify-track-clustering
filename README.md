# spotify-track-clustering

This project uses Unsupervised Machine Learning to discover patterns and group Spotify tracks based on their audio features.

The project applies three clustering algorithms: K-Means, Hierarchical Clustering, and DBSCAN. The K-Means model is then integrated into a Streamlit web application to predict the cluster of a song based on its audio features.

## Objectives

- Explore and analyze Spotify track audio features.
- Clean and preprocess the dataset.
- Apply different clustering algorithms.
- Identify similarities and patterns among songs.
- Evaluate clustering performance using suitable metrics.
- Build a web application using Streamlit.

## Dataset

Dataset: Spotify Tracks Dataset

The dataset contains information about Spotify tracks, including their audio features and genres.

- Original dataset: approximately 114,000 tracks
- Final dataset after cleaning: 113,549 tracks
- Total columns: 20

Selected Features

- Duration
- Danceability
- Energy
- Loudness
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib

 ## Project Workflow

1. Data loading
2. Data cleaning and preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature selection
5. Feature scaling using StandardScaler
6. Clustering using K-Means
7. Hierarchical Clustering
8. DBSCAN Clustering
9. Model evaluation
10. PCA visualization
11. Model saving using Joblib
12. Streamlit application development

## Algorithms Used

1. K-Means Clustering

K-Means was used to group tracks into two clusters based on their audio features.

2. Hierarchical Clustering

Agglomerative Clustering was applied to a sample of tracks to identify groups based on similarities.

3. DBSCAN

DBSCAN was used to identify dense groups and detect tracks that did not fit into the identified clusters.

## Key Findings

- K-Means identified two broad groups of tracks.
- Cluster 0 generally contains tracks with lower energy and higher acousticness.
- Cluster 1 generally contains tracks with higher energy and danceability.
- The clusters overlap, so they should not be interpreted as exact music genres.
- K-Means achieved a Silhouette Score of approximately 0.244 on a 10,000-track evaluation sample.

##  Streamlit Web Application

A Streamlit application was developed using the trained K-Means model.

Users can enter a song's audio features and receive a predicted cluster.


## project files

- "app.py" – Streamlit application
- "spotify_clustering_model.pkl" – Saved K-Means model and preprocessing components
- "requirements.txt" – Required Python libraries
- "README.md" – Project documentation


## Future Improvements

- Experiment with additional clustering techniques and parameters.
- Improve cluster separation through feature selection and dimensionality reduction.
- Explore methods for recommending similar tracks.
- Improve the Streamlit interface with interactive visualizations.

