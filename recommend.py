import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load Data
interactions = pd.read_csv('../data/interactions.csv')
shoes = pd.read_csv('../data/shoes.csv')
users = pd.read_csv('../data/users.csv')

# Step 1: Collaborative Filtering
def prepare_cf_data(df):
    df = df[df['action'].isin(['purchase', 'like'])].copy()
    df['rating'] = df['action'].apply(lambda x: 5 if x == 'purchase' else 3)
    return df[['user_id', 'shoe_id', 'rating']]

cf_data = prepare_cf_data(interactions)
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(cf_data[['user_id', 'shoe_id', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
model = SVD()
model.fit(trainset)

def get_collab_recs(user_id, top_n=3):
    shoe_ids = shoes['shoe_id'].tolist()
    predictions = [(iid, model.predict(user_id, iid).est) for iid in shoe_ids]
    sorted_preds = sorted(predictions, key=lambda x: x[1], reverse=True)
    return [s[0] for s in sorted_preds[:top_n]]

# Step 2: Content-based Filtering
def get_content_recs(user_id, top_n=3):
    user_views = interactions[(interactions['user_id'] == user_id)]['shoe_id'].tolist()
    if not user_views:
        return []

    shoe_features = shoes.set_index('shoe_id')[['type', 'material', 'color']]
    enc = OneHotEncoder()
    features_encoded = enc.fit_transform(shoe_features).toarray()

    viewed_vectors = []
    for sid in user_views:
        if sid in shoe_features.index:
            idx = list(shoe_features.index).index(sid)
            viewed_vectors.append(features_encoded[idx])

    user_profile = np.mean(viewed_vectors, axis=0)
    similarities = cosine_similarity([user_profile], features_encoded)[0]

    sim_scores = list(zip(shoe_features.index, similarities))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    return [s[0] for s in sim_scores[:top_n]]

# Step 3: Combine both
def hybrid_recommend(user_id):
    cf = get_collab_recs(user_id)
    cb = get_content_recs(user_id)
    merged = list(dict.fromkeys(cf + cb))  # merge while preserving order
    return merged[:5]

# Test
for uid in users['user_id']:
    print(f"Recommendations for {uid}: {hybrid_recommend(uid)}")
