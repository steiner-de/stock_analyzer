"""
Periodic background tasks for Stock Analyzer
Handles scheduled operations like ticker data updates
"""

import schedule
import threading
import time
from typing import Callable, Optional
from utils.ticker_manager import TickerManager


class TaskScheduler:
    """Schedule and run background tasks"""
    
    def __init__(self):
        self.scheduler_thread: Optional[threading.Thread] = None
        self.is_running = False
    
    def schedule_ticker_update(self, ticker_manager: TickerManager, interval_hours: int = 24):
        """
        Schedule periodic ticker data updates
        
        Args:
            ticker_manager: TickerManager instance
            interval_hours: Update interval in hours (default: 24)
        """
        def update_job():
            print(f"Starting scheduled ticker update...")
            success = ticker_manager.update_database(force=True)
            status = "completed" if success else "failed"
            print(f"Ticker update {status}")
        
        schedule.every(interval_hours).hours.do(update_job)
    
    def schedule_custom_job(
        self, 
        job: Callable, 
        interval: int, 
        interval_type: str = "hours"
    ):
        """
        Schedule a custom job
        
        Args:
            job: Callable function to execute
            interval: Time interval
            interval_type: "hours", "minutes", "days", etc.
        """
        if interval_type == "hours":
            schedule.every(interval).hours.do(job)
        elif interval_type == "minutes":
            schedule.every(interval).minutes.do(job)
        elif interval_type == "days":
            schedule.every(interval).days.do(job)
        else:
            raise ValueError(f"Unknown interval type: {interval_type}")
    
    def start(self):
        """Start the scheduler in a background thread"""
        if self.is_running:
            print("Scheduler already running")
            return
        
        self.is_running = True
        self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.scheduler_thread.start()
        print("Background scheduler started")
    
    def _run_scheduler(self):
        """Run the scheduler loop"""
        while self.is_running:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    def stop(self):
        """Stop the scheduler"""
        self.is_running = False
        schedule.clear()
        print("Background scheduler stopped")


# Global scheduler instance
scheduler = TaskScheduler()


def start_background_tasks(ticker_json_url: str):
    """
    Initialize and start all background tasks
    
    Args:
        ticker_json_url: URL to ticker JSON data source
    """
    # Initialize ticker manager
    ticker_manager = TickerManager(ticker_json_url)
    
    # Schedule ticker updates every 24 hours
    scheduler.schedule_ticker_update(ticker_manager, interval_hours=24)
    
    # Start scheduler
    scheduler.start()


if __name__ == "__main__":
    # Example usage
    ticker_url = "https://your-data-source.com/tickers.json"
    start_background_tasks(ticker_url)
    
    # Keep running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        scheduler.stop()
