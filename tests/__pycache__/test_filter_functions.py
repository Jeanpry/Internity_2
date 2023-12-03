# test_filter_functions.py

import pytest
import pandas as pd
from filter_functions import filter_by_type, filter_by_location, filter_by_duration

# Exemple de données pour les tests
data = [
    {"Type_of_internship": "Sales & Marketing", "location": "New York", "duration": "3 Months"},
    {"Type_of_internship": "Fundraising", "location": "San Francisco", "duration": "2 Months"},
    {"Type_of_internship": "Digital Marketing", "location": "New York", "duration": "1 Month"}
]
df = pd.DataFrame(data)

# Test pour filter_by_type
def test_filter_by_type():
    filtered_df = filter_by_type(df, "Sales & Marketing")
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['Type_of_internship'] == "Sales & Marketing"
    assert all(filtered_df['Type_of_internship'] == "Sales & Marketing")

# Test pour filter_by_location
def test_filter_by_location():
    filtered_df = filter_by_location(df, "New York")
    assert len(filtered_df) == 2
    assert all(filtered_df['location'] == "New York")

# Test pour filter_by_duration
def test_filter_by_duration():
    filtered_df = filter_by_duration(df, "3 Months")
    assert len(filtered_df) == 1
    assert all(filtered_df['duration'] == "3 Months")

# Ajoutez ici des tests supplémentaires pour d'autres scénarios et fonctions
