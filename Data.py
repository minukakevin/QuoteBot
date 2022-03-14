from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
Welcome to {}
You can use me to search quotes on different topics and great people any time you want. To know how to use me press 'How to Use' below.
By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Search a Quote ✨", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Search a Quote ✨", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Rawana_Developers")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/Rawana_Developers_Chat")],
    ]

    # Help Message
    HELP = """
**✨ Inline Mode ✨**
 
**1) Search Quotes**
Just pass the topic/name on which you wanna search quotes.
Example : `@QuoteBot Albert Einstein`
**2) Quote of the Day**
To get 'Quote of the Day' pass `#q` or `#qod`. You will get that for 5 different topics.
Example : `@BQuoteBot #qod`
**3) Random Quote**
To get a single random quote pass `#r` or `#random`.
Example : `@QuoteBot #random`
**4) A Single Quote**
By default, when you will use 1st option, you will get 20-30 quotes. But if you want only 1 random quote of that topic, use `#1` in end.
Example : `@QuoteBot Sushant Singh Rajput #1`
More features in development. Keep track by joining @Rawana_Developers.
    """

    # About Message
    ABOUT = """
**About This Bot** 
Bot created by https://t.me/Rawana_Developers which provides quotes from brainyquotes.com using Python.
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @Minukakevin
    """
