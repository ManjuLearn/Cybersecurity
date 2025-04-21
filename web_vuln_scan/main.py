import argparse
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def main():
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("url", help="Target URL to scan")
    parser.add_argument("-o", "--output", help="Output file for the report", default="vulnerability_report.html")
    args = parser.parse_args()

    try:
        from scanner import WebVulnerabilityScanner
        from report_generator import ReportGenerator
    except ImportError as e:
        logger.error(f"Error importing required modules: {e}")
        sys.exit(1)

    try:
        scanner = WebVulnerabilityScanner(args.url)
        vulnerabilities = scanner.run_scan()

        report_generator = ReportGenerator(args.url, vulnerabilities)
        report_generator.generate_report(args.output)

        print(f"Scan completed. Report saved to {args.output}")
    except Exception as e:
        logger.error(f"An error occurred during the scan: {e}")
        sys.exit(1)
if __name__ == "__main__":

    main()