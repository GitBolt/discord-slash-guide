# Discord slash guide
Simple guide with examples to create Discord bot slash commands from scratch
in *Python* and *Rust* for people who are too lazy to read 
[Discord documentation](https://discord.com/developers/docs/interactions/application-commands)

### Important
Slash commands registration have rate limitings, and it's important to keep and eye on it during testing/development.<br>
The global rate limit is 200 application command registrations per day, per guild. <br>
For testing/development, create guild scoped slash commands as they are instant, while global slash command registration
may take upto one hour to spread across all servers.

### Structure
The examples are in **Python** and **Rust**, one folder for each
inside which there are files with one example each for **global** and **guild**
scoped slash commands.

```
├── python/    
│   |   ├── delete_commands.py/                                                       
│   │   ├── get_commands.py/    
│   |   ├── register_commands.py/                                                       
├── rust/
│   ├── src/     
│   │   ├── delete_commands.rs/  
│   │   ├── get_commands.rs/  
│   │   ├── main.rs/             'Main entry point, functions are called here'                                             
│   │   ├── register_commands.rs/  
│   |── Cargo.lock 
|   |── Cargo.toml          
└── README.md
```

### Working locally
Make sure to replace the example IDs when calling functions with yours.
#### Python
You should have `requests` module installed in order to test the functions. <br>
For the server, install the required packages from `requirements.txt` file
#### Rust
Just do `cargo run`
#### Environment variables
`TOKEN= ...` (You bot's token)
`PUBLIC_KEY= ...`(Your application public key from developer portal)
