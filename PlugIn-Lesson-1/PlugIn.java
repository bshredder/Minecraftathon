package minecraftathon;


import org.bukkit.Bukkit;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.conversations.Conversable;
import org.bukkit.conversations.Conversation;
import org.bukkit.conversations.ConversationAbandonedEvent;
import org.bukkit.entity.Player;
import org.bukkit.plugin.java.JavaPlugin;
 

public final class PlugIn extends JavaPlugin {

    @Override
    public void onEnable(){
    	getLogger().info("MinecraftPlugin Lesson 1 mod has been invoked onEnable");	
    }
 
    @Override
    public void onDisable() {
		getLogger().info("MinecraftPlugin Lesson 1 mod has been disabled!");
        getServer().getPluginManager().disablePlugin(this);
    }
    

    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args){
  
    	// check if the command typed was "Lesson1" and be cool if they didn't get the case right
    	if(cmd.getName().equalsIgnoreCase("Lesson1")){ 
    		
    		// check that they specified a player - if not give them a little friendly grief
        	if(args.length == 0){
            	getLogger().info("Hey Minecraft rookie - you have to specify the player to torch ;-)");
            	return false;
        	}
        		
        	// get the object representing player they specified in the command
        	Player target = Bukkit.getServer().getPlayer(args[0]); 
        	
            // Make sure the player is online.
            if (target == null) {
                sender.sendMessage(args[0] + " is not currently online.");
                return true;
            }        	
        	
        	getLogger().info("Torching player" + target.getName() );
            
            // Set the player on fire for 500 ticks (there are ~20 ticks in second, so 25 seconds total).            
            target.setFireTicks(500);
        	
    		return true;
    	} //If this has happened the function will return true. 
    	
    	getLogger().info("MinecraftPlugin Lesson 1 mod basic command return false");
    	return false; 
    }
}
