
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
from saa import hae_saa


st.set_page_config(
    page_title="Frisbeegolf-säävahti",
    page_icon="🥏",
    layout="centered"
)

st.title("🥏 Frisbeegolf-säävahti")

st.write(
    "Tarkista sääolosuhteet ennen frisbeegolfkierrosta!"
)


# Paikkakuntien radat ja maksullisuustiedot
RADAT = {
    "Helsinki": [
        {
            "nimi": "Talin Frisbeegolfrata",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Kivikon frisbeegolfrata",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Paloheinän frisbeegolfrata",
            "maksu": "Ilmainen",
            "varaus": False
        }
    ],

    "Tampere": [
        {
            "nimi": "Tampereen frisbeegolfkeskus",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Teiskon frisbeegolfrata",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Epilän frisbeepuisto",
            "maksu": "Ilmainen",
            "varaus": False
        }
    ],

    "Turku": [
        {
            "nimi": "Lausteen frisbeegolfrata",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Luolavuoren frisbeegolfrata",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Hirvensalo DiscGolfPark",
            "maksu": "Ilmainen",
            "varaus": False
        }
    ],

    "Espoo": [
        {
            "nimi": "Espoo DiscGolfPark World",
            "maksu": "Maksullinen",
            "varaus": True
        },
        {
            "nimi": "Puolarmaari frisbeegolf",
            "maksu": "Ilmainen",
            "varaus": False
        },
        {
            "nimi": "Äijänpelto frisbeegolf",
            "maksu": "Ilmainen",
            "varaus": False
        }
    ]
}


# Ruuhkaisuuden arviointi vuodenajan, viikonpäivän
# kellonajan ja valoisuuden perusteella
def arvioi_ruuhkaisuus(nyt, auringonnousu, auringonlasku):

    tunti = nyt.hour
    kuukausi = nyt.month
    viikonloppu = nyt.weekday() >= 5

    # Muutetaan ajat minuuteiksi
    nykyhetki = nyt.hour * 60 + nyt.minute

    nousu = datetime.fromisoformat(
        auringonnousu
    )

    lasku = datetime.fromisoformat(
        auringonlasku
    )

    nousu_min = nousu.hour * 60 + nousu.minute
    lasku_min = lasku.hour * 60 + lasku.minute

    # Tarkistetaan, onko aurinko noussut
    valoisaa = nousu_min <= nykyhetki <= lasku_min

    # Pimeän aikaan arvioidaan radat hiljaisiksi
    if not valoisaa:
        return "Hiljainen", "#2eaa65"

    # Talvi: marraskuu–helmikuu
    if kuukausi in [11, 12, 1, 2]:

        if viikonloppu and 11 <= tunti < 15:
            return "Kohtalainen", "#d99b20"

        return "Vähäinen", "#2eaa65"

    # Kevät ja syksy
    elif kuukausi in [3, 4, 5, 9, 10]:

        if viikonloppu and 10 <= tunti < 16:
            return "Kohtalainen", "#d99b20"

        elif not viikonloppu and 15 <= tunti < 19:
            return "Kohtalainen", "#d99b20"

        return "Vähäinen", "#2eaa65"

    # Kesä
    else:

        if viikonloppu and 11 <= tunti < 18:
            return "Ruuhkainen", "#e05252"

        elif not viikonloppu and 16 <= tunti < 20:
            return "Ruuhkainen", "#e05252"

        elif tunti < 10:
            return "Vähäinen", "#2eaa65"

        return "Kohtalainen", "#d99b20"


paikkakunta = st.selectbox(
    "Valitse paikkakunta:",
    ["Helsinki", "Tampere", "Turku", "Espoo"]
)


if st.button("Hae säätiedot"):

    try:
        saa = hae_saa(paikkakunta)

        lampotila = saa["temperature_2m"]
        tuuli = saa["wind_speed_10m"]
        sade = saa["precipitation"]
        pilvisyys = saa["cloud_cover"]

        auringonnousu = saa["sunrise"]
        auringonlasku = saa["sunset"]

        # Suomen paikallinen kellonaika
        nyt = datetime.now(
            ZoneInfo("Europe/Helsinki")
        )

        # Lasketaan ruuhkaisuus
        ruuhkaisuus, ruuhka_vari = arvioi_ruuhkaisuus(
            nyt,
            auringonnousu,
            auringonlasku
        )

        st.divider()

        # Ratasuositukset
        st.subheader("🥏 Suositellut frisbeegolfradat")

        nimi_sarake, maksu_sarake, ruuhka_sarake = st.columns(
            [4, 1.5, 2]
        )

        with nimi_sarake:
            st.write("**Rata**")

        with maksu_sarake:
            st.write("**Hinta**")

        with ruuhka_sarake:
            st.write("**Ruuhkaisuus**")

        st.divider()

        # Jokainen rata omalla rivillään
        for rata in RADAT[paikkakunta]:

            nimi_sarake, maksu_sarake, ruuhka_sarake = st.columns(
                [4, 1.5, 2]
            )

            with nimi_sarake:
                st.write(f"**{rata['nimi']}**")

            with maksu_sarake:
                st.write(rata["maksu"])

            with ruuhka_sarake:

                if rata["varaus"]:
                    tila = "Riippuu varauksista"
                    vari = "#3984d6"

                else:
                    tila = ruuhkaisuus
                    vari = ruuhka_vari

                st.markdown(
                    f"""
                    <span style="
                        background-color: {vari};
                        color: white;
                        padding: 5px 9px;
                        border-radius: 6px;
                        font-size: 13px;
                        font-weight: bold;
                        white-space: nowrap;
                    ">
                        {tila}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        if paikkakunta == "Espoo":
            st.info(
                "Espoo DiscGolfPark World vaatii lähtöajan "
                "varaamisen. Tarkista vapaat ajat ennen lähtöä."
            )

        st.divider()

        # Säätiedot
        st.subheader(f"Sää paikkakunnalla {paikkakunta}")

        st.metric("Lämpötila", f"{lampotila} °C")
        st.metric("Tuulen nopeus", f"{tuuli} m/s")
        st.metric("Sademäärä", f"{sade} mm")

        # Taivaan tila
        st.subheader("🌤️ Taivaan tila")

        if pilvisyys <= 20:
            st.write("☀️ Aurinkoista")

        elif pilvisyys <= 60:
            st.write("⛅ Puolipilvistä")

        else:
            st.write("☁️ Pilvistä")

        st.caption(f"Pilvipeite: {pilvisyys} %")

        st.divider()

        # Frisbeegolfin sääarvio
        st.subheader("🥏 Frisbeegolf-sääarvio")

        if lampotila >= 5 and tuuli <= 5 and sade <= 0.2:

            st.success(
                "Hyvä pelisää! Olosuhteet ovat suotuisat pelaamiseen."
            )

            st.write(
                "Lämpötila, tuuli ja sademäärä ovat hyvällä tasolla frisbeegolfiin."
            )

        elif lampotila >= 0 and tuuli <= 10 and sade <= 1:

            st.warning(
                "Kohtalainen pelisää. Olosuhteissa on hieman huomioitavaa."
            )

            if lampotila < 5:
                st.write("• Lämpötila on melko alhainen.")

            if tuuli > 5:
                st.write("• Tuuli voi vaikeuttaa kiekon hallintaa.")

            if sade > 0.2:
                st.write("• Sateesta voi olla haittaa pelaamiselle.")

        else:

            st.error(
                "Huono pelisää. Sääolosuhteet eivät ole parhaat pelaamiseen."
            )

            if lampotila < 0:
                st.write("• Pakkaslämpötila voi vaikeuttaa pelaamista.")

            if tuuli > 10:
                st.write("• Voimakas tuuli vaikeuttaa kiekon hallintaa.")

            if sade > 1:
                st.write("• Sademäärä on melko suuri.")

    except Exception as e:
        st.error(
            f"Säätietojen hakeminen epäonnistui: {e}"
        )
