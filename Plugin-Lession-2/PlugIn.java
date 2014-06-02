package minecraftathon;

import org.bukkit.plugin.java.JavaPlugin;
 

public final class PlugIn extends JavaPlugin {

    @Override
    public void onEnable(){
    	getLogger().info("MinecraftPlugin Lesson 2 mod has been invoked onEnable");	
    	
    	// initialize listeners
    	// note how we did the same thing tow different ways - which do you think is better?
    	
    	// init the egg listener
		getServer().getPluginManager().registerEvents(new EggEventListener(), this);
		
		// init the player listener
        new PlayerMoveListener(this);    	
    }
 
    @Override
    public void onDisable() {
		getLogger().info("MinecraftPlugin Lesson 2 mod has been disabled!");
        getServer().getPluginManager().disablePlugin(this);			
    }
}
