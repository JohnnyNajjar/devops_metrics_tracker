from pyspark.sql import SparkSession
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

def process_data():
    spark = SparkSession.builder.appName("SimpleSparkJob").getOrCreate()
    data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
    df = spark.createDataFrame(data, ["name", "age"])
    df_filtered = df.filter(df.age > 30)
    result = df_filtered.collect()
    logging.info(f"Filtered records: {result}")
    spark.stop()
    return result

if __name__ == "__main__":
    process_data()
