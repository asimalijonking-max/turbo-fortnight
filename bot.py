import logging
import os

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable set کریں")

WELCOME_TEXT = """🖤 Welcome to Aizen TG SMS 🖤
WELCOME TO THE OFFICIAL BOT OF
Aizen TG SMS 🔥
━━━━━━━━━━━━━━━━━━
👤 Name: {name}
‼️ ID: {user_id}
━━━━━━━━━━━━━━━━━━
🔑 Fast Number —
💎 Premium Rate —
⏰ Fast Response —
🚫 100% Safe —"""


def main_menu() -> ReplyKeyboardMarkup:
    keyboard = [
        ["📞 numbers", "📶 status"],
        ["🎁 stock", "🔝 traffic"],
        ["💰 balance", "💗 Refer & Earn"],
        ["🟢 Create Session"],
    ]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        is_persistent=True,
        input_field_placeholder="Select an option",
    )


async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user else "User"
    user_id = user.id if user else "N/A"
    await update.message.reply_text(
        WELCOME_TEXT.format(name=name, user_id=user_id),
        reply_markup=main_menu(),
    )


async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    responses = {
        "📞 numbers": "📞 Numbers\n\n⏳ This option is coming soon.",
        "📶 status": "📶 Status\n\n✅ Bot: Online\n✅ Service: Running\n🟢 Status: Active",
        "🎁 stock": "🎁 Stock\n\n⏳ Stock service is coming soon.",
        "🔝 traffic": "🔝 Traffic\n\n📊 Today’s traffic: 0\n📈 Service is active.",
        "💰 balance": "💰 Balance\n\n💵 Current balance: 0.00",
        "💗 Refer & Earn": "💗 Refer & Earn\n\nInvite your friends and earn rewards.",
        "🟢 Create Session": "🟢 Create Session\n\n⏳ Session creation is coming soon.",
    }
    response = responses.get(text)
    if response:
        await update.message.reply_text(response, reply_markup=main_menu())


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", send_welcome))
    app.add_handler(CommandHandler("menu", send_welcome))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))
    logger.info("Aizen-style bot شروع ہو گیا ہے")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
