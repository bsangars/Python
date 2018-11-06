-- Program to Count The Ratings in Movie Database 

val sc = SparkContext("local[*]", "ProgramName" )
-- Not required if running in a  Spark-shell

--Load the Data from textFile to RDD 

val lines = sc.textFile("../somefile.data")

--You have an RDD with parallelized Data we just need the 3rd field of the line seperated by tab '\t'

val ratings  = lines.map(x=>x.toString().split("/t")(2))

-- Now you have all the ratings and deleted all the unwanted data 

val Count = ratings.countByValue()

--Sort the Values 

val Sorted = Count.toSeq.sortBy(_._1)

Sorted.foreach(println)




