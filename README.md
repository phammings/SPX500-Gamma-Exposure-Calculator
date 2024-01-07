# S&P 500 Gamma Calculator
<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">S&P 500 Gamma Calculator</h3>

  <p align="center">
This script is designed to generate the absolute gamma exposure and gamma profile charts of the S&P 500 index based on the current options market.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#instructions">Instructions</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project


The project obtains options data from [CBOE](https://www.cboe.com/delayed_quotes/spx/quote_table) on the S&P 500 index to generate the absolute gamma exposure (by dollars and by calls/puts) and the gamma profile of the current market.
<br/>
<br/>
<br/>
**Gamma Exposure in Equity Markets and Options Trading**

Gamma exposure refers to the impact of options trading, particularly in equity markets, and plays a crucial role in influencing market dynamics. This exposure is significant, especially in the case of S&P 500 options, which constitute a substantial portion (16%) of the S&P 500 market cap.

Options traders, often viewed as market makers, utilize delta-hedging to manage risks. Delta-hedging involves adjusting their positions in the underlying equity markets based on changes in the price of the asset. This process is essential to flatten risk, but it results in non-discretionary flows known as gamma exposure.

The gamma exposure depends on gamma, a measure indicating the potential delta-hedging activity. It has become more critical as the options market has grown, representing a sizable portion of the underlying equity market.

<br/>
Two key states are described based on gamma exposure:
<br/>

**Long Gamma**: Market makers are net buyers of options, providing liquidity during market rallies and absorbing it during drops. This contributes to reduced volatility.

**Short Gamma**: Market makers are net sellers of options, exacerbating market moves and reducing liquidity. This intensifies price actions, particularly during market downturns.

<br/>

Understanding net gamma positioning involves estimating the direction of options trades. Puts are generally associated with negative gamma, while calls carry positive gamma. The concept of a "gamma flip," where gamma is zero, is closely monitored as it indicates potential shifts in market conditions.

- When the S&P 500 spot price is at this gamma flip level, flows are zero, as delta doesn’t need rebalancing due to spot moves.


- When the S&P 500 spot price is above the gamma flip level, dealer hedging flows are stabilizing and add liquidity to the market.
  - A trader that is net long options has a positive gamma position, and hedges by selling stock as it goes up, and buying stock as it goes down. This can have the effect of dampening the underlying stocks movement and creating a low volatility environment.


- When the S&P 500 spot price is below the gamma flip level, dealer hedging flows are destabilizing and add to the volatility instead.
  - If a trade is net short options then the trader must hedge by selling the underlying as the stock goes down, and buying as the stock goes up. This could make the stock more volatile as this trading pressure pushes the stock in its prevailing direction. 


The impact of gamma exposure is influenced by factors such as time to expiry, open interest, market liquidity, and volatility. High open interest, especially around large expiries and at-the-money options, increases the likelihood of gamma flows impacting the market.

Despite its influence, gamma tends to lose potency in high volatility environments. In such situations, delta becomes less sensitive to underlying moves, affecting the concentration of gamma around the strike.

This project emphasizes the importance of recognizing and understanding gamma exposure to be prepared for its effects on equity markets.

<br/>

*All code and information above gives credits to [Perfiliev](https://perfiliev.co.uk/market-commentary/how-to-calculate-gamma-exposure-and-zero-gamma-level/) and [Spot Gamma](https://support.spotgamma.com/hc/en-us/articles/15413261162387-Gamma-Flip).*
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.py]][Python-url]
* [![Selenium][Selenium]][Selenium-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Scipy][Scipy]][Scipy-url]
* [![Shell Script][Shell]][Shell-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- ✔️ Employed Selenium for dynamic web scraping, seamlessly gathering data from online sources.
- ✔️ Utilized Python's powerful matplotlib and scipy libraries to perform intricate calculations and craft visually engaging image charts.
- ✔️ Orchestrated an efficient automation workflow using a shell script to streamline and execute the entire process effortlessly.



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- INSTRUCTIONS -->
## Instructions

- For Windows:
  - Git clone this repository
  - run ```gammaCalculator.sh``` to generate 3 charts:
    - Absolute Gamma Exposure by dollars chart
    - Absolute Gamma Exposure by calls/puts chart
    - Gamma Profile Exposure chart

    
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Gamma Exposure code calculations used from https://perfiliev.co.uk/market-commentary/how-to-calculate-gamma-exposure-and-zero-gamma-level/.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/
[Scipy]: https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white
[Scipy-url]: https://scipy.org/
[Shell]: https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white
[Shell-url]: https://www.shellscript.sh/

