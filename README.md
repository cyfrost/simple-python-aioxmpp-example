## Simple aioxmpp demo for python-based XMPP messaging

A simple pipenv project demoing how to send messages between two JIDs via XMPP using the very-mature [aioxmpp](https://github.com/horazont/aioxmpp) library.

### What does this do
This is an extremely basic script demoing aioxmpp's sending XMPP messages between two JIDs. You'll need to edit the `bot-config.ini` file and change the JIDs for sender and recipient, also configure the local JID's password and an XMPP message (could also be a command). Once the configuration is done, simply running the demo will just send the configured message from the local JID to the recipient's JID.

### Instructions
* Clone this repo (or download it as a zip)
* Make sure [pipenv](https://pypi.org/project/pipenv/) is installed
* Open a terminal and install the dependencies of this demo python app like this:
  `pipenv install` (if you get an error about pipenv missing, try it this way instead: `python3 -m pipenv install`)
* Open the `bot-config.ini` file in a text editor and change the values of the variables to whatever you like, save and close it.
* Now run the script by doing `pipenv run python aioxmpp-demo.py` (or `python3 -m pipenv run python aioxmpp.py`)
* You should now see that the configured message will be sent from the local JID to the recipient JID.

### Bonus

For tons of other awesome ready-to-use examples made, check [this](https://github.com/horazont/aioxmpp/tree/devel/examples) page.
