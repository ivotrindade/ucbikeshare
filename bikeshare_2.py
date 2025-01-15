"""

  Bike Share Project - Statistics on Bike Share Services
  
  Author: Ivo Veiga
  Date: January 2025


"""

import time
import pandas as pd
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def check_city(input_city):
    """
       user input check for the city.

    """
    while True:
        input_read=input(input_city)
        try:
            if input_read in ['chicago','new york city','washington']:
                break
            else:
                print("Please, enter chicago, new york city or washington.")
 
        except ValueError:
            print("Please, enter one of the cities presented!")
    return input_read

def check_month(input_month):
    """
      input check for month

    """
    while True:
        input_read=input(input_month)
        try:
            if input_read in ['all', 'january','february','march', 
                              'april', 'may', 'june']:
                break
            else:
                print("Please, enter all, january, february, march, april, may or june.")
 
        except ValueError:
            print("Please, enter one of the months presented!")
    return input_read

def check_wkday(input_wkday):
    """
      input check for day of the week

    """
    while True:
        input_read=input(input_wkday)
        try:
            if input_read in ['all', 'monday','tuesday', 'wednesday', 
                              'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print("Please, enter all, monday, tuesday, wednesday, thursday, friday, saturday or sunday.")
 
        except ValueError:
            print("Please, enter one of the days of the week presented!")
    return input_read

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_city("Would you like to see the data for chicago, new york city or washington? \n")

    # get user in  put for month (all, january, february, ... , june)
    month = check_month("Would you like to see the data for january, february, march, april, may, june or all months? \n")
    # print("and the month is: " + month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_wkday("Would you like to see the data for monday, tuesday, wednesday, thursday, friday, saturday, sunday or all days? \n")
    # print("and the day of the week is: " + day)

    print("\n")
    print('-'*40)
    print(f"See Stats below for city {city}, month {month} and day {day}, Year 2017 ")

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
    
    # Loads data in the dataframe df
    df = pd.read_csv(CITY_DATA[city])

    # converts the Start Time column format to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extracts month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    top_month = df['month'].mode()[0]

    print('Top Month:', top_month)

    # display the most common day of week
    top_day_of_week = df['day_of_week'].mode()[0]

    print('Top Day of the Week:', top_day_of_week)

    # display the most common start hour
    top_common_start_hour = df['hour'].mode()[0]

    print('Top Start Hour:', top_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]

    print('Top Start Station: ', top_start_station)

    # display most commonly used end station
    top_end_station = df['End Station'].mode()[0]

    print('Top End Station:', top_end_station)

    # display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    top_combined_station = group_field.size().sort_values(ascending=False).head(1)
    print('Top Start and End Station combined trip:\n', top_combined_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)
    print('Total Travel Time is a variable of type: ',type(total_travel_time))
    
    # convert seconds into hour, minutes and seconds for total travel time
    td = timedelta(seconds = int(total_travel_time))
    
    #get the hh, mm and ss from the string
    td1 = str(td)
    days1, hhmmss1 = td1.split(',')
    hh1, mm1, ss1 = hhmmss1.split(':')

    print(td)    
    print(f"The {total_travel_time} seconds are equal to {days1} days,{hh1} hours, {mm1} minutes, and {ss1} seconds ")
       
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Mean Travel Time:', mean_travel_time)
    
    # convert seconds into hour, minutes and seconds for mean travel time
    td = timedelta(seconds = int(mean_travel_time))

    print(f"The {mean_travel_time} seconds are equal to ", td)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    
    """
        >>> Gender and Birth Year Statistics Exception <<<
        - washington.csv source data has no 'Gender' and 'Birth Year' columns
        - therefore skipping 'Gender' and 'Birth Year' Stats when city equals
          to Washington
    """
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
    
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:',most_common_year)
        
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Birth Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Birth Year:',earliest_year)
    else:
        print("Washington has no stats for Gender and Birth Year.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Function to display records in chunks of 5
def display_records(df):
    start = 0
    chunk_size = 5
    while start < len(df):
        print(df[start:start + chunk_size])
        start += chunk_size
        user_input = input("Do you want to see the next 5 records? (yes/no): ")
        if user_input.lower() != 'yes':
            break

def main():
    while True:
        
        # Setup Filters
        city, month, day = get_filters()
        
        # Load File
        df = load_data(city, month, day)

        # Provide Time Stats
        time_stats(df)
        
        # Provide Stations Stats
        station_stats(df)
        
        # Provide travels duration stats
        trip_duration_stats(df)
        
        # Provide User Stats
        user_stats(df, city)
        
        # Offer if raw data should be viewed
        check_raw_data = input('\nWould you like to view raw data? Enter yes or no.\n')
        if check_raw_data.lower() == 'yes':
            display_records(df)

        # asks if finishes or start it over
        restart = input('\nWould you like to start it over? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
