# Trianglebot

Pull contact info from a Google Sheet and serve it to Groupme on demand. Built for [Triangle UMN](http://triangleumn.com).

# Installation

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mplewis/trianglebot)

## 1. Initial Deploy to Heroku

1. Click the **Deploy to Heroku** button above.
1. Fill in `GROUPME_BOT_ID` with `DUMMY` for now. (You'll fill it in with real data later.)
1. Fill in the config variables as prompted by Heroku. You can leave the App Name blank.
1. Click **Deploy** to launch your app.
1. Wait for the deploy to complete.
1. Right click on the **View** button at the bottom and select **Copy Link Address**. This is the URL that points to your running Heroku app.

## 2. Create a Groupme Bot

1. Go to https://dev.groupme.com/bots and sign in.
1. Click **Create Bot**.
1. Give the bot a name. Optionally, give it a URL for an avatar.
1. Into **Callback URL**, paste your Heroku app URL from step 6.
1. Click **Submit**.

## 3. Configure Your Heroku App

1. Copy your **Bot ID** from the Groupme dashboard.
1. Go to [dashboard.heroku.com](https://dashboard.heroku.com) and click on the app you created.
1. Click the **Settings** tab.
1. Under **Config Variables**, click **Reveal Config Vars**.
1. Click the Edit pencil next to `GROUPME_BOT_ID`.
1. Paste your Bot ID into the **Value** field and click **Save Changes**.
