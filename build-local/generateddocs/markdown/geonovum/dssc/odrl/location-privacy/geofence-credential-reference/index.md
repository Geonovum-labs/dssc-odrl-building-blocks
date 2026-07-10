
# Participant Geofence Credential Reference (Schema)

`nl.geonovum.dssc.odrl.location-privacy.geofence-credential-reference` *v0.1.0*

A Verifiable Credential subject shape that references a participant geofence by resolvable URL and SHA-256 hash.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Geofence credential subject
#### json
```json
{
  "credentialSubject": {
    "id": "did:geofence:example-participant-area",
    "geofence": {
      "URL": "https://example.org/geofences/participant-area.geojson",
      "hash": "4e6e861333fdb00112233445566778899aabbccddeeff00112233445566778899"
    }
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/geofence-credential-reference/schema.json
title: Participant Geofence Credential Reference
type: object
required:
- credentialSubject
properties:
  credentialSubject:
    type: object
    required:
    - id
    - geofence
    properties:
      id:
        type: string
      geofence:
        type: object
        required:
        - URL
        - hash
        properties:
          URL:
            type: string
            format: uri
          hash:
            type: string
            pattern: ^[A-Fa-f0-9]{64}$
        additionalProperties: true
    additionalProperties: true
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/geofence-credential-reference/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/geofence-credential-reference/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
