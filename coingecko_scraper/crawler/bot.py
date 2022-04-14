import os
import time
import json
import requests
from tqdm import tqdm
from datetime import datetime
from bs4 import BeautifulSoup as bs


class COINGECKO_BOT:
    """ A class to scrap data from 'coingecko' website. """

    def __init__(self, pageLimit, progress_bar=False):
        """ Initialize a BOT class object. """

        self.page_number = 0                # Used to get volume data 
        self.volume_only_50 = 0             # Used to get volume data
        self.pageLimit = pageLimit          # web page to scrap
        self.prograss_bar_enabled = progress_bar        # Used to show progress bar
        self.initialize_time = datetime.now().strftime("%m/%d/%Y_T(h=%H,m=%M,s=%S)").replace("/", "-")   #DateTime to create unique fname
        self.fname = f"data{self.initialize_time}.json"      # Unique file name

    def __get_soup(self, page=None, _url=None):
        """ This private method handles connection requests and get bs4 soup """

        # Get response from target url
        if page is not None:
            try:
                url = f"https://www.coingecko.com/en/exchanges/pancakeswap/show_more_tickers?page={page}&per_page=50&verified_ticker=true&ticker_type=undefined"
                response = requests.get(url)
            except:
                print(f"Faced problem with the request url: {url}!! retrying in 10s")
                time.sleep(10)
                self.__get_soup(page=page)
        else:
            try:
                url = _url
                response = requests.get(url)
            except:
                print(f"Faced problem with the request url: {url}!! retrying in 10s")
                time.sleep(10)
                self.__get_soup(_url=_url)

        # Check for valid response and creates bs4 soup
        if response.status_code >= 200 and response.status_code < 300:
            soup = bs(response.content, 'html.parser')
        else:
            print(f"Faced Error with status code {response.status_code} !! retrying in 10s")
            time.sleep(10)
            if page is not None:
                self.__get_soup(page=page)
            else:
                self.__get_soup(_url=_url)

        return soup

    def __write_data(self, data):
        """ This private method write's data of per row to a json file.  """

        # Check's if the json file exit's and empty or not.
        if os.path.isfile(self.fname) and os.path.getsize(self.fname) > 0:  
            # If the file has pre-stored data it will update the data.
            with open(self.fname, "r") as f:
                stored_data = json.load(f)
                for d in data:
                    stored_data.append(d)
            with open(self.fname, "w") as f:
                json.dump(stored_data, f, indent=4, sort_keys=True)
        else:
            # Create's the file and entry data
            with open(self.fname, "w") as f:
                json.dump(data, f, indent=4, sort_keys=True)

    def __get_data(self):
        """ This private method read's data from file and returns it as python list """
        try:
            with open(self.fname, "r") as f:
                stored_data = json.load(f)
        except:
            stored_data = []

        return stored_data

    def __get_trust_score(self, color):
        """ This private method get trust_score data by 'css' class """

        if color == "text-green":
            return "high"
        elif color == "text-warning":
            return "medium"
        else:
            return "low"

    def __get_liveChatUrl_data(self, data, liveChatUel):
        """ This private method scrap's selected data from live chat url. """

        soup = self.__get_soup(_url=liveChatUel)    # Get's the html soup from live-chat url.
        trs = soup.find_all("tr")                   # Collect all 'tr' tags.

        # Storing all selected data from html soup to 'data (type: dict)'. 
        data["market_cap"] = trs[4].find("span", "text-gray-900 dark:text-gray-200 font-medium").string.replace("\n", "")
        data["chains"]["binance"]["24h_volume"] = trs[3].find("span", "text-gray-900 dark:text-gray-200 font-medium").string.replace("\n", "")
        data["chains"]["binance"]["pairs"]["_"]["liquidity"] = trs[2].find("span", "text-gray-900 dark:text-gray-200 font-medium").string.replace("\n", "")
        data["chains"]["binance"]["pairs"]["_"]["price_change_24_hour"] = [span.string for span in soup.find_all("span") if span.get("data-price-target") is not None][-1].replace("\n", "")
        data["chains"]["binance"]["pairs"]["_"]["address"] = [div.text.replace("\n", "") for div in soup.find_all("div", "truncate")][0].replace(" ", "")

        return data

    def __get_volume(self, data, tr_tags_data):
        """ This private method sracps 1st 50 volume data."""

        if self.volume_only_50 < 50:
            for tr in tr_tags_data[1:]:
                table_number = int(tr.find("td", class_='table-number').string.replace("\n", ""))
                if (table_number-1) == self.volume_only_50:
                    tds = tr.find_all("td", "text-right")
                    data["chains"]["binance"]["pairs"]["_"]["volume"] = tds[6].text.replace("\n", "")
                    break
            self.volume_only_50 += 1

        return data

    def __handle_row_data(self, soup, start_index=0, end_index=12):
        """ This is the most important private method. This method handles every row 
        data collected from one page and saves those to json file. Every other methods
        are called from this method.
        """
        # checks if the page index is 0 and only if so, it will scrap volume data.
        if self.page_number == 0:
            _table = self.__get_soup(_url="https://www.coingecko.com/en/exchanges/pancakeswap").find_all("table", "table table-scrollable")[0]
            _table_soup = bs('\n'.join([str(ele) for ele in _table]), 'html.parser')
            trs = _table_soup.find_all("tr")

        # Data of all rows in a page will store in bigData (type: list)
        bigData = []

        # Get's 50 rows data one by one and populate bigData
        for itr in tqdm(range(50), ascii=True, desc="Row") if self.prograss_bar_enabled is True else range(50):

            # Temporary data (type: dict) to store row data later
            data = {
                "token_name": None,                        #done in __handle_row_data 
                "token_symbol": None,                      #done in __handle_row_data 
                "coingecko_id": None,                      #done in __handle_row_data 
                "token_image": None,                       #done in __handle_row_data 
                "market_cap": None,                        #done in __get_liveChatUrl_data 
                "chains": {
                    "binance":{
                        "exchange": "pancakeswap",
                        "token_address": None,             #done in __handle_row_data 
                        "24h_volume": None,                #done in __get_liveChatUrl_data 
                        "pairs": {
                            "_": {                                      #done in __handle_row_data 
                                "address": None,                        #done in __get_liveChatUrl_data 
                                "liquidity": None,                      #done in __get_liveChatUrl_data 
                                "price" : None,                         #done in __handle_row_data 
                                "spread" : None,                        #done in __handle_row_data 
                                "two_percent_positive_depth" : None,    #done in __handle_row_data 
                                "two_percent_negative_depth" : None,    #done in __handle_row_data 
                                "24h_volume" : None,                    #done in __handle_row_data 
                                "last_traded" : None,                   #done in __handle_row_data 
                                "volume" : None,                        #done in __get_volume 
                                "trust_score" : None,                   #done in __handle_row_data 
                                "price_change_24_hour" : None           #done in __get_liveChatUrl_data 
                            }
                        }
                    }
                }
            }

            row_raw_data = bs('\n'.join([str(ele) for ele in soup.findAll("td")[start_index:end_index]]), 'html.parser')
            divs = row_raw_data.find_all("div")
            tds = row_raw_data.find_all("td", "text-right")
            pair_token_name = row_raw_data.find_all("img")[1]['alt']

            data["token_name"] = row_raw_data.img['alt']
            data["token_symbol"] = row_raw_data.a['href'].split('/')[3]
            data["coingecko_id"] = row_raw_data.a['href'].split('/')[3]
            data["token_image"] = row_raw_data.img['src']
            data["chains"]["binance"]["token_address"] = row_raw_data.small.string
            try:
                data["chains"]["binance"]["pairs"]["_"]["last_traded"] = row_raw_data.find("td", "text-right tw-text-gray-500 tw-text-xs").string.replace("\n", "")
            except AttributeError as e:
                data["chains"]["binance"]["pairs"]["_"]["last_traded"] = row_raw_data.find("td", "text-right tw-text-gray-500 tw-text-xs").string

            try:
                data["chains"]["binance"]["pairs"]["_"]["trust_score"] = self.__get_trust_score(row_raw_data.find("td", "text-center").span["class"][0])
            except:
                data["chains"]["binance"]["pairs"]["_"]["trust_score"] = "N/A"

            for div in divs:
                if div.get("data-is-anomaly") is not None:
                    try:
                        data["chains"]["binance"]["pairs"]["_"]["price"] = div.string.replace("\n", "").split()[1]
                    except:
                        data["chains"]["binance"]["pairs"]["_"]["price"] = div.string.replace("\n", "")
                    break

            temp = [td.string.replace("\n", "") for td in tds[:5] if td.get("data-sort") is not None]
            data["chains"]["binance"]["pairs"]["_"]["spread"] = temp[0]
            data["chains"]["binance"]["pairs"]["_"]["two_percent_positive_depth"] = temp[1]
            data["chains"]["binance"]["pairs"]["_"]["two_percent_negative_depth"] = temp[2]

            for div in divs:
                if div.get("data-no-decimal") is not None and div.get("data-price-btc") is not None and div.get("data-target") is not None:
                    data["chains"]["binance"]["pairs"]["_"]["24h_volume"] = div.string.replace("\n", "")

            if self.page_number == 0:
                data = self.__get_volume(data=data, tr_tags_data=trs)

            data = self.__get_liveChatUrl_data(data=data, liveChatUel=row_raw_data.find("a", "underline text-body")['href'])
            data["chains"]["binance"]["pairs"][f"{pair_token_name}"] = data["chains"]["binance"]["pairs"]["_"]
            del data["chains"]["binance"]["pairs"]["_"]
            

            
            bigData.append(data)
            start_index = end_index
            end_index = start_index + 12
            

        # write/store page data to json file.
        self.__write_data(bigData)
        # sets the page_number to 1 inorder to avoid '__get_volume' method
        self.page_number = 1

    def scrap(self):
        """ This method is user callable and calling this function will 
            start the scrap process with the page limit.
        """
        for page in tqdm(range(0, self.pageLimit), ascii=True, desc="Page") if self.prograss_bar_enabled is True else range(0, self.pageLimit):
            soup = self.__get_soup(page=page)
            if len(soup.find_all("td")) > 0:
                self.__handle_row_data(soup=soup)
            else:
                print(f"There are no content on page {page}. valid limit is {page-1}")
                break

        return self.__get_data()