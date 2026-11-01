#!/usr/bin/env python3
"""
Simple Time Module Demo
"""

import time

print("Time Module Demo")
print("=" * 20)

# Current time
print(f"Current time (epoch): {time.time()}")

# Local time
local_time = time.localtime()
print(f"Local time: {time.asctime(local_time)}")

# Sleep demo
print("Sleeping for 1 second...")
time.sleep(1)
print("Awake!")

#Measure code execution time
start = time.perf_counter()
# Some sample work
for i in range(1000000):
    pass
end=time.perf_counter()

print(f"Execution time: {end-start} seconds")

print("Done!")
