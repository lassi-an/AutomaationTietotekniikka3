
import requests

PAIKKAKUNNAT = {
    "Helsinki": (60.17, 24.94),
    "Tampere": (61.50, 23.76),
    "Turku": (60.45, 22.27),
    "Espoo": (60.21, 24.66),
}


def hae_saa(paikkakunta):
    leveysaste, pituusaste = PAIKKAKUNNAT[paikkakunta]

    url = "https://api.open-meteo.com/v1/forecast"

    parametrit = {
        "latitude": leveysaste,
        "longitude": pituusaste,
        "current": "temperature_2m,wind_speed_10m,precipitation,cloud_cover",
        "daily": "sunrise,sunset",
        "forecast_days": 1,
        "wind_speed_unit": "ms",
        "timezone": "Europe/Helsinki",
    }

    vastaus = requests.get(url, params=parametrit, timeout=10)
    vastaus.raise_for_status()

    data = vastaus.json()

    saa = data["current"]

    # Lisätään auringonnousu ja -lasku säätietoihin
    saa["sunrise"] = data["daily"]["sunrise"][0]
    saa["sunset"] = data["daily"]["sunset"][0]

    return saa
