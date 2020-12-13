## CS-UY 1114 — Lab 3
# Variables, Arithmetic, and Simple IO
#### September 24th & 25th, 2020

**All lab work must be submitted within 24 hours of the start of your lab period on Gradescope** (we will be checking
this using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a
solution before your allotted lab time, you will get no credit. You must try each problem at least once (that is,
submitting at least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the
problems and continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to
remember to submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab.

The programs at this point will be getting a bit more complicated, so please do not hesitate to check with your TAs if
you are ever confused as to how to proceed!

---

### Problem 1: The Volume of a Cone

As usual, let's start off with some simple stuff. In the file **[ConeVolume.py](ConeVolume.py)**, create a function
**`cone_volume`**, that will ask the use to enter _any **positive**_ values for the variables needed to calculate the
volume of a cone: its height and the radius of its base. The formula looks as follows:

![cone_volume](docs/images/cone_volume_formula.png)

_**Figure 1**: Formula for the volume of a cone with a circular base._

Once your program receives these two values from the user, it will calculate the resulting volume and print it out to
the user in **exactly** the following way:

```
Please enter a positive value for the height: 5
Please enter a positive value for the radius of the base: 10.0
The volume of a cone with a height of 5.0 and a base-radius of 10.0 is: 523.59878
```

For this problem, you may assume that the value of pi is 3.1416. Again, **your function must work for any and all
positive numerical values the user can enter.**

### Problem 2: Creating New Classrooms

You work for NYU's software engineering team, and you were tasked with creating a system that takes an existing number
of complete classes and students and creates new student distributions according the user's input. This what this looks
like in practice:

```text
How many students fit in each class? 25
How many full classes do you have at the moment? 1
How many students are left over at the moment? 10
How many students do you want your new classes to have? 30
Your new class distribution can form 1 new full class(es) with 5 left over student(s).
```

Here's another example:

```text
How many students fit in each class? 10
How many full classes do you have at the moment? 7
How many students are left over at the moment? 40
How many students do you want your new classes to have? 25
Your new class distribution can form 4 new full class(es) with 10 left over student(s).
```

As you can see, your system must work with any positive integer input. Do this in the
**[ClassDistributor.py](ClassDistributor.py)** file, in the function **`class_distributor`**.

### Problem 3: Fusing Two Schools

Let's augment our program from problem 2. Now, we have to fuse two student bodies into a single class-student
distribution. Here's what that looks like in practice:

```text
How many students fit in each class in school A? 60
How many full classes do you have at the moment in school A? 4
How many students are left over at the moment in school A? 10
How many students fit in each class in school B? 100
How many full classes do you have at the moment in school B? 4
How many students are left over at the moment in school B? 5
How many students do you want your new school's classes to have? 250
Your new class distribution can form 2 new full class with 155 left over student(s).
```

Write this program in the function **`new_school_class_distributor`**, inside the file
**[NewSchoolClassDistributor.py](NewSchoolClassDistributor.py)**.

### Problem 4: How old are Saturnians?

It takes Saturn approximately 10,759 Earth-days to orbit the sun. In the file
**[SaturnianToEarthAgeConverter.py](SaturnianToEarthAgeConverter.py)**, write a function
**`saturnian_to_earth_age_converter`** that will translate a Saturnian's age into Earth units. Take a look at the
sample behaviour below:

```text
How old is the Saturnian you are talking to? 10
This Saturnian is 294 Earth-years, 9 Earth-months, and 24 Earth-days old.
```

For this problem, you may assume that Earth-years are always 365 days long, and Earth-months are always 30 days long.

### Problem 5: How old are Earthlings?

Using the same assumptions about Earth units as in problem 4, can you write a program to determine your Saturnian age?
In this problem, you only need to determine Saturn-years. Here's the catch: Instead of entering the Earthling's age, you
enter their birthdate (the format is **[year][month][day]**):

```text
When was the Earthling you are talking to born on Earth? 19930315
This Earthling is 0.9204387024816433 Saturn-years old. How cute.
```

Do this in the function **`earth_to_saturnian_age_converter`**, inside the file
**[EarthToSaturnianAgeConverter.py](EarthToSaturnianAgeConverter.py)**.

**HINT**: You may not use any string methods in this problem, but modulo (`%`) and integer division (`//`) may come in
handy if you consider the birthdate (i.e. `19930315`) as an integer.
