import re

def extract_h3_headers(html_content):
    pattern = r'<h3>(.*?)</h3>'
    
    headers = re.findall(pattern, html_content, re.DOTALL)
    
    return headers

def main():
    html_content = """
    <html>
    <head><title>Sample Web Page</title></head>
    <body>
        <h3>CONTENTS</h3>
        <h3>1. Creating a Web Page</h3>
        <h3>2. HTML Syntax</h3>
        <h3>3. Special Characters</h3>
        <h3>4. Converting Plain Text to HTML</h3>
        <h3>5. Effects</h3>
        <h3>6. Lists</h3>
        <h3>7. Links</h3>
        <h3>8. Tables</h3>
        <h3>9. Viewing Your Web Page</h3>
        <h3>10. Installing Your Web Page on the Internet</h3>
        <h3>11. Where to go from here</h3>
        <h3>12. Postscript: Cell Phones</h3>
    </body>
    </html>
    """
    
    headers = extract_h3_headers(html_content)
    
    print(headers)

if __name__ == "__main__":
    main()
