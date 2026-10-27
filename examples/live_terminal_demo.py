import asyncio
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from src.core.terminal_engine import MarketHackerEngine
from src.licensing.license_guard import LicenseGuard

console = Console()

async def main():
    fingerprint = LicenseGuard.get_device_signature()
    console.print(Panel(f"[bold cyan]CB MARKET HACKER AI TERMINAL v4.2[/bold cyan]\n"
                        f"[green]Hardware Fingerprint:[/green] {fingerprint}\n"
                        f"[yellow]Official API:[/yellow] https://api1.api.cbtradersbd.com/docs\n"
                        f"[magenta]Commercial Bot Orders:[/magenta] @YouKnowWho_am (Telegram)",
                        title="Institutional Trading Terminal"))
    
    engine = MarketHackerEngine(asset="EURUSD_otc", min_confidence=0.88)
    price = 1.08500
    console.print("[dim]Ingesting high-frequency OTC price ticks...[/dim]")
    
    table = Table(title="Live Neural Confluence Stream")
    table.add_column("Timestamp", style="cyan")
    table.add_column("Asset", style="bold")
    table.add_column("Signal", style="bold green")
    table.add_column("Confidence", justify="right")
    table.add_column("Entropy", justify="right")
    table.add_column("Status", style="yellow")
    
    for i in range(5):
        price += (0.00015 if i % 2 == 0 else -0.00012)
        engine.ingest_tick(price)
        res = engine.evaluate_signal()
        table.add_row(
            time.strftime("%H:%M:%S"),
            res["asset"],
            f"[bold green]CALL[/bold green]" if res["direction"] == "CALL" else f"[bold red]PUT[/bold red]",
            f"{res['confidence']}%",
            str(res["entropy"]),
            "[green]DISPATCHED[/green]" if res["is_valid"] else "[dim]FILTERED[/dim]"
        )
        await asyncio.sleep(0.5)

    console.print(table)
    console.print("\n[bold green]✓ Live terminal demo cycle completed successfully![/bold green]")

if __name__ == "__main__":
    asyncio.run(main())
