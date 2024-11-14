from pyspark.sql import *
from config.definitions import DATA_DIR
from lib.logger import Log4j
from logging_config import setup_logging
import logging

if __name__ == "__main__":
    # Step 1: Set up logging
    setup_logging()

    # Step 2: Get the logger and use it
    logger = logging.getLogger(__name__)

    spark = SparkSession.builder \
        .appName("Spark File Reads") \
        .getOrCreate()

    #logger = Log4j(spark)
    logger.info("Starting Spark File Read")

    file_path = f"{DATA_DIR}/ratings.csv"

    ratings_df = spark.read.csv(file_path)
    ratings_df.show(truncate=False)

    spark.stop()
