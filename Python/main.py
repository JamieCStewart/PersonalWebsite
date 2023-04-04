import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import fastf1 as ff1
from fastf1.core import Laps
from fastf1 import utils
from fastf1 import plotting
plotting.setup_mpl()
from timple.timedelta import strftimedelta

ff1.Cache.enable_cache('/Users/jamie/Desktop/Uni/Year2/Coding/Cache')

abu_dhabi_qualification = ff1.get_session(2021, 'Abu Dhabi', 'Q')
print(abu_dhabi_qualification.date)

abu_dhabi_qualification.load();
abu_dhabi_qualification.results[:3]

abu_dhabi_race = ff1.get_session(2021, 'Abu Dhabi', 'R')

abu_dhabi_race.load();
laps_r = abu_dhabi_race.laps

print(laps_r['LapNumber'].max())

fastest_lap = laps_r.pick_fastest()
print(fastest_lap['Driver'])
