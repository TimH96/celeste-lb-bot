"""
__main__.py

Reads out settings and CLI params and runs bot with them
"""

from celeste_bot import CelesteLeaderboardBot

# TODO read out settings
config : dict = {
    "key"   : None,
    "timer" : 10,
    "games" : [
        {
            "id"      : "o1y9j9v6",
            "name"    : "Celeste",
            "version" : {
                "id_var" : "38do9y4l",
                "id_val" : "5q8e7y3q"
            }
        }
        #
        #{
        #    "id"      : "j1ne9me1",
        #    "name"    : "Celeste Category Extensions",
        #    "version" : {
        #        "id_var" : "TODO",
        #        "id_val" : "TODO"
        #    }
        #},
        #{
        #    "id"      : "w6j7lx46",
        #    "name"    : "Celeste D-Sides",
        #    "version" : {
        #        "id_var" : "TODO",
        #        "id_val" : "TODO"
        #    }
        #},
        #{
        #    "id"      : "w6jl3ked",
        #    "name"    : "Celeste Custom Maps",
        #    "version" : {
        #        "id_var" : "TODO",
        #        "id_val" : "TODO"
        #    }
        #},
        #{
        #    "id"      : "y6554g36",
        #    "name"    : "Celeste Glyph",
        #    "version" : {
        #        "id_var" : "TODO",
        #        "id_val" : "TODO"
        #    }
        #},
        #{
        #    "id"      : "46w3p271",
        #    "name"    : "Celeste Quickie Mountain 2",
        #    "version" : {
        #        "id_var" : "TODO",
        #        "id_val" : "TODO"
        #    }
        #},
        #{
        #    "id"      : "k6qw4q06",
        #    "name"    : "Celeste 2020 Spring Collab",
        #    "version" : {
        #        "id_var" : "TODO",
        #        "id_val" : "TODO"
        #    }
        #}
    ]
}

CelesteLeaderboardBot(**config).start()
