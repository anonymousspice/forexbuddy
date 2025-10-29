import typer
from commands import risk, reward


app = typer.Typer()

risk.register(app)
reward.register(app)



if __name__ == "__main__":
    app()








