import json
import asyncio
from spade import agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class NotificationAgent(agent.Agent):
    class NotifyBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)  # Wait for messages
            if msg:
                deal = json.loads(msg.body)
                game = deal["game"]
                price = deal["price"]
                platform = deal["platform"]
                
                # Hardcoded wishlist with target prices
                wishlist = {
                    "Cyberpunk 2077": 35.00,
                    "Among Us": 5.00
                }
                
                # Autonomous decision: Notify if price is below target
                if game in wishlist and price <= wishlist[game]:
                    print(f"NotificationAgent: Deal found! {game} is ${price} on {platform} (target: ${wishlist[game]})")
                    # Simulate sending notification (e.g., email/app)
                    # In real implementation, use SMTP or push notification API
                else:
                    print(f"NotificationAgent: Ignored {game} at ${price} (target: ${wishlist.get(game, 'N/A')})")
    
    async def setup(self):
        notify_behaviour = self.NotifyBehaviour()
        self.add_behaviour(notify_behaviour)

async def main():
    notification_agent = NotificationAgent("notification_agent@localhost", "password123")
    await notification_agent.start()
    print("Search agent started")
    await asyncio.sleep(10000)  # keep it running

if __name__ == "__main__":
    # Replace with your XMPP server and credentials
    # notification_agent = NotificationAgent("notification_agent@localhost", "password123")
    # future = notification_agent.start()
    # future.result()  # Wait for the agent to start
    # asyncio.get_event_loop().run_forever()
    asyncio.run(main())