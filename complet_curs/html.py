_file = open("index.html", "w", encoding="utf-8")
_file.write(
    """
    <!DOCTYPE HTML>
        <HTML lang=\"pt-br\">
            <HEAD>
                <title>Test</title>
            </HEAD>
            <BODY>
                andlucsil
            </BODY>
        </HTML>
    """
)
_file.flush()
_file.close()