from src.data_cleaning import load_data, clean_data, save_data
from src.eda import plot_readmission, plot_age, correlation_heatmap
from src.model import train_model
from src.utils import print_insights

# Load data
df = load_data("data/raw_data.csv")

# Clean data
df = clean_data(df)
save_data(df, "data/cleaned_data.csv")

# EDA
plot_readmission(df)
plot_age(df)
correlation_heatmap(df)

# Model
model, accuracy = train_model(df)

# Insights
print_insights(accuracy)
