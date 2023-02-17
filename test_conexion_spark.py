from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.master("spark://172.16.1.120:7077")
    .appName("SparkSessionEG") \
    .config("spark.mongodb.input.uri", "mongodb://172.16.1.41:27017,172.16.1.42:27017,172.16.1.43:27017/management-records.managementrecords/?replicaSet=haddacloud-rs") \
    .config("spark.mongodb.output.uri" "mongodb://Admin:T3c4dmin1.@172.16.1.228:27017/sparktest?authSource=admin") \
    .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.2') \
    .getOrCreate()
)

spark2 = SparkSession.builder\
        .master("spark://spark-01:7077/")\
        .appName("Test Setup")\
        .getOrCreate()

print(spark)
print(spark2)

df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()