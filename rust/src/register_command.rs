/*
JSON body format
{
    "type": 1
    "name": "",
    "description": "",
    "options": [
        {
            "type": 1
            "name": "",
            "description: "",
            "required": False,
            "choices": [
                "name": "",
                "value": ""
            ],
            "options": [same format here]

        }
    ],
    "default_permission": True,
}

'type' (only in base command), 'default_permission', 'required' and 'options' 
fields are optional and have the default values as shown in the example.
'options' field can be used to create sub commands which isn't mandatory and 'type'
inside options is required to define what kind of option is it (usually a subcommand with value 1)

There are 3 'types' for the actual base command: 
https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types

and 10 'types' for the options:
https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type
*/


use reqwest;
use serde_json;
use std::env;
use lazy_static::lazy_static;
use std::collections::HashMap;


lazy_static! {
    pub static ref TOKEN: String = env::var("TOKEN").unwrap();
}

// No fields with default values are used
const EXAMPLE_COMMAND: &str = r#"{
        "name": "rustyfact",
        "description": "Shows a random Rust fact!"
    }"#;
    
#[allow(dead_code)]
pub async fn register_global_command(application_id: i64) 
    -> Result<(), Box<dyn std::error::Error>> {
    /*
    https://discord.com/developers/docs/interactions/application-commands#create-global-application-command
    Register slash commands globally.
    Takes the application(bot) ID as a single arguments.
    */

    let url: String = format!("https://discord.com/api/v9/applications/{}/commands", application_id);

    let res = reqwest::Client::new()
        .post(url)
        .body(EXAMPLE_COMMAND)
        .header("Authorization", format!("Bot {}", *TOKEN)) 
        .header("Content-Type", "application/json") 
        .send()
        .await?
        .text()
        .await?;
    
    let result = serde_json::from_str::<HashMap<String, serde_json::Value>>(&res);
    
    println!("{:?}", result);
    Ok(())
}


#[allow(dead_code)]
pub async fn register_guild_command(application_id: i64, guild_id: i64) 
    -> Result<(), Box<dyn std::error::Error>> {
    /*
    https://discord.com/developers/docs/interactions/application-commands#create-global-application-command
    Register slash commands to specific guilds.
    */

    let url: String = format!("https://discord.com/api/v9/applications/{}/guilds/{}/commands", application_id, guild_id);

    let res = reqwest::Client::new()
        .post(url)
        .body(EXAMPLE_COMMAND)
        .header("Authorization", format!("Bot {}", *TOKEN)) 
        .header("Content-Type", "application/json") 
        .send()
        .await?
        .text()
        .await?;
    
    let result = serde_json::from_str::<HashMap<String, serde_json::Value>>(&res);
    
    println!("{:?}", result);
    Ok(())
}
