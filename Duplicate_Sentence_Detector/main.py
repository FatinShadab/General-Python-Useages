import spacy
import logging
import warnings
from tqdm import tqdm


# IGNORE UserWarning
warnings.filterwarnings("ignore", message=r"\[W007\]", category=UserWarning)

# Create and configure logger
logging.basicConfig(filename="similarity_check_results.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def check_sub(sentence_one, sentence_two):
    """
    This function checks for noun or verb as noun(when noun is none) 
    to check if both sentences are same or not.
    """

    # get nouns/verbs from sentences
    senI = [token.text for token in sentence_one if token.tag_ in ('NN', 'NNP', 'NNS')]
    senII = [token.text for token in sentence_two if token.tag_ in ('NN', 'NNP', 'NNS')]

    if len(senI) == 0 and len(senII) != 0:
        return False

    if len(senI) != 0 and len(senII) == 0:
        return False

    if len(senI) == 0 and len(senII) == 0:
        senI = [token.text for token in sentence_one if token.tag_ == 'VB']
        senII = [token.text for token in sentence_two if token.tag_ == 'VB']

    # check nouns/verbs similarity
    for word in senII:
        if word in senI:
            pass
        else:
            return False

    return True

def check_similarity(sentence_I, sentence_II):
    """
    This function checks similarity between two sentences,
    and if the similarity is higher or equal to 75~76% it
    calls the check_sub function and return's 
    True/False depending on the results.
    """

    nlp = spacy.load("en_core_web_sm")

    sentence_one = nlp(sentence_I)
    sentence_two = nlp(sentence_II)

    sim_val = sentence_one.similarity(sentence_two)

    if sim_val >= 0.755:
        condition = check_sub(sentence_one, sentence_two)
        if condition:
            logger.info(f"[+] {sentence_one} matched {sentence_two} || similarity: {sim_val} || sub_matched :{condition}")
            return True
        else:
            logger.info(f"[-] {sentence_one} didn't matched {sentence_two} || similarity: {sim_val} || sub_matched :{condition}")
            return False
    else:
        logger.info(f"[-] {sentence_one} didn't matched {sentence_two} || similarity: {sim_val}")
    return False

def find_duplicate(all_in_list):
    """
    This is the main function to call by a user and 
    it take's a list of sentence's as input and checks
    duplicate sentence's among them and returns a dict
    containing the results.
    """

    output = {}

    for  case in tqdm(all_in_list):
        alpha = case
        duplicates = [beta for beta in all_in_list if check_similarity(alpha, beta)]
        output[alpha] = duplicates
        
    return output



if __name__ == "__main__":
    test = [
        "What to do when you're in New York City",
        "How to plan your trip to New York City",
        "Places to visit in Bangladesh",
        "How to get around in New York City",
        "How to get rid of flies in your house.",
        "What to do in New York City",
        "Things to do in New York City",
        "Tasty street food in India",
        "What should you do in Nyc?",
        "How to get rid of flies from your yard.",
        "How to save money in Nyc?",
        "Get rid of food scraps and trash.",
        "Get rid of flies with vinegar and baking soda.",
        "How to swim fast.",
        "How to swim quickly.",
        "How to eat mango.",
        "How to eat orange.",
        "How to Visit Nyc on the cheap.",
        "How to remove flies near your yard.",
        "Where should you stay in Nyc?",
        "Remove food scraps and trash.",
        "How To Visit Nyc",
        "What are the best sites to visit in NYC",
        "Ways to get rid of flies in your house.",
        "What are some of the best museums to visit in NYC?",
        "What are some of the best restaurants to visit in NYC",
        "How to get rid of flies in your car.",
        "How to get around in Nyc.",
        "How to save money while in NYC",
        "List of street food in India",
        "How to Visit Nyc",
        "How to get around in New York City",
        "Most vistor places in Bangladesh",
        "Tips for getting rid of flies in your home.",
        "How to get rid of flies without chemicals.",
        "Tips for getting rid of flies outside.",
        "How to get rid of flies in your yard.",
        "How to get rid of flies in your yard near your home.",
    ]

    try:
        dup = find_duplicate(all_in_list=test)

        for key in dup.keys():
            print(f"{key} --> {dup[key]} \n")
    except KeyboardInterrupt:
        print("Process Stoped by 'ctrl+c' cmd!")