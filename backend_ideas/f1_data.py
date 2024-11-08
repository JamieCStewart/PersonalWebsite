import fastf1

# Enable cache for faster data access
fastf1.Cache.enable_cache('cache_directory')

# Load a session (e.g., 2023 Monaco GP race)
session = fastf1.get_session(2023, 'Monaco', 'R')

# Load data for the session
session.load()

# Get lap times for a specific driver
laps = session.laps.pick_driver('VER')  # E.g., for Max Verstappen

# Get telemetry data for a single lap
telemetry = laps.pick_fastest().get_car_data().add_distance()

# Plot the telemetry data
import matplotlib.pyplot as plt

plt.plot(telemetry['Distance'], telemetry['Speed'])
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.title('Max Verstappen - Fastest Lap Telemetry (Speed vs Distance)')
plt.show()
