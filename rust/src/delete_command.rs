use reqwest;
use serde_json;
use std::env;
use lazy_static::lazy_static;
use std::collections::HashMap;


lazy_static! {
    pub static ref TOKEN: String = env::var("TOKEN").unwrap();
}

#[allow(dead_code)]
pub async fn delete_global_command(application_id: i64, command_id: i64) 
    -> Result<(), Box<dyn std::error::Error>> {
    /*
    https://discord.com/developers/docs/interactions/application-commands#delete-global-application-command
    Delete a globally registered slash command.
    Takes the application(bot) ID as a single arguments.
    */

    let url: String = format!("https://discord.com/api/v9/applications/{}/commands/{}", 
                            application_id, 
                            command_id);
    let res = reqwest::Client::new()
        .delete(url)
        .header("Authorization", format!("Bot {}", *TOKEN))
        .send()
        .await?
        .text()
        .await?;
    
    let result = serde_json::from_str::<Vec<HashMap<String, serde_json::Value>>>(&res);
    
    println!("{:?}", result);
    Ok(())
}

#[allow(dead_code)]
pub async fn delete_guild_command(application_id: i64, guild_id: i64, command_id: i64) 
    -> Result<(), Box<dyn std::error::Error>> {
    /*
    https://discord.com/developers/docs/interactions/application-commands#delete-guild-application-command
    Delete a guild specfic registered slash command.
    Takes the application (bot) ID and guild ID respectively as arguments.
    */

    let url: String = format!("https://discord.com/api/v9/applications/{}/guilds/{}/commands/{}", 
                            application_id, 
                            guild_id, 
                            command_id);
    let res = reqwest::Client::new()
        .delete(url)
        .header("Authorization", format!("Bot {}", *TOKEN))
        .send()
        .await?
        .text()
        .await?;
    
    let result = serde_json::from_str::<Vec<HashMap<String, serde_json::Value>>>(&res);
    
    println!("{:?}", result);
    Ok(())
}

