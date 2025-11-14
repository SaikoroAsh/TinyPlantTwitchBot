import json

def save_state():
    with open('data/state_logs.json', 'r') as h:
        state_logs = json.load(h)
        print(state_logs)
        
    with open('data/state.json', 'r') as f:
        state = json.load(f)

        print("Sauvegarde de l'état actuel dans data/state_logs.json")
        print(state)

    with open('data/state_logs.json', 'w') as g:
        json.dump(state, g, indent=4)

        print("État sauvegardé avec succès.")

    with open('data/state_logs.json', 'r') as h:
        state_logs = json.load(h)
        print(state_logs)

    return
