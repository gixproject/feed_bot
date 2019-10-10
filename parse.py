import feedparser


def parse_rss(bot, call, url):
    message = 'Latest news:\n\n'
    feed = feedparser.parse(url)

    for post in range(5):
        message += (feed['entries'][post]['title'] +
                   '\n' + feed['entries'][post].link + '\n\n')
    message += '\nEnjoy :)'
    bot.send_message(call.chat.id, message, disable_web_page_preview=True)
