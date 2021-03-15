import time
import pandas as pd
import numpy as np
import math

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

month_list = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'All': 0
}

day_list = {'Mon': 'Monday',
            'Tues': 'Tuesday',
            'Wed': 'Wednesday',
            'Thurs': 'Thursday',
            'Fri': 'Friday',
            'Sat': 'Saturday',
            'Sun': 'Sunday',
            'All': 0}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    is_city = False
    city = input(
        "Please Enter one of those city filter\n(Chicago, New York City, Washington): ").title().strip()
    while is_city == False:
        if city not in CITY_DATA:
            city = input(
                "Invalid input please Try again\n(Chicago, New York City, Washington): ").title().strip()
        else:
            is_city = True

    # TO DO: get user input for month (all, january, february, ... , june)
    is_month = False
    month = input(
        "Please Enter a month filter\n(January, February, March...,June): ").title().strip()
    while is_month == False:
        if month not in month_list:
            month = input(
                "Invalid input please Try again\n(All,January, February, March...,June): ").title().strip()
        else:
            is_month = True

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    is_day = False
    day = input(
        "Please Enter a Day filter from this list \n(All, Mon, Tues, wed, Thurs, Fri, Sat, Sun): ").title().strip()
    while is_day == False:
        if day not in day_list:
            day = input(
                "Invalid input please Try again\n(All, Mon, Tues, wed, Thurs, Fri, Sat, Sun): ").title().strip()
        else:
            is_day = True

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    if month_list[month] != 0:
        df = df[df['Month'] == month_list[month]]
    
        
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    if day_list[day] != 0:
        df = df[df['Day of Week'] == day_list[day]]
    
    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_freq_month = df['Month'].mode()[0]
    
    for name,value in month_list.items():
        if most_freq_month == value:
            print('The most common month is: ', name)
            
    # TO DO: display the most common day of week

    most_freq_day = df['Day of Week'].mode()[0]
    print('The most common day is: ',most_freq_day)

    # TO DO: display the most common start hour
    df['Hours'] = df['Start Time'].dt.hour
    most_freq_hr = df['Hours'].mode()[0]
    print('The most common hour is: ',most_freq_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_freq_start = df['Start Station'].mode()[0]
    print('The most commonly used Start Station: ', most_freq_start)
    # TO DO: display most commonly used end station
    most_freq_end = df['End Station'].mode()[0]
    print('The most commonly used End Station: ',most_freq_end)

   # TO DO: display most frequent combination of start station and end station trip
   
    df['trip route']=df['Start Station']+"  'AND'  "+df['End Station']
    common_route=df['trip route'].mode()[0]
    print('The most used combination is: ',common_route)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    td_sum = df['Trip Duration'].sum()
    sum_seconds = td_sum%60
    sum_minutes = td_sum//60%60
    sum_hours = td_sum//3600%60
    sum_days = td_sum//24//3600
    print('Passengers travelled a total of {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    # TO DO: display mean travel time
    print()
    td_mean = math.ceil(df['Trip Duration'].mean())
    mean_seconds = td_mean%60
    mean_minutes = td_mean//60%60
    mean_hours = td_mean//3600%60
    mean_days = td_mean//24//3600
    print('Passengers travelled an average of {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print(user_types,"\n")
    
    # TO DO: Display counts of gender
    # To fill NAN values
    if 'Gender' in df:
        df['Gender'].fillna("Undefined Gender", inplace=True)
        gender_types = df['Gender'].value_counts().to_frame()
        print(gender_types,"\n")
#         print(df.shape)
    else:
        print("Gender data not available in this dataset \n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_by = df['Birth Year'].min()
        print('The earliest year of birth is : ',int(earliest_by))
        most_recent_by = df['Birth Year'].max()
        print('The most recent year of birth is : ',int(most_recent_by))
        most_freq_by = df['Birth Year'].mode()[0]
        print('The most common year of birth is : ',int(most_freq_by))
    else:
        print("Birth Year data not available in this dataset")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(city):
    print('\nRaw data is available to check... \n')
    display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
    while display_raw not in ('yes', 'no'):
        print('That\'s invalid input, please check your spelling and try again')
        display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes or No if you don\'t want \n').lower()
   # The second while loop is on the same level and doesn't belong to the first.
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(chunk)
                display_raw = input('To View another sample of raw data in chuncks of 5 rows type: Yes\n').lower()
                if display_raw != 'yes':
                    print('Thank You!')
                    break
            break
        except KeyboardInterrupt:
            print('Thank you!')
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        x = display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()