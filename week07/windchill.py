# Your assignment is to write a program that asks the user for a 

# temperature and then shows the wind chill values for various wind speeds at that temperature.

# Your program should compute and display the wind chill for wind 

# speeds of 5, 10, 15, ..., 60 miles per hour, just like the 

# National Weather Service chart does. To help users who are 

# more familiar with Celsius, your program should allow temperature

#  to be entered in either Celsius or Fahrenheit, and if needed,
 
#  convert the Celsius temperature to Fahrenheit before using the formula.

# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

# Wind Chill (C) = ((35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)) - 32) * (5 / 9)

# (0°C × 9/5) + 32 = 32°F

def wind_chill_calc_f(temperature, wind_speed):
    wind_chill_f = 35.74 + 0.6215 * (temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * (temperature) * (wind_speed ** 0.16)
    return wind_chill_f

def c_to_f_convert(temperature):
    f_temp =  (temperature * (9/5) + 32)
    return f_temp

user_play = ''

wind_speed = 5

temperature = 0

while user_play.lower() != 'quit':
    temperature = float(input('What is the temperature?'))
    user_pref = input('Fahrenheit or Celsius (F/C)?')
    if user_pref.upper() == 'C':
        temperature = c_to_f_convert(temperature)
    while wind_speed < 61:
        wind_chill_temp = wind_chill_calc_f(temperature, wind_speed)
        print(f'At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_temp:.2f}F')
        wind_speed += 5
    wind_speed = 5