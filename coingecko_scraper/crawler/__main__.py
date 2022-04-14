import os
import argparse
from . import COINGECKO_BOT


def main():

    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding arguments
    parser.add_argument("-pl", "--pageLimit", type=int, help = "Enter the page limit (ex: 20 to scrap page(0 - 19))")
    parser.add_argument("-pb", "--progressBar", type=bool, help = "Type True to enable progress bar (default: False)")
    parser.add_argument("-sd", "--showData", type=bool, help = "Type True to print data in terminal (default: False)")

    # Extracting argument value
    args = parser.parse_args()
    if args.showData is None:
        args.showData = False 

    # Initializing COINGECKO_BOT instance
    bot = COINGECKO_BOT(int(args.pageLimit), progress_bar=bool(args.progressBar))

    # Starting the scraping
    data = bot.scrap()

    # Prints data in terminal
    if args.showData:
        if len(data) > 0:
            for i in range(1, (len(data)//50)+1):
                print(data[(i*50)-50:i*50])
                cmd = input("Press Enter to continue or q to quit - ")
                os.system("cls") if os.name == 'nt' else os.system("clear")
                if cmd == "q":
                    break
        else:
            print(data)


if __name__ == "__main__":
    main()