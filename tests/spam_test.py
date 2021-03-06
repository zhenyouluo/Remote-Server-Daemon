
import socket, time
from struct import *

TAG_FIELD_LENGTH = 1 
LENGTH_FIELD_LENGTH = 4
HEADER_FIELD_LENGTH = 5
RECEIVEBUFFER_LENGTH = 2048

TAG = 93


def makeHeader(value):
 	return pack('>BI', TAG, value)


def readHeader(header):
	temp = unpack('>BI', header)
	return temp[1]


def sendToRSD(s, msg):
	header = makeHeader(len(msg))
	s.send(header)
	s.send(msg)


def receiveFromRSD(s):
	data = s.recv(RECEIVEBUFFER_LENGTH)
	header = readHeader(data[0:HEADER_FIELD_LENGTH])
	while(header > len(data)+HEADER_FIELD_LENGTH):
		temp = s.recv(RECEIVEBUFFER_LENGTH)	
		data += temp
	return data[HEADER_FIELD_LENGTH:header+HEADER_FIELD_LENGTH]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))

for i in range (2048):
  header = []
  
  print "unkown function"
  msg = "{\"jsonrpc\": \"2.0\", \"params\":  {\"port\": 0}, \"method\": \"Aardvark.aa_foo\", \"id\": 1}"
  sendToRSD(s, msg)
 

  print "unkown plugin"
  msg = ("{\"jsonrpc\": \"2.0\", \"params\":  {\"port\": 0}, \"method\": \"dfasdf.aa_open\", \"id\": 2}")
  sendToRSD(s, msg)
 
  print "no namespace but DOT"
  msg  =  ("{\"jsonrpc\": \"2.0\", \"params\":  {\"port\": 0}, \"method\": \".aa_open\", \"id\": 3}")
  sendToRSD(s, msg)

  print "parsing error"
  msg  =  ("{\"jsonrpc\": \"2.0\", \"params\":  \"port\": 0}, \"method\": \"aa_open\", \"id\": 5}")
  sendToRSD(s, msg)
 

  print "no id"
  msg  =  ("{\"jsonrpc\": \"2.0\", \"method\":  \"Aardvark.aa_unique_id\", \"params\" : { \"port\": 9 }}")
  sendToRSD(s, msg)
  
  # Msg for RSd 
  
  print "Requesting plugin list"
  msg  =  ("{\"jsonrpc\": \"2.0\", \"method\": \"RSD.showAllRegisteredPlugins\", \"params\" : { \"nothing\": 0 }, \"id\" : 95}")
  sendToRSD(s, msg)

  print "Requesting function list"
  msg  =  ("{\"jsonrpc\": \"2.0\", \"method\": \"RSD.showAllKownFunctions\", \"params\" : { \"nothing\": 0 }, \"id\" : 96}")
  sendToRSD(s, msg)

time.sleep(30)
s.close()
