# How to get the dates of yesterday, today and tomorrow?

import numpy as np

today = np.datetime64('today')
yesterday = today + np.timedelta64(-1)
tomorrow = today + np.timedelta64(1)
print(np.array((yesterday, today, tomorrow)))

# Unit argument — controls precision
np.datetime64('2026-05-08T10:30:45') # date and time
np.datetime64('today')             # current date
np.datetime64('now')               # current date and time
np.datetime64('2026-05-08', 'Y')   # year precision  → 2026
np.datetime64('2026-05-08', 'M')   # month precision → 2026-05
np.datetime64('2026-05-08', 'D')   # day precision   → 2026-05-08
np.datetime64('2026-05-08', 'h')   # hour precision  → 2026-05-08T00
np.datetime64('2026-05-08', 'm')   # minute precision
np.datetime64('2026-05-08', 's')   # second precision
np.datetime64('2026-05-08', 'ms')  # millisecond precision
np.datetime64('2026-05-08', 'us')  # microsecond precision
np.datetime64('2026-05-08', 'ns')  # nanosecond precision

# timedelta64 units:
np.timedelta64(1, 'Y')    # 1 year
np.timedelta64(6, 'M')    # 6 months
np.timedelta64(7, 'D')    # 7 days
np.timedelta64(24, 'h')   # 24 hours
np.timedelta64(30, 'm')   # 30 minutes
np.timedelta64(60, 's')   # 60 seconds
np.timedelta64(500, 'ms') # 500 milliseconds
np.timedelta64(1, 'ns')   # 1 nanosecond

