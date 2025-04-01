import subprocess

def reiniciar_qtile():
    """Reinicia Qtile usando comando interno."""
    subprocess.run(["qtile", "cmd-obj", "-o", "cmd", "-f", "restart"], check=True)