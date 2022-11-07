import setuptools

setuptools.setup(
    name="robinhood_crypto_trader",
    version="1.0.0",
    author="Tyler Pruitt",
    description="A Python package for an automated cryptocurrency trader on the popular trading platform Robinhood",
    url="https://github.com/tyler-pruitt/robinhood-crypto-trader",
    packages=["robinhood_crypto_trader"],
    requires=["numpy", "robin_stocks", "pandas", "datetime", "time", "matplotlib", "pandas_ta", "random", "sys", "discord_webhook"],
    install_requires=["numpy", "robin_stocks", "pandas", "datetime", "time", "matplotlib", "pandas_ta", "random", "sys", "discord_webhook"],
    keywords=["robinhood", "crypto", "cryptocurrency", "trading", "autotrading", "investing", "robinhood crypto trader"],
    license="MIT"
)