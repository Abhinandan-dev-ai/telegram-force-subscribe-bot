"""
Telegram Force-Subscribe Bot
Ensures users join a specified channel/group before using the bot.

Author: Abhinandan-dev-ai
License: MIT
"""

import os
import random
import logging
import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")  # Without '@', e.g. "mychannel"

if not BOT_TOKEN or not CHANNEL_USERNAME:
    raise ValueError("BOT_TOKEN and CHANNEL_USERNAME must be set in your .env file.")

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Tracks which funny messages have been shown to each user
user_message_tracker: dict[int, list[str]] = {}

# Bilingual funny messages shown to non-members
FUNNY_MESSAGES = [
    "I like your smartness, but don't be over-smart! Join {name} first! 😜",
    "Oh no! You forgot to join {name}. Do it now to access amazing content! 😅",
    "Be part of our amazing community at {name}! Join now or miss out! 🤓",
    "Smart people join {name} first! Don't be the odd one out! 😄",
    "Oops! Looks like you're not in {name} yet. Join us to continue! 🤭",
    "Aap bina {name} join kiye message kar rahe hain? Aise nahi chalega! 😆",
    "Sharma ji ka ladka {name} join kar chuka hai. Aap kab karenge? 😏",
    "Pehle {name} join karein, tabhi baat banegi! 🚀",
    "Dekha jaa raha hai ki aap humare {name} mein nahi hain. Please join! 😇",
    "Mujhe pata hai aapko join karna hai, to jaldi se {name} join karein! 😉",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

async def is_member(user_id: int) -> bool:
    """Check whether a user is a member of the configured channel."""
    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember"
        f"?chat_id=@{CHANNEL_USERNAME}&user_id={user_id}"
    )
    try:
        response = requests.get(url, timeout=10).json()
        return response.get("ok") and response["result"]["status"] in (
            "member",
            "administrator",
            "creator",
        )
    except (requests.RequestException, KeyError) as e:
        logger.error("Membership check failed: %s", e)
        return False


def get_unique_message(user_id: int) -> str:
    """Return the next unique funny message for a user, cycling through all before repeating."""
    if not user_message_tracker.get(user_id):
        shuffled = FUNNY_MESSAGES.copy()
        random.shuffle(shuffled)
        user_message_tracker[user_id] = shuffled

    return user_message_tracker[user_id].pop(0)


def progress_bar(percentage: int) -> str:
    """Generate a simple text-based progress bar."""
    filled = int(percentage / 10)
    bar = "█" * filled + "░" * (10 - filled)
    return f"[{bar}] {percentage}%"


def join_keyboard() -> InlineKeyboardMarkup:
    """Return the standard Join + Why Join keyboard."""
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
        [InlineKeyboardButton("ℹ️ Why Join?", callback_data="why_join")],
    ])


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start command — greet members, prompt others to join."""
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name

    if await is_member(user_id):
        await update.message.reply_text(
            f"🎉 Thank you for joining @{CHANNEL_USERNAME}, {first_name}! "
            "You can now use this bot. 😊"
        )
    else:
        message = get_unique_message(user_id).format(name=f"@{CHANNEL_USERNAME}")
        await update.message.reply_text(
            f"{message}\n\n{progress_bar(0)}",
            reply_markup=join_keyboard(),
        )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Block non-members from using the bot for regular messages."""
    user_id = update.effective_user.id

    if not await is_member(user_id):
        message = get_unique_message(user_id).format(name=f"@{CHANNEL_USERNAME}")
        await update.message.reply_text(
            f"{message}\n\n{progress_bar(0)}",
            reply_markup=join_keyboard(),
        )
    else:
        await update.message.reply_text(
            "🎉 Aap ne channel join kar liya hai. Ab aap bot ka use kar sakte hain! 😊"
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle inline button callbacks."""
    query = update.callback_query
    await query.answer()

    if query.data == "why_join":
        reasons = (
            "🌟 *Why Join Our Channel?* 🌟\n\n"
            "• 🎥 Access exclusive content\n"
            "• 📰 Get the latest updates first\n"
            "• 🎉 Be part of a growing community\n"
            "• 🚀 Unlock all bot features\n\n"
            "👉 Click below to join now!"
        )
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")]
        ])
        await query.edit_message_text(reasons, reply_markup=keyboard, parse_mode="Markdown")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    application.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
