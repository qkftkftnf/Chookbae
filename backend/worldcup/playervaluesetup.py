from .models import Player
from .translation import team_k

# 리그 정보
def value_p(team):
    leagues = [
        {"pk": 1, "weight": 1.50, "league": "EPL", "rank": 1, "id": 9, "team_name": "Arsenal FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15669942151527.png",},
        {"pk": 2, "weight": 1.49, "league": "EPL", "rank": 2, "id": 4, "team_name": "Manchester City", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524863261959.png",},
        {"pk": 3, "weight": 1.48, "league": "EPL", "rank": 3, "id": 2, "team_name": "Tottenham Hotspur FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552486480602.png",},
        {"pk": 4, "weight": 1.47, "league": "EPL", "rank": 4, "id": 10, "team_name": "Newcastle United FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524864301957.png",},
        {"pk": 5, "weight": 1.46, "league": "EPL", "rank": 5, "id": 7, "team_name": "Manchester United", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552486381728.png",},
        {"pk": 6, "weight": 1.45, "league": "EPL", "rank": 6, "id": 8, "team_name": "Chelsea FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524829401976.png",},
        {"pk": 7, "weight": 1.44, "league": "EPL", "rank": 7, "id": 5, "team_name": "Fulham FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524831212190.png",},
        {"pk": 8, "weight": 1.43, "league": "EPL", "rank": 8, "id": 19, "team_name": "Brighton & Hove Albion", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524825522856.png",},
        {"pk": 9, "weight": 1.42, "league": "EPL", "rank": 9, "id": 3, "team_name": "Liverpool FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16258353592797.png",},
        {"pk": 10, "weight": 1.41, "league": "EPL", "rank": 10, "id": 15, "team_name": "Crystal Palace", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524867882856.png",},
        {"pk": 11, "weight": 1.40, "league": "EPL", "rank": 11, "id": 186, "team_name": "Brentford FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681868821055.png",},
        {"pk": 12, "weight": 1.39, "league": "EPL", "rank": 12, "id": 6, "team_name": "Everton FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524829951130.png",},
        {"pk": 13, "weight": 1.38, "league": "EPL", "rank": 13, "id": 1, "team_name": "West Ham United", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524865522808.png",},
        {"pk": 14, "weight": 1.37, "league": "EPL", "rank": 14, "id": 16, "team_name": "AFC Bournemouth", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524821011860.png",},
        {"pk": 15, "weight": 1.36, "league": "EPL", "rank": 15, "id": 176, "team_name": "Leeds United FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568183667499.png",},
        {"pk": 16, "weight": 1.35, "league": "EPL", "rank": 16, "id": 112, "team_name": "Aston Villa", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15650923042439.png",},
        {"pk": 17, "weight": 1.34, "league": "EPL", "rank": 17, "id": 17, "team_name": "Southampton FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552486916606.png",},
        {"pk": 18, "weight": 1.33, "league": "EPL", "rank": 18, "id": 14, "team_name": "Leicester City", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl155248319886.png",},
        {"pk": 19, "weight": 1.32, "league": "EPL", "rank": 19, "id": 13, "team_name": "Wolverhampton Wanderers", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524866411365.png",},
        {"pk": 20, "weight": 1.31, "league": "EPL", "rank": 20, "id": 183, "team_name": "Nottingham Forest FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1598387963213.png",},
        {"pk": 21, "weight": 1.50, "league": "La Liga", "rank": 1, "id": 37, "team_name": "Real Madrpk", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15699196532768.png",},
        {"pk": 22, "weight": 1.49, "league": "La Liga", "rank": 2, "id": 23, "team_name": "FC Barcelona", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529033261956.png",},
        {"pk": 23, "weight": 1.48, "league": "La Liga", "rank": 3, "id": 39, "team_name": "Atlético Madrpk", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529031822494.png",},
        {"pk": 24, "weight": 1.47, "league": "La Liga", "rank": 4, "id": 30, "team_name": "Real Betis", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529045282082.png",},
        {"pk": 25, "weight": 1.46, "league": "La Liga", "rank": 5, "id": 32, "team_name": "Real Sociedad", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529046931338.png",},
        {"pk": 26, "weight": 1.45, "league": "La Liga", "rank": 6, "id": 40, "team_name": "Athletic Bilbao", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529030931150.png",},
        {"pk": 27, "weight": 1.44, "league": "La Liga", "rank": 7, "id": 114, "team_name": "CA Osasuna", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1565093374989.png",},
        {"pk": 28, "weight": 1.43, "league": "La Liga", "rank": 8, "id": 38, "team_name": "Villarreal CF", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529040772871.png",},
        {"pk": 29, "weight": 1.42, "league": "La Liga", "rank": 9, "id": 29, "team_name": "Rayo Vallecano", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16258455191493.png",},
        {"pk": 30, "weight": 1.41, "league": "La Liga", "rank": 10, "id": 25, "team_name": "Valencia CF", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529056661540.png",},
        {"pk": 31, "weight": 1.40, "league": "La Liga", "rank": 11, "id": 28, "team_name": "Real Valladolpk CF", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1655813069257.png",},
        {"pk": 32, "weight": 1.39, "league": "La Liga", "rank": 12, "id": 115, "team_name": "RCD Mallorca", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15650934332331.png",},
        {"pk": 33, "weight": 1.38, "league": "La Liga", "rank": 13, "id": 350, "team_name": "UD Almería", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15737464261213.png",},
        {"pk": 34, "weight": 1.37, "league": "La Liga", "rank": 14, "id": 24, "team_name": "Getafe CF", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529038152342.png",},
        {"pk": 35, "weight": 1.36, "league": "La Liga", "rank": 15, "id": 31, "team_name": "RCD Espanyol", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529036851486.png",},
        {"pk": 36, "weight": 1.35, "league": "La Liga", "rank": 16, "id": 21, "team_name": "Celta de Vigo", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529034002054.png",},
        {"pk": 37, "weight": 1.34, "league": "La Liga", "rank": 17, "id": 26, "team_name": "Girona FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16659715192718.png",},
        {"pk": 38, "weight": 1.33, "league": "La Liga", "rank": 18, "id": 33, "team_name": "Sevilla FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529048391082.png",},
        {"pk": 39, "weight": 1.32, "league": "La Liga", "rank": 19, "id": 349, "team_name": "Cádiz CF", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15737463872884.png",},
        {"pk": 40, "weight": 1.31, "league": "La Liga", "rank": 20, "id": 355, "team_name": "Elche CF", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15737472842633.png",},
        {"pk": 41, "weight": 1.50, "league": "Serie A", "rank": 1, "id": 103, "team_name": "SSC Napoli", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1655810578947.png",},
        {"pk": 42, "weight": 1.49, "league": "Serie A", "rank": 2, "id": 106, "team_name": "Atalanta BC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1655810924168.png",},
        {"pk": 43, "weight": 1.48, "league": "Serie A", "rank": 3, "id": 96, "team_name": "AC Milan", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529152022759.png",},
        {"pk": 44, "weight": 1.47, "league": "Serie A", "rank": 4, "id": 91, "team_name": "AS Roma", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529154451730.png",},
        {"pk": 45, "weight": 1.46, "league": "Serie A", "rank": 5, "id": 92, "team_name": "SS Lazio", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529151451117.png",},
        {"pk": 46, "weight": 1.45, "league": "Serie A", "rank": 6, "id": 108, "team_name": "Inter Milan", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16263445851274.png",},
        {"pk": 47, "weight": 1.44, "league": "Serie A", "rank": 7, "id": 105, "team_name": "Juventus FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529142502894.png",},
        {"pk": 48, "weight": 1.43, "league": "Serie A", "rank": 8, "id": 97, "team_name": "Udinese Calcio", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552917860762.png",},
        {"pk": 49, "weight": 1.42, "league": "Serie A", "rank": 9, "id": 104, "team_name": "Torino FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552915669736.png",},
        {"pk": 50, "weight": 1.41, "league": "Serie A", "rank": 10, "id": 920, "team_name": "US Salernitana 1919", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16154627271875.png",},
        {"pk": 51, "weight": 1.40, "league": "Serie A", "rank": 11, "id": 107, "team_name": "US Sassuolo", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529155562454.png",},
        {"pk": 52, "weight": 1.39, "league": "Serie A", "rank": 12, "id": 110, "team_name": "Bologna FC 1909", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529135761295.png",},
        {"pk": 53, "weight": 1.38, "league": "Serie A", "rank": 13, "id": 95, "team_name": "ACF Fiorentina", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1661777613788.png",},
        {"pk": 54, "weight": 1.37, "league": "Serie A", "rank": 14, "id": 99, "team_name": "Empoli FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl162634452073.png",},
        {"pk": 55, "weight": 1.36, "league": "Serie A", "rank": 15, "id": 919, "team_name": "AC Monza", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16558107622193.png",},
        {"pk": 56, "weight": 1.35, "league": "Serie A", "rank": 16, "id": 645, "team_name": "Spezia Calcio", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15997561391388.png",},
        {"pk": 57, "weight": 1.34, "league": "Serie A", "rank": 17, "id": 123, "team_name": "US Lecce", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15650938222201.png",},
        {"pk": 58, "weight": 1.33, "league": "Serie A", "rank": 18, "id": 101, "team_name": "UC Sampdoria", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552915500725.png",},
        {"pk": 59, "weight": 1.32, "league": "Serie A", "rank": 19, "id": 124, "team_name": "Hellas Verona", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1599758373268.png",},
        {"pk": 60, "weight": 1.31, "league": "Serie A", "rank": 20, "id": 927, "team_name": "US Cremonese", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16154627162904.png",},
        {"pk": 61, "weight": 1.50, "league": "Bundesliga", "rank": 1, "id": 118, "team_name": "1. FC Union Berlin", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1565093319341.png",},
        {"pk": 62, "weight": 1.49, "league": "Bundesliga", "rank": 2, "id": 47, "team_name": "FC Bayern München", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552906705521.png",},
        {"pk": 63, "weight": 1.48, "league": "Bundesliga", "rank": 3, "id": 58, "team_name": "SC Freiburg", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529080011859.png",},
        {"pk": 64, "weight": 1.47, "league": "Bundesliga", "rank": 4, "id": 42, "team_name": "Borussia Dortmund", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529067672087.png",},
        {"pk": 65, "weight": 1.46, "league": "Bundesliga", "rank": 5, "id": 46, "team_name": "Eintracht Frankfurt", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529068992902.png",},
        {"pk": 66, "weight": 1.45, "league": "Bundesliga", "rank": 6, "id": 45, "team_name": "RB Leipzig", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15968705672759.png",},
        {"pk": 67, "weight": 1.44, "league": "Bundesliga", "rank": 7, "id": 54, "team_name": "TSG 1899 Hoffenheim", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529082542209.png",},
        {"pk": 68, "weight": 1.43, "league": "Bundesliga", "rank": 8, "id": 43, "team_name": "SV Werder Bremen", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529089752122.png",},
        {"pk": 69, "weight": 1.42, "league": "Bundesliga", "rank": 9, "id": 50, "team_name": "1. FSV Mainz 05", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15968707221583.png",},
        {"pk": 70, "weight": 1.41, "league": "Bundesliga", "rank": 10, "id": 117, "team_name": "1. FC Köln", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15695949812761.png",},
        {"pk": 71, "weight": 1.40, "league": "Bundesliga", "rank": 11, "id": 49, "team_name": "Borussia Mönchengladbach", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552906838454.png",},
        {"pk": 72, "weight": 1.39, "league": "Bundesliga", "rank": 12, "id": 48, "team_name": "VfL Wolfsburg", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529084001846.png",},
        {"pk": 73, "weight": 1.38, "league": "Bundesliga", "rank": 13, "id": 44, "team_name": "FC Augsburg", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552906553237.png",},
        {"pk": 74, "weight": 1.37, "league": "Bundesliga", "rank": 14, "id": 55, "team_name": "Hertha BSC", "logo": "https://api.statorium.com/media/bearleague/bl1552907318643.png",},
        {"pk": 75, "weight": 1.36, "league": "Bundesliga", "rank": 15, "id": 56, "team_name": "VfB Stuttgart", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529088221586.png",},
        {"pk": 76, "weight": 1.35, "league": "Bundesliga", "rank": 16, "id": 57, "team_name": "Bayer 04 Leverkusen", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529066291244.png",},
        {"pk": 77, "weight": 1.34, "league": "Bundesliga", "rank": 17, "id": 905, "team_name": "VfL Bochum", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16154606122283.png",},
        {"pk": 78, "weight": 1.33, "league": "Bundesliga", "rank": 18, "id": 41, "team_name": "FC Schalke 04", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529087481504.png",},
        {"pk": 79, "weight": 1.45, "league": "Ligue 1", "rank": 1, "id": 66, "team_name": "Paris Saint-Germain", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529128511565.png",},
        {"pk": 80, "weight": 1.44, "league": "Ligue 1", "rank": 2, "id": 546, "team_name": "Racing Club de Lens", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1594642235883.png",},
        {"pk": 81, "weight": 1.43, "league": "Ligue 1", "rank": 3, "id": 67, "team_name": "Stade Rennais FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529129971644.png",},
        {"pk": 82, "weight": 1.42, "league": "Ligue 1", "rank": 4, "id": 545, "team_name": "FC Lorient", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15946422262798.png",},
        {"pk": 83, "weight": 1.41, "league": "Ligue 1", "rank": 5, "id": 59, "team_name": "Olympique de Marseille", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529127102491.png",},
        {"pk": 84, "weight": 1.40, "league": "Ligue 1", "rank": 6, "id": 76, "team_name": "AS Monaco", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1655819996256.png",},
        {"pk": 85, "weight": 1.39, "league": "Ligue 1", "rank": 7, "id": 69, "team_name": "LOSC Lille", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529107162230.png",},
        {"pk": 86, "weight": 1.38, "league": "Ligue 1", "rank": 8, "id": 61, "team_name": "Olympique Lyonnais", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529126462611.png",},
        {"pk": 87, "weight": 1.37, "league": "Ligue 1", "rank": 9, "id": 622, "team_name": "Clermont Foot 63", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1655819785514.png",},
        {"pk": 88, "weight": 1.36, "league": "Ligue 1", "rank": 10, "id": 64, "team_name": "OGC Nice", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529122451246.png",},
        {"pk": 89, "weight": 1.35, "league": "Ligue 1", "rank": 11, "id": 63, "team_name": "Toulouse FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16558204532134.png",},
        {"pk": 90, "weight": 1.34, "league": "Ligue 1", "rank": 12, "id": 632, "team_name": "Troyes AC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15979297741683.png",},
        {"pk": 91, "weight": 1.33, "league": "Ligue 1", "rank": 13, "id": 72, "team_name": "Stade de Reims", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15946469891436.png",},
        {"pk": 92, "weight": 1.32, "league": "Ligue 1", "rank": 14, "id": 65, "team_name": "HSC Montpellier", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15529109402994.png",},
        {"pk": 93, "weight": 1.31, "league": "Ligue 1", "rank": 15, "id": 60, "team_name": "FC Nantes", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16558202112936.png",},
        {"pk": 94, "weight": 1.30, "league": "Ligue 1", "rank": 16, "id": 619, "team_name": "AJ Auxerre", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15979273992750.png",},
        {"pk": 95, "weight": 1.29, "league": "Ligue 1", "rank": 17, "id": 68, "team_name": "RC Strasbourg Alsace", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552913121645.png",},
        {"pk": 96, "weight": 1.28, "league": "Ligue 1", "rank": 18, "id": 121, "team_name": "Stade Brestois 29", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1566076932959.png",},
        {"pk": 97, "weight": 1.27, "league": "Ligue 1", "rank": 19, "id": 618, "team_name": "AC Ajaccio", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15979273442218.png",},
        {"pk": 98, "weight": 1.26, "league": "Ligue 1", "rank": 20, "id": 70, "team_name": "Angers SCO", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl162582671170.png",},
        {"pk": 99, "weight": 1.40, "league": "Portugal", "rank": 1, "id": 131, "team_name": "SL Benfica", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1657210856628.png",},
        {"pk": 100, "weight": 1.39, "league": "Portugal", "rank": 2, "id": 169, "team_name": "SC Braga", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16572108271819.png",},
        {"pk": 101, "weight": 1.38, "league": "Portugal", "rank": 3, "id": 138, "team_name": "FC Porto", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568031999126.png",},
        {"pk": 102, "weight": 1.37, "league": "Portugal", "rank": 4, "id": 156, "team_name": "Vitória de Guimarães", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568030459868.png",},
        {"pk": 103, "weight": 1.36, "league": "Portugal", "rank": 5, "id": 1315, "team_name": "Casa Pia AC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16572106932764.png",},
        {"pk": 104, "weight": 1.35, "league": "Portugal", "rank": 6, "id": 149, "team_name": "Sporting CP", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568031267934.png",},
        {"pk": 105, "weight": 1.34, "league": "Portugal", "rank": 7, "id": 346, "team_name": "Boavista FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1572010177393.png",},
        {"pk": 106, "weight": 1.33, "league": "Portugal", "rank": 8, "id": 983, "team_name": "GD Estoril Praia", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16260970911682.png",},
        {"pk": 107, "weight": 1.32, "league": "Portugal", "rank": 9, "id": 339, "team_name": "Portimonense SC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15720099182833.png",},
        {"pk": 108, "weight": 1.31, "league": "Portugal", "rank": 10, "id": 981, "team_name": "FC Arouca", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1626096594746.png",},
        {"pk": 109, "weight": 1.30, "league": "Portugal", "rank": 11, "id": 1314, "team_name": "GD Chaves", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl165721072721.png",},
        {"pk": 110, "weight": 1.29, "league": "Portugal", "rank": 12, "id": 982, "team_name": "FC Vizela", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1626096855846.png",},
        {"pk": 111, "weight": 1.28, "league": "Portugal", "rank": 13, "id": 344, "team_name": "Rio Ave FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1572010110460.png",},
        {"pk": 112, "weight": 1.27, "league": "Portugal", "rank": 14, "id": 335, "team_name": "FC Famalicão", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15720097094.png",},
        {"pk": 113, "weight": 1.26, "league": "Portugal", "rank": 15, "id": 345, "team_name": "CD Santa Clara", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15997554812082.png",},
        {"pk": 114, "weight": 1.25, "league": "Portugal", "rank": 16, "id": 340, "team_name": "Gil Vicente FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1657210766595.png",},
        {"pk": 115, "weight": 1.24, "league": "Portugal", "rank": 17, "id": 343, "team_name": "CS Marítimo", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16572106642867.png",},
        {"pk": 116, "weight": 1.23, "league": "Portugal", "rank": 18, "id": 337, "team_name": "FC Paços de Ferreira", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16262047201251.png",},
        {"pk": 117, "weight": 1.40, "league": "Eredivisie", "rank": 1, "id": 137, "team_name": "AFC Ajax", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15737307582317.png",},
        {"pk": 118, "weight": 1.39, "league": "Eredivisie", "rank": 2, "id": 150, "team_name": "PSV Eindhoven", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16237099772718.png",},
        {"pk": 119, "weight": 1.38, "league": "Eredivisie", "rank": 3, "id": 173, "team_name": "AZ Alkmaar", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568028251845.png",},
        {"pk": 120, "weight": 1.37, "league": "Eredivisie", "rank": 4, "id": 328, "team_name": "FC Twente", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15720083601120.png",},
        {"pk": 121, "weight": 1.36, "league": "Eredivisie", "rank": 5, "id": 159, "team_name": "Feyenoord Rotterdam", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl156802815882.png",},
        {"pk": 122, "weight": 1.35, "league": "Eredivisie", "rank": 6, "id": 331, "team_name": "Sparta Rotterdam", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15720084522011.png",},
        {"pk": 123, "weight": 1.34, "league": "Eredivisie", "rank": 7, "id": 334, "team_name": "FC Utrecht", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16558149691510.png",},
        {"pk": 124, "weight": 1.33, "league": "Eredivisie", "rank": 8, "id": 333, "team_name": "SC Heerenveen", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15720085081999.png",},
        {"pk": 125, "weight": 1.32, "league": "Eredivisie", "rank": 9, "id": 322, "team_name": "RKC Waalwijk", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15720080561870.png",},
        {"pk": 126, "weight": 1.31, "league": "Eredivisie", "rank": 10, "id": 547, "team_name": "Go Ahead Eagles", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1595497887909.png",},
        {"pk": 127, "weight": 1.30, "league": "Eredivisie", "rank": 11, "id": 560, "team_name": "SBV Excelsior", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16558146712113.png",},
        {"pk": 128, "weight": 1.29, "league": "Eredivisie", "rank": 12, "id": 323, "team_name": "Fortuna Sittard", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1572008163395.png",},
        {"pk": 129, "weight": 1.28, "league": "Eredivisie", "rank": 13, "id": 329, "team_name": "FC Groningen", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1572008384721.png",},
        {"pk": 130, "weight": 1.27, "league": "Eredivisie", "rank": 14, "id": 321, "team_name": "SBV Vitesse", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1572008013842.png",},
        {"pk": 131, "weight": 1.26, "league": "Eredivisie", "rank": 15, "id": 559, "team_name": "NEC Nijmegen", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15955007322769.png",},
        {"pk": 132, "weight": 1.25, "league": "Eredivisie", "rank": 16, "id": 551, "team_name": "SC Cambuur", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15954988062599.png",},
        {"pk": 133, "weight": 1.24, "league": "Eredivisie", "rank": 17, "id": 326, "team_name": "FC Emmen", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1572008286140.png",},
        {"pk": 134, "weight": 1.23, "league": "Eredivisie", "rank": 18, "id": 555, "team_name": "FC Volendam", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1595499202498.png",},
        {"pk": 135, "weight": 1.30, "league": "EPL 2", "rank": 1, "id": 12, "team_name": "Burnley FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15524826922399.png",},
        {"pk": 136, "weight": 1.29, "league": "EPL 2", "rank": 2, "id": 189, "team_name": "Blackburn Rovers FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681870751083.png",},
        {"pk": 137, "weight": 1.28, "league": "EPL 2", "rank": 3, "id": 113, "team_name": "Sheffield United", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1565092102202.png",},
        {"pk": 138, "weight": 1.27, "league": "EPL 2", "rank": 4, "id": 181, "team_name": "Queens Park Rangers FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681865391915.png",},
        {"pk": 139, "weight": 1.26, "league": "EPL 2", "rank": 5, "id": 111, "team_name": "Norwich City", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1655827847717.png",},
        {"pk": 140, "weight": 1.25, "league": "EPL 2", "rank": 6, "id": 174, "team_name": "Swansea City AFC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl16558275871892.png",},
        {"pk": 141, "weight": 1.24, "league": "EPL 2", "rank": 7, "id": 180, "team_name": "Preston North End FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568186462854.png",},
        {"pk": 142, "weight": 1.23, "league": "EPL 2", "rank": 8, "id": 11, "team_name": "Watford FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1552486729625.png",},
        {"pk": 143, "weight": 1.22, "league": "EPL 2", "rank": 9, "id": 185, "team_name": "Millwall FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568186829939.png",},
        {"pk": 144, "weight": 1.21, "league": "EPL 2", "rank": 10, "id": 187, "team_name": "Luton Town FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681869751188.png",},
        {"pk": 146, "weight": 1.19, "league": "EPL 2", "rank": 12, "id": 182, "team_name": "Birmingham City FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681865941166.png",},
        {"pk": 145, "weight": 1.20, "league": "EPL 2", "rank": 11, "id": 188, "team_name": "Reading FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681870281223.png",},
        {"pk": 147, "weight": 1.18, "league": "EPL 2", "rank": 13, "id": 313, "team_name": "Rotherham United FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1571901785174.png",},
        {"pk": 148, "weight": 1.17, "league": "EPL 2", "rank": 14, "id": 179, "team_name": "Bristol City FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl156818412035.png",},
        {"pk": 149, "weight": 1.16, "league": "EPL 2", "rank": 15, "id": 312, "team_name": "Blackpool FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1571901759723.png",},
        {"pk": 150, "weight": 1.15, "league": "EPL 2", "rank": 16, "id": 253, "team_name": "Sunderland AFC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15718396531982.png",},
        {"pk": 151, "weight": 1.14, "league": "EPL 2", "rank": 17, "id": 18, "team_name": "Cardiff City FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl155248278212.png",},
        {"pk": 152, "weight": 1.13, "league": "EPL 2", "rank": 18, "id": 190, "team_name": "Mpkdlesbrough FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681871252300.png",},
        {"pk": 153, "weight": 1.12, "league": "EPL 2", "rank": 19, "id": 251, "team_name": "Coventry City FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15718387092444.png",},
        {"pk": 154, "weight": 1.11, "league": "EPL 2", "rank": 20, "id": 192, "team_name": "Hull City AFC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681903641982.png",},
        {"pk": 155, "weight": 1.10, "league": "EPL 2", "rank": 21, "id": 195, "team_name": "Stoke City FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568191198420.png",},
        {"pk": 156, "weight": 1.09, "league": "EPL 2", "rank": 22, "id": 193, "team_name": "Wigan Athletic FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl15681886272356.png",},
        {"pk": 157, "weight": 1.08, "league": "EPL 2", "rank": 23, "id": 177, "team_name": "West Bromwich Albion FC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1568183822340.png",},
        {"pk": 158, "weight": 1.07, "league": "EPL 2", "rank": 24, "id": 20, "team_name": "Huddersfield Town AFC", "logo": "https://dxl9rl52p7hhu.cloudfront.net/media/bearleague/bl1598387813365.png",},
        # {"pk": 159, "weight": 1.20, "league": "K-League", "rank": 1, "id": 0, "team_name": "Ulsan", "logo": "",},
        # {"pk": 160, "weight": 1.19, "league": "K-League", "rank": 2, "id": 0, "team_name": "Jeonbuk", "logo": "",},
        # {"pk": 161, "weight": 1.18, "league": "K-League", "rank": 3, "id": 0, "team_name": "Pohang Steelers", "logo": "",},
        # {"pk": 162, "weight": 1.17, "league": "K-League", "rank": 4, "id": 0, "team_name": "Incheon", "logo": "",},
        # {"pk": 163, "weight": 1.16, "league": "K-League", "rank": 5, "id": 0, "team_name": "Jeju", "logo": "",},
        # {"pk": 164, "weight": 1.15, "league": "K-League", "rank": 6, "id": 0, "team_name": "Gangwon", "logo": "",},
        # {"pk": 165, "weight": 1.14, "league": "K-League", "rank": 7, "id": 0, "team_name": "Suwon FC", "logo": "",},
        # {"pk": 166, "weight": 1.13, "league": "K-League", "rank": 8, "id": 0, "team_name": "FC Seoul", "logo": "",},
        # {"pk": 167, "weight": 1.12, "league": "K-League", "rank": 9, "id": 0, "team_name": "Daegu", "logo": "",},
        # {"pk": 168, "weight": 1.11, "league": "K-League", "rank": 10, "id": 0, "team_name": "Sangju Sangmu", "logo": "",},
        # {"pk": 169, "weight": 1.10, "league": "K-League", "rank": 11, "id": 0, "team_name": "Suwon Bluewings", "logo": "",},
        # {"pk": 170, "weight": 1.09, "league": "K-League", "rank": 12, "id": 0, "team_name": "Seongnam", "logo": "",},
    ]
    for t in leagues:
        if t["team_name"] == team:
            return t["weight"]