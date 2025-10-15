def get_top_states_by_death_count(file_path, file_encoding='utf-8'):
    state_column = 1
    death_column = 19

    try:
        with open(file_path, 'r', encoding=file_encoding, newline='') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: Input file not found:", file_path)
        raise SystemExit(1)
    except UnicodeDecodeError as e:
        print(f"Error: Failed to decode file with encoding '{file_encoding}'.")
        raise SystemExit(1)
    except OSError as e:
        print("Error: Could not read the file:", e)
        raise SystemExit(1)

    lines = [line.strip() for line in lines if line.strip()]
    if len(lines) < 2:
        print("Error: The file has no data rows.")
        raise SystemExit(1)

    header = lines[0].split(',')
    data_rows = [line.split(',') for line in lines[1:]]

    state_deaths = {}

    for row in data_rows:
        if len(row) <= max(state_column, death_column):
            continue

        try:
            state_code = row[state_column].strip()
            death_str = row[death_column].strip()

            if not state_code:
                continue

            if death_str == '' or death_str.lower() == 'null':
                death_count = 0
            else:
                death_count = int(death_str)

            if state_code in state_deaths:
                state_deaths[state_code] += death_count
            else:
                state_deaths[state_code] = death_count

        except (ValueError, IndexError):
            continue

    if not state_deaths:
        return [], 0

    # Sort states by death count (highest first)
    sorted_states_by_deaths = sorted(state_deaths.items(), key=lambda x: x[1], reverse=True)

    # Return the top 5 states
    top_states = sorted_states_by_deaths[:5]

    return top_states


if __name__ == "__main__":
    # Example usage of the function
    file_path = "usscv19d.csv"  # Update with the actual file path
    top_states = get_top_states_by_death_count(file_path)

    if not top_states:
        print("No data found or processed successfully.")
    else:
        print("\nTop 5 States by COVID-19 Death Count")
        print("=" * 50)
        for state, death_count in top_states:
            print(f"{state}: {death_count:,} deaths")
