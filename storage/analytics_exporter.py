import csv


class AnalyticsExporter:

    FILE_NAME = "analytics.csv"

    def export(self, entries):
        with open(self.FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Short", "Long URL", "Clicks"])

            for e in entries:
                writer.writerow([e.short, e.long_url, e.clicks])
