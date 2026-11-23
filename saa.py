
import requests
import math


# --------------------------------------------------
# PAIKKAKUNTIEN HAKU
# --------------------------------------------------

def hae_paikkakunnat(nimi):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    parametrit = {
        "name": nimi,
        "count": 20,
        "language": "fi",
        "format": "json"
    }

    vastaus = requests.get(url, params=parametrit, timeout=15)
    vastaus.raise_for_status()

    tulokset = vastaus.json().get("results", [])

    return [
        paikka for paikka in tulokset
        if paikka.get("country_code", "").upper() == "FI"
    ]


# --------------------------------------------------
# SÄÄTIETOJEN HAKU
# --------------------------------------------------

def hae_saa(leveysaste, pituusaste):
    url = "https://api.open-meteo.com/v1/forecast"

    parametrit = {
        "latitude": leveysaste,
        "longitude": pituusaste,
        "current": (
            "temperature_2m,wind_speed_10m,precipitation,"
            "cloud_cover,weather_code"
        ),
        "hourly": (
            "temperature_2m,wind_speed_10m,precipitation,"
            "cloud_cover,weather_code"
        ),
        "forecast_days": 2,
        "timezone": "Europe/Helsinki",
        "wind_speed_unit": "ms"
    }

    vastaus = requests.get(url, params=parametrit, timeout=15)
    vastaus.raise_for_status()

    return vastaus.json()


# --------------------------------------------------
# ETÄISYYDEN LASKEMINEN
# --------------------------------------------------

def laske_etaisyys(lat1, lon1, lat2, lon2):
    sade = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    a = min(1, max(0, a))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return sade * c


# --------------------------------------------------
# FRISBEEGOLFRATOJEN HAKU DISCGOLFAPISTA
# --------------------------------------------------

def hae_radat(leveysaste, pituusaste):
    url = "https://io.discgolfapi.com/v1/courses"

    kaikki_radat = []
    offset = 0
    limit = 100

    # Haetaan Suomen radat sivutettuna.
    while True:
        parametrit = {
            "country": "FI",
            "limit": limit,
            "offset": offset
        }

        vastaus = requests.get(
            url,
            params=parametrit,
            timeout=30
        )

        vastaus.raise_for_status()

        data = vastaus.json()
        haetut = data.get("courses", [])

        if not haetut:
            break

        kaikki_radat.extend(haetut)

        total = data.get("total")

        offset += limit

        if len(haetut) < limit:
            break

        if total is not None and offset >= total:
            break

    radat = []

    maksutiedot = {
        "public_free": "Ilmainen",
        "public_paid": "Maksullinen",
        "members_only": "Vaatii jäsenyyden",
        "private_permission_required": "Vaatii luvan",
        "unknown": "Ei tietoa"
    }

    # Espoo DiscGolfPark Worldin sijainti.
    espoo_lat = 60.2433
    espoo_lon = 24.5393

    # Käydään DiscGolfAPI:n radat läpi.
    for rata in kaikki_radat:

        lat = rata.get("lat", rata.get("latitude"))
        lon = rata.get("lon", rata.get("longitude"))

        if lat is None or lon is None:
            continue

        lat = float(lat)
        lon = float(lon)

        nimi = rata.get("name") or "Nimetön rata"
        nimi_pienilla = nimi.lower()

        # Yhdistetään Espoo DiscGolfPark Worldin
        # yksittäiset radat yhdeksi merkinnäksi.
        espoo_world_nimet = [
            "espoo discgolfpark world",
            "hyzr arena",
            "nuori espoo park",
            "ramirent park"
        ]

        on_espoo_world = any(
            hakusana in nimi_pienilla
            for hakusana in espoo_world_nimet
        )

        etaisyys_espoo = laske_etaisyys(
            lat,
            lon,
            espoo_lat,
            espoo_lon
        )

        # Ohitetaan Espoon keskuksen yksittäiset
        # ratamerkinnät, jotta niitä ei tule kahteen kertaan.
        if on_espoo_world and etaisyys_espoo <= 0.75:
            continue

        etaisyys = laske_etaisyys(
            float(leveysaste),
            float(pituusaste),
            lat,
            lon
        )

        # Rajataan haku 50 kilometriin.
        if etaisyys > 50:
            continue

        access_model = rata.get("access_model") or "unknown"

        maksu = maksutiedot.get(
            access_model,
            "Ei tietoa"
        )

        reikiä = rata.get("holes")

        if reikiä is None:
            layout = rata.get("primary_layout") or {}
            reikiä = layout.get("holes")

        if reikiä is None:
            reikiä = "Ei tietoa"

        radat.append({
            "nimi": nimi,
            "lat": lat,
            "lon": lon,
            "etaisyys": round(etaisyys, 1),
            "maksu": maksu,
            "paikkakunta": rata.get("locality") or "",
            "reikiä": reikiä,
            "linkki": (
                f"https://www.openstreetmap.org/"
                f"?mlat={lat}&mlon={lon}"
                f"#map=15/{lat}/{lon}"
            ),
            "verkkosivu": rata.get("website")
        })

    # --------------------------------------------------
    # ESPOO DISCGOLFPARK WORLD
    # --------------------------------------------------

    espoo_etaisyys = laske_etaisyys(
        float(leveysaste),
        float(pituusaste),
        espoo_lat,
        espoo_lon
    )

    # Lisätään Espoon keskus vain kerran,
    # jos se on 50 kilometrin säteellä.
    if espoo_etaisyys <= 50:

        radat.append({
            "nimi": "Espoo DiscGolfPark World",
            "lat": espoo_lat,
            "lon": espoo_lon,
            "etaisyys": round(espoo_etaisyys, 1),
            "maksu": "Vaatii varauksen",
            "paikkakunta": "Espoo",
            "reikiä": "45 (3 rataa)",
            "linkki": (
                "https://www.openstreetmap.org/"
                f"?mlat={espoo_lat}&mlon={espoo_lon}"
                f"#map=15/{espoo_lat}/{espoo_lon}"
            ),
            "verkkosivu": (
                "https://espooflyers.fi/"
                "espoo-discgolfpark-world/"
            )
        })

    # Lähimmät radat ensimmäiseksi.
    radat.sort(key=lambda x: x["etaisyys"])

    return radat


# --------------------------------------------------
# SÄÄTILOJEN KUVAUKSET
# --------------------------------------------------

def kuvaile_saa(koodi):
    kuvaukset = {
        0: "Selkeää",
        1: "Enimmäkseen selkeää",
        2: "Puolipilvistä",
        3: "Pilvistä",
        45: "Sumua",
        48: "Kuuraa ja sumua",
        51: "Heikkoa tihkusadetta",
        53: "Tihkusadetta",
        55: "Voimakasta tihkusadetta",
        61: "Heikkoa sadetta",
        63: "Sadetta",
        65: "Voimakasta sadetta",
        71: "Heikkoa lumisadetta",
        73: "Lumisadetta",
        75: "Voimakasta lumisadetta",
        80: "Heikkoja sadekuuroja",
        81: "Sadekuuroja",
        82: "Voimakkaita sadekuuroja",
        95: "Ukkosta",
        96: "Ukkosta ja rakeita",
        99: "Voimakasta ukkosta ja rakeita"
    }

    return kuvaukset.get(koodi, "Sääolosuhteet")


# --------------------------------------------------
# FRISBEEGOLF-SÄÄN ARVIOINTI
# --------------------------------------------------

def arvioi_saa(lampotila, tuuli, sade):
    pisteet = 0
    perustelut = []

    if lampotila < 0:
        pisteet += 2
        perustelut.append("Pakkasta")
    elif lampotila < 5:
        pisteet += 1
        perustelut.append("Viileä sää")
    elif lampotila > 25:
        pisteet += 1
        perustelut.append("Kuuma sää")

    if tuuli >= 10:
        pisteet += 3
        perustelut.append("Voimakas tuuli")
    elif tuuli >= 7:
        pisteet += 2
        perustelut.append("Melko voimakas tuuli")
    elif tuuli >= 5:
        pisteet += 1
        perustelut.append("Tuulinen sää")

    if sade >= 1:
        pisteet += 3
        perustelut.append("Sateinen sää")
    elif sade > 0:
        pisteet += 1
        perustelut.append("Mahdollista sadetta")

    if pisteet >= 4:
        arvio = "Huono"
        emoji = "🔴"
    elif pisteet >= 2:
        arvio = "Kohtalainen"
        emoji = "🟡"
    else:
        arvio = "Hyvä"
        emoji = "🟢"

    if not perustelut:
        perustelut.append(
            "Sääolosuhteet ovat hyvät pelaamiseen"
        )

    return arvio, emoji, perustelut
