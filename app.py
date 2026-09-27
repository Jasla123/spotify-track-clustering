import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Spotify Track Clustering",
    page_icon="🎵",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    data = joblib.load("spotify_clustering_model.pkl")
    return data

data = load_model()

model = data["model"]
scaler = data["scaler"]
features = data["features"]
duration_limit = data["duration_limit"]

# ---------------- HEADER ----------------
st.title("🎵 Spotify Track Clustering")
st.write(
    "Discover patterns in Spotify tracks using "
    "unsupervised machine learning."
)

st.info(
    "This application uses a trained K-Means model "
    "to group songs according to their audio features. "
    "It does not predict the official music genre."
)

# ---------------- PROJECT OVERVIEW ----------------
with st.expander("About This Project"):
    st.write("""
    **Objective:** To discover similarities and patterns
    among Spotify tracks using audio features.

    **Algorithms explored:**
    - K-Means Clustering
    - Hierarchical Clustering
    - DBSCAN

    **Final model:** K-Means with 2 clusters.

    **Technologies:** Python, Pandas, Scikit-learn,
    Joblib and Streamlit.
    """)

st.divider()

# ---------------- CLUSTER INFORMATION ----------------
st.subheader("🎧 Understanding the Clusters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟣 Cluster 0")
    st.write("Generally associated with:")
    st.markdown("""
    - Lower energy
    - Lower danceability
    - Higher acousticness
    """)

with col2:
    st.markdown("### 🔵 Cluster 1")
    st.write("Generally associated with:")
    st.markdown("""
    - Higher energy
    - Higher danceability
    - Lower acousticness
    """)

st.caption(
    "These descriptions reflect average cluster characteristics. "
    "Individual songs may have different features."
)

st.divider()

# ---------------- INPUT FORM ----------------
st.subheader("🎼 Analyze a Song")
st.write("Enter the song's audio features below.")

with st.form("song_features"):

    col1, col2 = st.columns(2)

    with col1:
        duration_ms = st.number_input(
            "Duration (milliseconds)",
            min_value=1.0,
            value=200000.0,
            step=1000.0
        )

        danceability = st.slider(
            "Danceability", 0.0, 1.0, 0.5
        )

        energy = st.slider(
            "Energy", 0.0, 1.0, 0.5
        )

        loudness = st.number_input(
            "Loudness (dB)",
            min_value=-60.0,
            max_value=10.0,
            value=-8.0
        )

        speechiness = st.slider(
            "Speechiness", 0.0, 1.0, 0.05
        )

    with col2:
        acousticness = st.slider(
            "Acousticness", 0.0, 1.0, 0.5
        )

        instrumentalness = st.slider(
            "Instrumentalness", 0.0, 1.0, 0.0
        )

        liveness = st.slider(
            "Liveness", 0.0, 1.0, 0.15
        )

        valence = st.slider(
            "Valence", 0.0, 1.0, 0.5
        )

        tempo = st.number_input(
            "Tempo (BPM)",
            min_value=1.0,
            max_value=250.0,
            value=120.0
        )

    submitted = st.form_submit_button(
        "🔍 Predict Cluster",
        use_container_width=True
    )

# ---------------- PREDICTION ----------------
if submitted:

    input_data = pd.DataFrame(
        [[
            duration_ms,
            danceability,
            energy,
            loudness,
            speechiness,
            acousticness,
            instrumentalness,
            liveness,
            valence,
            tempo
        ]],
        columns=features
    )

    # Apply the same duration cap used during training
    input_data["duration_ms"] = input_data[
        "duration_ms"
    ].clip(upper=duration_limit)

    # Scale features and predict
    scaled_input = scaler.transform(input_data)
    cluster = int(model.predict(scaled_input)[0])

    st.divider()
    st.subheader("📊 Prediction Result")

    if cluster == 0:
        st.success("Predicted Cluster: 0")
        st.write(
            "This song is assigned to Cluster 0. "
            "This cluster generally has lower energy "
            "and higher acousticness."
        )
    else:
        st.success("Predicted Cluster: 1")
        st.write(
            "This song is assigned to Cluster 1. "
            "This cluster generally has higher energy "
            "and danceability."
        )

    st.caption(
        "The result is based on audio features and "
        "should not be interpreted as a genre prediction."
    )

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "Machine Learning Project | Spotify Track Clustering "
    "| Built with Python and Streamlit"
)