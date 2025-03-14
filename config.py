from typing import List, Dict
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Database Configuration
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Channel Configuration
DB_CHANNEL_ID = int(os.getenv("DB_CHANNEL_ID"))
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL"))

# Bot Identity
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_NAME = os.getenv("BOT_NAME")
BOT_VERSION = "1.1"

# Links
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
DEVELOPER_LINK = os.getenv("DEVELOPER_LINK")
SUPPORT_LINK = os.getenv("SUPPORT_LINK")

# Admins (Comma-separated IDs in .env)
ADMIN_IDS: List[int] = [
    int(admin_id.strip())
    for admin_id in os.getenv("ADMIN_IDS", "").split(",")
    if admin_id.strip().isdigit()
]

# Max upload size (2GB)
MAX_FILE_SIZE = 2000 * 1024 * 1024

# Supported Types & Extensions
SUPPORTED_TYPES = [
    "document", "video", "audio", "photo",
    "voice", "video_note", "animation"
]

SUPPORTED_EXTENSIONS = [
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    "py", "js", "html", "css", "json", "xml", "yaml", "yml",
    "zip", "rar", "7z", "tar", "gz", "bz2",
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov",
    "webm", "3gp", "m4v", "ogg", "opus",
    "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico",
    "apk", "exe", "msi", "deb", "rpm",
    "text", "log", "csv", "md", "srt", "sub"
]

SUPPORTED_MIME_TYPES = [
    "application/pdf", "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip", "application/x-rar-compressed",
    "application/x-7z-compressed", "video/mp4", "audio/mpeg",
    "audio/mp4", "image/jpeg", "image/png", "image/gif",
    "application/vnd.android.package-archive", "application/x-executable"
]

# UI Messages
class Messages:
    START_TEXT = """
🎉 **Welcome to {bot_name}!** 🎉

Hello {user_mention}! I'm your secure file sharing assistant.

🔐 **Key Features:**
• Secure File Sharing
• Unique Download Links
• Multiple File Types Support

📢 Join @InfoxRavi for updates!
👨‍💻 Contact @Unknown_RK01 for support

Use /help to see available commands!
"""

    HELP_TEXT = """
📚 **Available Commands** 

👤 **User Commands:**
• /start - Start bot
• /help - Show this help
• /about - About bot

👑 **Admin Commands:**
• /upload - Upload file (reply to file)
• /stats - View statistics
• /broadcast - Send broadcast
• Auto-Delete Feature:
Files are automatically deleted after the set time.
Use /auto_del to change the deletion time.

📝 **Supported File Types:**
• Documents (PDF, DOC, XLS, etc.)
• Videos (MP4, MKV, AVI, etc.)
• Audio (MP3, M4A, WAV, etc.)
• Images (JPG, PNG, GIF, etc.)
• Archives (ZIP, RAR, 7Z, etc.)
• Applications (APK, EXE, etc.)
• Other Formats

⚠️ For support: @Unknown_RK01
"""

    ABOUT_TEXT = """
ℹ️ **About {bot_name}**

**Version:** `{version}`
**Developer:** @Unknown_RK01
**Language:** Python
**Framework:** Pyrogram

📢 **Updates:** @InfoxRavi
🛠 **Support:** @Unknown_RK01

**Features:**
• Secure File Sharing
• Admin Controls
• Real-time Stats
• Multiple File Types
• Enhanced Security
• Automatic File Type Detection

Made with ❤️ by @Unknown_RK01
"""

    FILE_TEXT = """
📁 **File Details**

**Name:** `{file_name}`
**Size:** {file_size}
**Type:** {file_type}
**Downloads:** {downloads}
**Uploaded:** {upload_time}
**By:** {uploader}

🔗 **Share Link:**
`{share_link}`
"""

    FORCE_SUB_TEXT = """
⚠️ **Access Restricted!**

Please join our channel to use this bot:
Bot By @InfoxRavi

Click button below, then try again!
"""

# UI Buttons
class Buttons:
    def start_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Help 📚", "callback_data": "help"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK},
                {"text": "Developer 👨‍💻", "url": DEVELOPER_LINK}
            ]
        ]

    def help_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def about_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "Help 📚", "callback_data": "help"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def file_buttons(file_uuid: str) -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Download 📥", "callback_data": f"download_{file_uuid}"},
                {"text": "Share 🔗", "callback_data": f"share_{file_uuid}"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

# File Upload Progress
class Progress:
    PROGRESS_BAR = "█"
    EMPTY_PROGRESS_BAR = "░"
    PROGRESS_TEXT = """
**{0}** {1}% 

**⚡️ Speed:** {2}/s
**💫 Done:** {3}
**💭 Total:** {4}
**⏰ Time Left:** {5}
"""
