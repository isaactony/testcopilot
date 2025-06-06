# Parse a log entry and return a tuple (timestamp, level, message).
# Example log entry: "2025-06-02 09:00:00 - ERROR - failed to connect"
# Expected output: (datetime(2025,6,2,9,0,0), "ERROR", "failed to connect")
from datetime import datetime
import re
def parse_log_entry(entry: str):
    # Regular expression to match the log entry format
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)'
    match = re.match(pattern, entry)
    
    if not match:
        raise ValueError("Log entry does not match expected format.")
    
    timestamp_str, level, message = match.groups()
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    
    return timestamp, level, message

  
    

#test cases
def test_parse_log_entry():
    # Test case 1: Valid log entry
    entry = "2025-06-02 09:00:00 - ERROR - failed to connect"
    expected = (datetime(2025, 6, 2, 9, 0, 0), "ERROR", "failed to connect")
    assert parse_log_entry(entry) == expected

    # Test case 2: Another valid log entry
    entry = "2023-10-15 14:30:45 - INFO - user logged in"
    expected = (datetime(2023, 10, 15, 14, 30, 45), "INFO", "user logged in")
    assert parse_log_entry(entry) == expected

    # Test case 3: Invalid log entry format
    try:
        parse_log_entry("Invalid log entry")
    except ValueError as e:
        assert str(e) == "Log entry does not match expected format."
    
    print("All test cases passed!")