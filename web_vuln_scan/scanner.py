from crawler import Crawler
from vulnerability_checks import XSSChecker, SQLInjectionChecker, InsecureDirectObjectReferenceChecker

class WebVulnerabilityScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.crawler = Crawler(target_url)
        self.vulnerability_checks = [
            XSSChecker(),
            SQLInjectionChecker(),
            InsecureDirectObjectReferenceChecker()
        ]

    def run_scan(self):
        pages = self.crawler.crawl()
        vulnerabilities = []

        for page in pages:
            for checker in self.vulnerability_checks:
                vulnerabilities.extend(checker.check(page))

        return vulnerabilities