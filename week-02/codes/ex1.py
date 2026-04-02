logs = [
 "ERROR 2023-10-01: Failed at module1",
 "WARNING 2023-10-02: Low memory",
 "ERROR 2023-10-03: Failed at module2",
 "INFO 2023-10-04: Started process"
]

import re


def extract_warning(logs, level):
    result=[]
    pattern=rf"^({level}) (\d{{4}}-\d{{2}}-\d{{2}}): (.+)"

    for log in logs:
        match=re.search(pattern, log)
        if match:
            levell=match.group(1)
            date=match.group(2)
            message=match.group(3)
            result.append((levell, date, message))

    return result

print(extract_warning(logs, 'INFO'))
            
