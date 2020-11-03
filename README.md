## Simple aioxmpp demo for python-based XMPP messaging

A simple pipenv project demoing how to send messages between two JIDs via XMPP using the [aioxmpp](https://github.com/horazont/aioxmpp) library.

### What does this do
This is a basic python script demoing aioxmpp's capability of sending XMPP messages between two JIDs. You'll need to edit the `config.ini` file and change the JIDs for sender and recipient, also configure the local JID's password and an XMPP message (could also be a command if remote can interpret messages and commands). Once the configuration is done, simply running the demo will just send the configured message from the local JID to the recipient's JID.

### Prerequisites
* Pipenv (to manage dependencies)
* Two JIDs from a server (get them from a self-hosted XMPP server instance or pick one provider from [here](https://xmpp.org/software/servers.html) and register with them.
* (Optional) Make sure the server supports stream management and better security features (use of privacy lists only, encryption, XEP etc)

### Instructions
* Clone this repo (or download it as a zip)
* Make sure [pipenv](https://pypi.org/project/pipenv/) is installed
* Open a terminal and install the dependencies of this demo python app like this:
  `pipenv install` (if you get an error about pipenv missing, try it this way instead: `python3 -m pipenv install`)
* Open the `config.ini` file in a text editor and change the values of the variables to whatever you like, save and close it.
* Now run the script by doing `./run.sh`
* You should now see that the configured message will be sent from the local JID to the recipient JID.

### Bonus

For tons of other awesome ready-to-use examples made, check [this](https://github.com/horazont/aioxmpp/tree/devel/examples) page.

## License

LGPL v3 inherited from upstream
