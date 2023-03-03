import ephem

def get_moon_position(location, date, time):
  # Set the observer location
  obs = ephem.Observer()
  obs.lon = location[0]
  obs.lat = location[1]
  obs.elevation = location[2]

  # Set the date and time
  obs.date = f"{date} {time}"

  # Calculate the moon position
  moon = ephem.Moon()
  moon.compute(obs)

  # Return the moon's altitude and azimuth
  return moon.alt, moon.az

# Example usage
location = (-2.6816552948061627, 50.790707850000004, 0)  # Longitude, latitude, elevation (in meters)
date = "2023/03/07"  # Year/month/day
time = "23:00:00"   # Hour:minute:second

alt, az = get_moon_position(location, date, time)
print(f"The moon's altitude is {alt} and azimuth is {az}.")


