from scapy.all import rdpcap
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP,TCP
from collections import Counter
class MyHttpClass:
    
    def __init__(self,sourceFile):
        #pcap file will bu used rest of the code
        self.pcapFile=rdpcap(sourceFile)

    #private method, called from GetHttpFlowFromTCP & GetHttpFlowFromHTTP method
    #verify whether flow is already in list or not
    def __IsFlowExist(self,flowList,tupleFlow):
        bl=True
        if len(flowList)==0:
            bl=True
        else:
            for t in flowList:
                #(1.1.1.1:4500 --> 2.2.2.2:80) and return traffic (2.2.2.2:80 --> 1.1.1.1:4500 is same flow)
                #set ignores tuple elements orders when making comparision
                if set(t) == set(tupleFlow):
                    bl=False
                    break
        return bl
    
    #private method, called from GetHttpFlowFromTCP & GetHttpFlowFromHTTP method

    def __GetHTTPFlowTunnel(self,packet):
        ip_src=packet[IP].src
        ip_dst=packet[IP].dst
        tcp_sport=packet[TCP].sport
        tcp_dport=packet[TCP].dport
        return (ip_src,tcp_sport,ip_dst,tcp_dport)
    

    #return Http Flows as list from TCP
    #each item in the list is a tuple
    #[(src_ip,src_port,dst_ip,sdt_port),(...) (...)]
    def GetHttpFlowFromTCP(self):
        # empty list to keep http flow, flow will be added as a tuple
        flow_list = []
        for packet in self.pcapFile:
            if packet.haslayer(TCP) and (packet.dport == 80 or packet.sport == 80  ):
                flow=self.__GetHTTPFlowTunnel(packet) #tuple
                if self.__IsFlowExist(flow_list,flow):
                    flow_list.append(flow) #list
        return flow_list
    
    #return Http Flows as list from HTTP, same output with the above method, different implementation
    #each item in the list is a tuple
    #[(src_ip,src_port,dst_ip,sdt_port),(...) (...)]
    def GetHttpFlowFromHTTP(self):
        # empty list to keep http flow, flow will be added as a tuple
        flow_list = []
        for packet in self.pcapFile:
            if  packet.haslayer(HTTPRequest):
                flow=self.__GetHTTPFlowTunnel(packet) #tuple
                if self.__IsFlowExist(flow_list,flow):
                    flow_list.append(flow) #list
        return flow_list
    

    #return (payload + header) as length
    def GetHttpFlowLength(self):
        total_len=0
        for packet in self.pcapFile:
            if packet.haslayer(TCP) and (packet.dport == 80 or packet.sport == 80  ):
                total_len=total_len+len(packet)
        return total_len


    #return top host and top host count values in a tuple
    # (top_host, top_host_count)
    def GetHttpTopHostandCount(self):
        host_list = []
        for packet in self.pcapFile:
            if  packet.haslayer(HTTPRequest):
                http_layer= packet.getlayer('HTTPRequest').fields
                #host=http_layer["Host"]# byte literal
                host = http_layer["Host"].decode("utf-8")# get Host value as a string 
                host_list.append(host)
        counter = Counter(host_list)
        top_host, count = counter.most_common(1)[0]
        return (top_host,count) 
    
    
    

    
