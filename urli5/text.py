import click
from .website import render

@click.command()
@click.option("--out-file", "-o", default="./output",
    help="Directory to store artifacts after processing url.")
@click.argument('url')
def url2text(out_file, url):
    """
    Summarizes any url to a text file
    """
    with open(f"{out_file}.html", "w") as out:
        text = render(url)
        print(text)
        out.write(text)

def main():
    url2text()

if __name__ =="__main__":
    main()
