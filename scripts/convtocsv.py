import os
import csv

with open("original.csv", "r") as orig_f:
    with open("m49.csv", "w") as res_f:
        reader = csv.DictReader(orig_f)
        writer = csv.DictWriter(res_f, fieldnames=["Country", "m49"])
        writer.writeheader()
        for row in reader:
            writer.writerow({"Country": row["Country or Area"], "m49": row["M49 Code"]})
