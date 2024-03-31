def html_text(name, verification_link) -> str:
    html_text: str = f"""
    <html>
    <body>
        <p>Hello {name}!</p>
        <p>Verification link <a href="{verification_link}">here</a></p>
    </body>
    </html>
    """

    return html_text
