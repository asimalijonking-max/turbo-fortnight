import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable set کریں")

WELCOME_TEXT = (
    "👋 Welcome to Aizen TG SMS\n\n"
    "⚡ Fast Number\n"
    "💎 Premium Rate\n"
    "🚀 Fast Response\n"
    "🔴 100% Safe\n\n"
    "نیچے سے کوئی option منتخب کریں:"
)


def main_menu() -> InlineKeyboardMarkup:
    """ویڈیو جیسا دو-column menu؛ stock اور Create Session شامل نہیں ہیں۔"""
    keyboard = [
        [
            InlineKeyboardButton("📱 numbers", callback_data="numbers"),
            InlineKeyboardButton("🔵 status", callback_data="status"),
        ],
        [
            InlineKeyboardButton("🚦 traffic", callback_data="traffic"),
            InlineKeyboardButton("💰 balance", callback_data="balance"),
        ],
        [InlineKeyboardButton("🌹 Refer & Earn", callback_data="refer")],
    ]
    return InlineKeyboardMarkup(keyboard)


def back_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙 Back to Menu", callback_data="menu")]]
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user else "User"
    text = f"{WELCOME_TEXT}\n\n👤 User: {name}"
    await update.message.reply_text(text, reply_markup=main_menu())


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_menu())


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "menu":
        await query.edit_message_text(WELCOME_TEXT, reply_markup=main_menu())
        return

    if query.data == "numbers":
        # User کی ہدایت کے مطابق ابھی countries، apps اور numbers نہیں دکھائے جاتے۔
        text = (
            "📱 Numbers\n\n"
            "⏳ یہ option ابھی تیار ہو رہا ہے۔\n"
            "Countries، apps اور numbers بعد میں شامل کیے جائیں گے۔"
        )
    elif query.data == "status":
        text = (
            "🔵 Status\n\n"
            "✅ Bot: Online\n"
            "✅ Service: Running\n"
            "🟢 Status: Active"
        )
    elif query.data == "traffic":
        text = (
            "🚦 Traffic\n\n"
            "📊 آج کا traffic: 0\n"
            "📈 Service ابھی active ہے۔"
        )
    elif query.data == "balance":
        text = (
            "💰 Balance\n\n"
            "💵 Current balance: 0.00\n"
            "💳 Balance system بعد میں connect کیا جا سکتا ہے۔"
        )
    elif query.data == "refer":
        user_id = query.from_user.id
        bot_username = context.bot.username or "your_bot"
        referral_link = f"https://t.me/{bot_username}?start=ref_{user_id}"
        text = (
            "🌹 Refer & Earn\n\n"
            "اپنے دوستوں کو invite کریں اور rewards حاصل کریں۔\n\n"
            f"🔗 آپ کا referral link:\n{referral_link}"
        )
    else:
        text = "❌ نامعلوم option"

    await query.edit_message_text(text, reply_markup=back_menu())


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Telegram update handle کرتے وقت error", exc_info=context.error)


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu_command))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_error_handler(error_handler)

    logger.info("Aizen-style bot شروع ہو گیا ہے")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
