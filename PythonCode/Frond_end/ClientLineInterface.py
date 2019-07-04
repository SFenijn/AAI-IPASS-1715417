import PatternAdjustingSimulation as inl
import ProfileSetup as pf
import MakeGraphs as graph


def run():
    """runs slaapritme-aanpassen programma"""
    # print titel
    print("IPASS Datagedreven slaapritme-aanpassen, door: Stijn Fenijn\n")

    # vraag welke controller gebruikt gaat worden
    controller = int(input("Welke controller wil je gebruiken?\n Proportional: PRESS 1\n PID: PRESS 2\n"))
    if controller == 1:
        print("Controller = Proportional\n")
    elif controller == 2:
        print("Controller = PID\n")

    # maak een seed aan
    seed = 12345
    s = int(input("Wil je de ingebouwde seed gebruiken?\n PRESS: 1 for yes and 0 for no\n"))
    if s == 1:
        s_choice = int(input("welke seed wil je gebruiken? \nPRESS: 1, 2 of 3\n"))
        if s_choice == 1:
            seed = 34799645
        elif s_choice == 2:
            seed = 12345
        elif s_choice == 3:
            seed = 11183
    elif s == 0:
        seed = input("Wat is de seed? INPUT: een aantal getallen naar keuze\n")

    # vraag aantal dagen om te testen en meten (wegehaald voor soepelheid presentatie)
    # days = input("Hoeveel dagen wil je testen?")
    # measure_days = input("Hoeveel dagen wil je meten voor dat het patroon word veranderd?")
    # change = input("Hoe snel kan er worden aangepast?")
    # max_value = input("Wat is de maximale snelheid waarmee het patroon kan worden aangepast?")
    days = 60
    measure_days = 6
    change = 0.2
    max_value = 1

    # setup profile
    profile = pf.profile_setup(days, seed)
    # use_profile = pf.use_profile(profile, measure_days)
    use_profile = profile

    # run simulation
    if controller == 1:
        altered_profile = inl.simulate_proportional(use_profile, change, max_value, days, measure_days)
    else:
        altered_profile = inl.simulate_pid(use_profile, days, measure_days)

    graph.drawgrapth(profile, altered_profile)


run()