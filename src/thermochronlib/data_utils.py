"""
A module for reading, writing, and reducing data files.

"""

# Function for reading age data file
def read_age_data(file):
    """
    Read in age data from a csv file and store sample data.

    Parameters
    ----------
    file : str
        A character string with the relative path of the age data file.

    Returns
    -------
    ahe_data : list
        A list containing apatite (U-Th)/He age data.
    aft_data : list
        A list containing apatite fission-track age data.
    zhe_data : list
        A list containing zircon (U-Th)/He age data.
    zft_data : list
        A list containing zircon fission track age data.
    """
    # Make empty lists for column values
    ahe_age = []
    ahe_uncertainty = []
    ahe_eu = []
    ahe_radius = []
    aft_age = []
    aft_uncertainty = []
    zhe_age = []
    zhe_uncertainty = []
    zhe_eu = []
    zhe_radius = []
    zft_age = []
    zft_uncertainty = []

    # Read in data file and create nested lists of values
    with open(file, "r") as file:
        data = file.read().splitlines()
        for i in range(1, len(data)):
            # Split lines by commas
            data[i] = data[i].split(",")
            # Strip whitespace
            data[i] = [line.strip() for line in data[i]]
            # Append measured age data to lists
            if data[i][0].lower() == "ahe":
                ahe_age.append(float(data[i][1]))
                ahe_uncertainty.append(float(data[i][2]))
                # Append eU value if it exists, -1 if missing (keeps list lengths consistent)
                if len(data[i][3]) > 0:
                    ahe_eu.append(float(data[i][3]))
                else:
                    ahe_eu.append(-1)
                # Append radius value if it exists, -1 if missing (keeps list lengths consistent)
                if len(data[i][4]) > 0:
                    ahe_radius.append(float(data[i][4]))
                else:
                    ahe_radius.append(-1)
            elif data[i][0].lower() == "aft":
                aft_age.append(float(data[i][1]))
                aft_uncertainty.append(float(data[i][2]))
            elif data[i][0].lower() == "zhe":
                zhe_age.append(float(data[i][1]))
                zhe_uncertainty.append(float(data[i][2]))
                # Append eU value if it exists, -1 if missing (keeps list lengths consistent)
                if len(data[i][3]) > 0:
                    zhe_eu.append(float(data[i][3]))
                else:
                    zhe_eu.append(-1)
                # Append radius value if it exists, -1 if missing (keeps list lengths consistent)
                if len(data[i][4]) > 0:
                    zhe_radius.append(float(data[i][4]))
                else:
                    zhe_radius.append(-1)
            elif data[i][0].lower() == "zft":
                zft_age.append(float(data[i][1]))
                zft_uncertainty.append(float(data[i][2]))
            else:
                print(
                    f"Warning: Unsupported age type ({data[i][0].lower()}) on line {i + 1}.")

        # Create new lists with data file values
        ahe_data = [ahe_age, ahe_uncertainty, ahe_eu, ahe_radius]
        aft_data = [aft_age, aft_uncertainty]
        zhe_data = [zhe_age, zhe_uncertainty, zhe_eu, zhe_radius]
        zft_data = [zft_age, zft_uncertainty]

    return ahe_data, aft_data, zhe_data, zft_data
