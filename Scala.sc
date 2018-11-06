-- Fibonacci Series Scala 
var a: Int = 0          
var b: Int = 1          
for (i <- 1 to 10) {
    println(a + " ")
    b += a
    a = b-a
}                       


-- String Function 
def convertUpper (x: String) : String = {
     | x.toUpperCase()
     | }

	 
=def transformInt (x: Int, f:Int => Int) : Int = {
     | f(x)
     | }

	 println(transformInt(3,x=> x*x*x))    // 27
	 
def lamdastr ( x: String, f:String => String) :String ={
f(x)
} 

println(lamdastr("hello this is smaller case", x=>x.toUpperCase()))


println(lamdastr("HELLO THIS IS UPPER CASE", x=>x.toLowerCase()))

-- Tuple 

var Tuple = ("Changed to x","Changed to y","Changed to z")
println(Tuple._1)
println(Tuple._2)
println(Tuple._3)

--List 

var SampleList = List("abc","pqr","xyz")
println (SampleList(1))
println (SampleList(2))

for (x <- SampleList) { println(x) }


-- map function to Reverse the String in List Map Function applies to all the values in the List
-- Applies a Function to the Whole RDD 

val backwardSampleList = SampleList.map((x:String) => {x.reverse})

for (x <-backwardSampleList) { println(x) }

-- Reduce Function 

val numberList = List (1,2,3,4,5,6)

val mul = numberList.reduce((x: Int, y:Int) => x*y)


-- Filter Function 
val noFives =  numberList.filter( (x:Int) =>x!=5)
println(noFives)

--Compact Code for Filter Function 

val NoThrees = numberList.filter(_ !=3)

val moreNum =  List(7,8,9,10)

val Numbers = numberList ++ moreNum

List functions 
List.max -- Gives max value
List.sorted  -- Sorted Values
List.reverse --reverses the Values from List 


-- Map (Key,Value)

var nummap = Map("a" -> 10, "b" -> 20, "c" -> 30, "d" -> 40)


-- Map Function for RDD 

val RDD = sc.parallelize(List(1,2,3,4,5))
val Square = RDD.map(x=>x*x)


     --Print an RDD use an collect Function if you want to limit the print use take function 
Square.collect().foreach(println)
Square.take(4).foreach(println)


