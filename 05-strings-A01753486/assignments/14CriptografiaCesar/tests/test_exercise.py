import pytest
import src.exercise


def test_codificacion():
    assert src.exercise.codificacion_cesar("Hola Mundo", 3) == "Krod#Pxqgr"
    assert src.exercise.codificacion_cesar("Hola Mundo", 4) == "Lspe$Qyrhs"
    assert src.exercise.codificacion_cesar("TC1028", 4) == "XG546<"


def test_decodificacion():
    assert src.exercise.decodificacion_cesar("Krod#Pxqgr", 3) == "Hola Mundo"
    assert src.exercise.decodificacion_cesar("Lspe$Qyrhs", 4) == "Hola Mundo"
    assert src.exercise.decodificacion_cesar(
        "Tirweqmirxs$Gsqtyxegmsrep$teve$Mrkirmivme", 4) == "Pensamiento Computacional para Ingenieria"
