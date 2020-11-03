import asyncio
import aioxmpp
import aioxmpp.dispatcher
import configparser
from framework import Example, exec_example

class SendMessage(Example):
    def run_simple_example(self):
        recipient = self.config.get("global", "xmpp_slave_jid")
        msgData = self.config.get("global", "xmpp_command")

        msg = aioxmpp.stanza.Message(
            to=aioxmpp.JID.fromstr(recipient),
            type_=aioxmpp.MessageType.CHAT,
        )

        msg.body[None] = msgData

        print("Sending message...")
        yield from self.client.send(msg)
        print("Message sent!")

if __name__ == "__main__":
    exec_example(SendMessage())
