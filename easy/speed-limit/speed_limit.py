def total_miles_travelled(data):
    mph_vals = [row[0] for row in data]
    hour_vals = [row[1] for row in data]
    hour_diffs = [hour_vals[0]]
    for index, hour_val in enumerate(hour_vals[1:]):
        i = index+1
        hour_diffs.append(hour_val - hour_vals[i-1])
    total = 0
    for i in range(0, len(data)):
        total += mph_vals[i] * hour_diffs[i]
    return total

def get_data():
    import sys
    raw_data = sys.stdin.readlines()
    miles_data = []
    while (len(raw_data) > 0):
        num_rows = int(raw_data.pop(0))
        if num_rows == -1:
            break
        record = []
        for i in range(0, num_rows):
            row = raw_data.pop(0)
            tokenized = row.split()
            numbers = list(map((lambda s: int(s)), tokenized))
            record.append(numbers)
        miles_data.append(record)
    return miles_data

def main():
    data = get_data()
    for miles_data in data:
        total_miles = total_miles_travelled(miles_data)
        print("%d miles" % total_miles)

if __name__ == '__main__':
    main()
