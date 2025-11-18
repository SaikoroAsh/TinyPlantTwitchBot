import json

def save_state():
    # Lecture de l'état actuel depuis le fichier state.json
    with open('data/state_logs.json', 'r') as h:
        state_logs = json.load(h)
        print(state_logs)
        
    # Sauvegarde de l'état actuel dans un nouveau fichier state_logs.json
    with open('data/state.json', 'r') as f:
        state = json.load(f)

        print("Sauvegarde de l'état actuel dans data/state_logs.json")
        print(state)

    # Écriture de l'état dans le fichier state_logs.json
    with open('data/state_logs.json', 'w') as g:
        json.dump(state, g, indent=4)

        print("État sauvegardé avec succès.")

    # Vérification de la sauvegarde en relisant le fichier state_logs.json
    with open('data/state_logs.json', 'r') as h:
        state_logs = json.load(h)
        print(state_logs)

    return
