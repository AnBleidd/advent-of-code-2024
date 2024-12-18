file = "input_2.txt"
counter = 0
reports = []
def get_reports(file):
    with open(file, "r") as f:
        for line in f:
            report = line.strip().split()
            reports.append(report)
    return reports    

reports = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
print(reports)

for report in reports:
    levels = [int(num) for num in report.strip().split()] 
    print(levels)
    n = len(levels)
    is_safe = True
    
    for k in range(n-1):
        if abs(levels[k] - levels[k + 1]) < 1 or abs(levels[k] - levels[k + 1]) > 3:
            is_safe = False
            break  
        
        if levels[k] > levels[k+1]:
            continue
        elif levels[k] < levels[k+1]:
            continue
        else:
            is_safe = False
            break
    if is_safe == True:
        counter +=1
        
print(counter)

                
            