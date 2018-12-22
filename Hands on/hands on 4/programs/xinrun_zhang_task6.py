from pyspark import SparkConf, SparkContext

from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

from pyspark.ml.linalg import DenseVector
from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Spark set-up
conf = SparkConf()
conf.setAppName("Logistic regression")

sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")

spark = SparkSession(sc)

# Load dataset file as RDD
rdd = sc.textFile("/user/spark/task5/task5.txt")
rdd = rdd.map(lambda x: x.split(','))

def renameLabel(x) :
	if x[4] == 'Iris-setosa':
		x[4] = 1
	elif x[4] == 'Iris-versicolor':
		x[4] = 2
	else:
		x[4] = 3
	return x

rdd = rdd.map(renameLabel)
rdd = rdd.map(lambda x: [float(x[0]), float(x[1]), float(x[2]), float(x[3]), int(x[4])]) 

# Create dataframe for ML model
df = spark.createDataFrame(rdd, ["sep_len", "sep_wid", "pet_len", "pet_wid", "class"])
data = df.rdd.map(lambda x: (DenseVector(x[:-1]), x[-1]))

df = spark.createDataFrame(data, ["features", "label"])

# Split data into train and test
train_data, test_data = df.randomSplit([.7,.3], seed=0)

# Declare ML model

rf = RandomForestClassifier(labelCol="label", featuresCol="features",numTrees=20)


# Train the model using training data

model = rf.fit(train_data)
# Check the model on test data
predicted = model.transform(test_data)
predictAndLabel = predicted.select("prediction", "label")
print(predictAndLabel.show(20))

# Model stats
evaluator = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy")

accuracy = evaluator.evaluate(predicted)
print("Error:"+str(1-accuracy))

