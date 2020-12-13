def saturnian_to_earth_age_converter():

    saturian_age_int= int(input("How old is the Saturnian you are talking to? "))
    saturian_age_days= saturian_age_int * 10759
    #print(saturian_age_days)

    saturian_age_earth_years= saturian_age_days // 365
    years_leftover_earth_days= saturian_age_days % 365

    saturian_age_earth_months= years_leftover_earth_days // 30
    months_leftover_earth_days= years_leftover_earth_days % 30

    #print(saturian_age_years)
    #print(years_leftover_days)
    #print(saturian_age_months)
    #print(months_leftover_days)

    print("This Saturnian is", saturian_age_earth_years,"Earth-years,", saturian_age_earth_months,"Earth-months, and", months_leftover_earth_days,"Earth-days old.")


# It takes Saturn approximately 10,759 Earth-days to orbit the sun.
# In the file SaturnianToEarthAgeConverter.py, write a function saturnian_to_earth_age_converter
# that will translate a Saturnian's age into Earth units. Take a look at the sample behaviour below:
#
# How old is the Saturnian you are talking to? 10
# This Saturnian is 294 Earth-years, 9 Earth-months, and 24 Earth-days old.
# For this problem, you may assume that Earth-years are always 365 days long, and Earth-months
# are always 30 days long.


### DO NOT WRITE CODE BEYOND THIS LINE ###

if __name__ == '__main__':
    saturnian_to_earth_age_converter()
