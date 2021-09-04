use tokio;
mod get_commands;

use get_commands::get_global_commands;


#[tokio::main]
async fn main(){

    println!(
        "{:?}", get_global_commands(792731230360961035).await
        );
}