#Vectors-----------------------------------

name <- "shivangee" , "praveen" , "actuators"

name <- c("shivangee" , "praveen" , "actuators")
length(name)
is.vector(name)
is.character(name)
is.numeric(name)
str(name)

a<- "actuators"
is.vector(a)

#coercing - a vector can only have single data type

age <- c(23,24,"25")
x <- c(23,24,FALSE)
y<- c(23,24,FALSE,"actuators")
print(y)
y
age<- as.numeric(age)
x
mean(x)

#other ways to create a vector

#sequential operator
a<- 1:100
length(a)
a

#sequence function
seq(from=6, to=24)
seq(from=6, to=24, by=2)
seq(6,24,2)

# store all values from 50 to 1
50:1
seq(50,1,by=-1)

#40 numbers between 1-60
seq(1,60,length=40)
(60-1)/(40-1)

seq(1,60,by=1.512821 ,length=40)
#cannot use by and length arguments together

#rep
d<- rep(10,times=100)
d
rep(c(2,3), times= 10)
rep(c(2,3), each= 10)

#numeric - only to repeat 0s
numeric(10)

#in built vector R
letters
LETTERS

#vector of vectors
x<- c(1,2,3)
y<- c(4,5,6)
c(x,y)

#basic funtions 
mean(x)
sum(x)
max(x)

x+y
x
y
x+2

#recycling of shorter vectors
x
z<- c(4,5)
z
x+z

y<- c(1,2,3,4)
y
z
y+z

x>3
x
x >= 2

#creating named vectors
age
names(age) <- c("a","b","c")
age
str(age)

names(age) <- c("a","b")
age

names(age) <- c("a","b", "c", "d") #error
age

#indexation

y <- c(34,67,56,45,89)
y
a[8] #position
y
y[4]

y[c(3,4)] 
y[2:4]

y[-3]
y[-c(3,4)] 

y
y[y>50]

#all values between 40 to 60 
y[y>=40 & y<=60]

x1<- y>=40 & y<=60
x1
y[x1]

#for named vectors
age
age["b"]
age[c("a","b")]

#paste function

actuators <- c("Hello","World")

paste("Hello","World")
paste("Hello","World",sep = ";")

paste(c("a","b"), c("c","d"))
paste(c("a","b"), c("c","d","e"))

paste(actuators)

paste("The ans is:",c("yes","no"))
paste("Yr",1:10)

paste("Yr",1:10, sep = "")
paste0("Yr",1:10)

paste("The ans is",c("yes","no"), collapse = " OR ")
#collapse is for separating two or more characters
#and getting it as a single character

paste("The ans is",c("yes","no"), collapse = " OR ", sep = "-")


