from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple

def readFile(file: Path) -> List[Tuple[str, str, str]]:
    readList = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if all(i):
                readList.append((i[0], i[1], i[2]))
            else:
                raise ValueError
        readList.pop(0) 
        return readList

def readAllFiles() -> List[SportClub]:
    fileCount = 0
    fileLineCount = 0
    csv_directory = Path('./')
    csvFiles = list(csv_directory.glob('*.csv'))
    finalList = []
    dictCounter = {}
    for file in csvFiles:
        try:
            tup_list = readFile(file)
            for tuple_ in tup_list:
                fileLineCount += 1
                if tuple_ not in dictCounter:
                    dictCounter[tuple_] = 1
                else:
                    dictCounter[tuple_] += 1
            fileCount += 1
        except ValueError:
            with open('error_log.txt', 'a') as file2:
                file2.write(str(file) + '\n')
    for i in dictCounter.keys():
        object = SportClub(i[0], i[1], i[2], dictCounter[i])
        finalList.append(object)
    with open('report.txt', 'w') as file1:
        file1.write(f'Number of files read: {fileCount}\n')
        file1.write(f'Number of lines read: {fileLineCount}\n')
    return finalList

