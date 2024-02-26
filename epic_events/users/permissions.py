import jwt
from django.contrib.auth import get_user_model


def is_token_valide():
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
    return payload


def is_authenticated(department):

    payload = is_token_valide()

    if payload:
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
    else:
        return


def is_support_contact(obj):

    payload = is_token_valide()
    if payload:
        if obj.support_contact.username == payload['username']:
            return True
        return False
    else:
        return
