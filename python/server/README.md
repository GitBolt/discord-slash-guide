# Python webhook server
Discord will send a webhook request to our server whenever an interaction is received

## Interaction response structure
[Documentation](https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object)
Example format with all fields:
```json
{
    "type": 4,
    "data": {
        "tts": False,
        "content": "Example content",
        "embeds": [],
        "allowed_mentions": {
            "parse": [],
            "roles": [],
            "user": [],
            "replied_user": False
        },
        "flags": 1,
        "components": []
    }
}
```

**type**
Field determining the type of response, values:
- `1` = Ack a ping
- `4` = Message
- `5` = Ack and edit with loading state for users
- `6` = for components, ack and edit without loading state
- `7` = for components, edit the message
**data**
Response object, fields:
- `tts` = boolean, whether the response is tts or not
- `content` = string, actual message content
- `embeds` = array, [embed objects](https://discord.com/developers/docs/resources/channel#embed-object) with max amount as 10
- `allowed_mentions` = [allowed mentions object](https://discord.com/developers/docs/resources/channel#allowed-mentions-object)
- `flags` = integer, 1 << 6 for ephemeral
- `components` - array, [components object](https://discord.com/developers/docs/interactions/message-components)
