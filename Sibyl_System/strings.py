on_string = """
「 Connected To Nexus System. 」
◦ Usᴇʀ: {name}
◦ Rᴀɴᴋ: {Enforcer}
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
$SCAN
「 Cʏᴍᴀᴛɪᴄ Sᴄᴀɴ Rᴇǫᴜᴇsᴛ! 」
**Eɴғᴏʀᴄᴇʀ:** {enforcer} 
**Usᴇʀ Sᴄᴀɴɴᴇᴅ:** {spammer}
**Rᴇᴀsᴏɴ:** `{reason}`
**Sᴄᴀɴ Sᴏᴜʀᴄᴇ:** {chat}
**Tᴀʀɢᴇᴛ Mᴇssᴀɢᴇ:** `{message}`
"""
forced_scan_string = """
$FORCED
**Iɴsᴘᴇᴄᴛᴏʀ:** {ins}
**Target:** {spammer}
**Rᴇᴀsᴏɴ:** `{reason}`
**Sᴄᴀɴ Sᴏᴜʀᴄᴇ:** {chat}
**Tᴀʀɢᴇᴛ Mᴇssᴀɢᴇ:** `{message}`
"""

reject_string = """
$REJECTED
**Crime Coefficient:** `Under 100`
Not a target for enforcement action. 
The trigger of Dominator will be locked.
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Rᴇᴀsᴏɴ**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
「 Lᴇᴛʜᴀʟ Eʟɪᴍɪɴᴀᴛᴏʀ 」
**Tᴀʀɢᴇᴛ Usᴇʀ:** {scam}
**Cʀɪᴍᴇ Cᴏᴇғғɪᴄɪᴇɴᴛ:** `Over 300`
**Rᴇᴀsᴏɴ:** `{reason}`
**Enforcer:** `{enforcer}`
**Cᴀsᴇ Nᴜᴍʙᴇʀ:** `{proof_id}`
"""

bot_gban_string = """
#DestroyDecomposer
**Enforcer:** `{enforcer}`
**Target User:** {scam}
**Reason:** `{reason}`
"""

# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
