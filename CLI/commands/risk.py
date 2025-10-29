import typer

def register(app: typer.Typer):
    @app.command()
    def risk(balance: float , percentage: float):
          #calculate risk per trade usiing percentage
          results = (percentage / 100) * balance
          typer.echo(f"{percentage}% of ${balance} = ${results:2f}")