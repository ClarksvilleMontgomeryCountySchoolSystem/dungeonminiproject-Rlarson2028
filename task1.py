good = r"""
      .----.__
     / c  ^  _`;
     |     .--'
      \   (
      /  -.\
     / .   \
    /  \    |
   ;    `-. `.
   |      /`'.`.
   |      |   \ \
   |    __|    `'
   ;   /   \
  ,'        |
 (_`'---._ /--,
   `'---._`'---..__
 jgs      `''''--, )
            _.-'`,`
             ````

"""

bad = r"""
                        d8b     888                888    
                        Y8P     888                888    
                                888                888    
 8888b.  .d8888b .d8888b888 .d88888 .d88b. 88888b. 888888 
    "88bd88P"   d88P"   888d88" 888d8P  Y8b888 "88b888    
.d888888888     888     888888  88888888888888  888888    
888  888Y88b.   Y88b.   888Y88b 888Y8b.    888  888Y88b.  
"Y888888 "Y8888P "Y8888P888 "Y88888 "Y8888 888  888 "Y888 
                                                          
                                                      
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: Thy torch leads the way!"
    print({good})
else:
    outcome = "Doom: You now journey in the shadows..."
    print({bad})
print(f"{outcome}")