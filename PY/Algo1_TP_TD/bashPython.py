def get_data(csv):
    pays = []
    capitales = []
    fd = open(csv, "r")
    for ligne in fd:
        data = ligne.split(",")
        pays.append(data[0])
        capitales.append(data[1][:-1])
    return {"pays" : pays, "capitales" : capitales}

def ask(nbQuestion, pays, capitales):
    return score

def main () :
    pays, capitales = get_data(capitales.csv)

if __name__ == "__main__":
    main()