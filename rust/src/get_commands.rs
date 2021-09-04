use reqwest;
use serde_json;
use std::env;
use lazy_static::lazy_static;
use std::collections::HashMap;


lazy_static! {
    pub static ref TOKEN: String = env::var("TOKEN").unwrap();
}


pub async fn get_global_commands(application_id: i64) 
    -> Result<(), Box<dyn std::error::Error>> {

    let url: String = format!("https://discord.com/api/v9/applications/{}/commands", application_id);
    let client = reqwest::Client::new();

    let res = client
        .get(url)
        .header("Authorization", format!("Bot {}", *TOKEN))
        .send()
        .await?
        .text()
        .await?;
    
    let result = serde_json::from_str::<HashMap<String, serde_json::Value>>(&res);
    
    println!("{:?}", result);
    Ok(())
}

