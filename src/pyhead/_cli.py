from pathlib import Path
from textwrap import dedent
from typing import Union, Optional

import click

from .presets import Favicon
from .tags import LinkTag

try:
    from favicons import Favicons
except ImportError:
    print("Please install the favicons library. Run 'pip install favicons'.")
    exit(1)


def check_source(source: Path) -> Optional[Path]:
    supported_file_ext = [".png", ".jpg", ".jpeg", ".gif", ".svg", ".tiff"]
    if source.is_file() and source.suffix.lower() in supported_file_ext:
        return source
    else:
        return None


py_file = """\
from pyhead import Head

head = Head()
head.set_favicon(
    ico_icon_href="{ico_icon_href}",
    png_icon_16_href="{png_icon_16_href}",
    png_icon_32_href="{png_icon_32_href}",
    png_icon_64_href="{png_icon_64_href}",
    png_icon_96_href="{png_icon_96_href}",
    png_icon_180_href="{png_icon_180_href}",
    png_icon_196_href="{png_icon_196_href}",
    png_apple_touch_icon_57_href="{png_apple_touch_icon_57_href}",
    png_apple_touch_icon_60_href="{png_apple_touch_icon_60_href}",
    png_apple_touch_icon_72_href="{png_apple_touch_icon_72_href}",
    png_apple_touch_icon_76_href="{png_apple_touch_icon_76_href}",
    png_apple_touch_icon_114_href="{png_apple_touch_icon_114_href}",
    png_apple_touch_icon_120_href="{png_apple_touch_icon_120_href}",
    png_apple_touch_icon_144_href="{png_apple_touch_icon_144_href}",
    png_apple_touch_icon_152_href="{png_apple_touch_icon_152_href}",
    png_apple_touch_icon_167_href="{png_apple_touch_icon_167_href}",
    png_apple_touch_icon_180_href="{png_apple_touch_icon_180_href}",
    png_mstile_70_href="{png_mstile_70_href}",
    png_mstile_270_href="{png_mstile_270_href}",
    png_mstile_310x150_href="{png_mstile_310x150_href}",
    png_mstile_310_href="{png_mstile_310_href}",
)"""


@click.group()
def cli() -> None:
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
@click.option(
    "--skip-code-generation",
    "-scg",
    is_flag=True,
    help="Skip generating the html and python code",
)
def generate_favicons(
    source: Path, output: Path, href_prefix: str, skip_code_generation: bool
) -> None:
    """
    Generate favicons from a source favicon file, supported file formats are [png, jpg, jpeg, gif, svg, tiff].

    Paths are relative to the current working directory.
    """
    cwd = Path.cwd()
    source = cwd / source
    output_dir = cwd / output

    raw_favicon = check_source(source)
    html_code = output_dir / "favicon-delete_me_after_use.html"
    object_code = output_dir / "favicon-delete_me_after_use.py"

    if raw_favicon is None:
        print(
            "Source file either does not exist, or is the incorrect format of [png, jpg, jpeg, gif, svg, tiff]"
        )
        exit(1)

    # Clear the output directory
    if not output_dir.exists():
        output_dir.mkdir()

    with Favicons(raw_favicon, output_dir) as favicons:
        favicons.generate()  #type: ignore
        favicon_tags = Favicon()
        for icon, meta in favicon_tags.icon_reference.items():
            setattr(
                favicon_tags,
                icon,
                LinkTag(
                    **{
                        k: v
                        for k, v in meta.items()
                        if k not in ["generated_filename", "content"]
                    },
                    href=f"{href_prefix if href_prefix.endswith('/') else href_prefix + '/'}"
                    f"{meta['generated_filename']}",
                ),
            )

        if not skip_code_generation:
            html_code.write_text(favicon_tags(), encoding="utf-8")
            object_code.write_text(
                dedent(
                    py_file.format(
                        **{
                            k: f"{href_prefix if href_prefix.endswith('/') else href_prefix + '/'}"
                            f"{v['generated_filename']}"
                            for k, v in favicon_tags.icon_reference.items()
                        }
                    )
                )
            )


if __name__ == "__main__":
    cli()
