import ast
from datetime import datetime

logs = open("download_1.log").readlines()

formatted_logs = []
for log in logs:
    log_dict = ast.literal_eval(log.strip())
    log_dict["timestamp"] = datetime.strptime(log_dict["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
    formatted_logs.append(log_dict)

sorted_logs = sorted(formatted_logs, key=lambda x: x["timestamp"])

for i in range(1, len(sorted_logs)):
    if not sorted_logs[i - 1]["progress_percentage"] < sorted_logs[i]["progress_percentage"]:
        print(False)
        break

    if i == len(sorted_logs) - 1:
        print(True)
        break
