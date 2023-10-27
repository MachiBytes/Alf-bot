from logging.config import dictConfig
from os import getenv, environ
from pathlib import Path
from dotenv import load_dotenv

# Environment Variables
load_dotenv()
TOKEN = getenv("TOKEN")
VERIFY_CHANNEL_TOKEN = int(environ["VERIFY_CHANNEL"])
WELCOME_CHANNEL_TOKEN = int(environ["WELCOME_CHANNEL"])
VERIFY_TICKET_CHANNEL = int(environ["VERIFY_TICKET_CHANNEL"])
VERIFIED_ROLE_ID = int(environ["VERIFIED_ROLE_ID"])

# Logging
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console1": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console1"],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}
dictConfig(LOGGING_CONFIG)

# Directories
BASE_DIR = Path(__file__).parent
COGS_DIR = BASE_DIR / "cogs"

# Variables
CUSTOM_MESSAGES = [
    "Holabels to the server, my lalambs {MEMBER} ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა ♡",
    "Wazzaap, {MEMBER}! ...and welcome to the most amazing org evauhh! ૮꒰˵•̀ ﻌ •´˵꒱ა",
    "Hellow, fellow recruit {MEMBER}! We've been expecting you ^^ ૮꒰ •̀⤙ •´˵꒱ა",
    "How are you, {MEMBER}? Fine, thank you~ It is good to finally have you NYAAA ૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა",
    "Acccxk! my cloud buddy, {MEMBER}, has finally arrived yaaay~ ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა",
    "Haeiyouuuw, {MEMBER}! >< So happy to have you here now with us~ ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
    "Aiyooo, {MEMBER}! -^^- Been waiting for you here for ages now, hmp! ૮꒰ •̀⤙ •´˵꒱ა",
    "You're finally here, {MEMBER}! >< Welcome to my space crew~ hehe ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
    "Elloow, {MEMBER}! Took you so long to arrive, eh? ૮꒰˵•̀ ﻌ •´˵꒱ა",
    "Emeji! That's my {MEMBER} right there! Welcome aboard, my cloud bud~ ૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა",
    "Welcome to the crew, {MEMBER}!!! Are ye ready for an adventure??? ૮꒰˵•̀ ﻌ •´˵꒱ა ",
    "Great to meet ya, mi alfaloves {MEMBER}! >< You're now part of the cloud crew~ ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
    "Holler up to the newly added cloud buddy, {MEMBER}! LET'S MAKE SUM NOISE~ ૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა",
    "Hemlooo, {MEMBER}!!! 'wag mo na ako iiwan, ha??? padlock tapon susi sa river mehehe ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა",
    "Hi, your name is (what?), your name is (who?), your name is {MEMBER} and welcome to the one and only server ૮꒰˵•̀ ﻌ •´˵꒱ა",
    "Whale-corn— ay mali... WELCOME TO THE SERVER, {MEMBER} ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
    "Andito na si {MEMBER} wala siyang apelyido, magbabagsakan dito in 5... 4... 3... 2...",
    "Annyeonghaseyo, {MEMBER} ♡♡♡ Are you ready to be AWSified by this server?!!",
    "Hola, {MEMBER}! miss na kita :((( AY KAKAJOIN MO LANG PALA... welcome!!! ACKXKX",
    "Buckle up, {MEMBER}! we're about to take you on a journey to reach the sky and raise the 'baa' together ૮꒰ ˶˃ ᵕ ˂˶꒱ა⸝♡",
]
