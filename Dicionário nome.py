nome=input("Qual o seu nome? ").lower()
vogais={}
vogal =vogais.fromkeys(['a','e','i','o','u'],0)
vogal["a"] = nome.count("a")
vogal["e"] = nome.count("e")
vogal["i"] = nome.count("i")
vogal["o"] = nome.count("o")
vogal["u"] = nome.count("u")

print(vogal)
