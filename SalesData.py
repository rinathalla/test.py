import pandas as pd
dataset = pd.read_csv('sales_data_sample.csv',header=0,encoding = 'unicode_escape')
print(dataset.iloc[:10, :10])
"""  
 To print first 10 columns & 10 rows
 ORDERNUMBER  QUANTITYORDERED  PRICEEACH  ...  QTR_ID  MONTH_ID YEAR_ID
0        10107               30      95.70  ...       1         2    2003
1        10121               34      81.35  ...       2         5    2003
2        10134               41      94.74  ...       3         7    2003
3        10145               45      83.26  ...       3         8    2003
4        10159               49     100.00  ...       4        10    2003
5        10168               36      96.66  ...       4        10    2003
6        10180               29      86.13  ...       4        11    2003
7        10188               48     100.00  ...       4        11    2003
8        10201               22      98.57  ...       4        12    2003
9        10211               41     100.00  ...       1         1    2004

[10 rows x 10 columns]"""

dataset.head(5)
"""Out[45]: To print first 5 rows
   ORDERNUMBER  QUANTITYORDERED  ...  CONTACTFIRSTNAME  DEALSIZE
0        10107               30  ...              Kwai     Small
1        10121               34  ...              Paul     Small
2        10134               41  ...            Daniel    Medium
3        10145               45  ...             Julie    Medium
4        10159               49  ...             Julie    Medium
[5 rows x 25 columns]"""

dataset.tail(5)
"""Out[46]: To print first 5 rows
      ORDERNUMBER  QUANTITYORDERED  ...  CONTACTFIRSTNAME  DEALSIZE
2818        10350               20  ...             Diego     Small
2819        10373               29  ...            Pirkko    Medium
2820        10386               43  ...             Diego    Medium
2821        10397               34  ...           Annette     Small
2822        10414               47  ...              Juri    Medium
[5 rows x 25 columns]"""


dataset.describe()
"""Out[62]: 
        ORDERNUMBER  QUANTITYORDERED    PRICEEACH  ORDERLINENUMBER         SALES       QTR_ID     MONTH_ID     YEAR_ID         MSRP
count   2823.000000      2823.000000  2823.000000      2823.000000   2823.000000  2823.000000  2823.000000  2823.00000  2823.000000
mean   10258.725115        35.092809    83.658544         6.466171   3553.889072     2.717676     7.092455  2003.81509   100.715551
std       92.085478         9.741443    20.174277         4.225841   1841.865106     1.203878     3.656633     0.69967    40.187912
min    10100.000000         6.000000    26.880000         1.000000    482.130000     1.000000     1.000000  2003.00000    33.000000
25%    10180.000000        27.000000    68.860000         3.000000   2203.430000     2.000000     4.000000  2003.00000    68.000000
50%    10262.000000        35.000000    95.700000         6.000000   3184.800000     3.000000     8.000000  2004.00000    99.000000
75%    10333.500000        43.000000   100.000000         9.000000   4508.000000     4.000000    11.000000  2004.00000   124.000000
max    10425.000000        97.000000   100.000000        18.000000  14082.800000     4.000000    12.000000  2005.00000   214.000000
"""


dataset.sample(5)
"""Out[49]: Sampledata
      ORDERNUMBER  QUANTITYORDERED  ...  CONTACTFIRSTNAME  DEALSIZE
1113        10390               40  ...           Valarie    Medium
804         10107               29  ...              Kwai     Small
1525        10262               34  ...             Diego    Medium
1295        10177               35  ...             Jesus     Small
1817        10405               47  ...        Frederique     Small
[5 rows x 25 columns]"""



dataset.query('ORDERNUMBER > QUANTITYORDERED')
"""Out[55]: 
      ORDERNUMBER  QUANTITYORDERED  ...  CONTACTFIRSTNAME  DEALSIZE
0           10107               30  ...              Kwai     Small
1           10121               34  ...              Paul     Small
2           10134               41  ...            Daniel    Medium
3           10145               45  ...             Julie    Medium
4           10159               49  ...             Julie    Medium
5           10168               36  ...              Juri    Medium
6           10180               29  ...           Martine     Small
7           10188               48  ...            Veysel    Medium
8           10201               22  ...             Julie     Small
9           10211               41  ...         Dominique    Medium
10          10223               37  ...             Peter    Medium
11          10237               23  ...           Michael     Small
12          10251               28  ...           William    Medium

[2823 rows x 25 columns]"""


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
pd.isnull(dataset)
"""Out[61]: To findout missing values from table
      ORDERNUMBER  QUANTITYORDERED  PRICEEACH  ORDERLINENUMBER  SALES  ...  COUNTRY  TERRITORY  CONTACTLASTNAME  CONTACTFIRSTNAME  DEALSIZE
0           False            False      False            False  False  ...    False       True            False             False     False
1           False            False      False            False  False  ...    False      False            False             False     False
2           False            False      False            False  False  ...    False      False            False             False     False
3           False            False      False            False  False  ...    False       True            False             False     False
4           False            False      False            False  False  ...    False       True            False             False     False
5           False            False      False            False  False  ...    False       True            False             False     False
6           False            False      False            False  False  ...    False      False            False             False     False
7           False            False      False            False  False  ...    False      False            False             False     False
8           False            False      False            False  False  ...    False       True            False             False     False
9           False            False      False            False  False  ...    False      False            False             False     False
10          False            False      False            False  False  ...    False      False            False             False     False
11          False            False      False            False  False  ...    False       True            False             False     False
12          False            False      False            False  False  ...    False       True            False             False     False
13          False            False      False            False  False  ...    False       True            False             False     False
14          False            False      False            False  False  ...    False      False            False             False     False
15          False            False      False            False  False  ...    False       True            False             False     False
16          False            False      False            False  False  ...    False      False            False             False     False
17          False            False      False            False  False  ...    False      False            False             False     False
18          False            False      False            False  False  ...    False       True            False             False     False
19          False            False      False            False  False  ...    False       True            False             False     False
20          False            False      False            False  False  ...    False      False            False             False     False
21          False            False      False            False  False  ...    False      False            False             False     False
22          False            False      False            False  False  ...    False      False            False             False     False
23          False            False      False            False  False  ...    False       True            False             False     False
24          False            False      False            False  False  ...    False      False            False             False     False
25          False            False      False            False  False  ...    False      False            False             False     False
26          False            False      False            False  False  ...    False      False            False             False     False
27          False            False      False            False  False  ...    False      False            False             False     False
28          False            False      False            False  False  ...    False      False            False             False     False
29          False            False      False            False  False  ...    False       True            False             False     False
           ...              ...        ...              ...    ...  ...      ...        ...              ...               ...       ...

[2823 rows x 25 columns]"""


dataset.isnull().sum() #to check null values
FillNullValues=dataset.fillna('0')  #to fill null values with 0
FillNullValues.isnull().sum()


# Drop rows with missing values
dataset.dropna(axis=0)

# Drop columns with missing values
dataset.dropna(axis=1)

#guess the value that is most likely
dataset.interpolate()