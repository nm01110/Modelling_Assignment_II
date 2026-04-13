import math

# Data (in meters)
room_length = 8.0
room_width  = 7.0
room_height = 3.0
ball_diameter = 0.1

# Calculations
# Room volume
room_volume = room_length * room_width * room_height

# Ball volume
ball_radius = ball_diameter / 2.0
ball_volume = (4.0/3.0) * math.pi * (ball_radius ** 3)

# Ideal number
ideal_count = room_volume / ball_volume

# Atomic Packing Factors (APF)
APF_SC  = math.pi / 6.0
APF_BCC = (math.pi * math.sqrt(3)) / 8.0
APF_FCC = math.pi / (3.0 * math.sqrt(2))

# Actual number of balls for each packing type
count_SC  = round(ideal_count * APF_SC)
count_BCC = round(ideal_count * APF_BCC)
count_FCC = round(ideal_count * APF_FCC)

#
counts = [count_SC, count_BCC, count_FCC]
labels = ['SC', 'BCC', 'FCC']
plt.bar(labels, counts, color=['red', 'blue', 'green'])
plt.ylabel('Number of Balls')
