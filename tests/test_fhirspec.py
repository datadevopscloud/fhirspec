# -*- coding: utf-8 -*-
import fhirspec


def test_fhirspec_init(settings):
    """"""
    config, sources = settings
    spec = fhirspec.FHIRSpec(config, sources[0])
    assert "Patient" in fhirspec.FHIRClass.known
    assert "patient" in spec.profiles
