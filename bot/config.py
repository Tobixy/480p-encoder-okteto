from bot.get_cfg import get_config
class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "AHCompressorBot")
    # AHCompressBot....
    # sucks Dude
    APP_ID = 11331366
    API_HASH = "6254b1f889fc35676a1a5c71d4259be3"
    LOG_CHANNEL = "Akatsuki_x_bot_support"
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
     # Get these values from my.telegram.org
    AUTH_USERS = {-1001751491174, 6263157611, 1424231015, 5715764478}
    
# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🤣
    # array to store the channel ID who are authorized to use the bot
    # dont u fucking remove this id 😤
    TG_BOT_TOKEN = "6957286840:AAH1cRtQMajYjlsd1S16DKH60l2-Mgxq3CU"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = "@Tobi480pbot"
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/4f9543c14158ff2dfaf62.jpg")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "💥")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "🚨")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
      # because, https://t.me/c/1494623325/5603
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", True)
