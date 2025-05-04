import json
import asyncio
from spade import agent
from spade.behaviour import PeriodicBehaviour
from spade.message import Message

class SearchAgent(agent.Agent):
    class SearchBehaviour(PeriodicBehaviour):
        async def run(self):
            mock_deals = [
                {"game": "Cyberpunk 2077", "price": 29.99, "platform": "Steam"},
                {"game": "Among Us", "price": 3.99, "platform": "Steam"},
            ]
            
            relevant_deals = [deal for deal in mock_deals if deal["price"] < 40]
            
            for deal in relevant_deals:
                msg = Message(to="notification_agent@localhost")
                msg.set_metadata("performative", "inform")
                msg.body = json.dumps(deal)
                await self.send(msg)
                print(f"SearchAgent sent deal: {deal}")
                
    async def setup(self):
        search_behaviour = self.SearchBehaviour(period=10)
        self.add_behaviour(search_behaviour)

async def main():
    search_agent = SearchAgent("search_agent@localhost", "password123")
    await search_agent.start()
    print("Search agent started")
    await asyncio.sleep(10000)  

if __name__ == "__main__":
    asyncio.run(main())