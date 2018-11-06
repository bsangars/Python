-- Program to Find the Average of the Friends# by Age 
/* Sample Data 
1,Sam,25,280
2,Wil,25,20
3,Eva,30,40
4,Jam,35,200
5,Jil,30,120
6,Dre,35,20
*/

--Lets save the data in txt file Friends.txt

--Lets make a Function to Just Pull the Age and Friend Count Fields 3 and 4 

def parseLine(line:String) ={
  val fields=line.split(",")
  val age= fields(2).toInt
  val numFriends = fields(3).toInt
  (age,numFriends)
}


val lines = sc.textFile("../Workspace/Scala/Friends.txt")
val rdd = lines.map(parseLine)
//Returns (25,280) ,(25,20)....

-- Group by Age means reduceByKey then add the Count and 1
val TotalsbyAge = rdd.mapValues(x=>(x,1)).reduceByKey((x,y) => (x._1+y._1,x._2+y._2))

val Average = TotalsbyAge.mapValues(x=>x._1/x._2)

Average.foreach(println)
