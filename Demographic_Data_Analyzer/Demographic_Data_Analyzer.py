#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def calculate_demographic_data(print_output=True):

    df = pd.read_csv('adult.data.csv')  

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    percentage_bachelors = (df['education'] == 'Bachelors').sum() / len(df) * 100

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = (higher_education['salary'] == '>50K').sum() / len(higher_education) * 100
    lower_education_rich = (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100

    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').sum() / len(df[df['native-country'] == highest_earning_country]) * 100

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_output:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Percentage with higher education and >50K:", higher_education_rich)
        print("Percentage without higher education and >50K:", lower_education_rich)
        print("Minimum work hours:", min_work_hours)
        print("Percentage of rich among those who work minimum hours:", rich_percentage)
        print("Country with the highest percentage of earners >50K:", highest_earning_country)
        print("Percentage of earners >50K in the highest earning country:", highest_earning_country_percentage)
        print("Top occupation in India for earners >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()


