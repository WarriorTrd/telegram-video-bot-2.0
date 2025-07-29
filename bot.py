import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from config import BOT_TOKEN, WEBHOOK_PATH, WEBHOOK_URL
from handlers.admin import register_admin_handlers
from handlers.handlers import register_handlers
from utils.stripe_webhook_handler import setup_stripe_webhook

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG


async def handle_root(request):
    return web.Response(text="Bot is running")


async def handle_webhook_get(request):
    return web.Response(text="Webhook is set up and working.")


async def on_startup(app):
    bot = app["bot"]
    webhook_url = WEBHOOK_URL + WEBHOOK_PATH
    logging.info(f"Setting webhook to {webhook_url}")
    try:
        await bot.set_webhook(webhook_url)
        webhook_info = await bot.get_webhook_info()
        logging.info(f"Webhook set successfully. Webhook info: {webhook_info}")
    except Exception as e:
        logging.error(f"Error setting webhook: {e}")


async def on_shutdown(app):
    bot = app["bot"]
    logging.info("Closing bot session")
    await bot.session.close()
    logging.info("Bot session closed")


async def handle_message(message: types.Message):
    try:
        await message.answer("Received your message")
    except Exception as e:
        logging.exception("Error in handle_message")  # Use logging.exception to include traceback


async def create_app():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    try:
        logging.info("Deleting webhook")
        await bot.delete_webhook(drop_pending_updates=True)
        logging.info("Webhook deleted")
    except Exception as e:
        logging.error(f"Error deleting webhook: {e}")

    register_handlers(dp)
    register_admin_handlers(dp)

    dp.message.register(handle_message)  # Register the handle_message function AFTER other handlers

    app = web.Application()
    app["bot"] = bot

    webhook_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)

    setup_stripe_webhook(app)

    app.router.add_route("*", "/", handle_root)
    app.router.add_get(WEBHOOK_PATH, handle_webhook_get)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app


async def main():
    app = await create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)

    logging.info("Starting web application")
    await site.start()

    try:
        # Run forever
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt received. Shutting down...")
    finally:
        logging.info("Cleaning up...")
        await runner.cleanup()
        logging.info("Cleanup complete. Exiting.")


if __name__ == "__main__":
    logging.info("Starting bot")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")
