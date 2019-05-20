# ToripollisiBot

Telegrambotti, joka näyttää livekuvan Oulun kaupungin Kauppatorilta. Käytetty feedi löytyy [Oulun Kaupungin sivuilta](https://www.ouka.fi/oulu/oulu-tietoa/nettikamerat). Botti löytyy nickillä [@ToripolliisiBot](http://t.me/ToripollisiBot)

## Vaatimukset
* Python 3
* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
```
$ pip install python-telegram-bot
```

## Asennus
* Luo botti ja saa API-avain [@BotFather](http://t.me/BotFather)
* Tallenna API-avain ENV-muuttujaksi
```
$ export TGTORI_TOKEN=”ApiAvainTähän”
```

## Käynnistys
```
$ screen -S toripolliisibot
$ python toripolliisi.py
```

## Käyttö
* Lähetä botille komento ```/toripolliisi```

<img src="http://www.oulunkaupunki.fi/_private/kamera/picture1.jpg" alt="Livefeedi" width="50%" height="50%" style="
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%; "/>

## Suuret kiitokset
* Oulun kaupunki
* Aalto yliopiston Fyysikkokillan kahvikone
