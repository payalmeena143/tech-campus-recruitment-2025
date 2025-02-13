import os
import mmap
import re
from datetime import datetime
from bisect import bisect_left

LOG_FILE_PATH = "large_log_file.txt"

def parse_log_line(line):
    """Extract timestamp, log level, and message from a log line."""
    match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)", line)
    if match:
        timestamp_str, log_level, message = match.groups()
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S"), log_level, message
    return None, None, None

def find_log_start_position(log_file, target_time):
    """Use binary search (if log file is sorted) to locate the start position of logs."""
    with open(log_file, "r", encoding="utf-8") as f:
        file_size = os.path.getsize(log_file)
        left, right = 0, file_size
        
        while left < right:
            mid = (left + right) // 2
            f.seek(mid)
            f.readline()  # Move to the next full line

            pos = f.tell()
            line = f.readline()
            if not line:
                right = mid
                continue

            log_time, _, _ = parse_log_line(line)
            if log_time and log_time < target_time:
                left = pos  # Move right
            else:
                right = mid  # Move left

        return left  # Approximate position of the first relevant log

def retrieve_logs(start_time, end_time, log_levels=None):
    """Retrieve logs efficiently based on time range and severity."""
    start_pos = find_log_start_position(LOG_FILE_PATH, start_time)

    results = []
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as f:
        f.seek(start_pos)
        for line in f:
            log_time, log_level, message = parse_log_line(line)
            if log_time and start_time <= log_time <= end_time:
                if not log_levels or log_level in log_levels:
                    results.append(line)
            elif log_time and log_time > end_time:
                break  # Stop early if we've passed the end time

    return results

# Example Usage:
start_time = datetime(2024, 12, 1, 14, 20, 0)  # Start range
end_time = datetime(2024, 12, 1, 15, 0, 0)    # End range
log_levels = {"ERROR", "WARN"}  # Retrieve only ERROR and WARN logs

logs = retrieve_logs(start_time, end_time, log_levels)
for log in logs:
    print(log.strip())
