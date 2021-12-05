"""
src_constants.py

holds global speedrun.com API constants
"""

from data_models    import CelesteGames
from dacite         import from_dict


PLATFORMS : dict = {
    "PlayStation 4" : "nzelkr6q",
    "Xbox One"      : "o7e2mx6w",
    "PC"            : "8gej2n93",
    "Switch"        : "7m6ylw9p",
    "Google Stadia" : "o064z1e3",
    "PlayStation 5" : "4p9zjrer",
    "Xbox Series S" : "o7e2xj9w",
    "Xbox Series X" : "nzelyv9q",
    "Xbox One X"    : "4p9z0r6r",
    "Xbox One S"    : "o064j163"
}

CELESTE_GAMES : CelesteGames = from_dict(
    data_class=CelesteGames,
    data={
        "games" : [
            {
                "id"      : "o1y9j9v6",
                "name"    : "Celeste",
                "version" : {
                    "variable_id" : "38do9y4l",
                    "default_ver" : "5q8e7y3q",
                    "invalid_ver" : {
                        "nzelkr6q" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "o7e2mx6w" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "o7e2xj9w" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "nzelyv9q" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "4p9z0r6r" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "o064j163" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "8gej2n93" : [],
                        "7m6ylw9p" : ["zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "o064z1e3" : ["810gdx5l", "zqoo4vxq"],
                        "4p9zjrer" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51", "p12wv871", "z1992w01", "z19rn0j1", "jq6766n1", "81w8xj91", "5lmn0eyq", "8107j55l", "z19zn7yq", "0q528evq", "0q52262q", "4qynnv41", "81wn7y51", "21d26k3l", "21d4ej31", "5lekw0zl", "gq7n65n1", "jq64d2j1", "gq7nm6n1", "81p7kme1", "814xmmwq", "zqoyep21", "p125p721", "klrzv5o1", "xqkr09d1", "81wmoemq", "4qyxe02l", "mlny6xj1", "8105e42q", "21d47051", "xqkrkxk1", "9qjzy331", "jq64kdj1", "5lmxj5m1", "81wmwkvq", "zqoyw7x1", "013veyxl", "rqv4wn6q", "8142k7kl", "5lekgwkl", "0q5oe021", "4lxxwj4l", "814xenvq", "z194gw8l", "p125e841", "81p7wg81", "klrz4jo1"]
                    }
                }
            },
            {
                "id"      : "j1ne9me1",
                "name"    : "Celeste Category Extensions",
                "version" : {
                    "variable_id" : "dlomdgd8",
                    "default_ver" : "xqkzpg4q",
                    "invalid_ver" : {
                        "nzelkr6q" : ["5lmvmd4l", "0137g6xl", "5q887vyq", "5lmg3eyl", "5lemyr51", "4lxe2o21"],
                        "o7e2mx6w" : ["5lmvmd4l", "0137g6xl", "5q887vyq", "5lmg3eyl", "5lemyr51", "4lxe2o21"],
                        "o7e2xj9w" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "nzelyv9q" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "4p9z0r6r" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "o064j163" : ["810gdx5l", "zqoo4vxq", "21dg78p1", "9qjxmo0l", "rqve2p71", "5lemyz51"],
                        "8gej2n93" : [],
                        "7m6ylw9p" : ["0137g6xl", "5q887vyq", "5lmg3eyl", "5lemyr51", "4lxe2o21"],
                        "o064z1e3" : ["5lmvmd4l", "0137g6xl"],
                        "4p9zjrer" : ["5lmvmd4l", "0137g6xl", "5q887vyq", "5lmg3eyl", "5lemyr51", "4lxe2o21", "jqz5gr4q", "21g49wx1", "p12z7gv1", "8107krpl", "mln3j2nq", "81pnr3nl", "8107jwwl", "810x4j51", "81pxr3nq", "gq77yvrq", "21gxkwoq", "jqz0ork1", "klr58ew1", "21d2pjgl", "5q8gnx6l", "4qynkvd1", "mln5g4nl", "810x2op1", "9qjgp6oq", "jq6289ol", "5lmd7r0l", "81wn6v61", "zqo5z84l", "0132zoyq", "rqvmjkyq", "5leep26l", "0q52dvvq", "4lxym5gq", "8142rokl", "z19z024q", "p122gv21", "81pxrynq", "xqkzpe4q", "gq77y5rq", "21gxknoq", "jqz0onk1", "klr583w1", "21d2pkgl", "5q8gnk6l", "4qynkzd1", "mln5g8nl", "810x2vp1", "9qjgp7oq", "jq6285ol", "5lmd7o0l", "81wn6461", "z196ev81", "jq6ngvnl", "zqokn7gl"]
                    }
                }
            },
            {
                "id"      : "w6jl3ked",
                "name"    : "Modded Celeste",
                "version" : {
                    "variable_id" : "p853km0n",
                    "default_ver" : "z19rw541",
                    "invalid_ver" : {
                        "8gej2n93" : []
                    }
                }
            },
            {
                "id"      : "j1lqq576",
                "name"    : "Into The Jungle",
                "version" : {
                    "variable_id" : "9l7x0xqn",
                    "default_ver" : "5q8p493l",
                    "invalid_ver" : {
                        "8gej2n93" : []
                    }
                }
            },
            {
                "id"      : "y6554g36",
                "name"    : "Glyph",
                "version" : {
                    "variable_id" : "5ly14pyl",
                    "default_ver" : "21dwwrgl",
                    "invalid_ver" : {
                        "8gej2n93" : []
                    }
                }
            },
            {
                "id"      : "w6j7lx46",
                "name"    : "D-Sides",
                "version" : {
                    "variable_id" : "e8m5krxn",
                    "default_ver" : "mlnnnrnl",
                    "invalid_ver" : {
                        "8gej2n93" : []
                    }
                }
            },
            {
                "id"      : "46w3p271",
                "name"    : "Quickie Mountain 2",
                "version" : {
                    "variable_id" : "68kodrkn",
                    "default_ver" : "013d623l",
                    "invalid_ver" : {
                        "8gej2n93" : []
                    }
                }
            },
            {
                "id"      : "k6qw4q06",
                "name"    : "2020 Spring Collab",
                "version" : {
                    "variable_id" : "6njzg4el",
                    "default_ver" : "0q5p3zrl",
                    "invalid_ver" : {
                        "8gej2n93" : []
                    }
                }
            }
        ]
    }
)
