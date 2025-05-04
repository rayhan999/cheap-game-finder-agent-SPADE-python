import json
import asyncio
from spade import agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class NotificationAgent(agent.Agent):
    class NotifyBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)  
            if msg:
                deal = json.loads(msg.body)
                game = deal["game"]
                price = deal["price"]
                platform = deal["platform"]
                
                wishlist = {
                    "Cyberpunk 2077": 35.00,
                    "Among Us": 5.00
                }
                
                if game in wishlist and price <= wishlist[game]:
                    print(f"NotificationAgent: Deal found! {game} is ${price} on {platform} (target: ${wishlist[game]})")
                else:
                    print(f"NotificationAgent: Ignored {game} at ${price} (target: ${wishlist.get(game, 'N/A')})")
    
    async def setup(self):
        notify_behaviour = self.NotifyBehaviour()
        self.add_behaviour(notify_behaviour)

async def main():
    notification_agent = NotificationAgent("notification_agent@localhost", "password123")
    await notification_agent.start()
    print("Search agent started")
    await asyncio.sleep(10000)  

if __name__ == "__main__":
    asyncio.run(main())