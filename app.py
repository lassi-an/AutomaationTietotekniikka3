
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

from saa import (
    hae_paikkakunnat,
    hae_saa,
    hae_radat,
    kuvaile_saa,
    arvioi_saa
)


AIKA_VYOHYKE = ZoneInfo("Europe/Helsinki")


# --------------------------------------------------
# SIVUN ASETUKSET
# --------------------------------------------------

st.set_page_config(
    page_title="Frisbeegolf-säävahti",
    page_icon="🥏",
    layout="wide"
)


# --------------------------------------------------
# TUMMA ULKOASU
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #101b16;
    color: #edf5ef;
}

[data-testid="stAppViewContainer"] {
    background-color: #101b16;
}

[data-testid="stHeader"] {
    background-color: transparent;
}

h1, h2, h3, h4 {
    color: #55cc83 !important;
}

p, li, label {
    color: #dce9df;
}

.stTextInput input {
    background-color: #1c2b23 !important;
    color: white !important;
    border: 1px solid #42634d !important;
    border-radius: 9px !important;
}

.stTextInput input::placeholder {
    color: #a4b7a9 !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #1c2b23 !important;
    color: white !important;
    border-color: #42634d !important;
}

.stButton button {
    background-color: #218653 !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: bold !important;
}

.stButton button:hover {
    background-color: #35a968 !important;
    color: white !important;
}

.weather-card {
    background-color: #1c2b23;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #365b42;
    margin-bottom: 12px;
    color: #edf5ef;
}

[data-testid="stMetric"] {
    background-color: #1c2b23;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #365b42;
}

[data-testid="stMetricValue"] {
    color: #55cc83 !important;
}

[data-testid="stMetricLabel"] {
    color: #c5d7ca !important;
}

hr {
    border-color: #365b42 !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# OTSIKKO
# --------------------------------------------------

st.title("🥏 Frisbeegolf-säävahti")

st.write(
    "Tarkista sää ennen frisbeegolfkierrosta, "
    "katso tuntiennuste ja löydä lähistöllä olevia ratoja."
)


# --------------------------------------------------
# ISTUNNON ALUSTUS
# --------------------------------------------------

if "paikkakuntatulokset" not in st.session_state:
    st.session_state.paikkakuntatulokset = []

if "valittu_paikka" not in st.session_state:
    st.session_state.valittu_paikka = None


# --------------------------------------------------
# PAIKKAKUNNAN HAKU
# --------------------------------------------------

st.header("📍 Etsi paikkakunta")

paikkakunta = st.text_input(
    "Kirjoita paikkakunnan nimi",
    placeholder="Esim. Helsinki, Tampere tai Kuopio"
)


if st.button("Hae paikkakunta", type="primary"):

    if not paikkakunta.strip():

        st.warning("Kirjoita ensin paikkakunnan nimi.")

    else:

        try:

            tulokset = hae_paikkakunnat(
                paikkakunta.strip()
            )

            st.session_state.paikkakuntatulokset = tulokset
            st.session_state.valittu_paikka = None

            if not tulokset:

                st.warning(
                    "Paikkakuntaa ei löytynyt. "
                    "Kokeile toista hakusanaa."
                )

        except Exception as e:

            st.error(
                f"Paikkakuntahaku epäonnistui: {e}"
            )


# --------------------------------------------------
# PAIKKAKUNNAN VALINTA
# --------------------------------------------------

if st.session_state.paikkakuntatulokset:

    vaihtoehdot = st.session_state.paikkakuntatulokset

    def paikan_nimi(paikka):

        alue = paikka.get("admin1", "")
        maa = paikka.get("country", "Suomi")

        if alue:

            return (
                f"{paikka['name']} – "
                f"{alue}, {maa}"
            )

        return f"{paikka['name']} – {maa}"

    valinta = st.selectbox(
        "Valitse oikea paikkakunta",
        vaihtoehdot,
        format_func=paikan_nimi
    )

    if st.button("Näytä säätiedot", type="primary"):

        st.session_state.valittu_paikka = valinta


# --------------------------------------------------
# SÄÄTIEDOT
# --------------------------------------------------

if st.session_state.valittu_paikka:

    paikka = st.session_state.valittu_paikka

    st.divider()

    st.header(
        f"🌤️ Sää: {paikka['name']}"
    )

    try:

        data = hae_saa(
            paikka["latitude"],
            paikka["longitude"]
        )

        nykyinen = data["current"]

        lampotila = nykyinen["temperature_2m"]
        tuuli = nykyinen["wind_speed_10m"]
        sade = nykyinen["precipitation"]
        pilvisyys = nykyinen["cloud_cover"]
        koodi = nykyinen["weather_code"]

        arvio, emoji, perustelut = arvioi_saa(
            lampotila,
            tuuli,
            sade
        )

        # NYKYINEN SÄÄ

        st.subheader("Tämänhetkinen sää")

        sarakkeet = st.columns(4)

        sarakkeet[0].metric(
            "🌡️ Lämpötila",
            f"{lampotila} °C"
        )

        sarakkeet[1].metric(
            "💨 Tuuli",
            f"{tuuli} m/s"
        )

        sarakkeet[2].metric(
            "🌧️ Sade",
            f"{sade} mm"
        )

        sarakkeet[3].metric(
            "☁️ Pilvisyys",
            f"{pilvisyys} %"
        )

        st.write(
            f"**Säätila:** {kuvaile_saa(koodi)}"
        )

        # PELAAMISSÄÄ

        st.subheader("🥏 Arvio frisbeegolfiin")

        if arvio == "Hyvä":

            st.success(
                f"{emoji} {arvio} pelaamissää"
            )

        elif arvio == "Kohtalainen":

            st.warning(
                f"{emoji} {arvio} pelaamissää"
            )

        else:

            st.error(
                f"{emoji} {arvio} pelaamissää"
            )

        st.write("**Arvion perustelut:**")

        for perustelu in perustelut:

            st.write(f"- {perustelu}")

        # --------------------------------------------------
        # TUNTIENNUSTE
        # --------------------------------------------------

        st.divider()

        st.header("🕒 Sää seuraavien tuntien aikana")

        tuntidata = data["hourly"]

        nykyhetki = datetime.now(AIKA_VYOHYKE)

        ennusteet = []

        for i, aika in enumerate(tuntidata["time"]):

            ennusteaika = datetime.fromisoformat(
                aika
            ).replace(tzinfo=AIKA_VYOHYKE)

            if ennusteaika >= nykyhetki:

                ennusteet.append(i)

            if len(ennusteet) >= 4:

                break

        if ennusteet:

            sarakkeet = st.columns(len(ennusteet))

            for sarake, i in zip(sarakkeet, ennusteet):

                aika = tuntidata["time"][i]

                lampo = tuntidata["temperature_2m"][i]

                tuuli_tunti = tuntidata["wind_speed_10m"][i]

                sade_tunti = tuntidata["precipitation"][i]

                koodi_tunti = tuntidata["weather_code"][i]

                with sarake:

                    st.markdown(
                        '<div class="weather-card">',
                        unsafe_allow_html=True
                    )

                    st.subheader(aika[11:16])

                    st.metric(
                        "Lämpötila",
                        f"{lampo} °C"
                    )

                    st.write(
                        f"💨 Tuuli: {tuuli_tunti} m/s"
                    )

                    st.write(
                        f"🌧️ Sade: {sade_tunti} mm"
                    )

                    st.write(
                        kuvaile_saa(koodi_tunti)
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

        else:

            st.info(
                "Tuntiennustetta ei löytynyt."
            )

        # --------------------------------------------------
        # FRISBEEGOLFRADAT
        # --------------------------------------------------

        st.divider()

        st.header(
            "🥏 Lähistöllä olevat frisbeegolfradat"
        )

        st.caption(
            "Etsitään ratoja 50 kilometrin säteeltä "
            "valitusta paikkakunnasta."
        )

        try:

            with st.spinner(
                "Haetaan Suomen frisbeegolfratoja..."
            ):

                radat = hae_radat(
                    paikka["latitude"],
                    paikka["longitude"]
                )

            if radat:

                st.success(
                    f"Löytyi {len(radat)} rataa lähialueelta!"
                )

                for i, rata in enumerate(radat[:10], 1):

                    with st.container(border=True):

                        st.subheader(
                            f"{i}. {rata['nimi']}"
                        )

                        if rata["paikkakunta"]:

                            st.write(
                                f"📍 Paikkakunta: "
                                f"{rata['paikkakunta']}"
                            )

                        st.write(
                            f"📏 Etäisyys: "
                            f"{rata['etaisyys']} km"
                        )

                        st.write(
                            f"💶 Maksutieto: "
                            f"{rata['maksu']}"
                        )

                        if rata["reikiä"]:

                            st.write(
                                f"🕳️ Väyliä: "
                                f"{rata['reikiä']}"
                            )

                        st.markdown(
                            f"[📍 Avaa rata kartalla]"
                            f"({rata['linkki']})"
                        )

                        if rata["verkkosivu"]:

                            st.markdown(
                                f"[🌐 Radatiedot ja verkkosivu]"
                                f"({rata['verkkosivu']})"
                            )

            else:

                st.warning(
                    "DiscGolfAPI ei löytänyt ratoja "
                    "50 kilometrin säteeltä."
                )

                st.info(
                    "Tietokannassa ei välttämättä ole "
                    "kaikkia Suomen frisbeegolfratoja."
                )

        except Exception as e:

            st.error(
                "Frisbeegolfratojen hakeminen epäonnistui."
            )

            with st.expander(
                "Näytä tekninen virheilmoitus"
            ):

                st.code(str(e))

    except Exception as e:

        st.error(
            f"Säätietojen hakeminen epäonnistui: {e}"
        )


# --------------------------------------------------
# ALATUNNISTE
# --------------------------------------------------

st.divider()

st.caption(
    "Frisbeegolf-säävahti | "
    "Säätiedot: Open-Meteo | "
    "Ratatiedot: DiscGolfAPI"
)

st.caption(
    "Course data supplied by DiscGolfAPI."
)
