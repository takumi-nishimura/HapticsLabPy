# with open('sample.csv') as f:
#     d = f.read()
#     print(d)
    # reader = csv.reader(f)
    # for row in reader:
    #     print(row)

# import pandas as pd
# d = pd.read_csv('sample.csv',header=None)
# print(d)

# import csv
# a = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# with open('export.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(a)

# import pandas as pd
# a = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# df = pd.DataFrame(a)
# df.to_csv('export_df.csv', header=False, index=False)

class Counter:
    def __init__(self):
        self.__num = 0

    def count(self):
        self.__num += 1
        print(self.__num)

counter = Counter()
counter.count()