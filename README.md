# Analysis-Determining-Factors-Placement-Job

An interactive dashboard built to visualize key patterns and trends in the dataset, such as CGPA distribution, internship experience, communication skills, and job placement rate.

##### Model Prediction
A **Binary Logistic Regression** model is trained using the dataset to predict whether a student is likely to get placed based on various academic and personal factors.

Features include:
- IQ  
- CGPA
- Previous Semester Results  
- Academic Performance  
- Internship Experience  
- Communication Skills  
- Extra-Curricular Score  
- Projects Completed
  
You can open my model predicition :
[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1X7JwBnRRjDH9y4gjF-1MTR_Q6_44d9On?usp=sharing)

---

##### Data Analysis
Comprehensive data cleaning, preprocessing, and feature analysis were performed to identify significant factors that impact job placement results.

- Checked data distribution and missing values  
- Identified correlation between features  
- Visualized insights for better understanding  

You can see my dashboard : 
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)](https://public.tableau.com/app/profile/natalia.budiarti/viz/Project1-CollegeCareerFactor/Final?publish=yes)

---

##### Key Insights
- Based on the results of the binary logistic regression analysis, three variables were found to have a statistically significant effect (p < 0.05) on students’ job placement outcomes: IQ (Coef = 0.1088, p = 4.93E−197), Communication Skills (Coef = 0.6481, p = 5.99E−228), Projects Completed (Coef = 0.6794, p = 2.05E−122).
- In the boxplot, there is a median difference of 0.665 (from 7.495 to 8.160), indicating that CGPA is indeed a significant distinguishing factor. Students who were placed generally have a substantially higher CGPA on average.
- In the bar chart, a total of 1,226 students out of 10,000 with communication skill scores between 8 and 10 were successfully placed in jobs, indicating that higher communication skills are strongly associated with job placement success.
- Interestingly, students without internship experience show a higher placement count than those who have internships, suggesting that academic and personal skills may have a stronger influence on employability in this dataset.
- The model achieved **81.1% accuracy** on test data.

---

##### Tools & Technologies
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)  
- Tableau
- Google Colab  
- GitHub

Data Source : https://www.kaggle.com/datasets/emanfatima2025/college-placement-analysis (Kaggle)
