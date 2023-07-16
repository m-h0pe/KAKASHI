import math
import random
from Art import Logo

print(Logo)
# Parameters
try:
    lawnmower_sound_level =   float(input("What is your lawnmower/ SOURCE frequency in decibels")) # dB
except ValueError:
    print("Invalid Value")


def wood_sim():
    distance_from_lawnmower = float(input("How far is the material from the Source in metres?\n")) #20  # meters
    wooden_house_thickness = float(input(" What is the thickness of the Material?"))#12  # inches
    wood_absorption_coefficient = float(input(" pick from 0.05 to 0.10  for the Wood AbsorptioN Coefficient"))

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
        print(f" The noise  is not Audible enough, you are safe  ")
    else:
        print (" You could try adding some sound insulation materials to reduce the sound")     
    
def concrete_sim():
     distance_from_lawnmower = float(input("How far is the material from the Source in metres?\n")) #20  # meters
     Concrete_layer_thickness = float(input(f" What is the thickness of the {Test}?")) # inches
     Sound_Reduction_thickness= Concrete_layer_thickness* 2.667
     additional_sound_level_reduction = 10 * math.log10(distance_from_lawnmower)-11

     sound_level_at_house = lawnmower_sound_level - (Sound_Reduction_thickness+ additional_sound_level_reduction)

     print(f"The estimated sound level at the wooden house is approximately {sound_level_at_house:.2f} dB.")
     if sound_level_at_house <= 45:
        print (f" The noise  is not Audible enough, you are safe")
     else:
        print(" You could try adding some sound insulation materials to reduce the sound")     


def glass_sim():
    STC_Rating=int(input("What is the STC Rating of the Glass Material in Decibels"))

    sound_level_of_material = lawnmower_sound_level - STC_Rating
    if sound_level_of_material <= 45:
        print (f"The sound now heard is {sound_level_of_material} Db, You are safe ")
    else:
        print(f" The sound now heard is {sound_level_of_material} Db, You could try adding some sound insulation materials to reduce the sound")


Test= input("Which Material do you want to test:\n Wood Glass or Concrete?").lower()
if Test== "wood":
    wood_sim()
elif Test == "glass":
     glass_sim()
elif Test== "concrete":
     concrete_sim()





