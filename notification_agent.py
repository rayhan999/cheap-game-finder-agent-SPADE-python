from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import json
import asyncio

class NotifyBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            try:
                content = json.loads(msg.body)

                # Handle deal message
                if "game" in content:
                    game = content["game"]
                    price = content["price"]
                    platform = content["platform"]
                    target_price = self.agent.target_prices.get(game, "N/A")

                    if isinstance(target_price, float) and price <= target_price:
                        print("----------------------------------------------------------------")
                        print(f"NotificationAgent: Deal found! {game} is ${price} on {platform} (target: ${target_price})")
                        print("----------------------------------------------------------------")
                    else:
                        print("----------------------------------------------------------------")
                        print(f"NotificationAgent: Ignored {game} at ${price} (target: ${target_price})")
                        print("----------------------------------------------------------------")

                # Handle recommendation message
                elif "recommendations" in content:
                    recommendations = content["recommendations"]
                    original = content.get("original", "N/A")
                    print("----------------------------------------------------------------")
                    print(f"NotificationAgent: Based on {original}, you may also like: {', '.join(recommendations)}")

                else:
                    print("NotificationAgent: Received unknown message format:", content)

            except Exception as e:
                print(f"NotificationAgent: Error processing message - {e}")
        else:
            await asyncio.sleep(1)

class NotificationAgent(Agent):
    def __init__(self, jid, password, target_prices):
        super().__init__(jid, password)
        self.target_prices = target_prices

    async def setup(self):
        print("Notification Agent started")
        self.add_behaviour(NotifyBehaviour())


if __name__ == "__main__":
    target_prices = {
        "Cyberpunk 2077": 35.0,
        "Among Us": 5.0,
        "Stardew Valley": 20.0,
        "The Witcher 3": 15.0,
        "Fortnite": 0.0
    }

    notification_agent = NotificationAgent("notification_agent@localhost", "password123", target_prices)

    async def main():
        await notification_agent.start()
        while True:
            await asyncio.sleep(1)

    asyncio.run(main())
