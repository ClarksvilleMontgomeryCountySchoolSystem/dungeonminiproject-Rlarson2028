drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: The bridge is down and ready to cross. Tread lightly..."
else:
    outcome = "Doom: The bridge remains raised and the chasm below takes you..."
print(f"{outcome}")