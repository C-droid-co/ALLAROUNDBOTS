import os

BOT_TOKEN = os.environ.get('6105667765:AAEtfcWZwSes71Nqm58U817uS0Fd4QO66eo')
API_ID = int(os.environ.get('3848094'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BAA6t54AlTRqcwDspttaD1uHJdcdUeE7sc0N-tV83YIrqlOWSJ9xH2T5Rpjld-NnCWUxMcLU4smKNyIc9E-qas7igU4guWJYKBv4LrTwpBinNRgGQ807MjqAXaqVbsSjg9HlcNjfegv42_z3S5Y2CtcUvXVWupbMV7bslZVapGm6R-Z0V-Lkq4pvsC6ClwTRac1EaRuDpf3F1azKaGgC2OMcsRKjcXGnlwSxM2oktPxWBpiAQr_UM1020AefSpOpntGUqLycRxuVObaPPSGwhi2dhvkMlgm8wQkM3IgK_rVqlvERDqdVCUxvHjWLetlrVnhFDSDWi2z3ja_dWGcPwAlbnt3tKgAAAABDWcfeAA')
API_HASH = os.environ.get('b5be7dd84556db235436187271576566')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', 'christechy')
PHONE_NUMBER = os.environ.get('+2348164143260')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '1129957342').split()))
GBAN_LOG_GROUP_ID = int(os.environ.get('1001866150834'))
LOG_GROUP_ID = int(os.environ.get('1001866150834'))
MESSAGE_DUMP_CHAT = int(os.environ.get('1001866150834'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('mongodb+srv://Admin:Admin@cluster0.uyeijl5.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY')
ARQ_API_URL = os.environ.get('ARQ_API_URL', '')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
SLAP_STICKERS = list(map(str, os.environ.get('SLAP_STICKERS').split()))
