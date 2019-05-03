# Fyysikkokillan fuksimatrikkeli 2019 pistebot

Aalto yliopiston Fyysikkokillan fuksimatrikkeli 2019 korttipelin pisteytys telegrambotti

## Vaatimukset
* Python 2.7.2+
* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
```
$ pip install python-telegram-bot
```

## Asennus
* Luo botti ja saa API-avain [@BotFather](http://t.me/BotFather)
* Tallenna API-avain ENV-muuttujaksi
```
$ export TGPISTE_TOKEN=”ApiAvainTähän”
```

## Käynnistys
```
$ screen -S pistebot
$ python pistebot.py
```

## Käyttö
Voit laskea pisteet komennolla "/pisteet x_1 x_2 ... x_n", missä x_n on korttien määrä jokaisessa ryhmässäsi.
* Jos jostain ryhmästä ei ole yhtään korttia, ei tarvitse merkitä 0.
Pisteet lasketaan oheisen kaavan mukaan.

<img src="https://raw.githubusercontent.com/NikoDaGreat/fk-fuksimatrikkeli-2019-pistebot/master/kaava.jpg" alt="LaTeX-kaava" width="50%" height="50%" style="
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%; "/>

## Suuret kiitokset
* Matrikkelitoimikunta 2019
* Fyysikkokillan kahvikone
* [kvantti-telegram-bot-example](https://github.com/EinariTuukkanen/kvantti-telegram-bot-example)
