import pandas as pd
import numpy as np
from pathlib import Path
DATA_PATH = Path("TripAdvisorTrainingDataProject1")
LABEL_COLUMNS = ["typeR"]
REVIEWS_COLUMNS = ["idplace","review","langue"]


def read_dataset():
    attraction_sub_categorie_path = (DATA_PATH / "AttractionSubCategorie").with_suffix(".csv")
    attraction_sub_type_path = (DATA_PATH / "AttractionSubType").with_suffix(".csv")
    cuisine_path = (DATA_PATH / "cuisine").with_suffix(".csv")
    dietary_restrictions_path = (DATA_PATH / "dietary_restrictions").with_suffix(".csv")
    restaurant_type_path = (DATA_PATH / "restaurantType").with_suffix(".csv")
    trip_advisor_path = (DATA_PATH / "Tripadvisor").with_suffix(".csv")

    attraction_sub_categorie = pd.read_csv(attraction_sub_categorie_path, sep=",")
    attraction_sub_type = pd.read_csv(attraction_sub_type_path, sep=",")
    cuisine = pd.read_csv(cuisine_path, sep=",")
    dietary_restrictions = pd.read_csv(dietary_restrictions_path, sep=",")
    restaurant_type = pd.read_csv(restaurant_type_path, sep=",")
    trip_advisor = pd.read_csv(trip_advisor_path, sep=",")

    return (attraction_sub_categorie,
            attraction_sub_type,cuisine,dietary_restrictions,
            restaurant_type,trip_advisor)


def add_name_from_id(dataset_input, input_column_name, dataset_id):
    if input_column_name not in dataset_input:
        print(f"No {input_column_name}")
        return dataset_input
    
    def mapping_multiple(index_string):
        if pd.isna(index_string):
            return np.nan
        
        ids_list = str(index_string).split(',')
        names = [mapping_id.get(i.strip(), "Unknown") for i in ids_list]
        
        return ", ".join(names)
    
    dataset_id['id'] = dataset_id['id'].astype(str)
    mapping_id = dataset_id.set_index('id')['name'].to_dict()

    dataset_input[f"{input_column_name}_name"] = dataset_input[input_column_name].apply(mapping_multiple)
    
    return dataset_input.drop(columns=[input_column_name]) 


def preprocess_dataset():
    attraction_sub_categorie,attraction_sub_type,cuisine,dietary_restrictions,restaurant_type,trip_advisor =read_dataset()
    
    trip_advisor = add_name_from_id(trip_advisor,"activiteSubCategorie",attraction_sub_categorie)
    trip_advisor = add_name_from_id(trip_advisor,"activiteSubType",attraction_sub_type) 
    trip_advisor = add_name_from_id(trip_advisor,"restaurantTypeCuisine",cuisine)       
    trip_advisor = add_name_from_id(trip_advisor,"restaurantDietaryRestrictions",dietary_restrictions) 
    trip_advisor = add_name_from_id(trip_advisor,"restaurantType",restaurant_type) 
    return trip_advisor


def get_label(reviews :pd.DataFrame, airbnb_info: pd.DataFrame) -> pd.DataFrame:
    label_columns = [col for col in LABEL_COLUMNS if col in airbnb_info.columns]
    
    if not label_columns:
        print("Error: None of the label columns are in airbnb_info")
        return reviews

    temp_airbnb_info = airbnb_info[['id'] + label_columns].copy()

    temp_airbnb_info['label'] = temp_airbnb_info[LABEL_COLUMNS].apply(
    lambda row: [str(val) if pd.notna(val) and str(val).lower() != 'nan' else "unknown" for val in row], 
    axis=1)

    reviews = reviews.merge(temp_airbnb_info[['id', 'label']],
    left_on='idplace', 
    right_on='id', 
    how='left')

    reviews = reviews.drop("id", axis=1)
    return reviews

def preprocess_reviews(trip_dataset):

    reviews_path = (DATA_PATH / "reviews83325").with_suffix(".csv")
    reviews = pd.read_csv(reviews_path, sep=",")
    reviews = reviews[[REVIEWS_COLUMNS]] 
    reviews_by_place = reviews.groupby('idplace').agg({'review': list,'langue': list}).reset_index()
    reviews_by_place = get_label(reviews_by_place,trip_dataset)
    return reviews

def preprocess():

    trip_dataset = preprocess_dataset()
    return preprocess_reviews(trip_dataset=trip_dataset)