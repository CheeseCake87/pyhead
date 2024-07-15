from pathlib import Path

import click

from pyhead.tags import FavIcon, LinkTag

try:
    from favicons import Favicons
except ImportError:
    print("Please install the favicons library. Run 'pip install favicons'.")
    exit(1)


def check_source(source: Path) -> Path | None:
    supported_file_ext = [".png", ".jpg", ".jpeg", ".gif", ".svg", ".tiff"]
    if source.is_file() and source.suffix.lower() in supported_file_ext:
        return source
    else:
        return None


@click.group()
def cli():
    pass


@cli.command("favicons")
@click.option("--source", "-s", type=click.Path(), help="Path to the raw favicon file.")
@click.option(
    "--output",
    "-o",
    type=click.Path(),
    help="Folder to save the generated favicons.",
    default="favicons",
)
@click.option(
    "--href-prefix",
    "-hp",
    type=click.STRING,
    help="value to prefix the href attribute of the link tag",
    default="",
)
def generate_favicons(source, output, href_prefix: str):
    """
    Generate favicons from a source favicon file, supported file formats are [png, jpg, jpeg, gif, svg, tiff].

    Paths are relative to the current working directory.
    """
    cwd = Path.cwd()
    source = cwd / source
    output_dir = cwd / output

    raw_favicon = check_source(source)
    html_code = output_dir / "favicon.html"

    if raw_favicon is None:
        print(
            "Source file either does not exist, or is the incorrect format of [png, jpg, jpeg, gif, svg, tiff]"
        )
        exit(1)

    # Clear the output directory
    if not output_dir.exists():
        output_dir.mkdir()

    with Favicons(raw_favicon, output_dir) as favicons:
        favicons.generate()
        favicon_tags = FavIcon()
        for icon, meta in favicon_tags.icon_reference.items():
            setattr(
                favicon_tags,
                icon,
                LinkTag(
                    **meta,
                    href=f"{href_prefix if href_prefix.endswith('/') else href_prefix + '/'}"
                    f"{meta['generated_filename']}",
                ),
            )

        html_code.write_text(favicon_tags(), encoding="utf-8")


if __name__ == "__main__":
    cli()
