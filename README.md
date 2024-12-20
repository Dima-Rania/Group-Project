# 🌟 Group-Project's Q&A 🌟

## 📚 **Assignment 2: Algorithm Design (Project Work)**

### ❓ **Question 1:**
🔎
The first step for this project would be to brainstorm with your teammates to decide what kind of data you would be interested in, and what you would like to be able to do with that data. This includes:
Finding or conceptualizing an interesting dataset
Defining a specific problem or need for the data, that can be resolved algorithmically
Modeling (or fine-tuning the pre-existing model of) your data in a way that it becomes relevant for your algorithm
This process involves discussing questions such as: Where would you find the data you want to work with? Or would you need to collect or fabricate the data yourself? In what format is the data available? Can we work with this format in our algorithm? Or do we need to translate the data to another format? Do we need to clean the data in any way (e.g.: delete irrelevant or duplicate information; structure the data differently; correct errors in the data, or add additional information to the data that would be useful for the algorithm)? How do we intend to use the data, and do we need to make any changes to the (way the) data (is structured) to facilitate this?
It is important for this step that you know your data. This requires you to have a good understanding of how the data you want to work with is modeled. E.g. for XML data: Which tags and attributes contain which information? Or, in the case of a database: Which attributes do the tables use, and how are the relations between different tables linked? At the same time, it is important to try to anticipate the needs of your algorithm. What kind of information would our algorithm require, and how is this information recorded in the dataset? Is the dataset modeled in a way that makes it easy for my algorithm to obtain the relevant data?
For example: if you were designing an algorithm that maps out a citation network (as in: who is citing who?) based on a selection of academic papers, your data would have to be modelled in a way that makes it easy for your algorithm to find a) the author names of each of the papers in your database; and b) the author names of each of the references cited in each of those papers.
If you are starting from pre-existing data, this means: understanding what kind of information it contains, and how it is structured. If you are developing your dataset, this means conceptualizing your model to map your data onto (as you did, for example, in Assignment 1). You may also want to do a little of both: use pre-existing data, but make some changes to the way it is structured (or the information it contains) that make it easier for your algorithm to access the information you need.

### 💡**Answer:**
  
To approach this step with our data we did the following steps:

1️⃣ **We are defining a problem or a need to address it such as:**

  🔸 **Predicting students’ performance:** Here we discuss if certain features (e.g.: parental education, test preparation, and lunch) can predict a student’s performance such as total or average score.
  
  🔸 **Analysis and comparison of performance differences among students:** In this point, we see if is there a significant difference between students’ performance especially between students who have completed the test preparation and those who haven't completed it.
  
  🔸 **Impact of social factors on students’ scores:** We discussed here how factors like race/ ethnicity and parental education level impact students’ scores.
 
2️⃣ **Data structure and format considerations:**

  🔸 The data in the dataset is structured in a table format, and each row represents a student. Additionally, it is well-formed in a CSV file so we can use it directly after a few checks.
  
  🔸 Data pre-processing steps:  
                     1. Check categorical fields: this step is essential to ensure that values are consistent. For example, race_ethnicity and parental_level_of_education should be spelled consistently.      
                     2. Verify binary fields: at this step, we ensure that binary fields such as (gender, lunch, test_preparation_course) are consistently coded as 0 and 1.
  

### ❓ **Question 2:**
🚀
Once you know how your data should be modelled, you can put it into practice. If you are collecting your own data: map it onto your data model. If you are starting from a dataset developed by others: clean the dataset and make relevant changes to the way it is modelled. The result of this step is that you will have a dataset that your algorithm can work with.

### 💡**Answer:**
 
1️⃣ Create a new column for performance levels: 
We can create categories for performance such as “High”, “Medium”, and “Low” based on the average score.

#### **Python Code**:
```python


import pandas as pd
import numpy as np
 
data = pd.read_csv('Cleaned_Students_Performance.csv')
 conditions = [
    (data['average_score'] >= 80),
    (data['average_score'] >= 60) & (data['average_score'] < 80),
    (data['average_score'] < 60)
]
performance_levels = ['High', 'Medium', 'Low']
 
data['performance_level'] = np.select(conditions, performance_levels, default='Unknown')
 
data.to_csv('Curated_Students_Performance.csv', index=False)
``` 
 
🧹 **Explanation:**

Before we added in the default argument a default=’Unkonwn’ argument to the np.select() function, we were getting an error because the data types were mismatched. The condition we are checking (average_score values) numbers, but the choices we are assigning (performance_levels) are strings like ‘High’, ‘Medium’, and ‘Low’. Numpy doesn’t know how to handle both at once.
So to fix this issue we added a default value (‘Unknown’) which helps in case none of the conditions are met, so we ensure that the program will still work if something goes wrong by putting ‘Unknown’ as the value.


2️⃣ Clean up categorical data: 
We make sure that our categorical fields such as race/ ethnicity, and parental education have consistent values.
3️⃣ Save the cleaned data: 
After we finished and cleaned our data, we saved the updated dataset.


### ❓ **Question 3:**

Step 3: Design Your Algorithm
Now that you have your dataset, you can start to process it. This is where your algorithm comes in. Using pseudocode, write out the different steps that are necessary to accomplish the task you have set out.
Note: For students who would like more of a challenge, we also allow you to write your algorithm in a full-fledged Turing-complete programming language, like Python. If successful, we would of course consider this a strong demonstration of your skills and understanding of the course materials — which would have a positive effect on our determination of your grade. That said, however, we feel the need to stress that this is in no way a requirement, and that it will be possible to obtain a perfect grade (A) for assignments where the algorithm is written in pseudocode.

### 💡**Answer:**
  
After we had done the curated dataset, we can now write an algorithm in simple pseudocode for each of our defined problems in step 1:

1️⃣ Predicting student performance:
Here we use a regression model to predict the average_score
. Load curated dataset
. Define the target variable as “average_score”
. Define more variables as “gender”, “race_ethnicity”, “parental_level_of_education”, “lunch”, “test_preparation_course”
. Split data into training and testing sets
. Train a regression model on training data
. Test model on test data
. Output model accuracy

2️⃣ Analysis and comparison of performance differences among students:
Here we write a pseudocode for comparing average scores between students who did and did not complete the test preparation course:
·   Load curated dataset
·   Split data into two groups:
·   Group 1: Students who complete test preparation
·   Group 2: Students who did not complete test preparation
·   For each score type (math, reading, writing):
·   Calculate the average score for Group 1 and Group 2
·   Compare the two average results to see if the differences are important
·   Output average differences and importance

3️⃣ Impact of social factors on students’ scores
Here we analyze the data to check how race/ethnicity factors affect the students’ scores:
·   Load curated dataset
·   Group data bt race_ethnicity and parental_level_of_education
·   Calculate average scores for each group
·   Test if the differences between the groups are important
·   Output average scores and the test results



## 🔗 **More Information**

For the rest of the questions, check out the **code in the repository!** 💻
