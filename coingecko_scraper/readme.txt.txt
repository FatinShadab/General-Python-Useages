The crawler can be user in 2 ways.

WAY 1:
----------------------------------------------------------------------------
In script:

#import and run.
#***In this case the data.json file will be created were the script is located.***

from crawler import COINGECKO_BOT

# Initializing COINGECKO_BOT instance
# progress_bar is by default False
# pass progress_bar=True to enable it.

bot = COINGECKO_BOT(pageLimit=int(input("Enter Page Limit: ")))

# Starting the scraping and store data to a variable
data = bot.scrap()



WAY 2:
----------------------------------------------------------------------------
By terminal/cmd
*** run this command to know valid options.
python -m crawler --help    

In windows :
================>
python -m crawler -pl 2 -pb True -sd True

or

python -m crawler --pageLimit 2 --progressBar False --showData False

In linux:
================>
python3 -m crawler -pl 2 -pb True -sd True

or

python3 -m crawler --pageLimit 2 --progressBar False --showData False

***In this case the data.json file will created were the terminal is located/opened.***