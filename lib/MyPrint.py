class MyPrint:
    def __init__(self) -> None:
        pass

    # takes argument as list and print Https Flow count and each item in it
    def PrintHttpFlow(self,flowList):
        print("HTTP Traffic Flows: "+str(len(flowList)) )
        print("HTTP Flows per connection :")
        for t in flowList:
            print(t)
    
    #print Http Bytes transmitted
    def PrintHttpLength(self,length):
        print("HTTP traffic bytes: "+str(length))
    
    #takes argument as tuple
    #first item is TopHost,second item is top host count
    def PrintTopHost(self,HttpTopHostAndCount):
        print("Top HTTP hostname : "+HttpTopHostAndCount[0] + "  Count:"+str(HttpTopHostAndCount[1]))
        