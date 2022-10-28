# robinhood-crypto-trader
An automated trader for crypto on Robinhood

## Donate to this project and help support open-sourced financial software (anything helps!)

### I am happy to accept the following crypto currencies as gifts, it is much appreciated!
- Bitcoin (BTC) wallet address: `bc1qvljdr72k3tz6w8k6hpnhv3722fmsgftkeeakx8`
- Ethereum (ETH), US Dollar Coin (USDC), Polygon (MATIC), Shiba Inu (SHIB), Avalanche (AVAX), Uniswap (UNI), Chainlink (LINK), Compound (COMP), Aave (AAVE) wallet address: `0xDd5E232561177e5E48432F6BA4fD12173Bbe869A`
- Cardano (ADA) wallet address: `addr1q8g90gwc2u82fnv6m0pw7crervtslar746rxx06apfcf44cg6h5us0avc20ee2azzun58lgylyl54sjr6y9efwq86krst57w35`
- Solana (SOL) wallet address: `EzQveUMk45NmuftUSGLqRH8DUBmxzCpS3HuEchFc5t1X`
- Dogecoin (DOGE) wallet address: `DQCzww2Sz9UhtAaMZbHHGofng1ioRgTkEu`
- Ethereum Classic (ETC) wallet address: `0x42D1125fB02D0eaAA3b0D57330EC46AaF5F95F15`
- Litecoin (LTC) wallet address: `ltc1qvwzqm4jxqt0gjf7fwzxpnvtlssxtc9lutrnxsh`
- Bitcoin Cash (BCH) wallet address: `bitcoincash:qr4h4edxt5muv2ns3kls0d4ca8lezu8x9v9d4r227h`
- Tezos (XTZ) wallet address: `tz1Wexc9bv6BxCBgyXwaqmJq1RNYxXBr9aff`

<!--
- Stellar Lumens (XLM): `Currently unable to send and receive on Robinhood`
- Bitcoin SV (BSV): `Currently unable to send and receive on Robinhood`
-->

## New to Robinhood?
Join Robinhood with my link and we'll both pick our own free stock 🤝 https://join.robinhood.com/tylerp5773

## How to run the code:
### 1. place all files in the same folder 
### 2. run code which follows the example code:

```python
import trader

config = {
            'crypto': ['BTC', 'ETH'],
            'username': 'your_robinhood_username',
            'password': 'your_robinhood_password',
            'days_to_run': 1,
            'export_csv': False,
            'plot_analytics': False,
            'plot_crypto': False,
            'plot_portfolio': False,
            'mode': 'safelive',
            'backtest': {
                'interval': '15second',
                'span': 'hour',
                'bounds': '24_7',
                'index': 10
            },
            'trader': {
                'interval': '15second',
                'span': 'hour',
                'bounds': '24_7'
            },
            'determine_trade_function': 'function_name',
            'cash': 2000,
            'use_cash': True,
            'loss_threshold': 50.00,
            'holdings_factor': 0.20,
            'cash_factor': 0.20
        }

tr = trader.Trader(config)

tr.run()
```
