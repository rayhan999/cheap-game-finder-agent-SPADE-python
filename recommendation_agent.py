import json
import asyncio
from spade import agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class RecommendationAgent(agent.Agent):
    class RecommendBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=60)
            if msg:
                print('----------------------------------------------------------------')
                data = json.loads(msg.body)
                game = data.get("game")

                genre_map = {
                    "Cyberpunk 2077": "RPG",
                    "The Witcher 3": "RPG",
                    "Fortnite": "Shooter",
                    "Dota 2": "MOBA",
                    "Genshin Impact": "Adventure",
                    "Stardew Valley": "Simulation",
                    "Elden Ring": "RPG",
                    "Among Us": "Party",
                    "FIFA 23": "Sports",
                    "Battlefield 2042": "Shooter"
                }

                genre = genre_map.get(game)
                if genre:
                    # Recommend games in the same genre
                    similar_games = [g for g, g_genre in genre_map.items() if g_genre == genre and g != game]
                    if similar_games:
                        rec_msg = Message(to="notification_agent@localhost")
                        rec_msg.set_metadata("performative", "inform")
                        rec_msg.body = json.dumps({"recommendations": similar_games, "original": game})
                        await self.send(rec_msg)
                        print(f"RecommendationAgent: Recommended {similar_games} based on {game}")

    async def setup(self):
        self.add_behaviour(self.RecommendBehaviour())

async def main():
    agent = RecommendationAgent("recommendation_agent@localhost", "password123")
    await agent.start()
    print("RecommendationAgent started")
    await asyncio.sleep(10000)

if __name__ == "__main__":
    asyncio.run(main())
