import re

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

import aiohttp


async def registration_start_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Welcome to PMS! Please enter your email\n Format: email@example.com"
    )
    return 1


async def registration_email_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    email = update.message.text
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        await update.message.reply_text(
            "Invalid email format. Please enter a valid email address."
        )
        return 1
    else:
        context.user_data["email"] = email
        await update.message.reply_text("Please enter your username")
        return 2


async def registration_username_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    username = update.message.text
    context.user_data["username"] = username
    await update.message.reply_text(f"Please enter your password")
    return 3


async def registration_password_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    password = update.message.text
    context.user_data["password"] = password
    await update.message.reply_text(f"Please enter your name\nFormat: John Doe")
    return 4


async def registration_name_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    context.user_data["name"] = name
    return await registration_success_handler(update, context)


async def registration_success_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://stask-bot.online:8000/api/v1/users/register",
            json=context.user_data,
        ) as response:
            if response.status == 200:
                await update.message.reply_text(
                    f"Registration successful!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="Follow link to continue ↗️",
                                    url=f"https://stask-bot.online/onboard/user/{user_id}/{email}",
                                )
                            ]
                        ]
                    ),
                )
        return ConversationHandler.END
