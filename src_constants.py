"""
src_constants.py

holds global speedrun.com API constants
"""

from data_models import CelesteGames
from dacite import from_dict


PLATFORMS: dict = {
    "PlayStation 4": "nzelkr6q",
    "Xbox One": "o7e2mx6w",
    "PC": "8gej2n93",
    "Switch": "7m6ylw9p",
    "Google Stadia": "o064z1e3",
    "PlayStation 5": "4p9zjrer",
    "Xbox Series S": "o7e2xj9w",
    "Xbox Series X": "nzelyv9q",
    "Xbox One X": "4p9z0r6r",
    "Xbox One S": "o064j163",
}

CELESTE_GAMES: CelesteGames = from_dict(
    data_class=CelesteGames,
    data={
        "games": [
            {
                "id": "o1y9j9v6",
                "name": "Celeste",
                "version": {
                    "variable_id": "38do9y4l",
                    "default_ver": "5q8e7y3q",
                    "invalid_ver": {
                        "nzelkr6q": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "o7e2mx6w": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "o7e2xj9w": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "nzelyv9q": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "4p9z0r6r": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "o064j163": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "8gej2n93": [],
                        "7m6ylw9p": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "o064z1e3": ["810gdx5l", "zqoo4vxq"],
                        "4p9zjrer": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                    },
                },
            },
            {
                "id": "j1ne9me1",
                "name": "Celeste Category Extensions",
                "version": {
                    "variable_id": "dlomdgd8",
                    "default_ver": "xqkzpg4q",
                    "invalid_ver": {
                        "nzelkr6q": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "o7e2mx6w": [
                            "5lmvmd4l",
                            "0137g6xl",
                            "5q887vyq",
                            "5lmg3eyl",
                            "5lemyr51",
                            "4lxe2o21",
                        ],
                        "o7e2xj9w": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "nzelyv9q": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "4p9z0r6r": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "o064j163": [
                            "810gdx5l",
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                        "8gej2n93": [],
                        "7m6ylw9p": [
                            "0137g6xl",
                            "5q887vyq",
                            "5lmg3eyl",
                            "5lemyr51",
                            "4lxe2o21",
                        ],
                        "o064z1e3": ["5lmvmd4l", "0137g6xl"],
                        "4p9zjrer": [
                            "zqoo4vxq",
                            "21dg78p1",
                            "9qjxmo0l",
                            "rqve2p71",
                            "5lemyz51",
                        ],
                    },
                },
            },
            {
                "id": "w6jl3ked",
                "name": "Modded Celeste",
                "version": {
                    "variable_id": "p853km0n",
                    "default_ver": "z19rw541",
                    "invalid_ver": {"8gej2n93": []},
                },
            },
            {
                "id": "j1lqq576",
                "name": "Into The Jungle",
                "version": {
                    "variable_id": "9l7x0xqn",
                    "default_ver": "5q8p493l",
                    "invalid_ver": {"8gej2n93": []},
                },
            },
            {
                "id": "y6554g36",
                "name": "Glyph",
                "version": {
                    "variable_id": "5ly14pyl",
                    "default_ver": "21dwwrgl",
                    "invalid_ver": {"8gej2n93": []},
                },
            },
            {
                "id": "w6j7lx46",
                "name": "D-Sides",
                "version": {
                    "variable_id": "e8m5krxn",
                    "default_ver": "mlnnnrnl",
                    "invalid_ver": {"8gej2n93": []},
                },
            },
            {
                "id": "46w3p271",
                "name": "Quickie Mountain 2",
                "version": {
                    "variable_id": "68kodrkn",
                    "default_ver": "013d623l",
                    "invalid_ver": {"8gej2n93": []},
                },
            },
            {
                "id": "k6qw4q06",
                "name": "2020 Spring Collab",
                "version": {
                    "variable_id": "6njzg4el",
                    "default_ver": "0q5p3zrl",
                    "invalid_ver": {"8gej2n93": []},
                },
            },
        ]
    },
)
