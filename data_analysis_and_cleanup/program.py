from cmath import log
import pandas as pd
import datetime
from datetime import datetime
import json

for x in [10, 11, 12, 13, 14 ,15, 16, 17]:
    folder = "datas/" + str(x)

    def parse_date(s):
        f = "%Y-%m-%d"
        return datetime.strptime(s, f)

    pd.set_option('display.max_columns', None)

    rows = pd.read_csv(folder + "/raw.csv")

    with open(folder + "/map.json", 'r') as f:
        stops = json.load(f)

    print(", ".join( ["\"" + x[1] + "\"" for x in stops]))

    stopsDict = dict((stops[i][1], i) for i in range(len(stops)))
    trains = dict()

    for (_, row) in rows.iterrows():
        if not row.date in trains:
            current_train = dict([(s[1], 0) for s in stops] + [(s[1] + "_days_before_last_booking", -1) for s in stops])

            current_train["capacity"] = int(row.capacity)
            trains[row.date] = current_train
        else:
            current_train = trains[row.date]

            if current_train["capacity"] != row.capacity:
                raise Exception("Different capacities for same train")

        start = stopsDict[row.bp_from]
        stop = stopsDict[row.bp_to]

        x = start
        start = min(start, stop)
        stop = max(stop, x)

        train_date = parse_date(row.date)
        res_date= parse_date(row.res_dt)

        res_diff = (train_date - res_date).days

        if start > stop:
            raise Exception("Stop most not be smaller than start")

        for i in range(stop - start): # not plus one, the stop is exclusive
            current_train[stops[i + start][1]] += 1

            days_before_key = stops[i + start][1] + "_days_before_last_booking"
            if current_train[days_before_key] == -1:
                current_train[days_before_key] = res_diff
            else: current_train[days_before_key] = min(res_diff, current_train[days_before_key])

        trains[row.date] = current_train



    df = pd.DataFrame.from_dict(trains, orient="index")

    df.to_csv(folder + "/train_congestion.csv")