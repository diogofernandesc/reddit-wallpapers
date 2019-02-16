# Usage guide

#### 1. You'll require a `praw.ini` file with the following contents:
Ensure you store this file in the same directory as the `reddit_ingest.py` script.
```
[earthporn]
client_id=This should be your own client_id
client_secret=This should be your own client_secret
```
You can get a client_id and client_secret for the Reddit API by the following the steps at:

https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps



#### 2. Create an environment variable in your `.bashrc` or `.zshrc` file:
This will be used to store the location of where you want your wallpapers to be saved
```
export REDDIT_IMAGE_STORAGE_PATH="/Path/to/wallpapers/here"
```
followed by `source .bashrc` for bash OR `source .zshrc` for zsh

#### 3. Right click your Mac desktop -> change desktop background
#### 4. Under folders, add the new folder which should point to the path you selected in step 2.

## Optional:
#### If you would like the script to check for new wallpapers on startup:
First, ensure the script is executable using
```
chmod +x startup_script.sh
```
Under System Preferences -> Users & Groups -> Login items, click the + icon and add the script to the list
