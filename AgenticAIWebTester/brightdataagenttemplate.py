import tkinter as tk
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import asyncio
import os

import agentTemplate


#key will be score in a file names my_secretkey.py



class BrightDataAgentTemplate:

    def __init__(self):

        self.userinput = ""
        self.chatgptresponse = ""
        self.root = tk.Tk()

        # Create left frame
        self.left_frame = tk.Frame(self.root,width=300)
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Create right frame
        right_frame = tk.Frame(self.root, width=300)
        right_frame.pack(side="right", fill="both", expand=True)

        self.root.geometry("1200x800")
        self.root.title("BrightData WebScaper Practice")

        self.label = tk.Label(text="Bright Data Webscaper", font=('Arial', 18))
        self.label.pack(padx=10,pady=10)

        self.userinputlabel = tk.Label(self.left_frame, text="Test Description (Steps)",font=('Arial', 18))
        self.userinputlabel.pack(padx=20,pady=20)

        self.entry_description = tk.Text(self.left_frame, height=20, width=60, font=('Arial',10))
        self.entry_description.pack(padx=5, pady=5)


        self.userinputlabel2 = tk.Label(self.left_frame, text="Expected Results", font=('Arial', 18))
        self.userinputlabel2.pack(padx=5, pady=5)

        self.entry_expected_results = tk.Text(self.left_frame, height=15, width=60, font=('Arial', 10))
        self.entry_expected_results.pack(padx=5, pady=5)


        self.userinputlabel3 = tk.Label(self.left_frame, text="Test Results. After Analysis", font=('Arial', 18))
        self.userinputlabel3.pack(padx=10, pady=5)

        self.final_result = tk.Text(self.left_frame, height=10, width=60, font=('Arial', 10))
        self.final_result.pack(padx=5, pady=5)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.button1 = tk.Button(self.buttonframe, text="Enter", font=('Arial', 18), command=self.enter_button_press)
        self.button1.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.button2 = tk.Button(self.buttonframe, text="Clear", font=('Arial', 18), command=self.clear_button_press)
        self.button2.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.buttonframe.pack(side="bottom")

        # text box to display the chatGPT answer
        self.answerlabel = tk.Label(right_frame, text="GPT Answer", font=('Arial', 15))
        self.answerlabel.pack(padx=10, pady=20)

        self.answertextbox = tk.Text(right_frame, height=70, width=80, font=('Arial', 10))
        self.answertextbox.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        print("hello world")

    def enter_button_press(self):
        print(":button ")
        description = self.entry_description.get("1.0",'end-1c')
        expected_results = self.entry_expected_results.get("1.0",'end-1c')
        results =  agentTemplate.run_agent(description,expected_results)

        # Add user input then insert
        self.answertextbox.insert("1.0", results)

        if "PASS" in results:
            self.final_result.insert("1.0", "PASS\n")
        elif "FAIL" in results:
            self.final_result.insert("1.0", "FAIL\n")
        if "UNDETERMINED" in results:
            self.final_result.insert("1.0", "UNDETERMINED\n")





    def clear_button_press(self):
        self.entry_description.delete(0,tk.END)
        self.entry_expected_results.delete(0, tk.END)

    def on_closing(self):
        self.root.destroy()



