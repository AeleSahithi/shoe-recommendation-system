
import pandas as pd
from datetime import datetime

def get_recommendations(user_id, users, interactions, shoes):
    # Dummy logic for now — you can improve later
    return ["Nike Air Max", "Adidas Ultraboost"]

def get_personalized_services(user_id, users, interactions, shoes, weather):
    interactions['timestamp'] = pd.to_datetime(interactions['timestamp'])
    today = datetime(2025, 8, 5)

    merged = interactions.merge(shoes, on='shoe_id', how='left')
    alerts = []

    # Filter only this user's data
    merged = merged[merged['user_id'] == user_id]

    for (user, shoe), group in merged.groupby(['user_id', 'shoe_id']):
        usage_count = len(group)
        last_used = group['timestamp'].max()
        days_since_used = (today - last_used).days

        purchases = group[group['action'] == 'purchase']
        if not purchases.empty:
            purchase_date = purchases['timestamp'].min()
            days_since_purchase = (today - purchase_date).days
            if days_since_purchase > 150 and usage_count >= 10:
                alerts.append(f"Consider replacing {shoe} — bought {days_since_purchase} days ago and used {usage_count} times.")

        material = group['material'].iloc[0]
        if material in ['leather', 'synthetic'] and days_since_used > 30:
            alerts.append(f"Reminder to clean your {material} shoe ({shoe}) — last used {days_since_used} days ago.")

    return alerts
