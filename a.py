from pathlib import Path

print(
    Path(__file__)
    .resolve()
    .parent.joinpath("helpers", "web_drivers", "chromedriver-linux64", "chromedriver")
)
