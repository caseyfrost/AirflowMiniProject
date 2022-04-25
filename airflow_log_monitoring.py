from pathlib import Path


def analyze_file(file):
    error_count = 0
    error_messages = []
    with open(file, 'r') as f:
        for line in f.readlines():
            if 'ERROR' in line:
                error_count += 1
                error_messages.append(line)
    return error_count, error_messages


def print_results(result):
    pass


# The folder where airflow should store its log files
# This path must be absolute
base_log_folder = r'/Users/caseyfrost/airflow/logs'

# marketvol log directory
log_dir = r'/Users/caseyfrost/airflow/logs/marketvol'

file_list = Path(log_dir).rglob('*.log')
for file in file_list:
    print(file)

errors = []
total_errors = 0

for file in file_list:
    count, cur_list = analyze_file(file)
    total_errors += count
    if len(cur_list) > 0:
        for error in cur_list:
            errors.append(error.strip('\n'))

print(total_errors)
for error in errors:
    print(error)
