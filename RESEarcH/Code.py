# MAXIMUM SENSIBLE SOUND == 85 Db
# Minimum sound you can hear== 0Db
# SOUND < 45Db is not regarded as noise
# THICKNESS OF MATERIALS
# GLASS, WOOD AND CONCRETE
# HOW DISTANCE AND THICKNESS OF MATERIALS BLOCK NOISE E.g a wood must be at 25m with 2In thickness to block the noise of a lawnmower
# Sound Absorption Coefficient depends on thickness 
#  The Sound level decreases with increasing distance
# DISTANCE RATIO
# INVerse square law states that  the sound level decreases by 6Db for every doubling of the distance from the source
import math
import random
from Art import Logo

print(Logo)
# Parameters
try:
    lawnmower_sound_level =   float(input("What is your lawnmower/ SOURCE frequency in decibels")) # dB
except ValueError:
    print("Invalid Value")

# distance_from_lawnmower = float(input("How far is the material from the lawnmower?\n"))  # meters
# wooden_house_thickness = float(input(" What is the thickness of the Material?"))  # inches
# wood_absorption_coefficient = 0.05

def wood_sim():
    distance_from_lawnmower = float(input("How far is the material from the lawnmower?\n")) #20  # meters
    wooden_house_thickness = float(input(" What is the thickness of the Material?"))#12  # inches
    wood_absorption_coefficient = random.randint(0.05,0.10)

# Calculate sound level reduction due to distance
    distance_ratio = distance_from_lawnmower / 1  # Assuming lawnmower is at 0 distance
    sound_level_reduction = 6 * math.log2(distance_ratio)

    # Calculate additional sound level reduction due to absorption
    additional_sound_level_reduction = 10 * math.log10(1 - wood_absorption_coefficient)

    # Calculate total sound level reduction
    total_sound_level_reduction = sound_level_reduction + additional_sound_level_reduction

    # Calculate sound level at the wooden house
    sound_level_at_house = lawnmower_sound_level - total_sound_level_reduction

    print(f"The estimated sound level at the wooden house is approximately {sound_level_at_house:.2f} dB.")
    if sound_level_at_house <= 45:
        print (f" The noise cannot be heard ")
    else:
        print (" You could try adding some sound insulation materials to reduce the sound")
# wood_sim()


Test= input("Which Material do you want to test:\n Wood Glass or Concrete?").lower()
if Test== "wood":
    wood_sim()




