import toml

with open("config.toml", "r") as file:
    toml_content = file.read()

parsed_toml = toml.loads(toml_content)
bot_token = parsed_toml.get("bot").get("token")
bot_guild = parsed_toml.get("bot").get("guild")
logo = """
                        Discord C2
                                                         c=====e
                                                            H
   ____________                                         _,,_H__
  (__((__((___()                                       //|     |
 (__((__((___()()_____________________________________// |C2   |
(__((__((___()()()------------------------------------'  |_____|


"""