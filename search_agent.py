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
                {"game": "The Witcher 3", "price": 19.99, "platform": "Epic Games"},
                {"game": "Fortnite", "price": 0.00, "platform": "Epic Games"},
                {"game": "Dota 2", "price": 0.00, "platform": "Steam"},
                {"game": "FIFA 23", "price": 59.99, "platform": "Steam"},
                {"game": "Genshin Impact", "price": 0.00, "platform": "Garena"},
                {"game": "Elden Ring", "price": 49.99, "platform": "Steam"},
                {"game": "Stardew Valley", "price": 14.99, "platform": "Steam"},
                {"game": "Battlefield 2042", "price": 39.99, "platform": "Epic Games"}
            ]
            
            relevant_deals = [deal for deal in mock_deals if deal["price"] < 40]
            print('----------------------------------------------------------------')
            for deal in relevant_deals:
                msg = Message(to="notification_agent@localhost")
                msg.set_metadata("performative", "inform")
                msg.body = json.dumps(deal)
                await self.send(msg)
                print(f"SearchAgent sent deal: {deal}")
                
    async def setup(self):
        search_behaviour = self.SearchBehaviour(period=60)
        self.add_behaviour(search_behaviour)

async def main():
    search_agent = SearchAgent("search_agent@localhost", "password123")
    await search_agent.start()
    print("Search agent started")
    await asyncio.sleep(10000)  

if __name__ == "__main__":
    asyncio.run(main())