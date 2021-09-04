# Discord slash guide
Simple guide with examples to create Discord bot slash commands from scratch
in *Python* and *Rust* for people who are too lazy to read 
[Discord documentation](https://discord.com/developers/docs/interactions/application-commands)
Rust one isn't completed yet btw

### Important
Slash commands creation have rate limitings, and it's important to keep and eye on it during testing/development.<br>
The global rate limit is 200 application command registrations per day, per guild.

### Structure
The examples are in **Python** and **Rust**, one folder for each
inside which there are files with one example each for **global** and **guild**
slash commands.

```
├── python/                                        
│   │   ├── get_commands.py/    
│   |   ├── register_commands.py/                                                       
├── rust/
│   ├── src/     
│   │   ├── main.rs/                    'Main entry point, functions are called here'                                             
│   │   ├── get_commands.rs/  
│   |── Cargo.lock 
|   |── Cargo.toml          
└── README.md
```
