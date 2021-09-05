use tokio;
mod get_commands;
mod register_command;
mod delete_command;
mod get_command;


#[tokio::main]
async fn main(){

    // get_commands::get_global_commands(884099662653562961).await.unwrap();
    // get_commands::get_guild_commands(884099662653562961, 845726630231932980).await.unwrap();

    // register_command::register_global_commands(884099662653562961).await.unwrap();
    // register_command::register_guild_commands(884099662653562961, 845726630231932980).await.unwrap();

    // delete_command::delete_global_command(884099662653562961, 1).await.unwrap();
    // delete_command::delete_guild_command(884099662653562961, 845726630231932980, 1).await.unwrap();

    // get_command::get_global_command(884099662653562961).await.unwrap();
    // get_command::get_global_command(884099662653562961, 1).await.unwrap();
}