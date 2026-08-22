"""Minimal example for WalletTracker."""

from wallettracker import wallettracker


def main():
 runner = wallettracker({"name": "WalletTracker", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()