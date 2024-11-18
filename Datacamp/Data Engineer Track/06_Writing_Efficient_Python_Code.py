# Databricks notebook source
# MAGIC %md
# MAGIC # Foundation for Efficiences

# COMMAND ----------

# MAGIC %md
# MAGIC Efficient **_Python_** code:
# MAGIC - Minimal completion time (fast runtime)
# MAGIC - Minimal resource consumption (small memory footprint)
# MAGIC - Focus on readability
# MAGIC - Using Python's construct as intended (i.e. _Pythonic_)
# MAGIC - Can reference to `"The Zen of Python by Tim Peters"`

# COMMAND ----------

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# COMMAND ----------

# Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# COMMAND ----------

# Better Pythonic approach
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# COMMAND ----------

# Best Pythonic approach --> list conprehensive
best_list = [name for name in names if len(name) >= 6]
print(best_list)

# COMMAND ----------

import this

# COMMAND ----------

# MAGIC %md
# MAGIC ## Built-ins

# COMMAND ----------

# DBTITLE 1,range()
# Create a range object that goes from 0 to 5
nums = range(0,6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)] #Thong: * = unpacking _range object_ into a list
print(nums_list2)

# COMMAND ----------

# DBTITLE 1,enumerate()
# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names, start = 1):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names, start = 1)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start = 1)]
print(indexed_names_unpack)

# COMMAND ----------

# DBTITLE 1,map()
# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

# COMMAND ----------

# MAGIC %md
# MAGIC ## The Power of Numpy Arrays
# MAGIC 1. Numpy Array is homogeneous = 1 datatype for all elements
# MAGIC 2. Numpy Array can be broadcasting = apply operation to all elements
# MAGIC 3. Numpy Array has boolean indexes

# COMMAND ----------

pip install numpy

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# DBTITLE 1,Working with Numpy Elements 1
import numpy as np

nums = [[1,2,3,4,5],[6,7,8,9,10]]
nums = np.array(nums)

print("Original Numpy Array")
print(nums)

# Print second row of nums
print("Second Row")
print(nums[1,:])

# Print all elements of nums that are greater than 3
print("Greater than 3 Elements")
print(nums[nums > 3])

# Double every element of nums
print("Double all Elements")
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums , with adding 1
print("Adding 1 to 3rd column")
nums[:,2] = nums[:,2] + 1
print(nums)

# COMMAND ----------

# DBTITLE 1,Working with Numpy Elements 2
def welcome_guest(guest_and_time):
    """
    Returns a welcome string for the guest_and_time tuple.
    
    Args:
        guest_and_time (tuple): The guest and time tuple to create
            a welcome string for.
            
    Returns:
        welcome_string (str): A string welcoming the guest to Festivus.
        'Welcome to Festivus {guest}... You're {time} min late.'
    
    """
    guest = guest_and_time[0]
    arrival_time = guest_and_time[1]
    welcome_string = "Welcome to Festivus {}... You're {} min late.".format(guest,arrival_time)
    return welcome_string

# COMMAND ----------

# Create a list of arrival times
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]
print(guest_arrivals)
print(type(guest_arrivals))

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

# COMMAND ----------

# MAGIC %md 
# MAGIC # Timing and Profilling Code

# COMMAND ----------

# MAGIC %md
# MAGIC ## Examining Runtime 
# MAGIC - ns = nanosecond = 10^-9
# MAGIC - µs (us) = microsecond = 10^-6
# MAGIC - ms = millisecond = 10^-3
# MAGIC - s = second = 10^0

# COMMAND ----------

# MAGIC %md
# MAGIC ### %timeit

# COMMAND ----------

# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(51)]
# print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
%timeit nums_unpack = [*range(51)]
# print(nums_unpack)

# COMMAND ----------

# MAGIC %md
# MAGIC ### formal name or literal syntax

# COMMAND ----------

# Create a list using the formal name
%timeit formal_list = list()
# print(formal_list)

# Create a list using the literal syntax
%timeit literal_list = []
# print(literal_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ### %%timeit

# COMMAND ----------

wts = [441.0, 65.0, 90.0, 441.0, 122.0, 88.0, 61.0, 81.0, 104.0, 108.0, 90.0, 90.0, 72.0, 169.0, 173.0, 101.0, 68.0, 57.0, 54.0, 83.0, 90.0, 122.0, 86.0, 358.0, 135.0, 106.0, 146.0, 63.0, 68.0, 57.0, 98.0, 270.0, 59.0, 50.0, 101.0, 68.0, 54.0, 81.0, 63.0, 67.0, 180.0, 77.0, 54.0, 57.0, 52.0, 61.0, 95.0, 79.0, 133.0, 63.0, 181.0, 68.0, 216.0, 135.0, 71.0, 54.0, 124.0, 155.0, 113.0, 95.0, 58.0, 54.0, 86.0, 90.0, 52.0, 92.0, 90.0, 59.0, 61.0, 104.0, 86.0, 88.0, 97.0, 68.0, 56.0, 77.0, 230.0, 495.0, 86.0, 55.0, 97.0, 110.0, 135.0, 61.0, 99.0, 52.0, 90.0, 59.0, 158.0, 74.0, 81.0, 108.0, 90.0, 116.0, 108.0, 74.0, 74.0, 86.0, 61.0, 61.0, 62.0, 97.0, 63.0, 81.0, 50.0, 55.0, 54.0, 86.0, 170.0, 70.0, 78.0, 225.0, 67.0, 79.0, 99.0, 104.0, 50.0, 173.0, 88.0, 68.0, 52.0, 90.0, 81.0, 817.0, 56.0, 135.0, 27.0, 52.0, 90.0, 95.0, 91.0, 178.0, 101.0, 95.0, 383.0, 90.0, 171.0, 187.0, 132.0, 89.0, 110.0, 81.0, 54.0, 63.0, 412.0, 104.0, 306.0, 56.0, 74.0, 59.0, 80.0, 65.0, 57.0, 203.0, 95.0, 106.0, 88.0, 96.0, 108.0, 50.0, 18.0, 56.0, 99.0, 56.0, 91.0, 81.0, 88.0, 86.0, 52.0, 81.0, 45.0, 92.0, 104.0, 167.0, 16.0, 81.0, 77.0, 86.0, 99.0, 630.0, 268.0, 50.0, 62.0, 90.0, 270.0, 115.0, 79.0, 88.0, 83.0, 77.0, 88.0, 79.0, 4.0, 95.0, 90.0, 79.0, 63.0, 79.0, 89.0, 104.0, 57.0, 61.0, 88.0, 54.0, 65.0, 81.0, 225.0, 158.0, 61.0, 81.0, 146.0, 83.0, 48.0, 18.0, 630.0, 77.0, 59.0, 58.0, 77.0, 119.0, 207.0, 65.0, 65.0, 81.0, 54.0, 79.0, 191.0, 79.0, 14.0, 77.0, 52.0, 55.0, 56.0, 113.0, 90.0, 88.0, 86.0, 49.0, 52.0, 855.0, 81.0, 104.0, 72.0, 356.0, 324.0, 203.0, 97.0, 99.0, 106.0, 18.0, 79.0, 58.0, 63.0, 59.0, 95.0, 54.0, 65.0, 95.0, 360.0, 230.0, 288.0, 236.0, 36.0, 191.0, 77.0, 79.0, 383.0, 86.0, 225.0, 90.0, 97.0, 52.0, 135.0, 56.0, 81.0, 110.0, 72.0, 59.0, 54.0, 140.0, 72.0, 90.0, 90.0, 86.0, 77.0, 101.0, 61.0, 81.0, 86.0, 128.0, 61.0, 338.0, 248.0, 90.0, 101.0, 59.0, 79.0, 79.0, 72.0, 70.0, 158.0, 61.0, 70.0, 79.0, 54.0, 125.0, 85.0, 101.0, 54.0, 83.0, 99.0, 88.0, 79.0, 83.0, 86.0, 293.0, 191.0, 65.0, 69.0, 405.0, 59.0, 117.0, 89.0, 79.0, 54.0, 52.0, 87.0, 80.0, 55.0, 50.0, 52.0, 81.0, 234.0, 86.0, 81.0, 70.0, 90.0, 74.0, 68.0, 83.0, 79.0, 56.0, 97.0, 50.0, 70.0, 117.0, 83.0, 81.0, 630.0, 56.0, 108.0, 146.0, 320.0, 85.0, 72.0, 79.0, 101.0, 56.0, 38.0, 25.0, 54.0, 104.0, 63.0, 171.0, 61.0, 203.0, 900.0, 63.0, 74.0, 113.0, 59.0, 310.0, 87.0, 149.0, 54.0, 50.0, 79.0, 88.0, 315.0, 153.0, 79.0, 52.0, 191.0, 101.0, 50.0, 92.0, 72.0, 52.0, 180.0, 49.0, 437.0, 65.0, 113.0, 405.0, 54.0, 56.0, 74.0, 59.0, 55.0, 58.0, 81.0, 83.0, 79.0, 71.0, 62.0, 63.0, 131.0, 91.0, 57.0, 77.0, 68.0, 77.0, 54.0, 101.0, 47.0, 74.0, 146.0, 99.0, 54.0, 443.0, 101.0, 225.0, 288.0, 143.0, 101.0, 74.0, 288.0, 158.0, 203.0, 81.0, 54.0, 76.0, 97.0, 81.0, 59.0, 86.0, 82.0, 105.0, 331.0, 58.0, 54.0, 56.0, 214.0, 79.0, 73.0, 117.0, 50.0, 334.0, 52.0, 71.0, 54.0, 41.0, 135.0, 135.0, 63.0, 79.0, 162.0, 95.0, 54.0, 108.0, 67.0, 158.0, 50.0, 65.0, 117.0, 39.0, 473.0, 135.0, 51.0, 171.0, 74.0, 117.0, 50.0, 61.0, 95.0, 83.0, 52.0, 17.0, 57.0, 81.0]

# COMMAND ----------

# MAGIC %%timeit
# MAGIC hero_wts_lbs = []
# MAGIC for wt in wts:
# MAGIC     hero_wts_lbs.append(wt * 2.20462)

# COMMAND ----------

# MAGIC %%timeit
# MAGIC wts_np = np.array(wts)
# MAGIC hero_wts_lbs_np = wts_np * 2.20462

# COMMAND ----------

# MAGIC %md
# MAGIC ## Code Profilling Runtime

# COMMAND ----------

# MAGIC %md
# MAGIC ### Code Profiling: Runtime
# MAGIC - Detailed stats on frequency and duration of function calls
# MAGIC - Line-by-line analyses
# MAGIC - Package: **`line_profiler`** and use **`%lprun`**

# COMMAND ----------

pip install line_profiler

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import numpy as np

heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([ 95.0, 101.0,  74.0])

# COMMAND ----------

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

# COMMAND ----------

# MAGIC %load_ext line_profiler
# MAGIC %lprun -f convert_units convert_units(heroes, hts, wts)

# COMMAND ----------

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

# COMMAND ----------

# MAGIC %reload_ext line_profiler
# MAGIC %lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Code Profiling for Memory Usage

# COMMAND ----------

# MAGIC %md
# MAGIC ### Code Profilling: Memory
# MAGIC We may
# MAGIC - Use method **`sys.getsizeof()`** to get sizre of individual object
# MAGIC
# MAGIC Or use other way:
# MAGIC - Detailed stats on memory comsumption
# MAGIC - Line-by-line analyses
# MAGIC - Package: **`memory_profiler`** and use **`%mprun`**
# MAGIC - Only read a function in a file, i.e. file .py 

# COMMAND ----------

pip install memory_profiler

# COMMAND ----------

pip install line_profiler

# COMMAND ----------

def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis

# COMMAND ----------

def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis

# COMMAND ----------

# #Thong: sample codes because cannot re-create data
# from bmi_lists import calc_bmi_lists

# %load_ext memory_profiler
# %mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)

# COMMAND ----------

# MAGIC %md
# MAGIC # Gaining Efficiencies

# COMMAND ----------

# MAGIC %md
# MAGIC ## Efficiently combining, counting and iterating

# COMMAND ----------

# MAGIC %md
# MAGIC - **Combining:** Instead of using **`enumerate()`** to combine 2 lists --> we use **`zip()`** which returns a tuple
# MAGIC - **Counting:** we use **`collections module`** for dict, list, set and tuple with Notable:
# MAGIC   - **`namedtuple()`**: tuple subclasses with named fields
# MAGIC   - **`deque()`**: list-like container with fast appends and pops
# MAGIC   - **`Counter()`**: dict for counting hashable object <--- Instead of loop and count for every element in the list
# MAGIC   - **`OrderedDict()`**: dict that retains order of entries
# MAGIC   - **`defaultdict()`**: dict that calls a fatory function to supply missing values
# MAGIC - **Iterating:** we use **`itertools module`** with Notable:
# MAGIC   - Infinite iterators: **`count`**, **`cycle`**, **`repeat`**
# MAGIC   - Finite iterators: **`accumulate`**, **`chain`**, **`zip_longest`**, etc.
# MAGIC   - Combination generators:: **`product`**, **`permutations`**, **`combinations`** <--- to efficiently yield Cartesian products, permutations and combination of objects

# COMMAND ----------

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola', 'Altaria', 'Amaura', 'Ambipom', 'Amoonguss', 'Ampharos', 'Anorith', 'Arbok', 'Arcanine', 'Arceus', 'Archen', 'Archeops', 'Ariados', 'Armaldo', 'Aromatisse', 'Aron', 'Articuno', 'Audino', 'Aurorus', 'Avalugg', 'Axew', 'Azelf', 'Azumarill', 'Azurill', 'Bagon', 'Baltoy', 'Banette', 'Barbaracle', 'Barboach', 'Basculin', 'Bastiodon', 'Bayleef', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem', 'Beldum', 'Bellossom', 'Bellsprout', 'Bergmite', 'Bibarel', 'Bidoof', 'Binacle', 'Bisharp', 'Blastoise', 'Blaziken', 'Blissey', 'Blitzle', 'Boldore', 'Bonsly', 'Bouffalant', 'Braixen', 'Braviary', 'Breloom', 'Bronzong', 'Bronzor', 'Budew', 'Buizel', 'Bulbasaur', 'Buneary', 'Bunnelby', 'Burmy', 'Butterfree', 'Cacnea', 'Cacturne', 'Camerupt', 'Carbink', 'Carnivine', 'Carracosta', 'Carvanha', 'Cascoon', 'Castform', 'Caterpie', 'Celebi', 'Chandelure', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Chatot', 'Cherrim', 'Cherubi', 'Chesnaught', 'Chespin', 'Chikorita', 'Chimchar', 'Chimecho', 'Chinchou', 'Chingling', 'Cinccino', 'Clamperl', 'Clauncher', 'Clawitzer', 'Claydol', 'Clefable', 'Clefairy', 'Cleffa', 'Cloyster', 'Cobalion', 'Cofagrigus', 'Combee', 'Combusken', 'Conkeldurr', 'Corphish', 'Corsola', 'Cottonee', 'Cradily', 'Cranidos', 'Crawdaunt', 'Cresselia', 'Croagunk', 'Crobat', 'Croconaw', 'Crustle', 'Cryogonal', 'Cubchoo', 'Cubone', 'Cyndaquil', 'Darkrai', 'DarmanitanStandard Mode', 'DarmanitanZen Mode', 'Darumaka', 'Dedenne', 'Deerling', 'Deino', 'Delcatty', 'Delibird', 'Delphox', 'Dewgong', 'Dewott', 'Dialga', 'Diancie', 'Diggersby', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Donphan', 'Doublade', 'Dragalge', 'Dragonair', 'Dragonite', 'Drapion', 'Dratini', 'Drifblim', 'Drifloon', 'Drilbur', 'Drowzee', 'Druddigon', 'Ducklett', 'Dugtrio', 'Dunsparce', 'Duosion', 'Durant', 'Dusclops', 'Dusknoir', 'Duskull', 'Dustox', 'Dwebble', 'Eelektrik', 'Eelektross', 'Eevee', 'Ekans', 'Electabuzz', 'Electivire', 'Electrike', 'Electrode', 'Elekid', 'Elgyem', 'Emboar', 'Emolga', 'Empoleon', 'Entei', 'Escavalier', 'Espeon', 'Espurr', 'Excadrill', 'Exeggcute', 'Exeggutor', 'Exploud', "Farfetch'd", 'Fearow', 'Feebas', 'Fennekin', 'Feraligatr', 'Ferroseed', 'Ferrothorn', 'Finneon', 'Flaaffy', 'Flabébé', 'Flareon', 'Fletchinder', 'Fletchling', 'Floatzel', 'Floette', 'Florges', 'Flygon', 'Foongus', 'Forretress', 'Fraxure', 'Frillish', 'Froakie', 'Frogadier', 'Froslass', 'Furfrou', 'Furret', 'Gabite', 'Gallade', 'Galvantula', 'Garbodor', 'Garchomp', 'Gardevoir', 'Gastly', 'Gastrodon', 'Genesect', 'Gengar', 'Geodude', 'Gible', 'Gigalith', 'Girafarig', 'Glaceon', 'Glalie', 'Glameow', 'Gligar', 'Gliscor', 'Gloom', 'Gogoat', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Golett', 'Golurk', 'Goodra', 'Goomy', 'Gorebyss', 'Gothita', 'Gothitelle', 'Gothorita', 'Granbull', 'Graveler', 'Greninja', 'Grimer', 'Grotle', 'Groudon', 'GroudonPrimal Groudon', 'Grovyle', 'Growlithe', 'Grumpig', 'Gulpin', 'Gurdurr', 'Gyarados', 'Happiny', 'Hariyama', 'Haunter', 'Hawlucha', 'Haxorus', 'Heatmor', 'Heatran', 'Heliolisk', 'Helioptile', 'Heracross', 'Herdier', 'Hippopotas', 'Hippowdon', 'Hitmonchan', 'Hitmonlee', 'Hitmontop', 'Ho-oh', 'Honchkrow', 'Honedge', 'Hoothoot', 'Hoppip', 'Horsea', 'Houndoom', 'Houndour', 'Huntail', 'Hydreigon', 'Hypno', 'Igglybuff', 'Illumise', 'Infernape', 'Inkay', 'Ivysaur', 'Jellicent', 'Jigglypuff', 'Jirachi', 'Jolteon', 'Joltik', 'Jumpluff', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Karrablast', 'Kecleon', 'Kingdra', 'Kingler', 'Kirlia', 'Klang', 'Klefki', 'Klink', 'Klinklang', 'Koffing', 'Krabby', 'Kricketot', 'Kricketune', 'Krokorok', 'Krookodile', 'Kyogre', 'KyogrePrimal Kyogre', 'Kyurem', 'KyuremBlack Kyurem', 'KyuremWhite Kyurem', 'Lairon', 'Lampent', 'Lanturn', 'Lapras', 'Larvesta', 'Larvitar', 'Latias', 'Latios', 'Leafeon', 'Leavanny', 'Ledian', 'Ledyba', 'Lickilicky', 'Lickitung', 'Liepard', 'Lileep', 'Lilligant', 'Lillipup', 'Linoone', 'Litleo', 'Litwick', 'Lombre', 'Lopunny', 'Lotad', 'Loudred', 'Lucario', 'Ludicolo', 'Lugia', 'Lumineon', 'Lunatone', 'Luvdisc', 'Luxio', 'Luxray', 'Machamp', 'Machoke', 'Machop', 'Magby', 'Magcargo', 'Magikarp', 'Magmar', 'Magmortar', 'Magnemite', 'Magneton', 'Magnezone', 'Makuhita', 'Malamar', 'Mamoswine', 'Manaphy', 'Mandibuzz', 'Manectric', 'Mankey', 'Mantine', 'Mantyke', 'Maractus', 'Mareep', 'Marill', 'Marowak', 'Marshtomp', 'Masquerain', 'Mawile', 'Medicham', 'Meditite', 'MeowsticFemale', 'MeowsticMale', 'Meowth', 'Mesprit', 'Metagross', 'Metang', 'Metapod', 'Mew', 'Mewtwo', 'Mienfoo', 'Mienshao', 'Mightyena', 'Milotic', 'Miltank', 'Mime Jr.', 'Minccino', 'Minun', 'Misdreavus', 'Mismagius', 'Moltres', 'Monferno', 'Mothim', 'Mr. Mime', 'Mudkip', 'Muk', 'Munchlax', 'Munna', 'Murkrow', 'Musharna', 'Natu', 'Nidoking', 'Nidoqueen', 'Nidoran♀', 'Nidoran♂', 'Nidorina', 'Nidorino', 'Nincada', 'Ninetales', 'Ninjask', 'Noctowl', 'Noibat', 'Noivern', 'Nosepass', 'Numel', 'Nuzleaf', 'Octillery', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Oshawott', 'Pachirisu', 'Palkia', 'Palpitoad', 'Pancham', 'Pangoro', 'Panpour', 'Pansage', 'Pansear', 'Paras', 'Parasect', 'Patrat', 'Pawniard', 'Pelipper', 'Persian', 'Petilil', 'Phanpy', 'Phantump', 'Phione', 'Pichu', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pidove', 'Pignite', 'Pikachu', 'Piloswine', 'Pineco', 'Pinsir', 'Piplup', 'Plusle', 'Politoed', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Poochyena', 'Porygon', 'Porygon-Z', 'Porygon2', 'Primeape', 'Prinplup', 'Probopass', 'Psyduck', 'Pupitar', 'Purrloin', 'Purugly', 'Pyroar', 'Quagsire', 'Quilava', 'Quilladin', 'Qwilfish', 'Raichu', 'Raikou', 'Ralts', 'Rampardos', 'Rapidash', 'Raticate', 'Rattata', 'Rayquaza', 'Regice', 'Regigigas', 'Regirock', 'Registeel', 'Relicanth', 'Remoraid', 'Reshiram', 'Reuniclus', 'Rhydon', 'Rhyhorn', 'Rhyperior', 'Riolu', 'Roggenrola', 'Roselia', 'Roserade', 'Rotom', 'RotomFan Rotom', 'RotomFrost Rotom', 'RotomHeat Rotom', 'RotomMow Rotom', 'RotomWash Rotom', 'Rufflet', 'Sableye', 'Salamence', 'Samurott', 'Sandile', 'Sandshrew', 'Sandslash', 'Sawk', 'Sawsbuck', 'Scatterbug', 'Sceptile', 'Scizor', 'Scolipede', 'Scrafty', 'Scraggy', 'Scyther', 'Seadra', 'Seaking', 'Sealeo', 'Seedot', 'Seel', 'Seismitoad', 'Sentret', 'Serperior', 'Servine', 'Seviper', 'Sewaddle', 'Sharpedo', 'Shedinja', 'Shelgon', 'Shellder', 'Shellos', 'Shelmet', 'Shieldon', 'Shiftry', 'Shinx', 'Shroomish', 'Shuckle', 'Shuppet', 'Sigilyph', 'Silcoon', 'Simipour', 'Simisage', 'Simisear', 'Skarmory', 'Skiddo', 'Skiploom', 'Skitty', 'Skorupi', 'Skrelp', 'Skuntank', 'Slaking', 'Slakoth', 'Sliggoo', 'Slowbro', 'Slowking', 'Slowpoke', 'Slugma', 'Slurpuff', 'Smeargle', 'Smoochum', 'Sneasel', 'Snivy', 'Snorlax', 'Snorunt', 'Snover', 'Snubbull', 'Solosis', 'Solrock', 'Spearow', 'Spewpa', 'Spheal', 'Spinarak', 'Spinda', 'Spiritomb', 'Spoink', 'Spritzee', 'Squirtle', 'Stantler', 'Staraptor', 'Staravia', 'Starly', 'Starmie', 'Staryu', 'Steelix', 'Stoutland', 'Stunfisk', 'Stunky', 'Sudowoodo', 'Suicune', 'Sunflora', 'Sunkern', 'Surskit', 'Swablu', 'Swadloon', 'Swalot', 'Swampert', 'Swanna', 'Swellow', 'Swinub', 'Swirlix', 'Swoobat', 'Sylveon', 'Taillow', 'Talonflame', 'Tangela', 'Tangrowth', 'Tauros', 'Teddiursa', 'Tentacool', 'Tentacruel', 'Tepig', 'Terrakion', 'Throh', 'Timburr', 'Tirtouga', 'Togekiss', 'Togepi', 'Togetic', 'Torchic', 'Torkoal', 'Torterra', 'Totodile', 'Toxicroak', 'Tranquill', 'Trapinch', 'Treecko', 'Trevenant', 'Tropius', 'Trubbish', 'Turtwig', 'Tympole', 'Tynamo', 'Typhlosion', 'Tyranitar', 'Tyrantrum', 'Tyrogue', 'Tyrunt', 'Umbreon', 'Unfezant', 'Unown', 'Ursaring', 'Uxie', 'Vanillish', 'Vanillite', 'Vanilluxe', 'Vaporeon', 'Venipede', 'Venomoth', 'Venonat', 'Venusaur', 'Vespiquen', 'Vibrava', 'Victini', 'Victreebel', 'Vigoroth', 'Vileplume', 'Virizion', 'Vivillon', 'Volbeat', 'Volcanion', 'Volcarona', 'Voltorb', 'Vullaby', 'Vulpix', 'Wailmer', 'Wailord', 'Walrein', 'Wartortle', 'Watchog', 'Weavile', 'Weedle', 'Weepinbell', 'Weezing', 'Whimsicott', 'Whirlipede', 'Whiscash', 'Whismur', 'Wigglytuff', 'Wingull', 'Wobbuffet', 'Woobat', 'Wooper', 'WormadamPlant Cloak', 'WormadamSandy Cloak', 'WormadamTrash Cloak', 'Wurmple', 'Wynaut', 'Xatu', 'Xerneas', 'Yamask', 'Yanma', 'Yanmega', 'Yveltal', 'Zangoose', 'Zapdos', 'Zebstrika', 'Zekrom', 'Zigzagoon', 'Zoroark', 'Zorua', 'Zubat', 'Zweilous']

# COMMAND ----------

primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock', 'Steel', 'Normal', 'Psychic', 'Water', 'Dragon', 'Rock', 'Normal', 'Grass', 'Electric', 'Rock', 'Poison', 'Fire', 'Normal', 'Rock', 'Rock', 'Bug', 'Rock', 'Fairy', 'Steel', 'Ice', 'Normal', 'Rock', 'Ice', 'Dragon', 'Psychic', 'Water', 'Normal', 'Dragon', 'Ground', 'Ghost', 'Rock', 'Water', 'Water', 'Rock', 'Grass', 'Ice', 'Bug', 'Bug', 'Psychic', 'Steel', 'Grass', 'Grass', 'Ice', 'Normal', 'Normal', 'Rock', 'Dark', 'Water', 'Fire', 'Normal', 'Electric', 'Rock', 'Rock', 'Normal', 'Fire', 'Normal', 'Grass', 'Steel', 'Steel', 'Grass', 'Water', 'Grass', 'Normal', 'Normal', 'Bug', 'Bug', 'Grass', 'Grass', 'Fire', 'Rock', 'Grass', 'Water', 'Water', 'Bug', 'Normal', 'Bug', 'Psychic', 'Ghost', 'Normal', 'Fire', 'Fire', 'Fire', 'Normal', 'Grass', 'Grass', 'Grass', 'Grass', 'Grass', 'Fire', 'Psychic', 'Water', 'Psychic', 'Normal', 'Water', 'Water', 'Water', 'Ground', 'Fairy', 'Fairy', 'Fairy', 'Water', 'Steel', 'Ghost', 'Bug', 'Fire', 'Fighting', 'Water', 'Water', 'Grass', 'Rock', 'Rock', 'Water', 'Psychic', 'Poison', 'Poison', 'Water', 'Bug', 'Ice', 'Ice', 'Ground', 'Fire', 'Dark', 'Fire', 'Fire', 'Fire', 'Electric', 'Normal', 'Dark', 'Normal', 'Ice', 'Fire', 'Water', 'Water', 'Steel', 'Rock', 'Normal', 'Ground', 'Normal', 'Normal', 'Normal', 'Ground', 'Steel', 'Poison', 'Dragon', 'Dragon', 'Poison', 'Dragon', 'Ghost', 'Ghost', 'Ground', 'Psychic', 'Dragon', 'Water', 'Ground', 'Normal', 'Psychic', 'Bug', 'Ghost', 'Ghost', 'Ghost', 'Bug', 'Bug', 'Electric', 'Electric', 'Normal', 'Poison', 'Electric', 'Electric', 'Electric', 'Electric', 'Electric', 'Psychic', 'Fire', 'Electric', 'Water', 'Fire', 'Bug', 'Psychic', 'Psychic', 'Ground', 'Grass', 'Grass', 'Normal', 'Normal', 'Normal', 'Water', 'Fire', 'Water', 'Grass', 'Grass', 'Water', 'Electric', 'Fairy', 'Fire', 'Fire', 'Normal', 'Water', 'Fairy', 'Fairy', 'Ground', 'Grass', 'Bug', 'Dragon', 'Water', 'Water', 'Water', 'Ice', 'Normal', 'Normal', 'Dragon', 'Psychic', 'Bug', 'Poison', 'Dragon', 'Psychic', 'Ghost', 'Water', 'Bug', 'Ghost', 'Rock', 'Dragon', 'Rock', 'Normal', 'Ice', 'Ice', 'Normal', 'Ground', 'Ground', 'Grass', 'Grass', 'Poison', 'Water', 'Water', 'Rock', 'Ground', 'Ground', 'Dragon', 'Dragon', 'Water', 'Psychic', 'Psychic', 'Psychic', 'Fairy', 'Rock', 'Water', 'Poison', 'Grass', 'Ground', 'Ground', 'Grass', 'Fire', 'Psychic', 'Poison', 'Fighting', 'Water', 'Normal', 'Fighting', 'Ghost', 'Fighting', 'Dragon', 'Fire', 'Fire', 'Electric', 'Electric', 'Bug', 'Normal', 'Ground', 'Ground', 'Fighting', 'Fighting', 'Fighting', 'Fire', 'Dark', 'Steel', 'Normal', 'Grass', 'Water', 'Dark', 'Dark', 'Water', 'Dark', 'Psychic', 'Normal', 'Bug', 'Fire', 'Dark', 'Grass', 'Water', 'Normal', 'Steel', 'Electric', 'Bug', 'Grass', 'Ice', 'Rock', 'Rock', 'Psychic', 'Bug', 'Normal', 'Bug', 'Normal', 'Water', 'Water', 'Psychic', 'Steel', 'Steel', 'Steel', 'Steel', 'Poison', 'Water', 'Bug', 'Bug', 'Ground', 'Ground', 'Water', 'Water', 'Dragon', 'Dragon', 'Dragon', 'Steel', 'Ghost', 'Water', 'Water', 'Bug', 'Rock', 'Dragon', 'Dragon', 'Grass', 'Bug', 'Bug', 'Bug', 'Normal', 'Normal', 'Dark', 'Rock', 'Grass', 'Normal', 'Normal', 'Fire', 'Ghost', 'Water', 'Normal', 'Water', 'Normal', 'Fighting', 'Water', 'Psychic', 'Water', 'Rock', 'Water', 'Electric', 'Electric', 'Fighting', 'Fighting', 'Fighting', 'Fire', 'Fire', 'Water', 'Fire', 'Fire', 'Electric', 'Electric', 'Electric', 'Fighting', 'Dark', 'Ice', 'Water', 'Dark', 'Electric', 'Fighting', 'Water', 'Water', 'Grass', 'Electric', 'Water', 'Ground', 'Water', 'Bug', 'Steel', 'Fighting', 'Fighting', 'Psychic', 'Psychic', 'Normal', 'Psychic', 'Steel', 'Steel', 'Bug', 'Psychic', 'Psychic', 'Fighting', 'Fighting', 'Dark', 'Water', 'Normal', 'Psychic', 'Normal', 'Electric', 'Ghost', 'Ghost', 'Fire', 'Fire', 'Bug', 'Psychic', 'Water', 'Poison', 'Normal', 'Psychic', 'Dark', 'Psychic', 'Psychic', 'Poison', 'Poison', 'Poison', 'Poison', 'Poison', 'Poison', 'Bug', 'Fire', 'Bug', 'Normal', 'Flying', 'Flying', 'Rock', 'Fire', 'Grass', 'Water', 'Grass', 'Rock', 'Rock', 'Rock', 'Water', 'Electric', 'Water', 'Water', 'Fighting', 'Fighting', 'Water', 'Grass', 'Fire', 'Bug', 'Bug', 'Normal', 'Dark', 'Water', 'Normal', 'Grass', 'Ground', 'Ghost', 'Water', 'Electric', 'Normal', 'Normal', 'Normal', 'Normal', 'Fire', 'Electric', 'Ice', 'Bug', 'Bug', 'Water', 'Electric', 'Water', 'Water', 'Water', 'Water', 'Fire', 'Dark', 'Normal', 'Normal', 'Normal', 'Fighting', 'Water', 'Rock', 'Water', 'Rock', 'Dark', 'Normal', 'Fire', 'Water', 'Fire', 'Grass', 'Water', 'Electric', 'Electric', 'Psychic', 'Rock', 'Fire', 'Normal', 'Normal', 'Dragon', 'Ice', 'Normal', 'Rock', 'Steel', 'Water', 'Water', 'Dragon', 'Psychic', 'Ground', 'Ground', 'Ground', 'Fighting', 'Rock', 'Grass', 'Grass', 'Electric', 'Electric', 'Electric', 'Electric', 'Electric', 'Electric', 'Normal', 'Dark', 'Dragon', 'Water', 'Ground', 'Ground', 'Ground', 'Fighting', 'Normal', 'Bug', 'Grass', 'Bug', 'Bug', 'Dark', 'Dark', 'Bug', 'Water', 'Water', 'Ice', 'Grass', 'Water', 'Water', 'Normal', 'Grass', 'Grass', 'Poison', 'Bug', 'Water', 'Bug', 'Dragon', 'Water', 'Water', 'Bug', 'Rock', 'Grass', 'Electric', 'Grass', 'Bug', 'Ghost', 'Psychic', 'Bug', 'Water', 'Grass', 'Fire', 'Steel', 'Grass', 'Grass', 'Normal', 'Poison', 'Poison', 'Poison', 'Normal', 'Normal', 'Dragon', 'Water', 'Water', 'Water', 'Fire', 'Fairy', 'Normal', 'Ice', 'Dark', 'Grass', 'Normal', 'Ice', 'Grass', 'Fairy', 'Psychic', 'Rock', 'Normal', 'Bug', 'Ice', 'Bug', 'Normal', 'Ghost', 'Psychic', 'Fairy', 'Water', 'Normal', 'Normal', 'Normal', 'Normal', 'Water', 'Water', 'Steel', 'Normal', 'Ground', 'Poison', 'Rock', 'Water', 'Grass', 'Grass', 'Bug', 'Normal', 'Bug', 'Poison', 'Water', 'Water', 'Normal', 'Ice', 'Fairy', 'Psychic', 'Fairy', 'Normal', 'Fire', 'Grass', 'Grass', 'Normal', 'Normal', 'Water', 'Water', 'Fire', 'Rock', 'Fighting', 'Fighting', 'Water', 'Fairy', 'Fairy', 'Fairy', 'Fire', 'Fire', 'Grass', 'Water', 'Poison', 'Normal', 'Ground', 'Grass', 'Ghost', 'Grass', 'Poison', 'Grass', 'Water', 'Electric', 'Fire', 'Rock', 'Rock', 'Fighting', 'Rock', 'Dark', 'Normal', 'Psychic', 'Normal', 'Psychic', 'Ice', 'Ice', 'Ice', 'Water', 'Bug', 'Bug', 'Bug', 'Grass', 'Bug', 'Ground', 'Psychic', 'Grass', 'Normal', 'Grass', 'Grass', 'Bug', 'Bug', 'Fire', 'Bug', 'Electric', 'Dark', 'Fire', 'Water', 'Water', 'Ice', 'Water', 'Normal', 'Dark', 'Bug', 'Grass', 'Poison', 'Grass', 'Bug', 'Water', 'Normal', 'Normal', 'Water', 'Psychic', 'Psychic', 'Water', 'Bug', 'Bug', 'Bug', 'Bug', 'Psychic', 'Psychic', 'Fairy', 'Ghost', 'Bug', 'Bug', 'Dark', 'Normal', 'Electric', 'Electric', 'Dragon', 'Normal', 'Dark', 'Dark', 'Poison', 'Dark']

# COMMAND ----------

secondary_types = ['Ice', 'nan', 'nan', 'nan', 'Flying', 'Rock', 'nan', 'nan', 'nan', 'Flying', 'Ice', 'nan', 'Poison', 'nan', 'Bug', 'nan', 'nan', 'nan', 'Flying', 'Flying', 'Poison', 'Bug', 'nan', 'Rock', 'Flying', 'nan', 'Ice', 'nan', 'nan', 'nan', 'Fairy', 'Fairy', 'nan', 'Psychic', 'nan', 'Water', 'Ground', 'nan', 'Steel', 'nan', 'nan', 'Flying', 'Poison', 'nan', 'Psychic', 'nan', 'Poison', 'nan', 'Water', 'nan', 'Water', 'Steel', 'nan', 'Fighting', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Flying', 'Fighting', 'Psychic', 'Psychic', 'Poison', 'nan', 'Poison', 'nan', 'nan', 'nan', 'Flying', 'nan', 'Dark', 'Ground', 'Fairy', 'nan', 'Rock', 'Dark', 'nan', 'nan', 'nan', 'Grass', 'Fire', 'nan', 'Flying', 'nan', 'nan', 'Flying', 'nan', 'nan', 'Fighting', 'nan', 'nan', 'nan', 'nan', 'Electric', 'nan', 'nan', 'nan', 'nan', 'nan', 'Psychic', 'nan', 'nan', 'nan', 'Ice', 'Fighting', 'nan', 'Flying', 'Fighting', 'nan', 'nan', 'Rock', 'Fairy', 'Grass', 'nan', 'Dark', 'nan', 'Fighting', 'Flying', 'nan', 'Rock', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Psychic', 'nan', 'Fairy', 'Grass', 'Dragon', 'nan', 'Flying', 'Psychic', 'Ice', 'nan', 'Dragon', 'Fairy', 'Ground', 'nan', 'nan', 'Flying', 'Flying', 'nan', 'Ghost', 'Dragon', 'nan', 'Flying', 'Dark', 'nan', 'Flying', 'Flying', 'nan', 'nan', 'nan', 'Flying', 'nan', 'nan', 'nan', 'Steel', 'nan', 'nan', 'nan', 'Poison', 'Rock', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Fighting', 'Flying', 'Steel', 'nan', 'Steel', 'nan', 'nan', 'Steel', 'Psychic', 'Psychic', 'nan', 'Flying', 'Flying', 'nan', 'nan', 'nan', 'Steel', 'Steel', 'nan', 'nan', 'nan', 'nan', 'Flying', 'Flying', 'nan', 'nan', 'nan', 'Dragon', 'Poison', 'Steel', 'nan', 'Ghost', 'nan', 'nan', 'Ghost', 'nan', 'nan', 'Ground', 'Fighting', 'Electric', 'nan', 'Ground', 'Fairy', 'Poison', 'Ground', 'Steel', 'Poison', 'Ground', 'Ground', 'nan', 'Psychic', 'nan', 'nan', 'nan', 'Flying', 'Flying', 'Poison', 'nan', 'Flying', 'nan', 'nan', 'Ground', 'Ghost', 'Ghost', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Ground', 'Dark', 'nan', 'nan', 'nan', 'Fire', 'nan', 'nan', 'nan', 'nan', 'nan', 'Flying', 'nan', 'nan', 'Poison', 'Flying', 'nan', 'nan', 'Steel', 'Normal', 'Normal', 'Fighting', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Flying', 'Flying', 'Ghost', 'Flying', 'Flying', 'nan', 'Fire', 'Fire', 'nan', 'Dragon', 'nan', 'Fairy', 'nan', 'Fighting', 'Psychic', 'Poison', 'Ghost', 'Fairy', 'Psychic', 'nan', 'Electric', 'Flying', 'Psychic', 'Water', 'Water', 'nan', 'Poison', 'nan', 'nan', 'nan', 'Dragon', 'nan', 'Fairy', 'nan', 'Fairy', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Dark', 'Dark', 'nan', 'nan', 'Ice', 'Ice', 'Ice', 'Rock', 'Fire', 'Electric', 'Ice', 'Fire', 'Ground', 'Psychic', 'Psychic', 'nan', 'Grass', 'Flying', 'Flying', 'nan', 'nan', 'nan', 'Grass', 'nan', 'nan', 'nan', 'Normal', 'Fire', 'Grass', 'nan', 'Grass', 'nan', 'Steel', 'Grass', 'Flying', 'nan', 'Psychic', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Rock', 'nan', 'nan', 'nan', 'Steel', 'Steel', 'Steel', 'nan', 'Psychic', 'Ground', 'nan', 'Flying', 'nan', 'nan', 'Flying', 'Flying', 'nan', 'nan', 'Fairy', 'nan', 'Ground', 'Flying', 'Fairy', 'Psychic', 'Psychic', 'nan', 'nan', 'nan', 'nan', 'Psychic', 'Psychic', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Fairy', 'nan', 'nan', 'nan', 'nan', 'Flying', 'Fighting', 'Flying', 'Fairy', 'nan', 'nan', 'nan', 'nan', 'Flying', 'nan', 'Flying', 'Ground', 'Ground', 'nan', 'nan', 'nan', 'nan', 'Ground', 'nan', 'Flying', 'Flying', 'Dragon', 'Dragon', 'nan', 'Ground', 'Dark', 'nan', 'Poison', 'Water', 'Water', 'Ground', 'nan', 'nan', 'Dragon', 'Ground', 'nan', 'Dark', 'nan', 'nan', 'nan', 'Grass', 'Grass', 'nan', 'Steel', 'Flying', 'nan', 'nan', 'nan', 'Grass', 'nan', 'nan', 'Flying', 'Flying', 'Flying', 'Flying', 'Fighting', 'nan', 'Ground', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Fighting', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Steel', 'nan', 'Ground', 'nan', 'nan', 'Normal', 'Ground', 'nan', 'nan', 'Poison', 'nan', 'nan', 'Fairy', 'nan', 'nan', 'nan', 'nan', 'Flying', 'nan', 'nan', 'nan', 'nan', 'Rock', 'nan', 'Fire', 'nan', 'Rock', 'Rock', 'Rock', 'nan', 'nan', 'Poison', 'Poison', 'Ghost', 'Flying', 'Ice', 'Fire', 'Grass', 'Water', 'Flying', 'Ghost', 'Flying', 'nan', 'Dark', 'nan', 'nan', 'nan', 'Grass', 'nan', 'nan', 'Steel', 'Poison', 'Fighting', 'Fighting', 'Flying', 'nan', 'nan', 'Water', 'nan', 'nan', 'Ground', 'nan', 'nan', 'nan', 'nan', 'Grass', 'Dark', 'Ghost', 'nan', 'nan', 'nan', 'nan', 'Steel', 'Dark', 'nan', 'nan', 'Rock', 'nan', 'Flying', 'nan', 'nan', 'nan', 'nan', 'Flying', 'nan', 'Flying', 'nan', 'Bug', 'Water', 'Dark', 'nan', 'nan', 'nan', 'Psychic', 'Psychic', 'Psychic', 'nan', 'nan', 'nan', 'Psychic', 'Ice', 'nan', 'nan', 'nan', 'Ice', 'nan', 'nan', 'Psychic', 'Flying', 'nan', 'Water', 'Poison', 'nan', 'Dark', 'nan', 'nan', 'nan', 'nan', 'Flying', 'Flying', 'Flying', 'Psychic', 'nan', 'Ground', 'nan', 'Electric', 'Dark', 'nan', 'nan', 'nan', 'nan', 'Water', 'Flying', 'Grass', 'nan', 'Ground', 'Flying', 'Flying', 'Ground', 'nan', 'Flying', 'nan', 'Flying', 'Flying', 'nan', 'nan', 'nan', 'nan', 'Poison', 'Poison', 'nan', 'Fighting', 'nan', 'nan', 'Rock', 'Flying', 'nan', 'Flying', 'nan', 'nan', 'Ground', 'nan', 'Fighting', 'Flying', 'nan', 'nan', 'Grass', 'Flying', 'nan', 'nan', 'nan', 'nan', 'nan', 'Dark', 'Dragon', 'nan', 'Dragon', 'nan', 'Flying', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'nan', 'Poison', 'Poison', 'Poison', 'Poison', 'Flying', 'Dragon', 'Fire', 'Poison', 'nan', 'Poison', 'Fighting', 'Flying', 'nan', 'Water', 'Fire', 'nan', 'Flying', 'nan', 'nan', 'nan', 'Water', 'nan', 'nan', 'Ice', 'Poison', 'Poison', 'nan', 'Fairy', 'Poison', 'Ground', 'nan', 'Fairy', 'Flying', 'nan', 'Flying', 'Ground', 'Grass', 'Ground', 'Steel', 'nan', 'nan', 'Flying', 'nan', 'nan', 'Flying', 'Flying', 'Flying', 'nan', 'Flying', 'nan', 'Electric', 'nan', 'nan', 'nan', 'Flying', 'Dragon']

# COMMAND ----------

generations = [1, 1, 1, 5, 3, 5, 1, 6, 1, 6, 5, 5, 4, 6, 3, 4, 2, 5, 2, 5, 4, 1, 1, 2, 6, 5, 5, 6, 6, 1, 4, 5, 6, 2, 6, 1, 3, 2, 4, 1, 5, 3, 5, 5, 1, 5, 5, 5, 5, 6, 1, 3, 4, 6, 1, 4, 5, 3, 5, 5, 1, 4, 1, 1, 5, 6, 5, 1, 1, 6, 5, 5, 4, 6, 1, 1, 4, 5, 4, 5, 6, 2, 3, 5, 6, 5, 3, 4, 5, 1, 5, 6, 1, 1, 2, 3, 3, 3, 4, 4, 1, 3, 6, 3, 5, 3, 5, 3, 3, 1, 3, 6, 4, 4, 4, 5, 3, 4, 4, 3, 5, 5, 3, 5, 4, 1, 1, 3, 5, 3, 2, 5, 4, 3, 2, 4, 3, 5, 3, 1, 2, 4, 3, 5, 3, 5, 4, 1, 2, 4, 3, 5, 5, 1, 4, 6, 3, 6, 3, 4, 1, 5, 6, 1, 5, 4, 4, 3, 3, 5, 2, 3, 1, 6, 5, 1, 5, 4, 3, 6, 1, 3, 3, 6, 4, 3, 5, 4, 2, 4, 4, 1, 2, 5, 1, 3, 6, 4, 1, 1, 1, 1, 2, 4, 1, 1, 4, 4, 5, 3, 1, 4, 5, 3, 4, 1, 3, 4, 2, 5, 3, 4, 1, 1, 1, 5, 1, 4, 4, 3, 4, 3, 5, 3, 2, 3, 3, 3, 2, 4, 1, 3, 4, 2, 6, 5, 2, 5, 5, 1, 1, 1, 5, 4, 2, 4, 2, 2, 5, 5, 5, 4, 2, 3, 3, 5, 4, 5, 6, 3, 1, 2, 4, 2, 5, 1, 4, 3, 1, 1, 1, 1, 3, 5, 1, 3, 3, 3, 3, 5, 2, 5, 4, 2, 2, 3, 6, 4, 2, 1, 2, 5, 5, 3, 1, 3, 5, 5, 5, 5, 6, 5, 1, 5, 1, 5, 5, 1, 6, 4, 3, 1, 6, 5, 1, 4, 6, 5, 1, 2, 5, 5, 3, 1, 5, 5, 3, 3, 3, 6, 1, 5, 1, 3, 3, 4, 5, 3, 1, 1, 1, 6, 3, 3, 4, 5, 3, 5, 4, 5, 1, 5, 5, 3, 5, 6, 5, 4, 5, 6, 1, 1, 4, 1, 3, 4, 1, 4, 1, 1, 5, 4, 4, 5, 5, 6, 1, 1, 2, 4, 2, 5, 2, 5, 5, 6, 1, 3, 3, 5, 6, 4, 3, 3, 1, 5, 5, 2, 3, 5, 3, 6, 3, 5, 2, 1, 2, 5, 2, 3, 3, 1, 3, 1, 1, 4, 3, 1, 3, 5, 1, 3, 6, 4, 5, 2, 2, 6, 2, 2, 5, 6, 2, 1, 3, 5, 3, 3, 5, 5, 5, 3, 5, 2, 2, 4, 4, 3, 5, 6, 1, 4, 1, 1, 4, 2, 3, 4, 5, 2, 4, 3, 3, 4, 3, 3, 3, 3, 1, 2, 3, 5, 5, 6, 4, 3, 5, 5, 5, 6, 1, 2, 3, 1, 5, 6, 2, 1, 3, 5]

# COMMAND ----------

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# COMMAND ----------

# MAGIC %md
# MAGIC ### Combine with zip()

# COMMAND ----------

# Combine all three lists together
names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# COMMAND ----------

# Combine all two lists together
names_types = [*zip(names, primary_types)]

print(*names_types[:5], sep='\n')

# COMMAND ----------

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:], primary_types[0:3])]

print(*differing_lengths, sep='\n') #Thong: it returns number of combination with the smallest number of elelemts

# COMMAND ----------

# MAGIC %md
# MAGIC ### Count with collections.Counter()

# COMMAND ----------

from collections import Counter

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Combine with itertools.combinations()

# COMMAND ----------

# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Set Theory
# MAGIC - Branch of Mathematics applied to collections of objects
# MAGIC     - i.e. **`sets`**
# MAGIC - Python has buit-in **`set`** datatype with accompaying methods:
# MAGIC     - **`intersection()`**: all elements that are in both sets
# MAGIC     - **`difference()`**: all elements in 1 set but not the other
# MAGIC     - **`symemetric_difference()`**: all elements in exactly 1 set
# MAGIC     - **`union()`**: all elements that are in either set
# MAGIC - Fast memebership testing:
# MAGIC     - Check if a value exists in a sequence or not
# MAGIC     - Using the **`in`** operator
# MAGIC
# MAGIC --> set {} is significantly faster than list [] or tuple ()

# COMMAND ----------

ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']
brock_pokedex = ['Dugtrio', 'Tauros', 'Kabutops', 'Machop', 'Omastar', 'Zubat', 'Golem', 'Onix', 'Vulpix', 'Geodude']

# COMMAND ----------

# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Compare running time list vs. set

# COMMAND ----------

brock_pokedex_set = set(brock_pokedex)

%timeit 'Psyduck' in ash_pokedex
%timeit 'Psyduck' in brock_pokedex_set

%timeit 'Machop' in ash_pokedex
%timeit 'Machop' in brock_pokedex_set

#Thong: member testing using set is faster than list

# COMMAND ----------

# MAGIC %md
# MAGIC ### Compare running time function vs. set

# COMMAND ----------

def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques

# COMMAND ----------

# MAGIC %%timeit
# MAGIC # Use find_unique_items() to collect unique Pokémon names
# MAGIC uniq_names_func = find_unique_items(names)
# MAGIC # print(len(uniq_names_func))

# COMMAND ----------

# Convert the names list to a set to collect unique Pokémon names
%timeit uniq_names_set = set(names)
# print(len(uniq_names_set))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Eliminating Loops

# COMMAND ----------

poke_names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola', 'Altaria', 'Amaura', 'Ambipom', 'Amoonguss', 'Ampharos', 'Anorith', 'Arbok', 'Arcanine', 'Arceus', 'Archen', 'Archeops', 'Ariados', 'Armaldo', 'Aromatisse', 'Aron', 'Articuno', 'Audino', 'Aurorus', 'Avalugg', 'Axew', 'Azelf', 'Azumarill', 'Azurill', 'Bagon', 'Baltoy', 'Banette', 'Barbaracle', 'Barboach', 'Basculin', 'Bastiodon', 'Bayleef', 'Beartic', 'Beautifly', 'Beedrill', 'Beheeyem', 'Beldum', 'Bellossom', 'Bellsprout', 'Bergmite', 'Bibarel', 'Bidoof', 'Binacle', 'Bisharp', 'Blastoise', 'Blaziken', 'Blissey', 'Blitzle', 'Boldore', 'Bonsly', 'Bouffalant', 'Braixen', 'Braviary', 'Breloom', 'Bronzong', 'Bronzor', 'Budew', 'Buizel', 'Bulbasaur', 'Buneary', 'Bunnelby', 'Burmy', 'Butterfree', 'Cacnea', 'Cacturne', 'Camerupt', 'Carbink', 'Carnivine', 'Carracosta', 'Carvanha', 'Cascoon', 'Castform', 'Caterpie', 'Celebi', 'Chandelure', 'Chansey', 'Charizard', 'Charmander', 'Charmeleon', 'Chatot', 'Cherrim', 'Cherubi', 'Chesnaught', 'Chespin', 'Chikorita', 'Chimchar', 'Chimecho', 'Chinchou', 'Chingling', 'Cinccino', 'Clamperl', 'Clauncher', 'Clawitzer', 'Claydol', 'Clefable', 'Clefairy', 'Cleffa', 'Cloyster', 'Cobalion', 'Cofagrigus', 'Combee', 'Combusken', 'Conkeldurr', 'Corphish', 'Corsola', 'Cottonee', 'Cradily', 'Cranidos', 'Crawdaunt', 'Cresselia', 'Croagunk', 'Crobat', 'Croconaw', 'Crustle', 'Cryogonal', 'Cubchoo', 'Cubone', 'Cyndaquil', 'Darkrai', 'DarmanitanStandard Mode', 'DarmanitanZen Mode', 'Darumaka', 'Dedenne', 'Deerling', 'Deino', 'Delcatty', 'Delibird', 'Delphox', 'Dewgong', 'Dewott', 'Dialga', 'Diancie', 'Diggersby', 'Diglett', 'Ditto', 'Dodrio', 'Doduo', 'Donphan', 'Doublade', 'Dragalge', 'Dragonair', 'Dragonite', 'Drapion', 'Dratini', 'Drifblim', 'Drifloon', 'Drilbur', 'Drowzee', 'Druddigon', 'Ducklett', 'Dugtrio', 'Dunsparce', 'Duosion', 'Durant', 'Dusclops', 'Dusknoir', 'Duskull', 'Dustox', 'Dwebble', 'Eelektrik', 'Eelektross', 'Eevee', 'Ekans', 'Electabuzz', 'Electivire', 'Electrike', 'Electrode', 'Elekid', 'Elgyem', 'Emboar', 'Emolga', 'Empoleon', 'Entei', 'Escavalier', 'Espeon', 'Espurr', 'Excadrill', 'Exeggcute', 'Exeggutor', 'Exploud', "Farfetch'd", 'Fearow', 'Feebas', 'Fennekin', 'Feraligatr', 'Ferroseed', 'Ferrothorn', 'Finneon', 'Flaaffy', 'Flabébé', 'Flareon', 'Fletchinder', 'Fletchling', 'Floatzel', 'Floette', 'Florges', 'Flygon', 'Foongus', 'Forretress', 'Fraxure', 'Frillish', 'Froakie', 'Frogadier', 'Froslass', 'Furfrou', 'Furret', 'Gabite', 'Gallade', 'Galvantula', 'Garbodor', 'Garchomp', 'Gardevoir', 'Gastly', 'Gastrodon', 'Genesect', 'Gengar', 'Geodude', 'Gible', 'Gigalith', 'Girafarig', 'Glaceon', 'Glalie', 'Glameow', 'Gligar', 'Gliscor', 'Gloom', 'Gogoat', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Golett', 'Golurk', 'Goodra', 'Goomy', 'Gorebyss', 'Gothita', 'Gothitelle', 'Gothorita', 'Granbull', 'Graveler', 'Greninja', 'Grimer', 'Grotle', 'Groudon', 'GroudonPrimal Groudon', 'Grovyle', 'Growlithe', 'Grumpig', 'Gulpin', 'Gurdurr', 'Gyarados', 'Happiny', 'Hariyama', 'Haunter', 'Hawlucha', 'Haxorus', 'Heatmor', 'Heatran', 'Heliolisk', 'Helioptile', 'Heracross', 'Herdier', 'Hippopotas', 'Hippowdon', 'Hitmonchan', 'Hitmonlee', 'Hitmontop', 'Ho-oh', 'Honchkrow', 'Honedge', 'Hoothoot', 'Hoppip', 'Horsea', 'Houndoom', 'Houndour', 'Huntail', 'Hydreigon', 'Hypno', 'Igglybuff', 'Illumise', 'Infernape', 'Inkay', 'Ivysaur', 'Jellicent', 'Jigglypuff', 'Jirachi', 'Jolteon', 'Joltik', 'Jumpluff', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan', 'Karrablast', 'Kecleon', 'Kingdra', 'Kingler', 'Kirlia', 'Klang', 'Klefki', 'Klink', 'Klinklang', 'Koffing', 'Krabby', 'Kricketot', 'Kricketune', 'Krokorok', 'Krookodile', 'Kyogre', 'KyogrePrimal Kyogre', 'Kyurem', 'KyuremBlack Kyurem', 'KyuremWhite Kyurem', 'Lairon', 'Lampent', 'Lanturn', 'Lapras', 'Larvesta', 'Larvitar', 'Latias', 'Latios', 'Leafeon', 'Leavanny', 'Ledian', 'Ledyba', 'Lickilicky', 'Lickitung', 'Liepard', 'Lileep', 'Lilligant', 'Lillipup', 'Linoone', 'Litleo', 'Litwick', 'Lombre', 'Lopunny', 'Lotad', 'Loudred', 'Lucario', 'Ludicolo', 'Lugia', 'Lumineon', 'Lunatone', 'Luvdisc', 'Luxio', 'Luxray', 'Machamp', 'Machoke', 'Machop', 'Magby', 'Magcargo', 'Magikarp', 'Magmar', 'Magmortar', 'Magnemite', 'Magneton', 'Magnezone', 'Makuhita', 'Malamar', 'Mamoswine', 'Manaphy', 'Mandibuzz', 'Manectric', 'Mankey', 'Mantine', 'Mantyke', 'Maractus', 'Mareep', 'Marill', 'Marowak', 'Marshtomp', 'Masquerain', 'Mawile', 'Medicham', 'Meditite', 'MeowsticFemale', 'MeowsticMale', 'Meowth', 'Mesprit', 'Metagross', 'Metang', 'Metapod', 'Mew', 'Mewtwo', 'Mienfoo', 'Mienshao', 'Mightyena', 'Milotic', 'Miltank', 'Mime Jr.', 'Minccino', 'Minun', 'Misdreavus', 'Mismagius', 'Moltres', 'Monferno', 'Mothim', 'Mr. Mime', 'Mudkip', 'Muk', 'Munchlax', 'Munna', 'Murkrow', 'Musharna', 'Natu', 'Nidoking', 'Nidoqueen', 'Nidoran♀', 'Nidoran♂', 'Nidorina', 'Nidorino', 'Nincada', 'Ninetales', 'Ninjask', 'Noctowl', 'Noibat', 'Noivern', 'Nosepass', 'Numel', 'Nuzleaf', 'Octillery', 'Oddish', 'Omanyte', 'Omastar', 'Onix', 'Oshawott', 'Pachirisu', 'Palkia', 'Palpitoad', 'Pancham', 'Pangoro', 'Panpour', 'Pansage', 'Pansear', 'Paras', 'Parasect', 'Patrat', 'Pawniard', 'Pelipper', 'Persian', 'Petilil', 'Phanpy', 'Phantump', 'Phione', 'Pichu', 'Pidgeot', 'Pidgeotto', 'Pidgey', 'Pidove', 'Pignite', 'Pikachu', 'Piloswine', 'Pineco', 'Pinsir', 'Piplup', 'Plusle', 'Politoed', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Poochyena', 'Porygon', 'Porygon-Z', 'Porygon2', 'Primeape', 'Prinplup', 'Probopass', 'Psyduck', 'Pupitar', 'Purrloin', 'Purugly', 'Pyroar', 'Quagsire', 'Quilava', 'Quilladin', 'Qwilfish', 'Raichu', 'Raikou', 'Ralts', 'Rampardos', 'Rapidash', 'Raticate', 'Rattata', 'Rayquaza', 'Regice', 'Regigigas', 'Regirock', 'Registeel', 'Relicanth', 'Remoraid', 'Reshiram', 'Reuniclus', 'Rhydon', 'Rhyhorn', 'Rhyperior', 'Riolu', 'Roggenrola', 'Roselia', 'Roserade', 'Rotom', 'RotomFan Rotom', 'RotomFrost Rotom', 'RotomHeat Rotom', 'RotomMow Rotom', 'RotomWash Rotom', 'Rufflet', 'Sableye', 'Salamence', 'Samurott', 'Sandile', 'Sandshrew', 'Sandslash', 'Sawk', 'Sawsbuck', 'Scatterbug', 'Sceptile', 'Scizor', 'Scolipede', 'Scrafty', 'Scraggy', 'Scyther', 'Seadra', 'Seaking', 'Sealeo', 'Seedot', 'Seel', 'Seismitoad', 'Sentret', 'Serperior', 'Servine', 'Seviper', 'Sewaddle', 'Sharpedo', 'Shedinja', 'Shelgon', 'Shellder', 'Shellos', 'Shelmet', 'Shieldon', 'Shiftry', 'Shinx', 'Shroomish', 'Shuckle', 'Shuppet', 'Sigilyph', 'Silcoon', 'Simipour', 'Simisage', 'Simisear', 'Skarmory', 'Skiddo', 'Skiploom', 'Skitty', 'Skorupi', 'Skrelp', 'Skuntank', 'Slaking', 'Slakoth', 'Sliggoo', 'Slowbro', 'Slowking', 'Slowpoke', 'Slugma', 'Slurpuff', 'Smeargle', 'Smoochum', 'Sneasel', 'Snivy', 'Snorlax', 'Snorunt', 'Snover', 'Snubbull', 'Solosis', 'Solrock', 'Spearow', 'Spewpa', 'Spheal', 'Spinarak', 'Spinda', 'Spiritomb', 'Spoink', 'Spritzee', 'Squirtle', 'Stantler', 'Staraptor', 'Staravia', 'Starly', 'Starmie', 'Staryu', 'Steelix', 'Stoutland', 'Stunfisk', 'Stunky', 'Sudowoodo', 'Suicune', 'Sunflora', 'Sunkern', 'Surskit', 'Swablu', 'Swadloon', 'Swalot', 'Swampert', 'Swanna', 'Swellow', 'Swinub', 'Swirlix', 'Swoobat', 'Sylveon', 'Taillow', 'Talonflame', 'Tangela', 'Tangrowth', 'Tauros', 'Teddiursa', 'Tentacool', 'Tentacruel', 'Tepig', 'Terrakion', 'Throh', 'Timburr', 'Tirtouga', 'Togekiss', 'Togepi', 'Togetic', 'Torchic', 'Torkoal', 'Torterra', 'Totodile', 'Toxicroak', 'Tranquill', 'Trapinch', 'Treecko', 'Trevenant', 'Tropius', 'Trubbish', 'Turtwig', 'Tympole', 'Tynamo', 'Typhlosion', 'Tyranitar', 'Tyrantrum', 'Tyrogue', 'Tyrunt', 'Umbreon', 'Unfezant', 'Unown', 'Ursaring', 'Uxie', 'Vanillish', 'Vanillite', 'Vanilluxe', 'Vaporeon', 'Venipede', 'Venomoth', 'Venonat', 'Venusaur', 'Vespiquen', 'Vibrava', 'Victini', 'Victreebel', 'Vigoroth', 'Vileplume', 'Virizion', 'Vivillon', 'Volbeat', 'Volcanion', 'Volcarona', 'Voltorb', 'Vullaby', 'Vulpix', 'Wailmer', 'Wailord', 'Walrein', 'Wartortle', 'Watchog', 'Weavile', 'Weedle', 'Weepinbell', 'Weezing', 'Whimsicott', 'Whirlipede', 'Whiscash', 'Whismur', 'Wigglytuff', 'Wingull', 'Wobbuffet', 'Woobat', 'Wooper', 'WormadamPlant Cloak', 'WormadamSandy Cloak', 'WormadamTrash Cloak', 'Wurmple', 'Wynaut', 'Xatu', 'Xerneas', 'Yamask', 'Yanma', 'Yanmega', 'Yveltal', 'Zangoose', 'Zapdos', 'Zebstrika', 'Zekrom', 'Zigzagoon', 'Zoroark', 'Zorua', 'Zubat', 'Zweilous']

poke_gens = [4, 1, 3, 5, 1, 3, 2, 1, 5, 3, 6, 4, 5, 2, 3, 1, 1, 4, 5, 5, 2, 3, 6, 3, 1, 5, 6, 6, 5, 4, 2, 3, 3, 3, 3, 6, 3, 5, 4, 2, 5, 3, 1, 5, 3, 2, 1, 6, 4, 4, 6, 5, 1, 3, 2, 5, 5, 4, 5, 6, 5, 3, 4, 4, 4, 4, 1, 4, 6, 4, 1, 3, 3, 3, 6, 4, 5, 3, 3, 3, 1, 2, 5, 1, 1, 1, 1, 4, 4, 4, 6, 6, 2, 4, 3, 2, 4, 5, 3, 6, 6, 3, 1, 1, 2, 1, 5, 5, 4, 3, 5, 3, 2, 5, 3, 4, 3, 4, 4, 2, 2, 5, 5, 5, 1, 2, 4, 5, 5, 5, 6, 5, 5, 3, 2, 6, 1, 5, 4, 6, 6, 1, 1, 1, 1, 2, 6, 6, 1, 1, 4, 1, 4, 4, 5, 1, 5, 5, 1, 2, 5, 5, 3, 4, 3, 3, 5, 5, 5, 1, 1, 1, 4, 3, 1, 2, 5, 5, 5, 4, 2, 5, 2, 6, 5, 1, 1, 3, 1, 1, 3, 6, 2, 5, 5, 4, 2, 6, 1, 6, 6, 4, 6, 6, 3, 5, 2, 5, 5, 6, 6, 4, 6, 2, 4, 4, 5, 5, 4, 3, 1, 4, 5, 1, 1, 4, 5, 2, 4, 3, 4, 2, 4, 1, 6, 1, 1, 1, 1, 5, 5, 6, 6, 3, 5, 5, 5, 2, 1, 6, 1, 4, 3, 3, 3, 1, 3, 3, 5, 1, 4, 3, 1, 6, 5, 5, 4, 6, 6, 2, 5, 4, 4, 1, 1, 2, 2, 4, 6, 2, 2, 1, 2, 2, 3, 5, 1, 2, 3, 4, 6, 1, 5, 1, 3, 1, 5, 2, 1, 1, 1, 1, 1, 1, 5, 3, 2, 1, 3, 5, 6, 5, 5, 1, 1, 4, 4, 5, 5, 3, 3, 5, 5, 5, 3, 5, 2, 1, 5, 2, 3, 3, 4, 5, 2, 2, 4, 1, 5, 3, 5, 5, 3, 6, 5, 3, 4, 3, 3, 4, 3, 2, 4, 3, 3, 4, 4, 1, 1, 1, 2, 2, 1, 1, 4, 1, 1, 4, 3, 6, 4, 4, 5, 3, 1, 2, 4, 5, 2, 2, 1, 3, 3, 3, 3, 3, 6, 6, 1, 4, 3, 3, 1, 1, 1, 5, 5, 3, 3, 2, 4, 5, 3, 2, 4, 1, 4, 4, 1, 3, 1, 4, 5, 2, 5, 2, 1, 1, 1, 1, 1, 1, 3, 1, 3, 2, 6, 6, 3, 3, 3, 2, 1, 1, 1, 1, 5, 4, 4, 5, 6, 6, 5, 5, 5, 1, 1, 5, 5, 3, 1, 5, 2, 6, 4, 2, 1, 1, 1, 5, 5, 1, 2, 2, 1, 4, 3, 2, 1, 1, 1, 1, 3, 1, 4, 2, 1, 4, 4, 1, 2, 5, 4, 6, 2, 2, 6, 2, 1, 2, 3, 4, 1, 1, 1, 3, 3, 4, 3, 3, 3, 2, 5, 5, 1, 1, 4, 4, 5, 3, 4, 4, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 1, 1, 5, 5, 6, 3, 2, 5, 5, 5, 1, 1, 1, 3, 3, 1, 5, 2, 5, 5, 3, 5, 3, 3, 3, 1, 4, 5, 4, 3, 4, 3, 2, 3, 5, 3, 5, 5, 5, 2, 6, 2, 3, 4, 6, 4, 3, 3, 6, 1, 2, 1, 2, 6, 2, 2, 2, 5, 1, 3, 4, 2, 5, 3, 1, 6, 3, 2, 3, 4, 3, 6, 1, 2, 4, 4, 4, 1, 1, 2, 5, 5, 4, 2, 2, 2, 2, 3, 3, 5, 3, 3, 5, 3, 2, 6, 5, 6, 3, 6, 1, 4, 1, 2, 1, 1, 5, 5, 5, 5, 5, 4, 2, 2, 3, 3, 4, 2, 4, 5, 3, 3, 6, 3, 5, 4, 5, 5, 2, 2, 6, 2, 6, 2, 5, 2, 2, 4, 5, 5, 5, 1, 5, 1, 1, 1, 4, 3, 5, 1, 3, 1, 5, 6, 3, 6, 5, 1, 5, 1, 3, 3, 3, 1, 5, 4, 1, 1, 1, 5, 5, 3, 3, 1, 3, 2, 5, 2, 4, 4, 4, 3, 3, 2, 6, 5, 2, 4, 6, 3, 1, 5, 5, 3, 5, 5, 1, 5]


# COMMAND ----------

# MAGIC %md
# MAGIC ### Combine Info

# COMMAND ----------

# DBTITLE 1,Original Loop
# MAGIC %%timeit
# MAGIC gen1_gen2_name_lengths_loop = []
# MAGIC
# MAGIC for name,gen in zip(poke_names, poke_gens):
# MAGIC     if gen < 3:
# MAGIC         name_length = len(name)
# MAGIC         poke_tuple = (name, name_length)
# MAGIC         gen1_gen2_name_lengths_loop.append(poke_tuple)
# MAGIC
# MAGIC # print(gen1_gen2_name_lengths_loop)

# COMMAND ----------

# DBTITLE 1,Replace for loop with some list comprehension
# MAGIC %%timeit
# MAGIC
# MAGIC # Collect Pokémon that belong to generation 1 or generation 2
# MAGIC gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]
# MAGIC
# MAGIC # Create a map object that stores the name lengths
# MAGIC name_lengths_map = map(len, gen1_gen2_pokemon)
# MAGIC
# MAGIC # Combine gen1_gen2_pokemon and name_lengths_map into a list
# MAGIC gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]
# MAGIC
# MAGIC # print(gen1_gen2_name_lengths_loop[:5])
# MAGIC # print(gen1_gen2_name_lengths)

# COMMAND ----------

# DBTITLE 1,Replace for loop with one list comprehension
# MAGIC %%timeit
# MAGIC
# MAGIC gen1_gen2_name_lengths2 = [(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]
# MAGIC # print(gen1_gen2_name_lengths2)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Calculate Total & Avg

# COMMAND ----------

import numpy as np

# COMMAND ----------

stats = np.array(
    [[90, 92, 75, 92, 85, 60], [25, 20, 15, 105, 55, 90], [65, 130, 60, 75, 60, 75], [80, 70, 40, 100, 60, 145], [80, 105, 65, 60, 75, 130], [70, 110, 180, 60, 60, 50], [55, 70, 55, 40, 55, 85], [55, 50, 45, 135, 95, 120], [165, 75, 80, 40, 45, 65], [75, 70, 90, 70, 105, 80], [77, 59, 50, 67, 63, 46], [75, 100, 66, 60, 66, 115], [114, 85, 70, 85, 80, 30], [90, 75, 85, 115, 90, 55], [45, 95, 50, 40, 50, 75], [60, 85, 69, 65, 79, 80], [90, 110, 80, 100, 80, 95], [120, 120, 120, 120, 120, 120], [55, 112, 45, 74, 45, 70], [75, 140, 65, 112, 65, 110], [70, 90, 70, 60, 60, 40], [75, 125, 100, 70, 80, 45], [101, 72, 72, 99, 89, 29], [50, 70, 100, 40, 40, 30], [90, 85, 100, 95, 125, 85], [103, 60, 86, 60, 86, 50], [123, 77, 72, 99, 92, 58], [95, 117, 184, 44, 46, 28], [46, 87, 60, 30, 40, 57], [75, 125, 70, 125, 70, 115], [100, 50, 80, 60, 80, 50], [50, 20, 40, 20, 40, 20], [45, 75, 60, 40, 30, 50], [40, 40, 55, 40, 70, 55], [64, 115, 65, 83, 63, 65], [72, 105, 115, 54, 86, 68], [50, 48, 43, 46, 41, 60], [70, 92, 65, 80, 55, 98], [60, 52, 168, 47, 138, 30], [60, 62, 80, 63, 80, 60], [95, 110, 80, 70, 80, 50], [60, 70, 50, 100, 50, 65], [65, 90, 40, 45, 80, 75], [75, 75, 75, 125, 95, 40], [40, 55, 80, 35, 60, 30], [75, 80, 95, 90, 100, 50], [50, 75, 35, 70, 30, 40], [55, 69, 85, 32, 35, 28], [79, 85, 60, 55, 60, 71], [59, 45, 40, 35, 40, 31], [42, 52, 67, 39, 56, 50], [65, 125, 100, 60, 70, 70], [79, 83, 100, 85, 105, 78], [80, 120, 70, 110, 70, 80], [255, 10, 10, 75, 135, 55], [45, 60, 32, 50, 32, 76], [70, 105, 105, 50, 40, 20], [50, 80, 95, 10, 45, 10], [95, 110, 95, 40, 95, 55], [59, 59, 58, 90, 70, 73], [100, 123, 75, 57, 75, 80], [60, 130, 80, 60, 60, 70], [67, 89, 116, 79, 116, 33], [57, 24, 86, 24, 86, 23], [40, 30, 35, 50, 70, 55], [55, 65, 35, 60, 30, 85], [45, 49, 49, 65, 65, 45], [55, 66, 44, 44, 56, 85], [38, 36, 38, 32, 36, 57], [40, 29, 45, 29, 45, 36], [60, 45, 50, 90, 80, 70], [50, 85, 40, 85, 40, 35], [70, 115, 60, 115, 60, 55], [70, 100, 70, 105, 75, 40], [50, 50, 150, 50, 150, 50], [74, 100, 72, 90, 72, 46], [74, 108, 133, 83, 65, 32], [45, 90, 20, 65, 20, 65], [50, 35, 55, 25, 25, 15], [70, 70, 70, 70, 70, 70], [45, 30, 35, 20, 20, 45], [100, 100, 100, 100, 100, 100], [60, 55, 90, 145, 90, 80], [250, 5, 5, 35, 105, 50], [78, 84, 78, 109, 85, 100], [39, 52, 43, 60, 50, 65], [58, 64, 58, 80, 65, 80], [76, 65, 45, 92, 42, 91], [70, 60, 70, 87, 78, 85], [45, 35, 45, 62, 53, 35], [88, 107, 122, 74, 75, 64], [56, 61, 65, 48, 45, 38], [45, 49, 65, 49, 65, 45], [44, 58, 44, 58, 44, 61], [65, 50, 70, 95, 80, 65], [75, 38, 38, 56, 56, 67], [45, 30, 50, 65, 50, 45], [75, 95, 60, 65, 60, 115], [35, 64, 85, 74, 55, 32], [50, 53, 62, 58, 63, 44], [71, 73, 88, 120, 89, 59], [60, 70, 105, 70, 120, 75], [95, 70, 73, 95, 90, 60], [70, 45, 48, 60, 65, 35], [50, 25, 28, 45, 55, 15], [50, 95, 180, 85, 45, 70], [91, 90, 129, 90, 72, 108], [58, 50, 145, 95, 105, 30], [30, 30, 42, 30, 42, 70], [60, 85, 60, 85, 60, 55], [105, 140, 95, 55, 65, 45], [43, 80, 65, 50, 35, 35], [55, 55, 85, 65, 85, 35], [40, 27, 60, 37, 50, 66], [86, 81, 97, 81, 107, 43], [67, 125, 40, 30, 30, 58], [63, 120, 85, 90, 55, 55], [120, 70, 120, 75, 130, 85], [48, 61, 40, 61, 40, 50], [85, 90, 80, 70, 80, 130], [65, 80, 80, 59, 63, 58], [70, 95, 125, 65, 75, 45], [70, 50, 30, 95, 135, 105], [55, 70, 40, 60, 40, 40], [50, 50, 95, 40, 50, 35], [39, 52, 43, 60, 50, 65], [70, 90, 90, 135, 90, 125], [105, 140, 55, 30, 55, 95], [105, 30, 105, 140, 105, 55], [70, 90, 45, 15, 45, 50], [67, 58, 57, 81, 67, 101], [60, 60, 50, 40, 50, 75], [52, 65, 50, 45, 50, 38], [70, 65, 65, 55, 55, 70], [45, 55, 45, 65, 45, 75], [75, 69, 72, 114, 100, 104], [90, 70, 80, 70, 95, 70], [75, 75, 60, 83, 60, 60], [100, 120, 120, 150, 100, 90], [50, 100, 150, 100, 150, 50], [85, 56, 77, 50, 77, 78], [10, 55, 25, 35, 45, 95], [48, 48, 48, 48, 48, 48], [60, 110, 70, 60, 60, 100], [35, 85, 45, 35, 35, 75], [90, 120, 120, 60, 60, 50], [59, 110, 150, 45, 49, 35], [65, 75, 90, 97, 123, 44], [61, 84, 65, 70, 70, 70], [91, 134, 95, 100, 100, 80], [70, 90, 110, 60, 75, 95], [41, 64, 45, 50, 50, 50], [150, 80, 44, 90, 54, 80], [90, 50, 34, 60, 44, 70], [60, 85, 40, 30, 45, 68], [60, 48, 45, 43, 90, 42], [77, 120, 90, 60, 90, 48], [62, 44, 50, 44, 50, 55], [35, 80, 50, 50, 70, 120], [100, 70, 70, 65, 65, 45], [65, 40, 50, 125, 60, 30], [58, 109, 112, 48, 48, 109], [40, 70, 130, 60, 130, 25], [45, 100, 135, 65, 135, 45], [20, 40, 90, 30, 90, 25], [60, 50, 70, 50, 90, 65], [50, 65, 85, 35, 35, 55], [65, 85, 70, 75, 70, 40], [85, 115, 80, 105, 80, 50], [55, 55, 50, 45, 65, 55], [35, 60, 44, 40, 54, 55], [65, 83, 57, 95, 85, 105], [75, 123, 67, 95, 85, 95], [40, 45, 40, 65, 40, 65], [60, 50, 70, 80, 80, 140], [45, 63, 37, 65, 55, 95], [55, 55, 55, 85, 55, 30], [110, 123, 65, 100, 65, 65], [55, 75, 60, 75, 60, 103], [84, 86, 88, 111, 101, 60], [115, 115, 85, 90, 75, 100], [70, 135, 105, 60, 105, 20], [65, 65, 60, 130, 95, 110], [62, 48, 54, 63, 60, 68], [110, 135, 60, 50, 65, 88], [60, 40, 80, 60, 45, 40], [95, 95, 85, 125, 65, 55], [104, 91, 63, 91, 73, 68], [52, 65, 55, 58, 62, 60], [65, 90, 65, 61, 61, 100], [20, 15, 20, 10, 55, 80], [40, 45, 40, 62, 60, 60], [85, 105, 100, 79, 83, 78], [44, 50, 91, 24, 86, 10], [74, 94, 131, 54, 116, 20], [49, 49, 56, 49, 61, 66], [70, 55, 55, 80, 60, 45], [44, 38, 39, 61, 79, 42], [65, 130, 60, 95, 110, 65], [62, 73, 55, 56, 52, 84], [45, 50, 43, 40, 38, 62], [85, 105, 55, 85, 50, 115], [54, 45, 47, 75, 98, 52], [78, 65, 68, 112, 154, 75], [80, 100, 80, 80, 80, 100], [69, 55, 45, 55, 55, 15], [75, 90, 140, 60, 60, 40], [66, 117, 70, 40, 50, 67], [55, 40, 50, 65, 85, 40], [41, 56, 40, 62, 44, 71], [54, 63, 52, 83, 56, 97], [70, 80, 70, 80, 70, 110], [75, 80, 60, 65, 90, 102], [85, 76, 64, 45, 55, 90], [68, 90, 65, 50, 55, 82], [68, 125, 65, 65, 115, 80], [70, 77, 60, 97, 60, 108], [80, 95, 82, 60, 82, 75], [108, 130, 95, 80, 85, 102], [68, 65, 65, 125, 115, 80], [30, 35, 30, 100, 35, 80], [111, 83, 68, 92, 82, 39], [71, 120, 95, 120, 95, 99], [60, 65, 60, 130, 75, 110], [40, 80, 100, 30, 30, 20], [58, 70, 45, 40, 45, 42], [85, 135, 130, 60, 80, 25], [70, 80, 65, 90, 65, 85], [65, 60, 110, 130, 95, 65], [80, 80, 80, 80, 80, 80], [49, 55, 42, 42, 37, 85], [65, 75, 105, 35, 65, 85], [75, 95, 125, 45, 75, 95], [60, 65, 70, 85, 75, 40], [123, 100, 62, 97, 81, 68], [75, 80, 70, 65, 75, 90], [45, 67, 60, 35, 50, 63], [80, 82, 78, 95, 80, 85], [80, 120, 130, 55, 65, 45], [59, 74, 50, 35, 50, 35], [89, 124, 80, 55, 80, 55], [90, 100, 70, 110, 150, 80], [45, 50, 35, 55, 75, 40], [55, 84, 105, 114, 75, 52], [45, 30, 50, 55, 65, 45], [70, 55, 95, 95, 110, 65], [60, 45, 70, 75, 85, 55], [90, 120, 75, 60, 60, 45], [55, 95, 115, 45, 45, 35], [72, 95, 67, 103, 71, 122], [80, 80, 50, 40, 50, 25], [75, 89, 85, 55, 65, 36], [100, 150, 140, 100, 90, 90], [100, 180, 160, 150, 90, 90], [50, 65, 45, 85, 65, 95], [55, 70, 45, 70, 50, 60], [80, 45, 65, 90, 110, 80], [70, 43, 53, 43, 53, 40], [85, 105, 85, 40, 50, 40], [95, 125, 79, 60, 100, 81], [100, 5, 5, 15, 65, 30], [144, 120, 60, 40, 60, 50], [45, 50, 45, 115, 55, 95], [78, 92, 75, 74, 63, 118], [76, 147, 90, 60, 70, 97], [85, 97, 66, 105, 66, 65], [91, 90, 106, 130, 106, 77], [62, 55, 52, 109, 94, 109], [44, 38, 33, 61, 43, 70], [80, 125, 75, 40, 95, 85], [65, 80, 65, 35, 65, 60], [68, 72, 78, 38, 42, 32], [108, 112, 118, 68, 72, 47], [50, 105, 79, 35, 110, 76], [50, 120, 53, 35, 110, 87], [50, 95, 95, 35, 110, 70], [106, 130, 90, 110, 154, 90], [100, 125, 52, 105, 52, 71], [45, 80, 100, 35, 37, 28], [60, 30, 30, 36, 56, 50], [35, 35, 40, 35, 55, 50], [30, 40, 70, 70, 25, 60], [75, 90, 50, 110, 80, 95], [45, 60, 30, 80, 50, 65], [55, 104, 105, 94, 75, 52], [92, 105, 90, 125, 90, 98], [85, 73, 70, 73, 115, 67], [90, 30, 15, 40, 20, 15], [65, 47, 55, 73, 75, 85], [76, 104, 71, 104, 71, 108], [53, 54, 53, 37, 46, 45], [60, 62, 63, 80, 80, 60], [100, 60, 70, 85, 105, 60], [115, 45, 20, 45, 25, 20], [100, 100, 100, 100, 100, 100], [65, 65, 60, 110, 95, 130], [50, 47, 50, 57, 50, 65], [75, 55, 70, 55, 95, 110], [65, 50, 35, 115, 95, 95], [30, 80, 90, 55, 45, 55], [60, 115, 105, 65, 70, 80], [40, 35, 30, 120, 70, 105], [45, 25, 50, 25, 25, 35], [105, 95, 80, 40, 80, 90], [50, 75, 45, 40, 45, 60], [60, 90, 70, 60, 120, 40], [75, 95, 95, 95, 95, 85], [55, 130, 115, 50, 50, 75], [38, 35, 35, 65, 55, 50], [60, 80, 95, 70, 85, 50], [57, 80, 91, 80, 87, 75], [40, 55, 70, 45, 60, 30], [60, 100, 115, 70, 85, 90], [40, 65, 95, 60, 45, 35], [30, 105, 90, 25, 25, 50], [37, 25, 41, 25, 41, 25], [77, 85, 51, 55, 51, 65], [60, 82, 45, 45, 45, 74], [95, 117, 80, 65, 70, 92], [100, 100, 90, 150, 140, 90], [100, 150, 90, 180, 160, 90], [125, 130, 90, 130, 90, 95], [125, 170, 100, 120, 90, 95], [125, 120, 90, 170, 100, 95], [60, 90, 140, 50, 50, 40], [60, 40, 60, 95, 60, 55], [125, 58, 58, 76, 76, 67], [130, 85, 80, 85, 95, 60], [55, 85, 55, 50, 55, 60], [50, 64, 50, 45, 50, 41], [80, 80, 90, 110, 130, 110], [80, 90, 80, 130, 110, 110], [65, 110, 130, 60, 65, 95], [75, 103, 80, 70, 80, 92], [55, 35, 50, 55, 110, 85], [40, 20, 30, 40, 80, 55], [110, 85, 95, 80, 95, 50], [90, 55, 75, 60, 75, 30], [64, 88, 50, 88, 50, 106], [66, 41, 77, 61, 87, 23], [70, 60, 75, 110, 75, 90], [45, 60, 45, 25, 45, 55], [78, 70, 61, 50, 61, 100], [62, 50, 58, 73, 54, 72], [50, 30, 55, 65, 55, 20], [60, 50, 50, 60, 70, 50], [65, 76, 84, 54, 96, 105], [40, 30, 30, 40, 50, 30], [84, 71, 43, 71, 43, 48], [70, 110, 70, 115, 70, 90], [80, 70, 70, 90, 100, 70], [106, 90, 130, 90, 154, 110], [69, 69, 76, 69, 86, 91], [70, 55, 65, 95, 85, 70], [43, 30, 55, 40, 65, 97], [60, 85, 49, 60, 49, 60], [80, 120, 79, 95, 79, 70], [90, 130, 80, 65, 85, 55], [80, 100, 70, 50, 60, 45], [70, 80, 50, 35, 35, 35], [45, 75, 37, 70, 55, 83], [50, 50, 120, 80, 80, 30], [20, 10, 55, 15, 20, 80], [65, 95, 57, 100, 85, 93], [75, 95, 67, 125, 95, 83], [25, 35, 70, 95, 55, 45], [50, 60, 95, 120, 70, 70], [70, 70, 115, 130, 90, 60], [72, 60, 30, 20, 30, 25], [86, 92, 88, 68, 75, 73], [110, 130, 80, 70, 60, 80], [100, 100, 100, 100, 100, 100], [110, 65, 105, 55, 95, 80], [70, 75, 60, 105, 60, 105], [40, 80, 35, 35, 45, 70], [65, 40, 70, 80, 140, 70], [45, 20, 50, 60, 120, 50], [75, 86, 67, 106, 67, 60], [55, 40, 40, 65, 45, 35], [70, 20, 50, 20, 50, 40], [60, 80, 110, 50, 80, 45], [70, 85, 70, 60, 70, 50], [70, 60, 62, 80, 82, 60], [50, 85, 85, 55, 55, 50], [60, 60, 75, 60, 75, 80], [30, 40, 55, 40, 55, 60], [74, 48, 76, 83, 81, 104], [74, 48, 76, 83, 81, 104], [40, 45, 35, 40, 40, 90], [80, 105, 105, 105, 105, 80], [80, 135, 130, 95, 90, 70], [60, 75, 100, 55, 80, 50], [50, 20, 55, 25, 25, 30], [100, 100, 100, 100, 100, 100], [106, 110, 90, 154, 90, 130], [45, 85, 50, 55, 50, 65], [65, 125, 60, 95, 60, 105], [70, 90, 70, 60, 60, 70], [95, 60, 79, 100, 125, 81], [95, 80, 105, 40, 70, 100], [20, 25, 45, 70, 90, 60], [55, 50, 40, 40, 40, 75], [60, 40, 50, 75, 85, 95], [60, 60, 60, 85, 85, 85], [60, 60, 60, 105, 105, 105], [90, 100, 90, 125, 85, 90], [64, 78, 52, 78, 52, 81], [70, 94, 50, 94, 50, 66], [40, 45, 65, 100, 120, 90], [50, 70, 50, 50, 50, 40], [105, 105, 75, 65, 100, 50], [135, 85, 40, 40, 85, 5], [76, 25, 45, 67, 55, 24], [60, 85, 42, 85, 42, 91], [116, 55, 85, 107, 95, 29], [40, 50, 45, 70, 45, 70], [81, 102, 77, 85, 75, 85], [90, 92, 87, 75, 85, 76], [55, 47, 52, 40, 40, 41], [46, 57, 40, 40, 40, 50], [70, 62, 67, 55, 55, 56], [61, 72, 57, 55, 55, 65], [31, 45, 90, 30, 30, 40], [73, 76, 75, 81, 100, 100], [61, 90, 45, 50, 50, 160], [100, 50, 50, 76, 96, 70], [40, 30, 35, 45, 40, 55], [85, 70, 80, 97, 80, 123], [30, 45, 135, 45, 90, 30], [60, 60, 40, 65, 45, 35], [70, 70, 40, 60, 40, 60], [75, 105, 75, 105, 75, 45], [45, 50, 55, 75, 65, 30], [35, 40, 100, 90, 55, 35], [70, 60, 125, 115, 70, 55], [35, 45, 160, 30, 45, 70], [55, 55, 45, 63, 45, 45], [60, 45, 70, 45, 90, 95], [90, 120, 100, 150, 120, 100], [75, 65, 55, 65, 55, 69], [67, 82, 62, 46, 48, 43], [95, 124, 78, 69, 71, 58], [50, 53, 48, 53, 48, 64], [50, 53, 48, 53, 48, 64], [50, 53, 48, 53, 48, 64], [35, 70, 55, 45, 55, 25], [60, 95, 80, 60, 80, 30], [45, 55, 39, 35, 39, 42], [45, 85, 70, 40, 40, 60], [60, 50, 100, 85, 70, 65], [65, 70, 60, 65, 65, 115], [45, 35, 50, 70, 50, 30], [90, 60, 60, 40, 40, 40], [43, 70, 48, 50, 60, 38], [80, 80, 80, 80, 80, 80], [20, 40, 15, 35, 35, 60], [83, 80, 75, 70, 70, 101], [63, 60, 55, 50, 50, 71], [40, 45, 40, 35, 35, 56], [50, 55, 50, 36, 30, 43], [90, 93, 55, 70, 55, 55], [35, 55, 40, 50, 50, 90], [100, 100, 80, 60, 60, 50], [50, 65, 90, 35, 35, 15], [65, 125, 100, 55, 70, 85], [53, 51, 53, 61, 56, 40], [60, 50, 40, 85, 75, 95], [90, 75, 75, 90, 100, 70], [40, 50, 40, 40, 40, 90], [65, 65, 65, 50, 50, 90], [90, 95, 95, 70, 90, 70], [50, 85, 55, 65, 65, 90], [35, 55, 35, 30, 30, 35], [65, 60, 70, 85, 75, 40], [85, 80, 70, 135, 75, 90], [85, 80, 90, 105, 95, 60], [65, 105, 60, 60, 70, 95], [64, 66, 68, 81, 76, 50], [60, 55, 145, 75, 150, 40], [50, 52, 48, 65, 50, 55], [70, 84, 70, 65, 70, 51], [41, 50, 37, 50, 37, 66], [71, 82, 64, 64, 59, 112], [86, 68, 72, 109, 66, 106], [95, 85, 85, 65, 65, 35], [58, 64, 58, 80, 65, 80], [61, 78, 95, 56, 58, 57], [65, 95, 75, 55, 55, 85], [60, 90, 55, 90, 80, 110], [90, 85, 75, 115, 100, 115], [28, 25, 25, 45, 35, 40], [97, 165, 60, 65, 50, 58], [65, 100, 70, 80, 80, 105], [55, 81, 60, 50, 70, 97], [30, 56, 35, 25, 35, 72], [105, 150, 90, 150, 90, 95], [80, 50, 100, 100, 200, 50], [110, 160, 110, 80, 110, 100], [80, 100, 200, 50, 100, 50], [80, 75, 150, 75, 150, 50], [100, 90, 130, 45, 65, 55], [35, 65, 35, 65, 35, 65], [100, 120, 100, 150, 120, 90], [110, 65, 75, 125, 85, 30], [105, 130, 120, 45, 45, 40], [80, 85, 95, 30, 30, 25], [115, 140, 130, 55, 55, 40], [40, 70, 40, 35, 40, 60], [55, 75, 85, 25, 25, 15], [50, 60, 45, 100, 80, 65], [60, 70, 65, 125, 105, 90], [50, 50, 77, 95, 77, 91], [50, 65, 107, 105, 107, 86], [50, 65, 107, 105, 107, 86], [50, 65, 107, 105, 107, 86], [50, 65, 107, 105, 107, 86], [50, 65, 107, 105, 107, 86], [70, 83, 50, 37, 50, 60], [50, 75, 75, 65, 65, 50], [95, 135, 80, 110, 80, 100], [95, 100, 85, 108, 70, 70], [50, 72, 35, 35, 35, 65], [50, 75, 85, 20, 30, 40], [75, 100, 110, 45, 55, 65], [75, 125, 75, 30, 75, 85], [80, 100, 70, 60, 70, 95], [38, 35, 40, 27, 25, 35], [70, 85, 65, 105, 85, 120], [70, 130, 100, 55, 80, 65], [60, 100, 89, 55, 69, 112], [65, 90, 115, 45, 115, 58], [50, 75, 70, 35, 70, 48], [70, 110, 80, 55, 80, 105], [55, 65, 95, 95, 45, 85], [80, 92, 65, 65, 80, 68], [90, 60, 70, 75, 70, 45], [40, 40, 50, 30, 30, 30], [65, 45, 55, 45, 70, 45], [105, 95, 75, 85, 75, 74], [35, 46, 34, 35, 45, 20], [75, 75, 95, 75, 95, 113], [60, 60, 75, 60, 75, 83], [73, 100, 60, 100, 60, 65], [45, 53, 70, 40, 60, 42], [70, 120, 40, 95, 40, 95], [1, 90, 45, 30, 30, 40], [65, 95, 100, 60, 50, 50], [30, 65, 100, 45, 25, 40], [76, 48, 48, 57, 62, 34], [50, 40, 85, 40, 65, 25], [30, 42, 118, 42, 88, 30], [90, 100, 60, 90, 60, 80], [45, 65, 34, 40, 34, 45], [60, 40, 60, 40, 60, 35], [20, 10, 230, 10, 230, 5], [44, 75, 35, 63, 33, 45], [72, 58, 80, 103, 80, 97], [50, 35, 55, 25, 25, 15], [75, 98, 63, 98, 63, 101], [75, 98, 63, 98, 63, 101], [75, 98, 63, 98, 63, 101], [65, 80, 140, 40, 70, 70], [66, 65, 48, 62, 57, 52], [55, 45, 50, 45, 65, 80], [50, 45, 45, 35, 35, 50], [40, 50, 90, 30, 55, 65], [50, 60, 60, 60, 60, 30], [103, 93, 67, 71, 61, 84], [150, 160, 100, 95, 65, 100], [60, 60, 60, 35, 35, 30], [68, 75, 53, 83, 113, 60], [95, 75, 110, 100, 80, 30], [95, 75, 80, 100, 110, 30], [90, 65, 65, 40, 40, 15], [40, 40, 40, 70, 40, 20], [82, 80, 86, 85, 75, 72], [55, 20, 35, 20, 45, 75], [45, 30, 15, 85, 65, 65], [55, 95, 55, 35, 75, 115], [45, 45, 55, 45, 55, 63], [160, 110, 65, 65, 110, 30], [50, 50, 50, 50, 50, 50], [60, 62, 50, 62, 60, 40], [60, 80, 50, 40, 40, 30], [45, 30, 40, 105, 50, 20], [70, 95, 85, 55, 65, 70], [40, 60, 30, 31, 31, 70], [45, 22, 60, 27, 30, 29], [70, 40, 50, 55, 50, 25], [40, 60, 40, 40, 40, 30], [60, 60, 60, 60, 60, 60], [50, 92, 108, 92, 108, 35], [60, 25, 35, 70, 80, 60], [78, 52, 60, 63, 65, 23], [44, 48, 65, 50, 64, 43], [73, 95, 62, 85, 65, 85], [85, 120, 70, 50, 60, 100], [55, 75, 50, 40, 40, 80], [40, 55, 30, 30, 30, 60], [60, 75, 85, 100, 85, 115], [30, 45, 55, 70, 55, 85], [75, 85, 200, 55, 65, 30], [85, 110, 90, 45, 90, 80], [109, 66, 84, 81, 99, 32], [63, 63, 47, 41, 41, 74], [70, 100, 115, 30, 65, 30], [100, 75, 115, 90, 115, 85], [75, 75, 55, 105, 85, 30], [30, 30, 30, 30, 30, 30], [40, 30, 32, 50, 52, 65], [45, 40, 60, 40, 75, 50], [55, 63, 90, 50, 80, 42], [100, 73, 83, 73, 83, 55], [100, 110, 90, 85, 90, 60], [75, 87, 63, 87, 63, 98], [60, 85, 60, 50, 50, 125], [50, 50, 40, 30, 30, 50], [62, 48, 66, 59, 57, 49], [67, 57, 55, 77, 55, 114], [95, 65, 65, 110, 130, 60], [40, 55, 30, 30, 30, 85], [78, 81, 71, 74, 69, 126], [65, 55, 115, 100, 40, 60], [100, 100, 125, 110, 50, 50], [75, 100, 95, 40, 70, 110], [60, 80, 50, 50, 50, 40], [40, 40, 35, 50, 100, 70], [80, 70, 65, 80, 120, 100], [65, 63, 45, 45, 45, 45], [91, 129, 90, 72, 90, 108], [120, 100, 85, 30, 85, 45], [75, 80, 55, 25, 35, 35], [54, 78, 103, 53, 45, 22], [85, 50, 95, 120, 115, 80], [35, 20, 65, 40, 65, 20], [55, 40, 85, 80, 105, 40], [45, 60, 40, 70, 50, 45], [70, 85, 140, 85, 70, 20], [95, 109, 105, 75, 85, 56], [50, 65, 64, 44, 48, 43], [83, 106, 65, 86, 65, 85], [62, 77, 62, 50, 42, 65], [45, 100, 45, 45, 45, 10], [40, 45, 35, 65, 55, 70], [85, 110, 76, 65, 82, 56], [99, 68, 83, 72, 87, 51], [50, 50, 62, 40, 62, 65], [55, 68, 64, 45, 55, 31], [50, 50, 40, 50, 40, 64], [35, 55, 40, 45, 40, 60], [78, 84, 78, 109, 85, 100], [100, 134, 110, 95, 100, 61], [82, 121, 119, 69, 59, 71], [35, 35, 35, 35, 35, 35], [58, 89, 77, 45, 45, 48], [95, 65, 110, 60, 130, 65], [80, 115, 80, 65, 55, 93], [48, 72, 48, 72, 48, 48], [90, 130, 75, 75, 75, 55], [75, 75, 130, 75, 130, 95], [51, 65, 65, 80, 75, 59], [36, 50, 50, 65, 60, 44], [71, 95, 85, 110, 95, 79], [130, 65, 60, 110, 95, 65], [30, 45, 59, 30, 39, 57], [70, 65, 60, 90, 75, 90], [60, 55, 50, 40, 55, 45], [80, 82, 83, 100, 100, 80], [70, 80, 102, 80, 102, 40], [50, 70, 50, 50, 50, 70], [100, 100, 100, 100, 100, 100], [80, 105, 65, 100, 70, 70], [80, 80, 80, 55, 55, 90], [75, 80, 85, 110, 90, 50], [91, 90, 72, 90, 129, 108], [80, 52, 50, 90, 50, 89], [65, 73, 55, 47, 75, 85], [80, 110, 120, 130, 90, 70], [85, 60, 65, 135, 105, 100], [40, 30, 50, 55, 55, 100], [70, 55, 75, 45, 65, 60], [38, 41, 40, 50, 65, 65], [130, 70, 35, 70, 35, 60], [170, 90, 45, 90, 45, 60], [110, 80, 90, 95, 90, 65], [59, 63, 80, 65, 80, 58], [60, 85, 69, 60, 69, 77], [70, 120, 65, 45, 85, 125], [40, 35, 30, 20, 20, 50], [65, 90, 50, 85, 45, 55], [65, 90, 120, 85, 70, 60], [60, 67, 85, 77, 75, 116], [40, 55, 99, 40, 79, 47], [110, 78, 73, 76, 71, 60], [64, 51, 23, 51, 23, 28], [140, 70, 45, 85, 50, 45], [40, 30, 30, 55, 30, 85], [190, 33, 58, 33, 58, 33], [55, 45, 43, 55, 43, 72], [55, 45, 45, 25, 25, 15], [60, 59, 85, 79, 105, 36], [60, 79, 105, 59, 85, 36], [60, 69, 95, 69, 95, 36], [45, 45, 35, 20, 30, 20], [95, 23, 48, 23, 48, 23], [65, 75, 70, 95, 70, 95], [126, 131, 95, 131, 98, 99], [38, 30, 85, 55, 65, 30], [65, 65, 45, 75, 45, 95], [86, 76, 86, 116, 56, 95], [126, 131, 95, 131, 98, 99], [73, 115, 60, 60, 60, 90], [90, 90, 85, 125, 90, 100], [75, 100, 63, 80, 63, 116], [100, 150, 120, 120, 100, 90], [38, 30, 41, 30, 41, 60], [60, 105, 60, 120, 60, 105], [40, 65, 40, 80, 40, 65], [40, 45, 35, 30, 40, 55], [72, 85, 70, 65, 70, 58]]
)

# COMMAND ----------

# DBTITLE 1,Original Loop
# MAGIC %%timeit
# MAGIC poke_list = []
# MAGIC
# MAGIC for pokemon,row in zip(names, stats):
# MAGIC     total_stats = np.sum(row)
# MAGIC     avg_stats = np.mean(row)
# MAGIC     poke_list.append((pokemon, total_stats, avg_stats))
# MAGIC
# MAGIC # print(poke_list[:3])

# COMMAND ----------

# DBTITLE 1,Replace for loop with one list comprehension
# MAGIC %%timeit
# MAGIC # Create a total stats array
# MAGIC total_stats_np = stats.sum(axis=1)
# MAGIC
# MAGIC # Create an average stats array
# MAGIC avg_stats_np = stats.mean(axis=1)
# MAGIC
# MAGIC # Combine names, total_stats_np, and avg_stats_np into a list
# MAGIC poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]
# MAGIC
# MAGIC # print(poke_list_np == poke_list, '\n')
# MAGIC # print(poke_list_np[:3])
# MAGIC # print(poke_list[:3], '\n')
# MAGIC # top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
# MAGIC # print('3 strongest Pokémon:\n{}'.format(top_3))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Writing Better Loops
# MAGIC - Understand what is being done with each loop iteration
# MAGIC - Move one-time calculation outside (above) the loop, i.e. the value does not change with each iteration
# MAGIC - Use holistic conversions outside (below) the loop, i.e. convert datatype of each element within each iteration, using map function
# MAGIC - Anything that is done **once** should be outside the loop

# COMMAND ----------

# MAGIC %md
# MAGIC ### One-time calculation loop

# COMMAND ----------

# DBTITLE 1,Original Loop
# MAGIC %%timeit
# MAGIC # Import Counter
# MAGIC from collections import Counter
# MAGIC
# MAGIC # Collect the count of each generation
# MAGIC gen_counts = Counter(generations)
# MAGIC
# MAGIC for gen,count in gen_counts.items():
# MAGIC     total_count = len(generations)
# MAGIC     gen_percent = round(count / total_count * 100, 2)
# MAGIC     # print(
# MAGIC     #   'generation {}: count = {:3} percentage = {}'
# MAGIC     #   .format(gen, count, gen_percent)
# MAGIC     # )
# MAGIC

# COMMAND ----------

# DBTITLE 1,Move one-time calculation outside the loop
# MAGIC %%timeit
# MAGIC
# MAGIC # Import Counter
# MAGIC from collections import Counter
# MAGIC
# MAGIC # Collect the count of each generation
# MAGIC gen_counts = Counter(generations)
# MAGIC
# MAGIC # Improve for loop by moving one calculation above the loop
# MAGIC total_count  = len(generations)
# MAGIC
# MAGIC for gen,count in gen_counts.items():
# MAGIC     gen_percent = round(count / total_count * 100, 2)
# MAGIC     # print('generation {}: count = {:3} percentage = {}'
# MAGIC     #       .format(gen, count, gen_percent))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Holistic conversion loop

# COMMAND ----------

pokemon_types = ['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Grass', 'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

# COMMAND ----------

# Import combinations from itertools
from itertools import combinations

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# COMMAND ----------

# DBTITLE 1,Original
# MAGIC %%timeit
# MAGIC
# MAGIC enumerated_pairs = []
# MAGIC
# MAGIC for i,pair in enumerate(possible_pairs, 1):
# MAGIC     enumerated_pair_tuple = (i,) + pair
# MAGIC     enumerated_pair_list = list(enumerated_pair_tuple)
# MAGIC     enumerated_pairs.append(enumerated_pair_list)
# MAGIC # print(enumerated_pairs)

# COMMAND ----------

# DBTITLE 1,Use holistic conversions outside (below) the loop
# MAGIC %%timeit
# MAGIC # Create an empty list called enumerated_tuples
# MAGIC enumerated_tuples = []
# MAGIC
# MAGIC # Append each enumerated_pair_tuple to the empty list above
# MAGIC for i,pair in enumerate(possible_pairs, 1):
# MAGIC     enumerated_pair_tuple = (i,) + pair
# MAGIC     enumerated_tuples.append(enumerated_pair_tuple)
# MAGIC
# MAGIC # Convert all tuples in enumerated_tuples to a list
# MAGIC enumerated_pairs = [*map(list, enumerated_tuples)]
# MAGIC # print(enumerated_pairs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Bring All Together

# COMMAND ----------

hps = np.array(
    [80.0, 60.0, 131.0, 62.0, 71.0, 109.0, 45.0, 53.0, 73.0, 60.0, 37.0, 63.0, 59.0, 84.0, 25.0, 50.0, 98.0, 116.0, 29.0, 85.0, 43.0, 46.0, 46.0, 57.0, 94.0, 87.0, 70.0, 59.0, 68.0, 65.0, 89.0, 52.0, 68.0, 66.0, 67.0, 75.0, 73.0, 103.0, 66.0, 109.0, 60.0, 56.0, 71.0, 77.0, 75.0, 102.0, 98.0, 81.0, 60.0, 66.0, 105.0, 74.0, 34.0, 50.0, 53.0, 98.0, 65.0, 127.0, 85.0, 71.0, 57.0, 93.0, 62.0, 47.0, 83.0, 69.0, 99.0, 66.0, 1.0, 89.0, 20.0, 108.0, 115.0, 57.0, 38.0, 32.0, 91.0, 63.0, 53.0, 62.0, 122.0, 77.0, 87.0, 88.0, 95.0, 96.0, 50.0, 63.0, 49.0, 50.0, 98.0, 55.0, 66.0, 50.0, 53.0, 89.0, 57.0, 56.0, 81.0, 81.0, 89.0, 73.0, 23.0, 85.0, 81.0, 95.0, 46.0, 133.0, 36.0, 87.0, 69.0, 56.0, 89.0, 61.0, 8.0, 38.0, 80.0, 126.0, 30.0, 68.0, 106.0, 84.0, 59.0, 32.0, 22.0, 49.0, 59.0, 10.0, 24.0, 76.0, 58.0, 49.0, 58.0, 47.0, 92.0, 111.0, 122.0, 87.0, 88.0, 106.0, 113.0, 106.0, 100.0, 52.0, 27.0, 91.0, 66.0, 67.0, 45.0, 35.0, 104.0, 80.0, 41.0, 78.0, 76.0, 82.0, 126.0, 67.0, 35.0, 69.0, 52.0, 82.0, 74.0, 77.0, 54.0, 79.0, 55.0, 82.0, 60.0, 39.0, 81.0, 50.0, 106.0, 80.0, 80.0, 71.0, 67.0, 7.0, 100.0, 47.0, 93.0, 52.0, 65.0, 62.0, 41.0, 64.0, 81.0, 58.0, 36.0, 53.0, 75.0, 98.0, 90.0, 76.0, 43.0, 92.0, 69.0, 62.0, 92.0, 84.0, 81.0, 38.0, 52.0, 24.0, 73.0, 69.0, 92.0, 74.0, 59.0, 123.0, 42.0, 34.0, 52.0, 82.0, 59.0, 57.0, 39.0, 106.0, 52.0, 40.0, 65.0, 47.0, 62.0, 103.0, 57.0, 67.0, 59.0, 63.0, 89.0, 82.0, 59.0, 44.0, 65.0, 90.0, 68.0, 65.0, 22.0, 94.0, 30.0, 35.0, 59.0, 69.0, 69.0, 48.0, 60.0, 53.0, 21.0, 62.0, 50.0, 79.0, 64.0, 93.0, 86.0, 91.0, 99.0, 86.0, 64.0, 103.0, 44.0, 67.0, 90.0, 61.0, 87.0, 47.0, 54.0, 82.0, 87.0, 99.0, 66.0, 76.0, 84.0, 80.0, 35.0, 54.0, 105.0, 36.0, 84.0, 57.0, 94.0, 48.0, 69.0, 16.0, 67.0, 96.0, 29.0, 99.0, 50.0, 67.0, 1.0, 96.0, 46.0, 54.0, 35.0, 43.0, 98.0, 55.0, 91.0, 64.0, 77.0, 55.0, 79.0, 135.0, 85.0, 81.0, 56.0, 94.0, 103.0, 24.0, 33.0, 123.0, 79.0, 72.0, 83.0, 97.0, 89.0, 62.0, 122.0, 69.0, 46.0, 54.0, 65.0, 58.0, 63.0, 76.0, 1.0, 48.0, 93.0, 83.0, 51.0, 52.0, 98.0, 62.0, 55.0, 116.0, 59.0, 86.0, 67.0, 70.0, 44.0, 47.0, 101.0, 39.0, 75.0, 37.0, 62.0, 67.0, 26.0, 98.0, 63.0, 100.0, 44.0, 92.0, 129.0, 74.0, 52.0, 81.0, 72.0, 63.0, 65.0, 53.0, 79.0, 58.0, 46.0, 89.0, 64.0, 137.0, 62.0, 50.0, 54.0, 78.0, 50.0, 36.0, 111.0, 36.0, 107.0, 72.0, 41.0, 111.0, 63.0, 42.0, 70.0, 101.0, 86.0, 90.0, 114.0, 74.0, 78.0, 62.0, 31.0, 64.0, 110.0, 24.0, 103.0, 75.0, 45.0, 70.0, 114.0, 53.0, 89.0, 97.0, 45.0, 85.0, 82.0, 56.0, 86.0, 59.0, 53.0, 36.0, 78.0, 57.0, 54.0, 39.0, 33.0, 48.0, 87.0, 47.0, 106.0, 79.0, 72.0, 37.0, 119.0, 31.0, 82.0, 112.0, 63.0, 51.0, 68.0, 92.0, 103.0, 84.0, 41.0, 51.0, 73.0, 35.0, 62.0, 126.0, 41.0, 98.0, 44.0, 59.0, 66.0, 29.0, 66.0, 102.0, 87.0, 86.0, 47.0, 64.0, 73.0, 86.0, 103.0, 42.0, 112.0, 61.0, 62.0, 37.0, 66.0, 62.0, 36.0, 61.0, 71.0, 58.0, 88.0, 42.0, 91.0, 63.0, 78.0, 21.0, 72.0, 67.0, 92.0, 38.0, 103.0, 40.0, 102.0, 83.0, 49.0, 124.0, 37.0, 64.0, 74.0, 82.0, 74.0, 89.0, 80.0, 69.0, 44.0, 59.0, 92.0, 38.0, 71.0, 15.0, 50.0, 26.0, 100.0, 21.0, 62.0, 87.0, 84.0, 88.0, 96.0, 80.0, 90.0, 67.0, 68.0, 23.0, 73.0, 101.0, 49.0, 38.0, 71.0, 98.0, 99.0, 29.0, 80.0, 51.0, 75.0, 10.0, 92.0, 58.0, 74.0, 64.0, 42.0, 82.0, 56.0, 50.0, 85.0, 66.0, 50.0, 92.0, 53.0, 67.0, 87.0, 93.0, 99.0, 111.0, 69.0, 48.0, 111.0, 104.0, 60.0, 86.0, 58.0, 28.0, 95.0, 77.0, 71.0, 112.0, 105.0, 52.0, 40.0, 19.0, 68.0, 58.0, 78.0, 69.0, 51.0, 58.0, 28.0, 100.0, 54.0, 84.0, 51.0, 70.0, 84.0, 61.0, 47.0, 128.0, 63.0, 83.0, 66.0, 48.0, 102.0, 78.0, 77.0, 9.0, 76.0, 90.0, 76.0, 64.0, 99.0, 75.0, 83.0, 95.0, 94.0, 34.0, 77.0, 49.0, 16.0, 76.0, 23.0, 56.0, 3.0, 42.0, 56.0, 68.0, 54.0, 44.0, 45.0, 108.0, 56.0, 66.0, 117.0, 23.0, 15.0, 42.0, 58.0, 39.0, 67.0, 66.0, 28.0, 72.0, 31.0, 86.0, 74.0, 125.0, 89.0, 63.0, 77.0, 72.0, 49.0, 31.0, 96.0, 107.0, 56.0, 61.0, 56.0, 94.0, 99.0, 46.0, 59.0, 54.0, 74.0, 88.0, 96.0, 61.0, 43.0, 82.0, 83.0, 59.0, 72.0, 77.0, 91.0, 70.0, 81.0, 73.0, 43.0, 86.0, 71.0, 95.0, 38.0, 50.0, 77.0, 24.0, 65.0, 57.0, 57.0, 62.0, 11.0, 69.0, 70.0, 95.0, 106.0, 77.0, 92.0, 6.0, 82.0, 97.0, 91.0, 74.0, 59.0, 59.0, 69.0, 79.0, 83.0, 66.0, 36.0, 115.0, 46.0, 1.0, 105.0, 94.0, 73.0, 93.0, 80.0, 47.0, 71.0, 36.0, 51.0, 46.0, 72.0, 96.0, 52.0, 80.0, 13.0, 41.0, 82.0, 93.0, 93.0, 96.0, 26.0, 55.0, 2.0, 64.0, 74.0, 59.0, 44.0, 79.0, 82.0, 72.0, 53.0, 69.0, 70.0, 75.0, 84.0, 68.0, 31.0, 61.0, 78.0, 57.0]
)


# COMMAND ----------

# DBTITLE 1,Original
# MAGIC %%timeit
# MAGIC poke_zscores = []
# MAGIC
# MAGIC for name,hp in zip(names, hps):
# MAGIC     hp_avg = hps.mean()
# MAGIC     hp_std = hps.std()
# MAGIC     z_score = (hp - hp_avg)/hp_std
# MAGIC     poke_zscores.append((name, hp, z_score))
# MAGIC highest_hp_pokemon = []
# MAGIC
# MAGIC for name,hp,zscore in poke_zscores:
# MAGIC     if zscore > 2:
# MAGIC         highest_hp_pokemon.append((name, hp, zscore))

# COMMAND ----------

# DBTITLE 1,Better
# MAGIC %%timeit
# MAGIC # Calculate the total HP avg and total HP standard deviation
# MAGIC hp_avg = hps.mean()
# MAGIC hp_std = hps.std()
# MAGIC
# MAGIC # Use NumPy to eliminate the previous for loop
# MAGIC z_scores = (hps - hp_avg)/hp_std
# MAGIC
# MAGIC # Combine names, hps, and z_scores
# MAGIC poke_zscores2 = [*zip(names, hps, z_scores)]
# MAGIC # print(*poke_zscores2[:3], sep='\n')
# MAGIC
# MAGIC # Use list comprehension with the same logic as the highest_hp_pokemon code block
# MAGIC highest_hp_pokemon2 = [(names, hps, z_scores) for names, hps, z_scores in poke_zscores2 if z_scores > 2]
# MAGIC # print(*highest_hp_pokemon2, sep='\n')

# COMMAND ----------

# MAGIC %md
# MAGIC # Basic Pandas Optimizations

# COMMAND ----------

import pandas as pd

# COMMAND ----------

pd.set_option('display.max_columns', None)

baseball_df = pd.read_csv('/Volumes/learning_datacamp/de_associate/06_writing_efficient_python_code/baseball_stats.csv')
print(baseball_df.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dataframe Iteration: iloc() in loop --> iterrows()
# MAGIC iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs
# MAGIC - If using i,row, you can access things from the row using square brackets (i.e., row['Team']).
# MAGIC - If using row_tuple, you would have to specify which element of the tuple you'd like to access before grabbing the team name (i.e., row_tuple[1]['Team'])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Iterating with .iterrows()

# COMMAND ----------

pit_df = baseball_df.loc[:2,['Team','League','Year','RS','RA','W','G','Playoffs']]
print(pit_df)

# COMMAND ----------

# Iterate over pit_df and print each index variable, row, and row type
for i,row in pit_df.iterrows():
    print(i)
    print(row['Team'])
    print(type(row))

# COMMAND ----------

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple[1]['Team'])
    print(row_tuple[1][0])
    print(type(row_tuple))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Differentials with .iterrows()

# COMMAND ----------

giants_df = baseball_df.loc[:, ['Team','League','Year','RS','RA','W','G','Playoffs']]
giants_df = giants_df[giants_df['Team'] == 'SFG'] #Filter Giant
print(giants_df.head())

# COMMAND ----------

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = runs_scored - runs_allowed
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dataframe Iteration: iloc() in loop --> itertuples()
# MAGIC itertuples() return **namedtuple** which is a specialized data types that exist within the **`collections`** module

# COMMAND ----------

# MAGIC %md
# MAGIC ### Iterating with .itertuples()

# COMMAND ----------

rangers_df = baseball_df.loc[:, ['Team','League','Year','RS','RA','W','G','Playoffs']]
rangers_df = rangers_df[rangers_df['Team'] == 'TEX'] #Filter Ranger
print(rangers_df.head())

# COMMAND ----------

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Differentials with .itertuples()

# COMMAND ----------

yankees_df = baseball_df.loc[:, ['Team','League','Year','RS','RA','W','G','Playoffs']]
yankees_df = yankees_df[yankees_df['Team'] == 'NYY'] #Filter Yankee
print(yankees_df.head())

# COMMAND ----------

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = runs_scored - runs_allowed
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df.sort_values(['RD'], ascending=[False]))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Alternative Pandas Loop
# MAGIC - **`pandas.apply()`** method takes a function and applies it to a Dataframe:
# MAGIC     - Must specify an axis to apply (**`0`** for columns; **`1`** for rows)

# COMMAND ----------

rays_df = baseball_df[baseball_df['Team'] == 'TBR'] #Filter Tamba Bay Ray
rays_df.index = rays_df['Year']
rays_df = rays_df.loc[:, ['RS','RA','W','G','Playoffs']]

print(rays_df.head())

# COMMAND ----------

# Gather sum of all columns
stat_totals = rays_df.apply(lambda column: sum(column), axis=0)
print(stat_totals)

# COMMAND ----------

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(lambda row: sum(row), axis=1)
print(total_runs_scored)

# COMMAND ----------

#Function
def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Optimal Pandas Looping

# COMMAND ----------

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Replacing iloc with Numpy Array

# COMMAND ----------

# DBTITLE 1,Original
win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

# COMMAND ----------

# DBTITLE 1,Using Numpy .values
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Compare 3 ways

# COMMAND ----------

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

# COMMAND ----------

# DBTITLE 1,Way 1: itertuples()
# MAGIC %%timeit
# MAGIC win_perc_preds_loop = []
# MAGIC
# MAGIC # Use a loop and .itertuples() to collect each row's predicted win percentage
# MAGIC for row in baseball_df.itertuples():
# MAGIC     runs_scored = row.RS
# MAGIC     runs_allowed = row.RA
# MAGIC     win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
# MAGIC     win_perc_preds_loop.append(win_perc_pred)

# COMMAND ----------

# DBTITLE 1,Way 2: apply()
# MAGIC %%timeit
# MAGIC # Apply predict_win_perc to each row of the DataFrame
# MAGIC win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# COMMAND ----------

# DBTITLE 1,Way 3: values --> fastest
# MAGIC %%timeit
# MAGIC # Calculate the win percentage predictions using NumPy arrays
# MAGIC win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
# MAGIC baseball_df['WP_preds'] = win_perc_preds_np
# MAGIC # print(baseball_df.head())
