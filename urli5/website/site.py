from requests_html import HTMLSession

_session = HTMLSession()

def renderSite(url: str):
    response = _session.get(url)

    # Render javascript
    response.html.render()
    return response.text

