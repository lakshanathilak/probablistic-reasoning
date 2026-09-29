

total = 20

rain = 8
not_rain = 12

cloudy_rain = 7
cloudy_not_rain = 3

p_rain = rain / total
p_not_rain = not_rain / total


p_cloudy_rain = cloudy_rain / rain
p_cloudy_not_rain = cloudy_not_rain / not_rain


p_cloudy = (p_cloudy_rain * p_rain) + (p_cloudy_not_rain * p_not_rain)


p_rain_cloudy = (p_cloudy_rain * p_rain) / p_cloudy
p_not_rain_cloudy = (p_cloudy_not_rain * p_not_rain) / p_cloudy

print("P(Rain) =", p_rain)
print("P(Not Rain) =", p_not_rain)

print("P(Cloudy | Rain) =", p_cloudy_rain)
print("P(Cloudy | Not Rain) =", p_cloudy_not_rain)

print("P(Rain | Cloudy) =", p_rain_cloudy)
print("P(Not Rain | Cloudy) =", p_not_rain_cloudy)

if p_rain_cloudy > p_not_rain_cloudy:
    print("Predicted Weather = Rain")
else:
    print("Predicted Weather = Not Rain")



#     The program uses Bayes' Theorem to predict the weather when the sky is Cloudy.

# Total days = 20
# Rainy days = 8
# Not rainy days = 12
# Cloudy during rain = 7
# Cloudy during no rain = 3

# First, we calculate the prior probabilities:

# P(Rain) = 8 / 20 = 0.4
# P(Not Rain) = 12 / 20 = 0.6

# Then:

# P(Cloudy | Rain) = 7 / 8 = 0.875
# P(Cloudy | Not Rain) = 3 / 12 = 0.25

# After applying Bayes' Theorem:

# P(Rain | Cloudy) = 0.7
# P(Not Rain | Cloudy) = 0.3

# Since 0.7 is greater than 0.3, the program predicts:

# Predicted Weather = Rain

# Bayes' Theorem helps us find the probability of rain based on the observed condition, which is Cloudy.