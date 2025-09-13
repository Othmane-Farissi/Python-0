import time
import shutil


def format_time(seconds):
    """
    Format the given time in seconds as MM:SS.

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time in the format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of a progress bar similar to tqdm.

    Iterates through the given range and displays:
    - A progress bar that fills as items are processed
    - Percentage of completion
    - Current iteration count out of total
    - Elapsed time and estimated time remaining (ETA)
    - Processing speed in iterations per second

    Args:
        lst (range): The range to iterate through.

    Yields:
        Any: The current item from the input range.
    """
    total = len(lst)
    start_time = time.time()

    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed

        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)

        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item


def main():
    """
    Example usage of the custom ft_tqdm progress bar.

    Iterates over a range of numbers (0–333) while displaying
    the progress bar in the terminal.
    """
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()
