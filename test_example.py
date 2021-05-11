import os
from os import listdir
from os.path import isfile, join

#install with  pip install jpype1
import jpype

#Change JAVA_HOME to the path on your machine
JAVA_HOME = "/Library/Java/JavaVirtualMachines/jdk-15.0.2.jdk/Contents/Home/bin/java"


def get_extent_classpath():
    extent_path = "extentreports"
    jars = [f for f in listdir(extent_path) if isfile(join(extent_path, f))]

    classpath = ""
    for jar in jars:
        classpath += os.path.abspath("{}/{}:".format(extent_path, jar))
    return classpath

#Before every test suite
classpath = get_extent_classpath()
jpype.startJVM(JAVA_HOME, "-Djava.class.path=%s" % classpath)
print("-Djava.class.path=%s" % classpath)

ExtentReports = jpype.JClass('com.aventstack.extentreports.ExtentReports')
ExtentTest = jpype.JClass('com.aventstack.extentreports.ExtentTest')
LogStatus = jpype.JClass('com.aventstack.extentreports.Status')
ExtentSparkReporter = jpype.JClass('com.aventstack.extentreports.reporter.ExtentSparkReporter')


extent_spark_reporter = ExtentSparkReporter("test_report.html") #This is the name of the test report file
extent = ExtentReports()
extent.attachReporter(extent_spark_reporter)


#Before Every Test
test = extent.createTest("Test Case 1", "Sample description")

test.log(LogStatus.INFO, "Clicked on element 1")
test.log(LogStatus.INFO, "Clicked on element 2")
test.log(LogStatus.INFO, "Clicked on element 3")
test.log(LogStatus.INFO, "Clicked on element 4")
test.log(LogStatus.INFO, "Clicked on element 5")
test.log(LogStatus.INFO, "Clicked on element 6")
test.log(LogStatus.INFO, "Clicked on element 7")
test.log(LogStatus.PASS, "Step Passed")

#At the end of each test
extent.flush()

#Before Every Test
test = extent.createTest("Test Case 2", "Sample description")
test.log(LogStatus.INFO, "This step shows usage of log(logStatus, details)")
test.log(LogStatus.PASS, "")
test.log(LogStatus.FAIL, "Step Passed")
#At the end of each test
extent.flush()

#At the end of the test stuite
jpype.shutdownJVM()