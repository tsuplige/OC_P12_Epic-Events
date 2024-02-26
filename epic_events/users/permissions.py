import jwt


def is_authenticated(department):
    token = ''
    try:
        with open('jwt_token.txt', 'r') as file:
            token = file.read().rstrip('\n')
    except FileNotFoundError:
        print("Aucun Jeton trouvé, veuillez vous connecter !")
        return False
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        print("Jeton expiré. Veuillez vous "
              "reconnecter pour obtenir un nouveau jeton.")
        return False
    except jwt.InvalidTokenError:
        print("Jeton invalide. Veuillez"
              " vous reconnecter avec un jeton valide.")
        return False

    if 'username' not in payload or 'department' not in payload:
        print("Vous n'avez pas les autorisations nécessaires.")
        return False
    if payload['department'] == department:
        print("token vérifieé avec succès")
        return True
    elif department == "any":
        print("token vérifieé avec succès")
        return True
    else:
        print("Vous n'avez pas les autorisations nécessaires.")
        return False
