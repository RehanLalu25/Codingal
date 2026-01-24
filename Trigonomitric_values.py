import math

# Input angle in degrees
angle_deg = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate trigonometric values
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

# Display results
print("Sine:", sin_value)
print("Cosine:", cos_value)
print("Tangent:", tan_value)
