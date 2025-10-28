import sys
from collections import Counter
from typing import List, Dict

LOG_LEVELS = ("INFO", "ERROR", "DEBUG", "WARNING")


def parse_log_line(line: str) -> Dict[str, str] | None:
    """
    Parse a log line in the format:
        YYYY-MM-DD HH:MM:SS LEVEL Message
    Returns a dict with keys: date, time, level, message.
    If the line does not match the expected format, returns None.
    """
    line = line.strip()
    if not line:
        return None

    parts = line.split(" ", 3)
    if len(parts) < 4:
        return None

    date, time, level, message = parts[0], parts[1], parts[2], parts[3]

    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message,
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs: List[Dict[str, str]] = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            logs = [p for line in f if (p := parse_log_line(line))]
    except Exception as e:
        print(f"Error: {e}")

    if not logs:
        print("Warning: no valid log entries found in the file.")

    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return list(filter(lambda r: r.get("level") == level.upper(), logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    counter = Counter(r["level"] for r in logs if r.get("level"))
    return {lvl: counter.get(lvl, 0) for lvl in LOG_LEVELS}


def display_log_counts(counts: Dict[str, int]) -> None:
    print("Log Level | Count")
    print("-----------------|------")
    for level in LOG_LEVELS:
        print(f"{level:<9} \t | {counts.get(level, 0)}")


def print_level_details(level: str, logs: List[Dict[str, str]]) -> None:
    print(f"\nLog details for level '{level.upper()}':")
    for r in logs:
        print(f"{r['date']} {r['time']} - {r['message']}")


def main():
    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "  python task03/main.py /path/to/logfile.log [level]\n"
            "Examples:\n"
            "  python task03/main.py log.txt\n"
            "  python task03/main.py log.txt error"
        )
        return

    file_path = sys.argv[1]
    requested_level = sys.argv[2] if len(sys.argv) >= 3 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if requested_level:
        level_norm = requested_level.upper()
        if level_norm not in LOG_LEVELS:
            print(
                f"\nWarning: level '{requested_level}' is not supported. "
                f"Available: {', '.join(LOG_LEVELS)}",
            )
            return

        lvl_logs = filter_logs_by_level(logs, level_norm)
        print_level_details(level_norm, lvl_logs)


if __name__ == "__main__":
    main()