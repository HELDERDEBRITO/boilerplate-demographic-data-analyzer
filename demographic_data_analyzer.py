
import pandas as pd

def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many people of each race?
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df['education'].eq('Bachelors').sum() / len(df)) * 100, 1
    )

    # 4. Percentage with advanced education earning >50K
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    higher_education_rich = round(
        (df[higher_education]['salary'].eq('>50K').sum()
         / higher_education.sum()) * 100, 1
    )

    # 5. Percentage without advanced education earning >50K
    lower_education = ~higher_education

    lower_education_rich = round(
        (df[lower_education]['salary'].eq('>50K').sum()
         / lower_education.sum()) * 100, 1
    )

    # 6. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people working minimum hours who earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(
        (min_workers['salary'].eq('>50K').sum()
         / len(min_workers)) * 100, 1
    )

    # 8. Country with highest percentage earning >50K
    country_earning = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').mean() * 100
    )

    highest_earning_country = country_earning.idxmax()

    highest_earning_country_percentage = round(
        country_earning.max(), 1
    )

    # 9. Most popular occupation for people earning >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degrees:", percentage_bachelors)
        print("Percentage with higher education earning >50K:", higher_education_rich)
        print("Percentage without higher education earning >50K:", lower_education_rich)
        print("Minimum work hours:", min_work_hours)
        print("Percentage of minimum-hour workers earning >50K:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

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