#!/usr/bin/env python3 
"""Alta3 Research | Author: ryanne.ross@tlgcohort.com

    Description:
    A script to interact with an "open" api,
    https://api.magicthegathering.io/v1/

    documentation for the API  is available via,
    https://docs.magicthegathering.io/"""

import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    """Run time code"""

    resp = requests.get(f"{API}sets")

    cardsets = resp.json().get("sets")

    with open("mtgsets.index", "w") as mtgfile:
        for cardset in cardsets:
            print(f"{cardset.get('name')} -- {cardset.get('code')}", file=mtgfile)

if __name__ == "__main__":
    main()
if __name__  == "__main__":
    main()
