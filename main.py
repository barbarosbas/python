import sys
from lib.HttpClass import MyHttpClass
from lib.MyPrint import MyPrint
import os.path

try:
    
    if len(sys.argv) == 1:
        print("No input, please enter file name")
    elif not os.path.isfile(sys.argv[1]):
        print("File not found")
    else:
        HttpClass=MyHttpClass(sys.argv[1])
        #two method same ouput
        #HttpFlowFromTCP=HttpClass.GetHttpFlowFromTCP()
        HttpFlowFromHTTP=HttpClass.GetHttpFlowFromHTTP()
        HttpLength=HttpClass.GetHttpFlowLength()
        HttpTopHostAndCount=HttpClass.GetHttpTopHostandCount()

        Print =MyPrint()
        #Print.PrintHttpFlow(HttpFlowFromTCP)
        Print.PrintHttpFlow(HttpFlowFromHTTP)
        Print.PrintHttpLength(HttpLength)
        Print.PrintTopHost(HttpTopHostAndCount)

except Exception as e:
     print("Error occured:")  
     print(e)
 
   
