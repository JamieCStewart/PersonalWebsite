# services/f1_telemetry.py
import io
import matplotlib.pyplot as plt
import fastf1

# Enable FastF1 cache
fastf1.Cache.enable_cache('cache_directory')

def get_telemetry_plot(year, driver, race):
    """Generate telemetry plot for a given year, driver, and race."""
    # Load the session data based on the inputs
    session = fastf1.get_session(year, race, 'R')  # 'R' is for the race session
    session.load()

    # Get laps and telemetry for the driver
    laps = session.laps.pick_driver(driver)
    fastest_lap = laps.pick_fastest()  # Pick the fastest lap
    telemetry = fastest_lap.get_car_data().add_distance()  # Add distance to telemetry

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))  # Optional: specify figure size
    ax.plot(telemetry['Distance'], telemetry['Speed'], label="Speed vs Distance")
    
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Speed (km/h)')
    ax.set_title(f'{driver} - {race} {year} Telemetry (Speed vs Distance)')
    ax.legend()

    # Save plot to a BytesIO object and return as PNG
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)

    return output
