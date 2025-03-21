from my_functions import build_person, build_experiment

if __name__=="__main__":
    supervisor = input("Name: ")

    subject = build_person("Lars", "Schroeder", "male", 26)

    experiment = build_experiment("Herzfrequenz-Analyse", "21.03.2025", supervisor, subject)

print(experiment)