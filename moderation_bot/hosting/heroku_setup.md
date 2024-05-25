heroku_setup.md
# Heroku Setup Guide

To host the moderation Discord bot on Heroku for 24/7 availability, follow these steps:

1. Create a Heroku account if you don't have one already.
2. Install the Heroku CLI on your local machine.
3. Login to Heroku using the command `heroku login`.
4. Create a new Heroku app using the command `heroku create`.
5. Set up the Discord API token as a Heroku environment variable by running `heroku config:set DISCORD_TOKEN=your_token_here`.
6. Add a MongoDB add-on to your Heroku app for data storage.
7. Deploy your bot to Heroku by pushing your code to the Heroku remote repository.
8. Scale the bot dyno to ensure it runs continuously with the command `heroku ps:scale worker=1`.

Your moderation Discord bot is now successfully hosted on Heroku for 24/7 availability.