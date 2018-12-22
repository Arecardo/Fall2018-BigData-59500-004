# Command: spark-submit spark_std.py
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import SQLContext

# Spark set-up
conf = SparkConf()
conf.setAppName("Purchase App")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# uncomment the sc.setLoglevel line, when your program works fine. 
# Run the program again to take the screenshot.
#sc.setLogLevel("WARN")

# Upload data file in Hadoop and provide its path in textFile function
rdd = sc.textFile("/user/spark/task3/task3.txt")

# Add a few lines of code here to split 
# the attributes in each line, pick only required attributes,
# cast attributes type if needed.
rdd = rdd.map(lambda x: x.split('\t'))
rdd = rdd.map(lambda x: Row(city_name = x[2], profit = float(x[4])))

sqlContext = SQLContext(sc)
# Add code to convert RDD to dataframe
df = sqlContext.createDataFrame(rdd)

# create SQL table from data frame.
df.registerTempTable('ds_table')

# Write query using sqlContext.sql() function
result = sqlContext.sql("SELECT city_name, ROUND(AVG(profit), 2) AS avg_profit, ROUND(STDDEV_POP(profit), 3) AS stddev_profit FROM ds_table GROUP BY city_name")

# You may convert SQL dataframe in RDD
out = result.rdd.map(lambda x:x.city_name + '\t' + str(x.avg_profit) + '\t' + str(x.stddev_profit))
# and use it for pretty formatting as mentioned below
# city\t(average sale with 2 digits after decimal)\t(standard deviation in sale with 3 digits after decimal) 
# For example:
# Las Vegas	1200.56	23.321
out = out.collect()
# Then you can get the output in out variable display the results.	
#for item in out:
	#print(item[1]+':\t'+ str(item[2])+', '+ str(item[3]))
for n in out:
	print(n)



