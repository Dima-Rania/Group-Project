import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Cleaned_Students_Performance.csv')

# Convert 'test_preparation_course' to string and clean up any inconsistencies
data['test_preparation_course'] = data['test_preparation_course'].astype(str).str.strip().str.lower()

# 1. Predicting Student Scores based on Features
def predict_average_score(row):
    # Check if student completed the test prep course
    if row['test_preparation_course'] == 'completed':
        # Increase the score prediction by a small amount if test prep is completed
        return row['average_score'] + 5
    else:
        return row['average_score']

data['predicted_score'] = data.apply(predict_average_score, axis=1)

# Plot Actual vs Predicted Average Scores for the First 20 Students
plt.figure(figsize=(10, 6))
plt.plot(data['average_score'][:20], label='Actual Average Score', marker='o')
plt.plot(data['predicted_score'][:20], label='Predicted Average Score', marker='x')
plt.xlabel('Student Index (First 20)')
plt.ylabel('Scores')
plt.title('Actual vs Predicted Average Scores (First 20 Students)')
plt.legend()
plt.show()

# 2. Checking if Test Preparation Helps
# Convert the 'test_preparation_course' column
# Here, we change '0' to 'none' and '1' to 'completed' to make it easier to understand
data['test_preparation_course'] = data['test_preparation_course'].replace({'0': 'none', '1': 'completed'})

# Calculate average scores for each group
# Create two groups: one for students who completed test prep, and one for those who didn't
prep_completed = data[data['test_preparation_course'] == 'completed']
prep_none = data[data['test_preparation_course'] == 'none']

# Find the average score for each group
# Calculate the average score for students with and without test preparation
avg_score_prep = prep_completed['average_score'].mean()
avg_score_no_prep = prep_none['average_score'].mean()

# Print the results so we can see the values
print("Average score with test prep:", avg_score_prep)
print("Average score without test prep:", avg_score_no_prep)

# Plot a simple bar chart to show the results
# This chart will compare the average scores of the two groups
plt.figure(figsize=(8, 5))
plt.bar(['With Test Prep', 'Without Test Prep'], [avg_score_prep, avg_score_no_prep], color=['green', 'red'])
plt.xlabel('Test Preparation Status')
plt.ylabel('Average Score')
plt.title('Average Score with and without Test Preparation')
plt.show()

# 3. Analyzing Social and Family Factors
def analyze_social_factors(data):
    # Group data by race/ethnicity and parental education
    factors = ['race_ethnicity', 'parental_level_of_education']
    
    for factor in factors:
        avg_scores = data.groupby(factor)['average_score'].mean()
        
        # Bar chart for each factor
        plt.figure(figsize=(10, 6))
        avg_scores.plot(kind='bar', color='skyblue')
        plt.xlabel(factor.replace('_', ' ').title())
        plt.ylabel('Average Score')
        plt.title(f'Average Scores based on {factor.replace("_", " ").title()}')
        plt.xticks(rotation=45)
        plt.show()

analyze_social_factors(data)
