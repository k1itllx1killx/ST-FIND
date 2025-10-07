#!/usr/bin/env python3
# st-find.py (fixed)
import requests
import time
import datetime
import subprocess
import sys

# DEBUG -> si quieres traza extra pon True
DEBUG = False

# Colors
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"
USER_AGENT = "Mozilla/5.0 (Termux) Python Script"
DEFAULT_TIMEOUT = 8
DEFAULT_DELAY = 0.35

NETWORKS = {
    "1":  ("TikTok", "https://www.tiktok.com/@{}"),
    "2":  ("Instagram", "https://www.instagram.com/{}"),
    "3":  ("Facebook", "https://www.facebook.com/{}"),
    "4":  ("X (Twitter)", "https://x.com/{}"),
    "5":  ("YouTube", "https://www.youtube.com/@{}"),
    "6":  ("Snapchat", "https://www.snapchat.com/add/{}"),
    "7":  ("Reddit", "https://www.reddit.com/user/{}"),
    "8":  ("GitHub", "https://github.com/{}"),
    "9":  ("Pinterest", "https://www.pinterest.com/{}"),
    "10": ("Twitch", "https://www.twitch.tv/{}"),
    "11": ("LinkedIn", "https://www.linkedin.com/in/{}"),
    "12": ("Discord", "https://discordapp.com/users/{}"),
    "13": ("Telegram", "https://t.me/{}"),
    "14": ("WhatsApp", "https://wa.me/{}"),
    "15": ("Threads", "https://www.threads.net/@{}"),
    "16": ("BeReal", "https://bere.al/{}"),
    "17": ("Tumblr", "https://{}.tumblr.com"),
    "18": ("Steam", "https://steamcommunity.com/id/{}"),
    "19": ("Epic Games", "https://www.epicgames.com/id/{}"),
    "20": ("Xbox Live", "https://account.xbox.com/profile?gamertag={}"),
    "21": ("PlayStation Network", "https://my.playstation.com/{}"),
    "22": ("Roblox", "https://www.roblox.com/user.aspx?username={}"),
    "23": ("Minecraft", "https://namemc.com/profile/{}"),
    "24": ("Fortnite", "https://fortnitetracker.com/profile/all/{}"),
    "25": ("Call of Duty", "https://www.callofduty.com/{}"),
    "26": ("League of Legends", "https://www.op.gg/summoners/{}"),
    "27": ("Valorant", "https://tracker.gg/valorant/profile/riot/{}"),
    "28": ("Counter-Strike 2", "https://csgostats.gg/player/{}"),
    "29": ("Apex Legends", "https://apex.tracker.gg/apex/profile/origin/{}"),
    "30": ("PUBG", "https://pubglookup.com/player/{}"),
    "31": ("Free Fire", "https://ff.garena.com/profile/{}"),
    "32": ("Mobile Legends", "https://m.mobilelegends.com/profile/{}"),
    "33": ("Clash Royale", "https://royaleapi.com/player/{}"),
    "34": ("Clash of Clans", "https://www.clashofstats.com/players/{}"),
    "35": ("Among Us", "https://amongus.fandom.com/wiki/User:{}"),
    "36": ("Genshin Impact", "https://enka.network/u/{}"),
    "37": ("Honkai Star Rail", "https://starrailstation.com/profile/{}"),
    "38": ("Pokémon GO", "https://pokemongohub.net/profile/{}"),
    "39": ("Rocket League", "https://rocketleague.tracker.network/rocket-league/profile/epic/{}"),
    "40": ("Overwatch", "https://overwatch.blizzard.com/en-us/career/{}"),
    "41": ("Dota 2", "https://dotabuff.com/players/{}"),
    "42": ("Battlefield", "https://battlefieldtracker.com/bfv/profile/origin/{}"),
    "43": ("Rainbow Six Siege", "https://r6.tracker.network/profile/ubi/{}"),
    "44": ("FIFA / EA FC", "https://www.ea.com/fifa/ultimate-team/web-app/{}"),
    "45": ("NBA 2K", "https://nba2k.com/profile/{}"),
    "46": ("Chess.com", "https://www.chess.com/member/{}"),
    "47": ("Kick", "https://kick.com/{}"),
    "48": ("Rumble", "https://rumble.com/user/{}"),
    "49": ("OnlyFans", "https://onlyfans.com/{}"),
    "50": ("Patreon", "https://www.patreon.com/{}"),
    "51": ("SoundCloud", "https://soundcloud.com/{}"),
    "52": ("Spotify", "https://open.spotify.com/user/{}"),
    "53": ("Apple Music", "https://music.apple.com/profile/{}"),
    "54": ("Deezer", "https://www.deezer.com/profile/{}"),
    "55": ("Shazam", "https://www.shazam.com/artist/{}"),
    "56": ("Vimeo", "https://vimeo.com/{}"),
    "57": ("Dailymotion", "https://www.dailymotion.com/{}"),
    "58": ("BitChute", "https://www.bitchute.com/channel/{}"),
    "59": ("Medium", "https://medium.com/@{}"),
    "60": ("Quora", "https://www.quora.com/profile/{}"),
    "61": ("Stack Overflow", "https://stackoverflow.com/users/{}"),
    "62": ("9GAG", "https://9gag.com/u/{}"),
    "63": ("Imgur", "https://imgur.com/user/{}"),
    "64": ("DeviantArt", "https://www.deviantart.com/{}"),
    "65": ("Dribbble", "https://dribbble.com/{}"),
    "66": ("Behance", "https://www.behance.net/{}"),
    "67": ("ArtStation", "https://www.artstation.com/{}"),
    "68": ("Etsy", "https://www.etsy.com/shop/{}"),
    "69": ("eBay", "https://www.ebay.com/usr/{}"),
    "70": ("Amazon", "https://www.amazon.com/shop/{}"),
    "71": ("Mercado Libre", "https://www.mercadolibre.com.ar/perfil/{}"),
    "72": ("AliExpress", "https://www.aliexpress.com/store/{}"),
    "73": ("Shein", "https://www.shein.com/user/{}"),
    "74": ("Netflix", "https://www.netflix.com/{}"),
    "75": ("Disney+", "https://www.disneyplus.com/profile/{}"),
    "76": ("HBO Max", "https://www.max.com/profile/{}"),
    "77": ("Prime Video", "https://www.primevideo.com/profile/{}"),
    "78": ("Crunchyroll", "https://www.crunchyroll.com/user/{}"),
    "79": ("Hulu", "https://www.hulu.com/profiles/{}"),
    "80": ("VK", "https://vk.com/{}"),
    "81": ("WeChat", "https://www.wechat.com/{}"),
    "82": ("QQ", "https://user.qzone.qq.com/{}"),
    "83": ("LINE", "https://line.me/R/{}"),
    "84": ("Signal", "https://signal.me/#p/{}"),
    "85": ("Viber", "https://invite.viber.com/?g2={}"),
    "86": ("OK.ru", "https://ok.ru/{}"),
    "87": ("Clubhouse", "https://www.clubhouse.com/@{}"),
    "88": ("Mastodon", "https://mastodon.social/@{}"),
    "89": ("Bluesky", "https://bsky.app/profile/{}"),
    "90": ("Truth Social", "https://truthsocial.com/@{}"),
    "91": ("Parler", "https://parler.com/{}"),
    "92": ("Gab", "https://gab.com/{}"),
    "93": ("Koo", "https://www.kooapp.com/profile/{}"),
    "94": ("Substack", "https://substack.com/@{}"),
    "95": ("BitClout / DeSo", "https://bitclout.com/u/{}"),
    "96": ("Gaia Online", "https://www.gaiaonline.com/profiles/{}"),
    "97": ("Newgrounds", "https://{}.newgrounds.com"),
    "98": ("Taringa", "https://www.taringa.net/{}"),
    "99": ("Bandcamp", "https://{}.bandcamp.com"),
    "100":("Mixcloud", "https://www.mixcloud.com/{}")
}

BANNER = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣧⡽⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣟⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⡅⠹⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣂⣥⣼⡯⡐⢌⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠰⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⢳⡈⠻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠻⣿⣭⡟⡠⢞⣿⣿⣟⣛⠎⢦⡡⠈⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠋⠠⠸⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣳⡀⠈⠐⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⠟⠁⣴⡿⠋⠁⠀⠲⣶⡄⢧⠀⠸⡿⣻⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡏⠙⢁⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⣀⠈⠉⢻⣿⣿⣿⣿⣿⣿⣻⣿⣍⡛⠀⡟⠀⠀⠀⠀⠀⠀⠙⠘⠀⡀⢉⣻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣠⣐⡛⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠹⣶⣦⡀⠈⠓⢼⣿⠿⠿⠛⠉⠁⠀⠐⢀⣀⠀⣘⢡⠤⠂⠀⠀⡀⢰⠀⠉⠻⠼⢿⣿⠿⡿⠋⢁⣀⣾⣿⡿⠁⣰⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⢀⠀⢹⣿⣖⡄⣢⠄⠀⠀⠀⠀⠠⠐⢀⠂⠀⣿⢀⢹⣒⠍⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠉⠀⠠⣴⣿⣿⣿⣯⠅⢀⣉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣰⡆⠀⠻⡟⠋⠁⠀⠀⠀⠀⠀⢀⡥⣰⠅⢸⣿⢸⡘⠁⠀⠀⡆⠀⠀⠀⠹⣌⠃⠀⢀⠀⠀⠀⠀⠲⣯⣽⡏⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢧⣀⡛⠀⠀⠀⠀⠀⠀⠀⠠⢀⣿⡧⠜⠃⠀⣼⣿⠀⠀⡀⣧⢀⣿⠀⠀⢸⠠⢻⣧⡀⢿⣧⣀⠀⠀⠀⠀⠛⠀⢠⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣷⣶⡿⠃⠀⠀⠀⠀⣤⣄⡀⡾⢛⡋⠅⠀⣰⣿⣏⠐⢐⣽⣿⣿⣿⠀⠨⠠⠃⠃⠻⢗⡈⢿⣿⣷⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⣿⣿⣿⠏⠀⠀⠀⠀⠀⣾⣿⡟⠠⣪⡔⠂⠀⣴⣿⣿⠏⠁⠈⠙⢿⣿⣿⣧⠀⠚⢁⠐⢠⣿⣧⠸⣿⣿⣧⣀⢀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢚⣿⠃⠀⠀⠀⢀⡄⠀⠹⡿⠂⣰⠋⢄⢀⣼⣿⣿⡟⡈⠀⠃⠀⠀⠙⡙⠟⠘⢳⣎⠀⠟⣁⣼⡆⣿⣯⢿⠇⠀⡀⠀⠐⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ┃         ⚡ Multi Social Media Checker ⚡     ┃
⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⡌⠃⠀⠀⠀⠀⢸⡷⠀⠀⠃⢀⣴⢋⢂⣾⣿⣿⣿⡗⠀⠀⢄⠀⠀⠀⠘⠄⠸⡇⣿⡐⠌⠩⢭⣁⠸⢿⡖⠀⢸⣷⡀⠀⠀⠠⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ┃        🔎 Username Availability Finder       ┃
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠇⠀⠀⠀⢀⣴⣾⣇⣥⠀⠀⠌⡃⠎⣼⣿⣿⣿⡿⠁⠀⠀⢸⠀⠀⠀⠀⠀⠰⡧⣽⣧⢹⠘⢶⣌⠀⠶⠀⣠⣼⣿⣧⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ┃            Version: 2.0                      ┃
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⠀⠀⠀⢨⣭⣿⣶⡗⢰⢠⢐⠀⠁⠸⣿⣿⡟⠁⢀⠀⢳⢸⣧⠀⢰⡄⠀⢰⣧⢺⣿⠘⣗⠘⣿⣄⠀⢰⣽⣿⣿⣿⡄⠀⠀⢀⠀⠯⣿⣿⣿⣿⣿⣿⣿⣿  ┃            Created by: satan                 ┃
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠓⠀⠀⠀⠼⣿⣿⣿⣿⣿⠀⣈⢸⡄⠀⠈⠁⠠⠂⠈⡀⢸⠀⣿⠀⠸⠃⠀⢸⣿⢸⣿⡇⣿⢆⡇⣿⠀⠹⣿⣿⣿⣿⡻⠀⠀⠀⠀⠲⣿⣿⣿⣿⣿⣿⣿⣿  ┃                                              ┃
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠂⠀⢛⣿⡿⠋⠁⣠⣤⡈⠸⠀⠀⢲⠈⠿⠇⠃⠀⢸⠀⣿⠀⡀⠠⢈⠈⣿⣼⣿⣷⠈⠀⠇⠋⠀⣄⠀⠙⠻⢿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠠⠀⠀⠋⢁⣠⣴⣾⣿⣿⣉⡀⢁⠀⣦⡴⠃⠠⠂⠀⡊⠀⣿⡇⢅⠠⠠⠀⢹⣟⣿⣿⡀⠀⠀⢀⢸⣿⣤⣶⣄⡀⠁⠀⠀⠀⣘⣳⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠐⣿⣿⣿⣿⣿⢿⣛⣓⠀⠑⠈⠈⢙⠇⠀⠀⣰⠀⢸⣧⢸⠀⠀⢰⠀⣏⣿⣿⡇⠀⠀⠘⠘⣿⣿⣿⣏⣛⠀⠀⠀⠀⠣⣶⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣀⠀⠠⠀⠀⢿⣿⣿⣿⣿⣿⣿⡟⠰⠀⢀⡔⠁⠀⠀⠀⢺⠀⢸⣿⢸⡇⠀⣀⡀⠀⣿⣿⣿⠀⠀⠀⢠⣿⣿⣿⡟⠿⠠⠀⠀⢰⣄⣀⠙⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠀⣀⣰⣾⣯⠳⠀⠀⠀⠀⠛⠿⠛⠿⠿⠗⠀⣪⠖⠋⠀⠀⡆⡴⠀⣚⢠⢸⣿⡈⣇⠀⣿⠀⢸⣿⢻⣿⡄⠀⠀⠺⢼⢿⠿⠿⠃⠀⠀⢰⠀⠿⠿⠶⠀⠈⠙⠿⣤⡿⠿
⣿⡟⠁⠙⠁⢀⢀⡀⢀⣀⢀⡀⠀⣀⠀⠀⠀⠀⣤⣤⣤⡀⡤⠄⠀⠀⠀⠀⢀⡆⡇⢠⢹⠠⠈⣿⡇⣵⠀⡿⠀⣾⣿⡾⣿⣇⠰⠁⣀⣀⡀⣠⠀⠀⠀⠀⣤⣄⣠⠀⣤⡄⢠⣤⢠⠀⠉⠘
⣷⡬⠄⢠⣼⣿⣾⢷⠾⣿⢸⣿⣿⣧⣥⡀⠀⠀⠈⠻⣿⣯⣿⠇⠀⠀⠀⠅⡸⢀⡇⠘⢸⠘⡃⣿⣧⠘⠸⠃⠀⣿⣿⣯⡿⠿⠀⢸⣭⣿⣧⠃⠀⠀⠂⡴⣿⣿⣿⣘⣿⡇⢸⣿⠸⣦⣾⣿
⣿⣷⣶⣿⣿⣿⣿⣟⠀⣭⣈⣿⣿⣿⣿⡄⢠⡀⠀⠀⠙⢿⣿⠀⡀⠀⡘⢠⠇⢸⠀⠀⣿⡀⠁⢿⣿⠈⠈⠀⠀⠠⢍⢁⠀⠀⢀⣿⠿⠗⠁⠀⠀⢠⣾⣧⣿⣿⣿⣿⣿⡇⢸⣿⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣷⢀⠀⠀⠘⠛⠀⠀⢠⠁⡼⠀⣾⠀⠀⠿⡆⠂⢻⣿⡀⣇⠀⠀⠀⣄⠀⣀⠄⠸⠉⠀⠀⠀⠠⡎⢸⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⡇⢸⣿⢸⠗⠀⡀⠀⠀⡆⡎⢰⡏⢀⡇⢀⠃⡆⣷⠀⢸⣿⡇⠀⠀⠀⠀⠐⣄⠓⠀⠀⠀⠀⠀⣦⢨⣥⠼⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡇⣼⣷⠸⡇⠲⣶⣤⡀⠿⠀⣾⠁⠸⠀⢸⢀⡇⣿⠀⠈⣿⣿⠀⢐⣮⠀⠊⣿⠀⠂⣀⡀⣾⢐⡇⢸⣿⣶⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣈⢻⣾⠿⣤⣆⠘⢰⣷⣠⡇⠀⡎⢸⡇⢿⠀⠀⠹⠳⠇⢠⡏⠀⠈⢋⠀⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣻⣿⣿⣿⣽⣿⣿⣿⡀⢸⣿⣿⠀⢰⠃⢸⣟⢻⡆⠐⢦⡀⠈⠊⢰⠂⠀⠇⠀⣿⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⡷⠻⣿⣿⣿⠀⠈⠐⡟⠀⡞⠀⢸⢿⣾⡇⠀⠀⠑⠂⠀⠃⡠⠆⠀⠀⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣾⣿⣿⣿⡆⠀⢸⠁⣸⠁⠀⢸⣸⡿⡇⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⠃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⢀⡇⢰⠃⠀⠀⢾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠇⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⣻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢀⡟⠀⠀⡀⠘⢿⡬⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⠇⠈⢸⡇⠀⠰⠀⢠⠀⠙⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⠿⠀⢀⣿⠀⠀⡃⠀⠸⠄⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣹⣿⣿⣿⣿⣿⡿⠾⠟⢘⣿⠀⢸⠁⠀⠔⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⣶⣿⣿⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢚⡃⢐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⡛⢙⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡟⠻⣿⣷⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠛⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣵⠈⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣦⡟⢺⣿⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠘⠆⠈⠤⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣓⠐⠆⠋⣯⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⡧⢠⠄⠐⣦⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠀⠠⠀⠀⡀⢠⡂⠀⠘⠣⡾⢸⣿⣿⣽⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣷⣀⡰⡴⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⢂⠀⠰⠀⢢⠀⡐⢿⡇⢸⣉⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣆⡙⠛⣧⣔⠢⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢤⠈⠄⠀⠀⠀⢀⠚⢫⣙⠿⣶⢿⣄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡅⠀⣤⠍⡀⠂⠀⠀⠀⠀⢀⡐⠁⠀⠀⠀⠘⠆⠀⠀⣆⠘⠆⠀⠀⠀⠀⠂⡍⠀⡼⣾⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡌⠙⠃⠈⠭⠑⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠥⠊⠍⠛⢉⡽⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣽⣤⣶⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⡼⢟⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣴⣶⡖⢻⡟⠀⠀⠀⠀⠀⠈⣻⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣏⣿⣉⣹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣟⠙⣷⣶⣿⣻⣏⣻⣿⣿⣷⣤⣤⣤⣤⣤⣤⣶⣶⣖⣀⣰⣆⠀⠀⠀⠀⠀⠤⠾⠛⠛⠛⠛⠻⠛⠛⠛⠛⠛⠛⠛⠋⠉⠛⠛⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣷⣾⣿⣿⣶⣶⣶⣶⣶⣶⣾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

def now_ts():
    return datetime.datetime.now().strftime("%H:%M:%S")

def header_ts():
    return f"{BLUE}[{now_ts()}] [INFO]{RESET}"

def print_banner():
    try:
        subprocess.run(f"echo '{BANNER}' | lolcat", shell=True, check=False)
    except Exception:
        print(BANNER)

def print_searching(network_name):
    if network_name == "all selected networks":
        print(f"{header_ts()} [=] Finding name on all selected networks...")
    else:
        print(f"{header_ts()} [=] Finding name on {network_name}...")
    time.sleep(1)
    print(f"{header_ts()} [=] Checking if the name is available...")
    time.sleep(2.5)
    print(f"{header_ts()} [=] Reading request")
    time.sleep(2)

def check_profile(username, key, timeout=DEFAULT_TIMEOUT):
    """
    Return tuple: (key, network_name, status, meta)
    status: 'available' / 'taken' / 'unknown' / 'error'
    """
    name, template = NETWORKS[key]
    full_url = template.format(username)
    headers = {"User-Agent": USER_AGENT}
    try:
        if DEBUG:
            print(f"[DEBUG] GET {full_url}")
        r = requests.get(full_url, headers=headers, timeout=timeout, allow_redirects=False)
        code = r.status_code
        if code == 200:
            return key, name, "taken", code
        elif code in (301, 302):
            # often means redirect -> treat as taken
            return key, name, "taken", code
        elif code == 429:
            return key, name, "unknown", "rate_limited"
        elif code == 403:
            return key, name, "unknown", "forbidden"
        else:
            return key, name, "unknown", code
    except requests.RequestException as e:
        return key, name, "error", str(e)

def print_result(username, network_name, status, meta):
    if status == "available":
        print(f"{header_ts()} {GREEN}[+] Name available \"{username} ({network_name})\"{RESET}")
        time.sleep(1)
    elif status == "taken":
        print(f"{header_ts()} {RED}[-] Name taken \"{username} ({network_name})\"{RESET}")
        time.sleep(1)
    elif status == "unknown":
        print(f"{header_ts()} {YELLOW}[?] Unknown for \"{username} ({network_name})\" (meta: {meta}){RESET}")
    else:  # error
        print(f"{header_ts()} {YELLOW}[?] Error checking \"{username} ({network_name})\" (err: {meta}){RESET}")
        time.sleep(1)

def run_checks_all_networks(username, delay=DEFAULT_DELAY):
    print(f"{header_ts()} [=] Starting scan for \"{username}\" across {len(NETWORKS)} networks...")

    # 👇 Mostrar mensajes de "Finding name..." solo una vez
    print_searching("all selected networks")

    # Iterar por las redes
    for key in sorted(NETWORKS.keys(), key=lambda x: int(x)):
        network_name = NETWORKS[key][0]
        key_res, network_name_res, status, meta = check_profile(username, key)
        print_result(username, network_name_res, status, meta)
        time.sleep(delay)

    print(f"{header_ts()} Checks finished.")

def main():
    # banner
    try:
        subprocess.run("clear", shell=True)
    except:
        pass
    print_banner()
    username = input(f"{ORANGE}Enter the username to check (no @): {RESET} ").strip()

    if not username:
        print(f"{header_ts()} No username entered. Exiting.")
        return

    run_checks_all_networks(username)

    # debug print to confirm variable exists
    if DEBUG:
        print(f"[DEBUG] username variable = '{username}'")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{header_ts()} Interrupted. Exiting.")
        sys.exit(0)
