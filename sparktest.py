from pyspark.sql import SparkSession
from pyspark.sql import functions as F


# Initialize Spark session
spark = SparkSession.builder \
    .appName("DatabricksLocalPython") \
    .master("local[*]") \
    .getOrCreate()

# Example of using Spark to read a JSON file and show the data
df = spark.read.option("multiLine", "true").json("people.json")

# Flatten the 'people' array using explode
df_exploded = df.select(F.explode(df.people).alias("person"))

# Now, df_exploded will contain each person as a separate row
#df_exploded.show(truncate=False)

# Access fields in the nested JSON structure
df_exploded.select("person.name", "person.age", "person.city").show(truncate=False)


# Stop the Spark session
spark.stop()
