# Cheap Computer Games Finder - Multi-Agent System

## Overview

The **Cheap Computer Games Finder** is a Multi-Agent System (MAS) developed for the _Agent Technologies for Developers_ course. Built using the **SPADE** (Smart Python Agent Development Environment) framework, this system autonomously searches for game deals across platforms, filters relevant deals, and notifies users when games on their wishlist meet target prices. The project follows the **GAIA methodology** for MAS design, ensuring a structured approach to defining roles, interactions, and services.

The system consists of two primary agents:

- **Search Agent**: Simulates querying gaming platforms (e.g., Steam) for game deals and sends relevant deals to the Notification Agent.
- **Notification Agent**: Receives deal data, checks against a user wishlist, and notifies users of matching deals.

This implementation meets the course requirements by demonstrating agent communication, autonomous behavior, and domain-specific interactions using SPADE’s XMPP-based messaging system.

## Features

- **Autonomous Agents**:
  - Search Agent filters deals below $40, making independent decisions.
  - Notification Agent decides to notify based on wishlist target prices.
- **Real-Time Communication**: Agents communicate via SPADE’s XMPP messaging, sending structured game deal data (title, price, platform).
- **Domain-Specific Interactions**: Messages contain game-related data, aligning with the cheap games finder context.
- **Scalable Design**: Modular architecture allows adding more agents (e.g., Price Comparison Agent) or platforms.
- **Mock Data**: Simulates platform queries with hardcoded deals for simplicity, extensible to real APIs.

## Project Structure

The project is designed using the GAIA methodology, with the following components:

- **Environmental Model**: Includes external platforms (e.g., Steam), a shared database, user wishlist, and notification channels.
- **Role Model**: Defines roles for Search Agent (data collection) and Notification Agent (user alerts).
- **Interaction Model**: Specifies protocols for deal data exchange (e.g., Search Agent informs Notification Agent of deals).
- **Agent Model**: Maps roles to SPADE agents, with multiple instances possible for scalability.
- **Service Model**: Outlines services like data collection and notification delivery.

## Requirements

- **Python**: 3.8 or higher
- **SPADE**: `pip install spade`
- **XMPP Server**: Local (e.g., Openfire) or public (e.g., jabber.org)
- **Operating System**: Windows, macOS, or Linux

## Installation

Follow these steps to set up the project:

1. **Install Python**:

   - Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/).
   - Verify installation: `python --version`.

2. **Install SPADE**:

   ```bash
   pip install spade
   ```

3. **Set Up an XMPP Server**:

   - **Option 1: Local Server (Recommended)**:
     - Download and install [Openfire](https://www.igniterealtime.org/projects/openfire/).
     - Follow the setup wizard to configure the server (default port: 5222).
     - Create two XMPP accounts:
       - JID: `search_agent@localhost`, Password: `password123`
       - JID: `notification_agent@localhost`, Password: `password123`
   - **Option 2: Public Server**:
     - Register accounts on a public XMPP server (e.g., `jabber.org`).
     - Example JIDs: `search_agent@jabber.org`, `notification_agent@jabber.org`.

4. **Clone or Download the Project**:

   - Download the project files (`search_agent.py`, `notification_agent.py`) or clone the repository (if hosted).
   - Place files in a project directory (e.g., `cheap-games-finder/`).

5. **Update XMPP Credentials**:
   - Open `search_agent.py` and `notification_agent.py`.
   - Replace `your_xmpp_server` with your XMPP server (e.g., `localhost` for Openfire, `jabber.org` for public).
   - Update passwords if different from `password123`.

## Usage

1. **Start the XMPP Server**:

   - If using Openfire, launch the server via its admin console or service.
   - Ensure the server is running and accessible.

2. **Run the Agents**:

   - Open two terminal windows (or command prompts).
   - In the first terminal, navigate to the project directory and run the Search Agent:
     ```bash
     python search_agent.py
     ```
   - In the second terminal, run the Notification Agent:
     ```bash
     python notification_agent.py
     ```

3. **Observe Output**:

   - **Search Agent**: Every 10 seconds, it simulates querying a platform and sends deals (e.g., “SearchAgent sent deal: {'game': 'Cyberpunk 2077', 'price': 29.99, 'platform': 'Steam'}”).
   - **Notification Agent**: Processes received deals and prints notifications for matching wishlist entries (e.g., “NotificationAgent: Deal found! Cyberpunk 2077 is $29.99 on Steam (target: $35.00)”).
   - Deals not meeting wishlist criteria are ignored (e.g., “NotificationAgent: Ignored Among Us at $3.99 (target: $5.00)”).

4. **Stop the Agents**:
   - Press `Ctrl+C` in each terminal to stop the agents.

## Example Output

**Search Agent**:

```
SearchAgent sent deal: {'game': 'Cyberpunk 2077', 'price': 29.99, 'platform': 'Steam'}
SearchAgent sent deal: {'game': 'Among Us', 'price': 3.99, 'platform': 'Steam'}
```

**Notification Agent**:

```
NotificationAgent: Deal found! Cyberpunk 2077 is $29.99 on Steam (target: $35.00)
NotificationAgent: Ignored Among Us at $3.99 (target: $5.00)
```

## Project Details

### Agents

- **Search Agent**:
  - **Role**: Collects game deal data from platforms (simulated with mock data).
  - **Behavior**: Uses `PeriodicBehaviour` to query every 10 seconds, autonomously filters deals below $40.
  - **Communication**: Sends JSON-encoded deal data to Notification Agent via XMPP with FIPA `inform` performative.
- **Notification Agent**:
  - **Role**: Checks deals against a wishlist and notifies users.
  - **Behavior**: Uses `CyclicBehaviour` to process incoming messages, autonomously decides to notify if prices meet wishlist targets.
  - **Communication**: Receives and processes deal messages, simulates notifications via console output.

### Implementation Notes

- **Mock Data**: The Search Agent uses hardcoded deals for simplicity. Real implementations can integrate APIs (e.g., Steam Web API) or web scraping.
- **Wishlist**: Hardcoded with games and target prices (`Cyberpunk 2077: $35.00`, `Among Us: $5.00`). Extensible to a database (e.g., SQLite).
- **Notifications**: Simulated by console output. Real notifications can use SMTP for email or Firebase for app alerts.
- **XMPP**: Requires a running XMPP server with configured accounts. Update JIDs and passwords in the code to match your setup.

<!-- ### Alignment with Requirements
- **Two Agents**: Search and Notification Agents are implemented.
- **SPADE Messaging**: XMPP-based communication with JSON payloads.
- **Real Interactions**: Search Agent provides deal data, Notification Agent processes it for notifications.
- **Autonomous Behavior**: Search Agent filters cheap deals, Notification Agent decides based on wishlist.
- **Domain Context**: Messages include game titles, prices, and platforms, ensuring relevance. -->

<!-- ## Troubleshooting
- **XMPP Connection Errors**:
  - Verify the XMPP server is running and JIDs/passwords are correct.
  - Check firewall settings (port 5222 for XMPP).
- **No Messages Received**:
  - Ensure both agents are running simultaneously.
  - Confirm JIDs match (e.g., `notification_agent@your_xmpp_server` in `search_agent.py`).
- **SPADE Issues**:
  - Ensure SPADE is installed (`pip show spade`).
  - Check Python version (3.8+). -->

<!-- ## Future Enhancements
- **Price Comparison Agent**: Add an agent to compare deals across platforms.
- **Real Platform Integration**: Use APIs or web scraping for live data.
- **Database**: Store wishlist and deal data in a persistent database.
- **Real Notifications**: Implement email or push notifications.
- **Scalability**: Add multiple Search Agents for different platforms/regions. -->

## Acknowledgments

- **SPADE**: For providing a robust MAS framework.
- **GAIA Methodology**: For guiding the system design.
- **Agent Technologies for Developers Course**: For inspiring this project.

---

_Generated on May 04, 2025_
