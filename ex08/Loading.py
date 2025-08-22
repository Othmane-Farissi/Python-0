import sys
import time

def ft_tqdm(iterable, total=None, desc=""):
    total = total if total is not None else len(iterable)
    count = 0

    for item in iterable:
        count += 1

        percent = (count / total) * 100
        bar_length = 30
        filled_length = int(bar_length * count // total)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        sys.stdout.write(
            f"\r{desc} |{bar}| {count}/{total} ({percent:.1f}%)"
        )
        sys.stdout.flush()
        yield item 
    sys.stdout.write("\n")
