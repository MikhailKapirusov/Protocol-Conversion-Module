#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
import sys
import cv2
from sleekxmpp import ClientXMPP
from aiortc import RTCPeerConnection, VideoStreamTrack
from aiortc.contrib.signaling import object_to_string
import subprocess

# XMPP server settings
XMPP_JID = ''
XMPP_PASSWORD = ''
XMPP_SERVER = ''
XMPP_PORT = 5222

# Path to the directory with images
IMAGE_DIRECTORY = '/path/to/images'

# Video stream track class
class ImageVideoStreamTrack(VideoStreamTrack):
    def __init__(self):
        super().__init__()
        self.image_index = 0

    async def next_timestamp(self):
        return 1

    async def recv(self):
        image_path = f'{IMAGE_DIRECTORY}/image_{self.image_index:05d}.jpeg'
        frame = cv2.imread(image_path)
        self.image_index += 1
        return frame

class VideoBot(ClientXMPP):
    def __init__(self, jid, password):
        super(VideoBot, self).__init__(jid, password)

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

        self.video_track = ImageVideoStreamTrack()

        self.call_accepted = False

    async def start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            print("Message received:", msg['body'])
            if msg['body'] == "inviting to call":
                self.accept_call()

    def accept_call(self):
        print("We accept the challenge...")
        self.call_accepted = True
        asyncio.ensure_future(self.initiate_webrtc())

    async def initiate_webrtc(self):
        if not self.call_accepted:
            return

        pc = RTCPeerConnection()

        pc.addTrack(self.video_track)

        offer = await pc.createOffer()
        await pc.setLocalDescription(offer)

        self.send_webrtc_offer(object_to_string(offer))

    def send_webrtc_offer(self, offer_str):
        self.send_message(mto="@", mbody=offer_str) #Specify the username of the client application

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

    xmpp = VideoBot(XMPP_JID, XMPP_PASSWORD)

    if xmpp.connect((XMPP_SERVER, XMPP_PORT)):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(xmpp.process(forever=False))
        print("Connection successfully established")
    else:
        print("Failed to connect to XMPP server")
        sys.exit(1)
