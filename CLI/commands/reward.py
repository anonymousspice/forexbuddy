import typer

def register(app: typer.Typer):
     @app.command()
     def risk_amount(riskamount: float,win_rate_ratio:float):
         #calculate reward

         reward = riskamount * win_rate_ratio
         
         typer.echo(f"rewads: ${reward:2f}")