min_life_expectancy = 1000

max_life_expectancy = 0

min_life_expectancy_year_of_interest = 1000

min_life_expectancy_year_of_interest_country = ''

max_life_expectancy_year_of_interest_country = ''

max_life_expectancy_year_of_interest = 0

average_life_expectancy_year_of_interest = 0

year_of_interest = int(input('Enter the year of interest.'))

year_list = []

with open("week06\life-expectancy.csv") as life_files:
    next(life_files)
    for line in life_files:
        line = line.strip()
        line = line.split(",")
        country = line[0]
        code = line[1]
        year = line[2]
        life_expectancy = float(line[3])
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy

            min_life_country = country

            min_life_year = year
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy

            max_life_country = country

            max_life_year = year

print(f'The overall max life expectancy is: {max_life_expectancy} from {max_life_country} in {max_life_year}')
print(f'The overall min life expectancy is: {min_life_expectancy} from {min_life_country} in {min_life_year}')        
print(f'For the year: {year_of_interest}\nThe average life expectancy across all countries was {average_life_expectancy_year_of_interest:.2f}\nThe max life expectancy was in {max_life_expectancy_year_of_interest_country} with {max_life_expectancy_year_of_interest:.2f}\nThe min life expectancy was in {min_life_expectancy_year_of_interest_country} with {min_life_expectancy_year_of_interest:.2f}')