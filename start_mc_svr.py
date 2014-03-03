#!/usr/local/bin/python


#
# required python libraries
#





import os, sys, time


class Minecraft_AutoStarter:

CONST_START_CMD="sudo java -Xmx512M -Xms512M -jar minecraft_server.1.7.2.jar nogui"
CONST_LOG_NAME="mc_start_log"

	#
	# constructor
	#

	def __init__(self):

		self.mc_logFileName=CONST_LOG_NAME
		self.mc_start_cmd=CONST_START_CMD


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
mc_starter.start( "sudo java -Xmx512M -Xms512M -jar /home/ec2-user/MinecraftServerTest/minecraft_server.1.7.2.jar nogui" )
mc_starter.deinit()

