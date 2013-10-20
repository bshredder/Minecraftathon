#!/usr/local/bin/python


#
# required python libraries
#





import os, sys


class Minecraft_Installer:



	#
	# constructor
	#

	def __init__(self):
        	self.outFile = None
		self.mc_dirName = "MinecraftServerTest"


		self.mc_logFileName = "install_mc_log"
		self.mc_svr_url = "https://s3.amazonaws.com/Minecraft.Download/versions/1.6.4/minecraft_server.1.6.4.jar"


	#
	# initialize 
	# 

	def init( self, logfile, dir ):
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

	def create_mc_dir( self, dir_name ):
	  try:
		self.log_msg( 'create_mc_dir() start' )
		if not os.path.isdir( dir_name ):
	
			self.log_msg( "creating directory " + dir_name ) 	
			os.mkdir( dir_name  ) 
		os.chdir( dir_name )

		self.log_msg( 'create_mc_dir() end' )  
	  except:
		self.log_msg( "unhandled exception in create directory for MC server block"
 )
		self.log_msg( str(sys.exc_info()[0]) )


	#



	# download minecraft vanilla server to MinecraftServer directory

	#

	def download_svr( self, url ):
  	  try:
		self.log_msg( 'download_svr() start' )
		download_cmd_string = "wget " + url
		os.system( download_cmd_string )

		self.log_msg( 'version downloaded: ' + url )
		self.log_msg( 'download_svr() end' )
  	  except:
		self.log_msg( "unhandled exception in download MC server block"
 )
		self.log_msg( str(sys.exc_info()[0]) )

	#
	# install minecraft server
	#
	def install_mc( self ):
		self.create_mc_dir( self.mc_dirName )
		self.download_svr( self.mc_svr_url )



#
# main program
#

init_script = Minecraft_Installer()

init_script.init( "mc_install_log", "MinecraftServerTest"
 )
init_script.install_mc()
init_script.deinit()

