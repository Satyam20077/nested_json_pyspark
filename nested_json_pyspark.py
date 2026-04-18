from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DoubleType,ArrayType
from pyspark.sql.functions import explode,col

#Build SparkSession
spark = SparkSession.builder\
        .appName("Readng Multi_Line_Json")\
        .master("local[*]")\
        .config("spark.driver.memory","4g")\
        .config("spark.executor.memory","4g")\
        .config("spark.sql.shuffle.partitions",32)\
        .getOrCreate()

#set LogLevel
spark.sparkContext.setLogLevel("ERROR")

#Schema Define
schema = StructType([
    StructField("user",StructType([
        StructField("id",IntegerType(),True),
        StructField("name",StringType(),True),
        StructField("email",StringType(),True),
        StructField("country",StringType(),True)
    ]),True),
    StructField("orders",ArrayType(
        StructType([
            StructField("order_id",IntegerType(),True),
            StructField("amount",DoubleType(),True),
            StructField("items",ArrayType(
                StructType([
                    StructField("item_id",IntegerType(),True),
                    StructField("product",StringType(),True),
                    StructField("price",DoubleType(),True)
                ])
            ),True)
        ])
    ),True)

])

#Reading Json
data = spark\
       .read\
       .schema(schema)\
       .option("multiLine",True)\
       .option("mode","PERMISSIVE")\
       .json("C:/Users/satya/PySpaak/nested_json_pyspark/nested_multiline_500.json")


#EXPLODE
data = data.withColumn("amount",explode("orders"))
data = data.withColumn("items",explode("amount.items"))


# #SELECT DATA
data =data.select(
    col("user.id").alias("USERID"),
    col("user.name").alias("USERNAME"),
    col("user.email").alias("EMAIL"),
    col("user.country").alias("COUNTRY"),
    col("amount.order_id").alias("ORDERID"),
    col("items.item_id").alias("ITEMID"),
    col("items.product").alias("PRODUCT"),
    col("items.price").alias("PRICE"),
    col("amount.amount").alias("AMOUNT")
)

data.show(truncate = False)
data.printSchema()
print(data.count())