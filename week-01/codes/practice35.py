spam = [
    "Bob 10 login",
   
    "Bob 25 login",
    "Bob 35 logout",
]


def processLogs(logs):
    memory = {}
    output = {}
    for item in logs:
        item = item.split()
        memory.setdefault(
            item[0], {"prev_state": "", "prev_time": 0, "total_time": 0, "sessions": 0}
        )
        if item[2] == "logout" and memory[item[0]]["prev_state"] == "login":
            memory[item[0]]["total_time"] += int(item[1]) - memory[item[0]]["prev_time"]
            memory[item[0]]["sessions"] += 1
        elif item[2] == "login" and memory[item[0]]["prev_state"] == "login":
            continue
        memory[item[0]]["prev_state"] = item[2]
        memory[item[0]]["prev_time"] = int(item[1])

    for k in memory.keys():
        output.setdefault(
            k,
            {"total_time": memory[k]["total_time"], "sessions": memory[k]["sessions"]},
        )
    return output


print(processLogs(spam))

# Corrections: I could have optimized this but recommended not to by one of my mentors(ChatGPT), as a proof for genuinivity in tracking my learning.
