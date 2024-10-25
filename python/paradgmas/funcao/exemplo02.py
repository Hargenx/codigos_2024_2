def clubes(*times):
    """Usamos uma tupla de times."""
    print(type(times))
    for nome in times:
        print(f"{nome}")
clubes("Flamengo", "Fluminense", "Vasco", "Botafogo", "Flamengo")
