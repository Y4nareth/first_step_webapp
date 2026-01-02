import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'game_room'

        # Join the group (Broadcast channel)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket (from the Player's browser)
    async def receive(self, text_data):
        data = json.loads(text_data)
        color = data.get('color')

        # Send message to the group (broadcasts to GM and all other players)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'color_message', # This calls the color_message method below
                'color': color
            }
        )

    # Receive message from the group_send above
    async def color_message(self, event):
        color = event['color']

        # Send the color to the actual WebSocket browser client
        await self.send(text_data=json.dumps({
            'color': color
        }))