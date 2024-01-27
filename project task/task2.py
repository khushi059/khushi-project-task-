import sys

def convert_to_hours_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    if hours > 0:
      return f"{hours} hours, {minutes} minutes"
    else:
      return f"{minutes} minutes"

def analyze_cat_shelter_log(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    total_entries_ours = 0
    total_intrusions = 0
    total_time_ours = 0
    longest_visit = 0
    shortest_visit = float('inf')

    for line in lines:
        if line.strip() == 'END':
            break
        cat_type, entry_time, exit_time = line.strip().split(',')
        entry_time = int(entry_time)
        exit_time = int(exit_time)

        if cat_type == 'OURS':
            total_entries_ours += 1
            total_time_ours += exit_time - entry_time
            longest_visit = max(longest_visit, exit_time - entry_time)
            shortest_visit = min(shortest_visit, exit_time - entry_time)
        else:
            total_intrusions += 1
    
    average_duration = round(total_time_ours / total_entries_ours, 2) if total_entries_ours > 0 else 0
    
    print("Log File Analysis")
    print("==================")
    print("\n")
    print(f"Cat Visits: {total_entries_ours}")
    print(f"Other Cats: {total_intrusions}")
    print("\n")
    print(f"Total Time in House: {convert_to_hours_minutes(total_time_ours)}")
    print("\n")
    print(f"Average Visit Length: {convert_to_hours_minutes(average_duration)}")
    print(f"Longest Visit: {convert_to_hours_minutes(longest_visit)}")
    print(f"Shortest Visit: {convert_to_hours_minutes(shortest_visit)} ")


def main():
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        sys.exit(1)

    log_file = sys.argv[1]
    try:
        analyze_cat_shelter_log(log_file)
    except FileNotFoundError:
        print(f"Cannot open '{log_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
