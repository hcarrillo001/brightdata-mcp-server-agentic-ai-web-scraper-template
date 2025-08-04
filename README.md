# brightdata-mcp-server-agentic-ai-web-scraper-template

BrightData MCP Server Agentic AI Web Scraper Template
      An intelligent, plug-and-play web scraper that combines Bright Data's Mobile Carrier Proxy (MCP) 
      with Anthropic’s Claude for agentic, natural language-based scraping. A lightweight        
      Tkinter GUI lets you describe what to scrape in plain English — no coding required.

✨ Key Features
🌐 Bright Data MCP Proxy Integration
     Bypass geo-restrictions, CAPTCHAs, and anti-bot defenses using mobile carrier IPs.

🧠 Agentic AI via Claude
     Claude interprets your natural language instructions and dynamically generates scraping behavior.

🧾 Natural Language Interface
     Just describe the task in plain English — the scraper figures out the rest.

💻 Tkinter GUI
   A desktop interface to enter instructions, monitor scraping progress, and view logs.

🔁 Retry & Adapt
   Uses reasoning to handle failed pages, change in structure, or blocking events.

🧱 Modular & Scalable
  Clearly separated logic (GUI, agent, scraper, MCP) for easier maintenance and extension.

📷 Demo Example
  "Go to zillow.com, search Denver, and scrape the price, address, and number of beds for the first 5 listings."

✅ Type this into the GUI.
✅ Claude interprets it.
✅ Scraper executes it using Bright Data’s mobile proxy.
✅ Results saved — no code touched.

🛠 Requirements
Node.js (v16 or higher)

Python 3.x

Bright Data account with MCP access

Claude Desktop App (Anthropic)

Internet connection


⚙️ Setup
🔹 1. Claude Desktop Setup
Download and install from Anthropic

Launch the app

1. Go to Settings → Developer Settings

🔹 2. Bright Data MCP Server
Option A – Use config.json
json
Copy
Edit
{
  "mcpServers": {
    "Bright Data": {
      "command": "npx",
      "args": ["@brightdata/mcp"],
      "env": {
        "API_TOKEN": "<BrightData API TOKEN>",
        "WEB_UNLOCKER_ZONE": "<BrightData Web Unlocker Zone>",
        "BROWSER_AUTH": "<BrightData Browser Auth>"
      }
    }
  }
}


For more bright data mpc set up visit: https://github.com/brightdata/brightdata-mcp



💻 Using the Tkinter GUI
bash
Copy
Edit
python gui.py
The GUI allows you to:

✍️ Enter natural language instructions

▶️ Start/Stop scraping

📜 View logs and status

