package minecraftathon;

import org.bukkit.Location;
import org.bukkit.Sound;
import org.bukkit.World;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerEggThrowEvent;

public class EggEventListener implements Listener {

	@EventHandler
	public void onPlayerThrowEgg (PlayerEggThrowEvent event)
	{
		Location impactLocation = event.getEgg().getLocation();
		World world = impactLocation.getWorld();
		
		// create an explosion but don't wreck the blocks 
		world.createExplosion(impactLocation.getX(), 
				impactLocation.getY(), 
				impactLocation.getZ(), 
				3, 
				false, 
				false
				);
		
		// repeat a crazy cat sound
		for(int x=0; x<5;x++){
			world.playSound(impactLocation, Sound.CAT_MEOW, 10, 1);
		}

	}
	
}
