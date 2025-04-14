import datetime

print(type(datetime.date(2012,1,1) - datetime.date(2010,1,1)))

import itertools
print([i for i in filter(lambda x: x%5, 
                   itertools.islice(itertools.count(5),10))])