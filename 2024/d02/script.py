
input_file = 'input.txt'

def is_safe(report: list) -> bool:
    # Acending
    if report[0] == sorted(report)[0]:
        prev = report[0]

        for n in report[1:]:
            if n < prev or n == prev or n > prev+3:
                return False
            prev = n
        
        return True

    # decending
    elif report[0] == sorted(report)[-1]:
        prev = report[0]

        for n in report[1:]:
            if n > prev or n == prev or n < prev-3:
                return False
            prev = n
        
        return True

def find_safe_reports(reports: list[list]):

    safe_reports = 0
    safe_reports_with_dampener = 0

    for report in reports:
        if is_safe(report):
            safe_reports += 1
            safe_reports_with_dampener += 1
        else:
            for i in range(len(report)):
                copy = report.copy()
                copy.pop(i)
                if is_safe(copy):
                    safe_reports_with_dampener += 1
                    break
        
    
    print(f"Number of safe reports: {safe_reports}")
    print(f"Number of safe reports with dampener: {safe_reports_with_dampener}")
    

def find_safe_reports_with_problem_dampener(li: list):
    pass

def main():

    reports = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            reports.append([int(n) for n in line.split()])

    find_safe_reports(reports)




if __name__ == '__main__':
    main()