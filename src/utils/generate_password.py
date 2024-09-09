import secrets
import string


def generate_password(name: str, lastname: str) -> str:

    base_password = f"{name[:3].lower()}{
        lastname[:3].lower()}"

    additional_chars = ''.join(secrets.choice(
        string.ascii_letters + string.digits + string.punctuation) for _ in range(8))

    password = base_password + additional_chars

    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)

    return ''.join(password_list)
