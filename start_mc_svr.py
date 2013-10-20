#!/usr/local/bin/python

# TODO list
#
# launch screen - independent shell program
# send email on status
#


#
# required python libraries
#





import os, sys, time


class Minecraft_AutoStarter:



	#
	# constructor
	#

	def __init__(self):

		self.mc_logFileName = "mc_start_log"
		self.mc_start_cmd = "sudo java -Xmx512M -Xms512M -jar minecraft_server.1.6.4.jar nogui"


	#
	# initialize 
	# 

	def init( self, logfile ):
		self.outFile = open( logfile, 'w' )
		self.log_msg( "init() end" )

	#
	# deinitialize
	#

	def deinit(self):
		self.log_msg( "deinit() start" )
		self.outFile.close()


	#
	# write message to log file
	#

	def log_msg( self, msg ):	
		self.outFile.write( msg )
		self.outFile.write( '\n' )

	#



	# create directory for MC server
	#

	def start( self, cmd_string ):
	  try:
		self.log_msg( 'start() start: ' + time.asctime(time.localtime()) )
		os.system( cmd_string )

		self.log_msg( 'start() end' )  
	  except:
		self.log_msg( "unhandled exception in start()"
 )
		self.log_msg( str(sys.exc_info()[0]) )




#
# main program
#

mc_starter = Minecraft_AutoStarter() 

mc_starter.init( "mc_start_log" )
mc_starter.start( "sudo java -Xmx512M -Xms512M -jar minecraft_server.1.6.4.jar nogui" )
mc_starter.deinit()

