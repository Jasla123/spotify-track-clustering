# spotify-track-clustering

## Project Overview

This project uses Unsupervised Machine Learning to discover patterns and group Spotify tracks based on their audio features.

Three clustering algorithms — K-Means, Hierarchical Clustering, and DBSCAN — were applied to explore similarities among tracks. The trained K-Means model was integrated into a Streamlit web application that predicts the cluster of a song based on its audio features.

## Live Streamlit Application

Try the application here:

### "Open Spotify Track Clustering App" (https://spotify-track-clustering-fld63t2uu8jjecjpzixuxs.streamlit.app/)

Users can enter a song's audio features and receive a predicted cluster from the trained K-Means model.

## Project Objectives

- Explore and analyze Spotify track audio features.
- Clean and preprocess the dataset.
- Apply different clustering algorithms.
- Identify patterns and similarities among tracks.
- Evaluate clustering performance using suitable metrics.
- Build an interactive web application using Streamlit.

## Dataset

- Dataset: Spotify Tracks Dataset
- Original dataset size: Approximately 114,000 tracks
- Final dataset after cleaning: 113,549 tracks
- Total columns: 20

The dataset contains information about Spotify tracks, including track details, artists, genres, and audio features.

Selected Audio Features

The following ten features were used for clustering:

1. Duration
2. Danceability
3. Energy
4. Loudness
5. Speechiness
6. Acousticness
7. Instrumentalness
8. Liveness
9. Valence
10. Tempo

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

1. Load the Spotify Tracks Dataset.
2. Clean the data and remove duplicate records.
3. Handle missing values.
4. Perform Exploratory Data Analysis (EDA).
5. Select relevant audio features.
6. Handle extreme values in track duration using percentile capping.
7. Scale the selected features using "StandardScaler".
8. Apply K-Means clustering.
9. Apply Hierarchical Clustering and DBSCAN for comparison.
10. Evaluate the clustering results.
11. Visualize clusters using PCA.
12. Save the trained model and preprocessing components using Joblib.
13. Develop and deploy the Streamlit web application.

## Clustering Algorithms

1. K-Means Clustering

K-Means was used to group tracks into two clusters based on similarities in their selected audio features.

The model assigns each track to one of the clusters according to its position relative to the cluster centers.

2. Hierarchical Clustering

Agglomerative Hierarchical Clustering was applied to a sample of tracks to explore how tracks could be grouped according to their feature similarities.

3. DBSCAN

DBSCAN was used to identify dense groups of tracks and detect observations that did not fit into the identified dense regions. Some tracks were classified as noise.

## Model Evaluation

Clustering performance was evaluated using the following metrics:

- Silhouette Score: Measures how well-separated the clusters are.
- Davies-Bouldin Index: Measures cluster similarity; lower values generally indicate better separation.

The K-Means model achieved a Silhouette Score of approximately 0.244 on a 10,000-track evaluation sample.

This indicates that the clusters have some structure but also overlap. The clusters should not be interpreted as exact music genres.

## Key Findings

- K-Means identified two broad groups of Spotify tracks.
- Cluster 0 generally contains tracks with lower energy and higher acousticness.
- Cluster 1 generally contains tracks with higher energy and danceability.
- The selected audio features helped identify differences in track characteristics.
- The clusters overlap, so cluster membership does not determine a song's exact genre.
- Hierarchical Clustering and DBSCAN provided additional perspectives on the dataset's structure.

## Streamlit Web Application

A web application was developed using Streamlit and the saved K-Means model.

### Application Features

- Accepts ten audio features as user inputs.
- Applies the same feature preprocessing used during model training.
- Predicts the cluster using the trained K-Means model.
- Displays the predicted cluster to the user.

### How to Use the Application

1. Open the "Spotify Track Clustering App" (https://spotify-track-clustering-fld63t2uu8jjecjpzixuxs.streamlit.app/).
2. Enter the required audio feature values.
3. Click the prediction button.
4. View the predicted cluster.

## Project Files

- "app.py" — Streamlit web application.
- "spotify_clustering_model.pkl" — Saved K-Means model, scaler, and preprocessing information.
- "requirements.txt" — Required Python libraries.
- "README.md" — Project documentation.

### How to Run the Project Locally

Step 1: Clone the repository

git clone https://github.com/Jasla123/spotify-track-clustering.git

Replace "jasla123" with your GitHub username.

Step 2: Navigate to the project folder

cd spotify-track-clustering

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Run the Streamlit application

streamlit run app.py

Open the local URL displayed in the terminal to use the application.

## Limitations

- The clusters are based only on the selected audio features.
- The clustering results do not represent exact music genres.
- Some tracks may have similar features despite belonging to different genres.
- The Silhouette Score indicates that cluster separation is limited.
- The application predicts clusters; it does not directly recommend songs.

## Future Improvements

- Experiment with different clustering algorithms and parameters.
- Improve cluster separation through feature selection and dimensionality reduction.
- Explore methods for recommending similar tracks.
- Add interactive visualizations to the Streamlit application.
- Investigate how additional audio features affect clustering performance.

## Conclusion

This project demonstrates how unsupervised machine learning can be used to explore patterns and similarities in Spotify tracks. By applying multiple clustering algorithms and evaluating their results, the project provides insights into the structure of the dataset.

The trained K-Means model was integrated into a Streamlit web application, making it possible for users to explore the model's predictions interactively.

---

Developed using Python, Scikit-learn, and Streamlit.




