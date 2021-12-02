import time

COLORS = {
  "reset": "\x1b[0m",
  "red": "\x1b[31m",
  "green": "\x1b[32m",
  "yellow": "\x1b[33m",
  "blue": "\x1b[34m"
}

THOUSAND = 1000
MILLION = THOUSAND * 1000
BILLION = MILLION * 1000

SECOND = BILLION
MILLISECOND = MILLION
MICROSECOND = THOUSAND

def run(prefix, fn, data):
  try:
    start = time.perf_counter_ns()
    res = fn(data)
    end = time.perf_counter_ns()
    res = str(res).ljust(20)
    res = f"{COLORS['blue']}{res}{COLORS['reset']}"
  except Exception as e:
    end = time.perf_counter_ns()
    e = str(e).ljust(20)
    res = f"{COLORS['red']}{e}{COLORS['reset']}"
  finally:
    span = end - start
    print(f"{prefix}: {res} ({fmt_time(span)})")

def fmt_time(span):
  color = COLORS["green"]
  if span >= SECOND:
    color = COLORS["yellow"]
    if span >= 10 * SECOND:
      color = COLORS["red"]
    int_part = span // SECOND
    frc_part = (span % SECOND) // MILLISECOND
    return f"{color}{int_part}.{frc_part:03} sec{COLORS['reset']}"
  if span >= MILLISECOND:
    if span >= 100 * MILLISECOND:
      color = COLORS["yellow"]
    int_part = span // MILLISECOND
    frc_part = (span % MILLISECOND) // MICROSECOND
    return f"{color}{int_part}.{frc_part:03} ms{COLORS['reset']}"
  elif span >= MICROSECOND:
    int_part = span // MICROSECOND
    frc_part = span % MICROSECOND
    return f"{color}{int_part}.{frc_part:03} \u03BCs{COLORS['reset']}"
  else:
    return f"{color}{span} ns{COLORS['reset']}"
