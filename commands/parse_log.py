import os
import re


def parse_log(log_path):
    if not os.path.exists(log_path):
        return f"[red]The file [/red][turquoise2]{log_path}[/turquoise2] [red]does not exist[/red]"
    log_dir, log_file = os.path.split(log_path)
    error_dir = os.path.join(log_dir, 'error')
    warning_dir = os.path.join(log_dir, 'warning')
    os.makedirs(error_dir)
    os.makedirs(warning_dir)
    error_log = os.path.join(error_dir, 'errors.log')
    warn_log = os.path.join(warning_dir, 'warnings.log')

    with open(log_path, 'r') as file:
        with open(error_log, 'w') as errors, open(warn_log, 'w') as warnings:
            for line in file:
                if 'ERROR' in line:
                    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), ERROR: (.+)', line)
                    if match:
                        err_time = match.group(1)
                        err_msg = match.group(2)
                        errors.write(f'{err_time}: {err_msg}\n')
                elif 'WARNING' in line:
                    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), WARNING: (.+)', line)
                    if match:
                        warn_time = match.group(1)
                        warn_msg = match.group(2)
                        warnings.write(f'{warn_time}: {warn_msg}\n')
    return "[green]Log successfully parsed.[/green]"
