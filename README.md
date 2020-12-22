# TFT Watcher TXT

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

TFT Watcher is an app designed to help TFT players prepare for tournaments by breaking down opponents' match history, item tendency, composition tendency, and average position.

This project is phase 1 of TFT Watcher, TFT Watcher TXT. In this project, the output and results found will be written onto a txt file. Stay tuned for future development for phase 2 and phase 3. 

### Built With

This project is built with:
* [League of Legends Watcher](https://riot-watcher.readthedocs.io/en/latest/riotwatcher/LeagueOfLegends/index.html)
* [Team Fight Tactics Watcher](https://riot-watcher.readthedocs.io/en/latest/riotwatcher/TeamFightTactics/index.html)
* [Pandas](https://pandas.pydata.org/getting_started.html)
* [JSON](https://docs.python.org/3/library/json.html)



<!-- GETTING STARTED -->
## Getting Started

Before you use this project, please follow the prerequisites and complete. 

<!-- USAGE EXAMPLES -->
### Prerequisites

Things you need to use the project and how to install them.

1. Get your API Key at [https://developer.riotgames.com/](https://developer.riotgames.com/)
2. Clone the repo
   ```sh
   git clone https://github.com/DevJFok/tft-watcher-txt
   ```
3. Install Riot Watcher packages
   ```sh
   pip install riotwatcher
   ```
4. Enter your API in `tft_api_main.py`
   ```JS
   api_key = 'enter-your-api-key'
   ```

<!-- USAGE EXAMPLES -->
## Usage

The program accepts 3 inputs:

1. Enter a valid League of Legends Summoner Name: 
  ```sh
   Enter Summoner Name: Xentury
   ```
2. Enter a valid League of Legends Region:
   Valid Regions include: na1, euw1, eun1, kr, jp1
   ```sh
   Please enter your server: na1
   ```
3. Enter a valid integer greater than 0:
   ```sh
   Enter Match History count: 10
   ```

The input should look like this:
[![Input Screenshot][input-screenshot]](https://example.com)

_For more examples, please refer to the [Documentation](https://example.com)_

<!-- CONTACT -->
## Contact

LinkedIn - [/jarrett-fok](https://www.linkedin.com/in/jarrett-fok/) - jarrettfok@gmail.com

Project Link: [https://github.com/DevJFok/tft-watcher-txt](https://github.com/DevJFok/tft-watcher-txt)

[input-screenshot]: images/input_screenshot.png