#!/usr/bin/env python
import os

from discum import Client

client = Client(token=os.environ.get("TEST_TOKEN"))


@client.gateway.command()
def asdf(resp):
    if resp.event.ready_supplemental:
        client.gateway.subscribeToGuildEvents(wait=1)
    if resp.event.message:
        m = resp.parsed.auto()
        guildID = (
            m["guild_id"] if "guild_id" in m else None
        )  # because DMs are technically channels too
        channelID = m["channel_id"]
        username = m["author"]["username"]
        discriminator = m["author"]["discriminator"]
        content = m["content"]
        print(
            f"> guild {guildID} channel {channelID} |\
              \n {username}#{discriminator}: {content}"
        )
