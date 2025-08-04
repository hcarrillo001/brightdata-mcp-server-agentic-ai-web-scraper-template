# brightdata-mcp-server-agentic-ai-web-scraper-template

BrightData MCP Server Agentic AI Web Scraper Template
      
      An intelligent, plug-and-play web scraper that combines Bright Data's Mobile Carrier Proxy (MCP) 
      with Anthropic’s Claude for agentic, natural language-based scraping. A lightweight        
      Tkinter GUI lets you describe what to scrape in plain English — no coding required.
      I can envison tool also reading step from QC/ALM and feed the agent the steps 

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

<img width="1184" height="822" alt="Screenshot 2025-08-01 at 4 56 28 PM" src="https://github.com/user-attachments/assets/0b174e25-0d04-4fe6-affb-42465e62d25a" />

<img width="1189" height="821" alt="Screenshot 2025-08-04 at 10 18 49 AM" src="https://github.com/user-attachments/assets/8d71bdcb-0cc4-4d03-88d8-cb2cd596308e" />



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

      Go to Settings → Developer Settings

      🔹 2. Create anthropic accound and Bright Data account with the correct tools
            - Anthropic API Key (will require credit card) https://console.anthropic.com/settings/keys  - This key will be used in the python project as a environment variable
            - Bright data create and account and add Browser API tool and a Unlocked API tool see images below. You can name it what you would like but on step three you will need to use the name WEB_UNLOCKER_ZONE = <Web unlocker name>

            
      🔹 3. Bright Data MCP Server
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

Tools needed 

<img width="1416" height="542" alt="Screenshot 2025-08-04 at 10 59 57 AM" src="https://github.com/user-attachments/assets/8b67a4e3-cfcc-427a-909f-8c6d1f5576e2" />


Python setup
## ⚙️ Setup

### 🔹 Environment Variables

You **must create a `.env` file in the Python root directory** 

```env
API_TOKEN=your_brightdata_api_token
WEB_UNLOCKER_ZONE=your_web_unlocker_zone
BROWSER_AUTH=your_browser_auth
ANTHROPIC_API_KEY=anthropic_key
















