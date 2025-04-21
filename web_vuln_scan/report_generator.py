class ReportGenerator:
    def __init__(self, target_url, vulnerabilities):
        self.target_url = target_url
        self.vulnerabilities = vulnerabilities

    def generate_report(self, output_file):
        html_content = f"""
        <html>
        <head>
            <title>Web Vulnerability Scan Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Web Vulnerability Scan Report</h1>
            <h2>Target URL: {self.target_url}</h2>
            <h3>Vulnerabilities Found: {len(self.vulnerabilities)}</h3>
            <table>
                <tr>
                    <th>Type</th>
                    <th>URL</th>
                    <th>Description</th>
                </tr>
                {''.join(f"<tr><td>{v['type']}</td><td>{v['url']}</td><td>{v['description']}</td></tr>" for v in self.vulnerabilities)}
            </table>
        </body>
        </html>
        """

        with open(output_file, 'w') as f:
            f.write(html_content)