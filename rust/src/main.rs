use tokio;
mod get_commands;
mod register_commands;


#[tokio::main]
async fn main(){

    // get_commands::get_global_commands(792731230360961035).await.unwrap();
    // get_commands::get_guild_commands(792731230360961035, 870330763772563476).await.unwrap();

    //register_commands::register_global_commands(792731230360961035).await.unwrap();
    //register_commands::register_guild_commands(792731230360961035, 870330763772563476).await.unwrap();
}